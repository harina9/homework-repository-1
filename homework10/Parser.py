import asyncio
import json
import operator
import xml.etree.ElementTree as ET
from datetime import datetime
from functools import reduce

import aiohttp
from bs4 import BeautifulSoup


class Company:
    def __init__(self):
        self._code = None
        self._name = None
        self._price = None
        self._p_e = None
        self._growth = None
        self._potential_profit = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def p_e(self):
        return self._p_e

    @p_e.setter
    def p_e(self, p_e):
        self._p_e = p_e

    @property
    def growth(self):
        return self._growth

    @growth.setter
    def growth(self, growth):
        self._growth = growth

    @property
    def potential_profit(self):
        return self._potential_profit

    @potential_profit.setter
    def potential_profit(self, potential_profit):
        self._potential_profit = potential_profit


all_companies = []


async def main():
    base_source_url = "https://markets.businessinsider.com{}"
    source_url = "https://markets.businessinsider.com/index/components/s&p_500?p={}"
    central_bank_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}"

    async with aiohttp.ClientSession() as session:
        today_datetime = datetime.today().strftime("%d/%m/%Y")
        async with session.get(central_bank_url.format(today_datetime)) as cb_response:
            cb = await cb_response.text()
            cb_tree = ET.fromstring(cb)
            dollar_value = float(
                list(filter(lambda valute: "R01235".__eq__(valute.get("ID")), cb_tree))[
                    0
                ]
                .find("Value")
                .text.strip()
                .replace(",", ".")
            )

        for i in range(1, 11):
            async with session.get(source_url.format(i)) as response:
                fifty_companies = []
                html = await response.text()

                soup = BeautifulSoup(html, "html.parser")
                table_body = soup.find("tbody", class_="table__tbody")
                table_rows = table_body.findAll("tr")

                for row in table_rows:
                    company = Company()
                    all_columns = row.findAll("td", class_="table__td")
                    header_column = row.find("td", class_="table__td table__td--big")
                    company_url = base_source_url.format(
                        header_column.find("a").attrs["href"]
                    )

                    name = header_column.find("a").contents[0]
                    company.name = name
                    print(name)

                    price_column = all_columns[1].contents[0].strip().replace(",", "")
                    price_dollars = float(price_column)
                    company.price = price_dollars * dollar_value
                    async with session.get(company_url) as company_response:
                        company_html = await company_response.text()
                        company_soup = BeautifulSoup(company_html, "html.parser")

                        company_code_elements = company_soup.find(
                            "span", class_="price-section__category"
                        )
                        code = (
                            company_code_elements.find("span")
                            .contents[0]
                            .replace(",", "")
                        )
                        company.code = code

                        company_snapshot = company_soup.find("div", class_="snapshot")
                        try:
                            snapshot_data_items = company_snapshot.findAll(
                                "div", class_="snapshot__data-item"
                            )
                        except:
                            AttributeError
                        p_e_ratio_item = list(
                            filter(
                                lambda item: "P/E Ratio".__eq__(
                                    item.find(
                                        "div", class_="snapshot__header"
                                    ).contents[0]
                                ),
                                snapshot_data_items,
                            )
                        )
                        if len(p_e_ratio_item) > 0:
                            company.p_e = float(
                                p_e_ratio_item[0].contents[0].strip().replace(",", "")
                            )

                        week_low_item = list(
                            filter(
                                lambda item: "52 Week Low".__eq__(
                                    item.find(
                                        "div", class_="snapshot__header"
                                    ).contents[0]
                                ),
                                snapshot_data_items,
                            )
                        )
                        week_high_item = list(
                            filter(
                                lambda item: "52 Week High".__eq__(
                                    item.find(
                                        "div", class_="snapshot__header"
                                    ).contents[0]
                                ),
                                snapshot_data_items,
                            )
                        )
                        if len(week_low_item) > 0 and len(week_high_item) > 0:
                            profit = float(
                                week_high_item[0].contents[0].strip().replace(",", "")
                            ) - float(
                                week_low_item[0].contents[0].strip().replace(",", "")
                            )
                            company.potential_profit = profit

                # find company growth
                growth_column = all_columns[-1]
                growth_percent = growth_column.findAll("span")[-1].contents[0]
                company.growth = growth_percent

                fifty_companies.append(company)

            all_companies.append(fifty_companies)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

new = reduce(operator.concat, all_companies)

print(new)


def top_10_high_price():
    """top 10 companies by highest price"""
    top = sorted(new, key=lambda company: company.price, reverse=True)[:11]
    return [
        {"code": company.code, "name": company.name, "price": company.price}
        for company in top
    ]


def top_10_low_Pe():
    """top 10 companies by lowest P/E"""
    top = sorted(new, key=lambda company: company.p_e)[:11]
    return [
        {"code": company.code, "name": company.name, "p/e": company.p_e}
        for company in top
    ]


def top_10_big_growth():
    """top 10 companies by biggest growth"""
    top = sorted(new, key=lambda company: company.growth, reverse=True)[:11]
    return [
        {"code": company.code, "name": company.name, "growth": company.growth}
        for company in top
    ]


def top_10_high_profit():
    """top 10 companies by highest profit"""
    top = sorted(new, key=lambda company: company.potential_profit, reverse=True)[:11]
    return [
        {
            "code": company.code,
            "name": company.name,
            "potential_profit": company.potential_profit,
        }
        for company in top
    ]


jsonData = json.dumps(top_10_high_price())
jsonData2 = json.dumps(top_10_low_Pe())
jsonData3 = json.dumps(top_10_big_growth())
jsonData4 = json.dumps(top_10_high_profit())

with open("price.json", "w") as file:
    file.write(jsonData)

with open("pe.json", "w") as file:
    file.write(jsonData2)

with open("growth.json", "w") as file:
    file.write(jsonData3)

with open("profit.json", "w") as file:
    file.write(jsonData4)

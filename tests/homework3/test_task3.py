import pytest

from homework3.task3 import make_filter, sample_data


def test_positive_case():
    assert make_filter(type="person", name="Bill").apply(sample_data) == [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        }
    ]


def test_negative_filter():
    assert make_filter(name="polly", type="person").apply(sample_data) == []


def test_no_filter():
    assert make_filter().apply(sample_data) == sample_data

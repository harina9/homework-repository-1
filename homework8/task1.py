class KeyValueStorage:
    def __init__(self, path):
        with open(path, "r") as file:
            data = file.read().splitlines()

            for line in data:
                key, value = line.split("=")

                if not key.isidentifier():
                    raise ValueError("Wrong key!")

                if value.isdigit():
                    value = int(value)

                if key not in self.__dict__:
                    setattr(self, key, value)

    def __getitem__(self, key):
        return self.__dict__.get(key, None)


if __name__ == "__main__":

    storage = KeyValueStorage("task1.txt")
    print(storage["name"])
    print(storage.song)
    print(storage.power)

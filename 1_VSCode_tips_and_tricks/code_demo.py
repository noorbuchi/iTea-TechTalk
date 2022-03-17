"""Just some code to try out shortcuts on."""

import json


def some_function(var1: int, arg2: int):
    another_function("my_file.json", {})
    print("Hello world")
    if var1 > arg2:
        return var1 + arg2
    else:
        return var1 - arg2


def another_function(file_path: str, contents: dict):
    with open(file_path, "w+", encoding="utf-8") as output_file:
        json.dump(contents, output_file)


if __name__ == "__main__":
    num1 = some_function(6, 5)
    num1 = some_function(4, 9)

from typing import TextIO


class LayoutHelper:

    _layout_file = r"./resources/layout/layout.txt"

    @staticmethod
    def load_layout_file() -> str:
        with open(LayoutHelper._layout_file, "r") as file:
            return file.read()

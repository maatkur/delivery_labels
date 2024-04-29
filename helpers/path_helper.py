class PathHelper:
    _main_execution = False

    @staticmethod
    def resolve():
        if PathHelper._main_execution:
            return ""
        else:
            return "../"

    @staticmethod
    def set_main_execution(value: bool) -> None:
        PathHelper._main_execution = value

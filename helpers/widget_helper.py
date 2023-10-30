

class WidgetHelper:

    @staticmethod
    def install_event_filters(window, widgets) -> None:
        for widget in widgets:
            widget.installEventFilter(window)

    @staticmethod
    def enable_widget(widget) -> None:
        widget.setDisabled(False)

    @staticmethod
    def disable_widget(widget) -> None:
        widget.setDisabled(True)

    @staticmethod
    def clear_widget(widgets: list) -> None:

        for widget in widgets:
            widget.clear()

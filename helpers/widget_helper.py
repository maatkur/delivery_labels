from PySide6.QtWidgets import QWidget


class WidgetHelper:

    @staticmethod
    def install_event_filters(window, widgets) -> None:
        for widget in widgets:
            widget.installEventFilter(window)

    @staticmethod
    def enable_widget(widgets: list or QWidget) -> None:

        if type(widgets) == list:
            for widget in widgets:
                widget.setDisabled(False)
        else:
            widgets.setDisabled(False)

    @staticmethod
    def disable_widget(widgets: list or QWidget) -> None:

        if type(widgets) == list:
            for widget in widgets:
                widget.setDisabled(True)
        else:
            widgets.setDisabled(True)

    @staticmethod
    def clear_widget(widgets: list or QWidget) -> None:

        if type(widgets) == list:
            for widget in widgets:
                widget.clear()
        else:
            widgets.clear()

    @staticmethod
    def clear_table(widgets: list or QWidget) -> None:

        if type(widgets) == list:
            for table in widgets:
                table.clearContents()
                table.setRowCount(0)
        else:
            widgets.clearContents()
            widgets.setRowCount(0)

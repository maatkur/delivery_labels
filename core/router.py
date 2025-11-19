from domain.entities.user_entity import UserEntity


class AppRouter:
    @staticmethod
    def open_initial_screen(user: UserEntity) -> None:
        perms = user.permissions

        if "COATING LABELS" in perms:
            from views.coating_labels_printer_view import CoatingLabelsPrinterView
            return CoatingLabelsPrinterView()

        from views.labels_printer_view import LabelsPrinterView
        return LabelsPrinterView()

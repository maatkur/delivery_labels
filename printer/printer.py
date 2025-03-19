from .layout import Layout


class Printer:

    @staticmethod
    def print_label(label_data: dict) -> None:
        """Gera e 'imprime' etiquetas para cada volume."""
        zpl_content = ""
        for current_label in range(1, label_data["volumes"] + 1):
            label_data["current_label"] = current_label

            zpl = Layout.generate_label(
                label_data
            )
            zpl_content += zpl
        # TODO: Implementar win32print aqui depois
        print(zpl_content)  # Só pra testar por enquanto

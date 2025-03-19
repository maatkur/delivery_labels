import os


class Layout:
    @staticmethod
    def load_template(template_name="label_template.zpl"):
        """Carrega o template ZPL de um arquivo externo."""
        template_path = os.path.join(os.path.dirname(__file__), "..", "templates", template_name)
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def generate_label(label_data: dict) -> str:
        """Gera o ZPL substituindo os placeholders com os valores dinâmicos."""
        template = Layout.load_template()
        try:
            return template.format(
                customer=label_data["customer"],
                store=label_data["store"],
                date=label_data["date"],
                user_id=label_data["user_id"],
                current_label=label_data["current_label"],
                volumes=label_data["volumes"],
                order=label_data["order_id"],
            )
        except KeyError as e:
            raise ValueError(f"Placeholder faltando no template: {e}")


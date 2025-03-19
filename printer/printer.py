# printer/printer.py
import win32print
from .layout import Layout
from components.dialog_window.dialog_window_manager import DialogWindowManager


class Printer:
    @staticmethod
    def get_zebra_printer():
        """Encontra a impressora Zebra redirecionada via RDP."""
        try:
            printers = win32print.EnumPrinters(2)
            for printer in printers:
                name = printer[2].lower()
                if "redirecionada" in name and "generic / text only" in name:
                    return printer[2]
            raise Exception("Impressora Zebra redirecionada não encontrada!")
        except Exception as e:
            DialogWindowManager.dialog().error(f"Erro ao encontrar impressora: {str(e)}")
            raise

    @staticmethod
    def print_label(label_data: dict) -> None:
        """Gera e imprime etiquetas para cada volume na Zebra.

        Args:
            label_data (dict): Dados da etiqueta (ex.: {'volumes': ..., 'customer': ..., ...}).
        """
        zpl_content = ""
        for current_label in range(1, label_data["volumes"] + 1):
            label_data["current_label"] = current_label
            zpl = Layout.generate_label(label_data)
            zpl_content += zpl

        printer_name = Printer.get_zebra_printer()
        try:
            hPrinter = win32print.OpenPrinter(printer_name)
            try:
                win32print.StartDocPrinter(hPrinter, 1, ("Etiqueta", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, zpl_content.encode("utf-8"))
                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hPrinter)
            finally:
                win32print.ClosePrinter(hPrinter)
        except Exception as e:
            DialogWindowManager.dialog().error(f"Erro ao imprimir: {str(e)}")
            raise
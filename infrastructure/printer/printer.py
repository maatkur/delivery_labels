import win32print
from .layout import Layout
from components.dialog_window.dialog_window_manager import DialogWindowManager
from database.repositories import RepositoryManager


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
        """Gera e imprime etiquetas para o intervalo especificado ou todos os volumes.

        Args:
            label_data (dict): Dados da etiqueta, incluindo 'volumes' e opcionalmente 'interval'.
        """
        zpl_content = ""
        interval = label_data.get("interval")
        if interval:
            start, end = interval
            if start < 1 or end > label_data["volumes"] or start > end:
                DialogWindowManager.dialog().error("Intervalo inválido para impressão!")
                return
        else:
            start, end = 1, label_data["volumes"]

        for current_label in range(start, end + 1):
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
                # Adiciona intervalo ao log como string
                log_data = label_data.copy()
                if interval and log_data["is_reprint"]:
                    log_data[
                        "reprint_reason"] = f"{log_data['reprint_reason']} (intervalo: {interval[0]};{interval[1]})"
                RepositoryManager.printer_logs_repository().create_printer_log(log_data)
            finally:
                win32print.ClosePrinter(hPrinter)
        except Exception as e:
            DialogWindowManager.dialog().error(f"Erro ao imprimir: {str(e)}")
            raise
# helpers/sanitize_str_helper.py
class SanitizeStrHelper:
    _words_to_remove = ["OBRA", "FACIL", "FOGOES", "SHP", "LTDA", "CASA", "TOGNINI", "LOJA", "ESPACO"]
    _prepositions = ["E", "DE", "DA", "DO"]  # Preposições curtas pra ignorar
    _max_length = 15  # Limite de caracteres pra etiqueta

    @staticmethod
    def sanitize_str(value):
        """Sanitiza uma string removendo palavras indesejadas e abreviando se necessário.

        Args:
            value (str): String original (ex.: 'OBRA FACIL-ESPACO PORTINARI E CEUSA').

        Returns:
            str: String sanitizada (ex.: 'PORT. CEUSA').
        """
        if not value or not isinstance(value, str):
            return ""

        # Converte pra maiúsculo pra padronizar
        sanitized = value.upper()

        # Remove as palavras da lista
        for word in SanitizeStrHelper._words_to_remove:
            sanitized = sanitized.replace(word, "")

        # Trata o hífen como separador e pega a parte depois do último hífen
        parts = sanitized.split("-")
        sanitized = parts[-1] if parts else sanitized

        # Remove espaços extras e separa em palavras, filtrando vazios
        sanitized = " ".join(sanitized.split())  # Junta com espaço único
        words = [word for word in sanitized.split(" ") if word]  # Só palavras não vazias

        # Se não tiver palavras, retorna vazio
        if not words:
            return ""

        # Filtra preposições curtas
        meaningful_words = [word for word in words if word not in SanitizeStrHelper._prepositions]

        # Junta as palavras pra checar o tamanho
        sanitized = " ".join(meaningful_words)

        # Se for menor ou igual ao limite, retorna como está
        if len(sanitized) <= SanitizeStrHelper._max_length:
            return sanitized

        # Se tiver várias palavras significativas, abrevia as últimas duas
        if len(meaningful_words) >= 2:
            second_last = meaningful_words[-2]  # "PORTINARI"
            last = meaningful_words[-1]         # "CEUSA"
            # Abrevia a penúltima pra 4 letras + ponto
            abbreviated = second_last[:4] + "." if len(second_last) > 4 else second_last
            result = f"{abbreviated} {last}"
            # Se ainda passar do limite, retorna só a última
            if len(result) > SanitizeStrHelper._max_length:
                return last
            return result
        else:
            # Se só tiver uma palavra longa, corta no limite
            return sanitized[:SanitizeStrHelper._max_length].strip()


if __name__ == '__main__':
    sanitized = SanitizeStrHelper.sanitize_str("OBRA FACIL-ESPACO PORTINARI E CEUSA               ")
    print(sanitized)  # Saída: "PORT. CEUSA"

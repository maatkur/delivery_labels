from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class UserEntity:
    """
    Entidade de domínio que representa um usuário do sistema.
    Independente de ORM ou infraestrutura.
    """

    id: Optional[int]
    name: str
    password: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    permissions: List[str] = field(default_factory=list)

    def __post_init__(self):
        """
        Executa validações após a criação da instância.
        """
        self.name = self.name.strip()
        self._validate()

    # -----------------------------
    # ✅ Validações
    # -----------------------------
    def _validate(self):
        if not self.name:
            raise ValueError("O nome do usuário não pode ser vazio.")
        if len(self.password) < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres.")

    # -----------------------------
    # 🔐 Controle de Permissões
    # -----------------------------
    def add_permission(self, permission: str) -> None:
        """
        Adiciona uma permissão ao usuário, se ainda não existir.
        """
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remove_permission(self, permission: str) -> None:
        """
        Remove uma permissão do usuário, se existir.
        """
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_permission(self, permission: str) -> bool:
        """
        Verifica se o usuário possui uma permissão específica.
        """
        return permission in self.permissions

    # -----------------------------
    # 🧠 Métodos utilitários
    # -----------------------------
    def update_timestamp(self) -> None:
        """
        Atualiza o campo updated_at para o horário atual.
        """
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        """
        Representação de depuração.
        """
        return (
            f"<UserEntity id={self.id}, "
            f"name='{self.name}', "
            f"permissions={self.permissions}>"
        )

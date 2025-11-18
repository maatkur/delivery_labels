from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class PermissionEntity:
    """
    Entidade de domínio que representa uma permissão no sistema.
    Não conhece SQLAlchemy — apenas regras de negócio.
    """
    id: Optional[int]
    description: str
    created_at: datetime
    updated_at: datetime
    users: Optional[List[int]] = None  # IDs de usuários (opcional)

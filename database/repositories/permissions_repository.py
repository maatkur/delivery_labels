from database.config import RepositoryConfig, get_session
from database.models import Permission
from domain.entities import PermissionEntity


class PermissionsRepository(RepositoryConfig):
    def __init__(self):
        super().__init__(table_name="permissions")

    def get_all_permissions(self) -> list[PermissionEntity]:
        """
        Retorna todas as permissões do banco convertidas em entidades de domínio.
        """
        try:
            with get_session() as session:
                records = session.query(Permission).all()
                return [
                    PermissionEntity(
                        id=record.id,
                        description=record.description,
                        created_at=record.created_at,
                        updated_at=record.updated_at
                    )
                    for record in records
                ]
        except Exception as e:
            print(f"Erro ao buscar permissões: {e}")
            return []

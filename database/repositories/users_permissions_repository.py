from database.config import RepositoryConfig, get_session
from database.models import users_permissions, Permission, User  # Importe o modelo User


class UsersPermissionsRepository(RepositoryConfig):

    def __init__(self):
        super().__init__(table_name="users_permissions")

    def get_user_permissions(self, user_id):
        try:
            with get_session() as session:
                result = session.query(users_permissions).filter_by(user_id=user_id).all()
                permissions = [
                    session.query(Permission).filter_by(id=row.permission_id).first().description for row in result
                ]
                return permissions
        except Exception as e:
            print(e)
            return None

    def get_all_users_with_permissions(self):
        try:
            with get_session() as session:
                # Fazemos o left join entre usuários e permissões
                result = session.query(User, Permission).outerjoin(
                    users_permissions, users_permissions.c.user_id == User.id
                ).outerjoin(
                    Permission, users_permissions.c.permission_id == Permission.id
                ).all()

                # Dicionário para agrupar permissões por usuário
                grouped_permissions = {}

                for user, permission in result:
                    if user.id not in grouped_permissions:
                        grouped_permissions[user.id] = {
                            "user_id": user.id,
                            "user_name": user.name,
                            "permissions": []
                        }
                    # Adiciona a permissão apenas se ela existir (caso do left join)
                    if permission:
                        grouped_permissions[user.id]["permissions"].append(permission.description)

                # Retornar apenas os valores do dicionário
                return list(grouped_permissions.values())

        except Exception as e:
            print(e)
            return None

    def update_user_permissions(self, user_id, permissions):
        try:
            with get_session() as session:
                # Obter permissões atuais do usuário
                current_permissions = {
                    row.permission_id for row in session.query(users_permissions).filter_by(user_id=user_id).all()
                }

                # Converter a lista de permissões para um conjunto
                new_permissions = set(permissions)

                # Identificar permissões para adicionar e remover
                to_add = new_permissions - current_permissions
                to_remove = current_permissions - new_permissions

                # Remover permissões desnecessárias
                if to_remove:
                    session.query(users_permissions).filter(
                        users_permissions.c.user_id == user_id,
                        users_permissions.c.permission_id.in_(to_remove)
                    ).delete(synchronize_session=False)

                # Adicionar permissões necessárias
                for permission_id in to_add:
                    session.execute(users_permissions.insert().values(user_id=user_id, permission_id=permission_id))

                session.commit()
                return True

        except Exception as e:
            print(e)
            return False

    def get_permission_id_by_name(self, permission_name):
        try:
            with get_session() as session:
                permission = session.query(Permission).filter_by(description=permission_name).first()
                return permission.id if permission else None
        except Exception as e:
            print(f"Erro ao buscar ID da permissão: {e}")
            return None

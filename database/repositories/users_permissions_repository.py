from database.config import RepositoryConfig, get_session
from database.models import users_permissions, Permission  # Importe o modelo User


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

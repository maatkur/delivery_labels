from typing import Optional
from database.config import RepositoryConfig, get_session
from database.models import User
from sqlalchemy.orm import joinedload
from helpers.encrypt_helper import EncryptHelper
from domain.entities import UserEntity


class UsersRepository(RepositoryConfig):
    def __init__(self):
        super().__init__(table_name="users")

    def create_user(self, user_data: dict) -> None:
        new_user = User(
            id=user_data["id"],
            name=user_data["name"].title(),
            password=EncryptHelper.encrypt_password(user_data["password"]),
        )
        self.execute_and_commit(new_user)

    def get_user_by_id(self, user_id: str) -> Optional[UserEntity]:
        # Use eager loading so that associated permissions are available
        # even after the session context is closed
        with get_session() as session:
            model = (
                session.query(User)
                .options(joinedload(User.permissions))
                .filter_by(id=user_id)
                .first()
            )
        if not model:
            return None
        # converte o SQLAlchemy model em Entity
        return UserEntity(
            id=model.id,
            name=model.name,
            password=model.password,
            created_at=model.created_at,
            updated_at=model.updated_at,
            permissions=[p.description for p in model.permissions],
        )

    def update_user(self, user_data: dict) -> None:
        filters = {"id": user_data["id"]}
        self.update(User, filters, user_data)

    def create_user_if_not_exists(self, user_data: dict) -> bool:
        if self.get_user_by_id(user_data["id"]):
            return False
        self.create_user(user_data)
        return True

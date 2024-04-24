from logging_config import configure_logger
from typing import Optional, List, Dict
from models import AbstractBaseUser, BaseManager

logger = configure_logger(__name__)

class User(AbstractBaseUser):
    pass

class UserManager(BaseManager):
    def add_item(self, name: str, user_id: str) -> None:
        try:
            self.items.append(User(name, user_id))
            logger.info(f"User added: {name}, {user_id}")
        except Exception as e:
            logger.error(f"Error adding user: {e}")

    def update_item(self, user_id: str, name: Optional[str] = None) -> bool:
        try:
            for user in self.items:
                if user.user_id == user_id:
                    if name:
                        user.name = name
                    logger.info(f"User updated: {user_id}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error updating user: {e}")
            return False

    def delete_item(self, user_id: str) -> bool:
        try:
            for user in self.items:
                if user.user_id == user_id:
                    self.items.remove(user)
                    logger.info(f"User deleted: {user_id}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error deleting user: {e}")
            return False

    def list_items(self) -> List[Dict[str, str]]:
        try:
            return [user.__dict__ for user in self.items]
        except Exception as e:
            logger.error(f"Error listing users: {e}")
            return []

    def search_items(self, name: Optional[str] = None, user_id: Optional[str] = None) -> Optional[User]:
        try:
            for user in self.items:
                if ((name and user.name == name) or
                    (user_id and user.user_id == user_id)):
                    return user
            return None
        except Exception as e:
            logger.error(f"Error searching users: {e}")
            return None

user_manager_object = UserManager()
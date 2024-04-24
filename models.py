from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict

class AbstractBaseUser:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    def __str__(self) -> str:
        return f"User ID: {self.user_id}, Name: {self.name}"
    

class BaseManager(ABC):
    def __init__(self):
        self.items: List[Any] = []

    @abstractmethod
    def add_item(self, item: Any) -> None:
        pass

    @abstractmethod
    def update_item(self, item_id: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def delete_item(self, item_id: Any) -> None:
        pass

    @abstractmethod
    def list_items(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def search_items(self, **kwargs: Any) -> Optional[Any]:
        pass
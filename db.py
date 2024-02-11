from typing import List

from model import Event
from storage import LocalStorage

class DBException(Exception):
    pass

class DB:
    def __init__(self):
        self._storage = LocalStorage()

    def create(self, event: Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Event:
        try:
            return self._storage.read(_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: Event):
        try:
            return self._storage.update(_id, event)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")

from typing import List

from model import Event
from db import DB

TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class Logic:
    def __init__(self):
        self._db = DB()

    @staticmethod
    def _validate(event: Event):
        if event is None:
            raise LogicException("event is None")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")


    def create(self, event: Event) -> str:
        self._validate(event)
        try:
            return self._db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Event:
        try:
            return self._db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: Event):
        self._validate(event)
        try:
            return self._db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")

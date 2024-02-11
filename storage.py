from typing import List
import time
from model import Event

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def _validate_date(self, event: Event):  # валидация даты - проверка ее структуры и уникальности
        try:
            date_valid = time.strptime(event.date, '%Y-%m-%d')
        except ValueError:
            raise StorageException('Invalid date (YYYY-MM-DD)')
        for stored in self._storage.values():
            if event.date == stored.date:
                raise StorageException('Only one event per day')

    def create(self, event: Event) -> str:
        self._validate_date(event) # валидация даты при создании
        self._id_counter += 1
        event._id = str(self._id_counter)
        self._storage[event._id] = event
        return event._id

    def list(self) -> List[Event]:
        return list(self._storage.values())

    def read(self, _id: str) -> Event:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, event: Event):
        # если это событие уже есть в бд, и мы не меняем его дату, тогда дату не валидируем
        if not (_id in self._storage and self._storage[_id].date == event.date):
            self._validate_date(event)
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        event._id = _id
        self._storage[event._id] = event

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        del self._storage[_id]

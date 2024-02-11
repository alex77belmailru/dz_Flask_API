from flask import Flask
from flask import request

from model import Event
from logic import Logic

_logic = Logic()

app = Flask(__name__)


class ApiException(Exception):
    pass


def _from_raw(raw: str) -> Event:  # Создание экземпляра Event из текста
    parts = raw.split('|')
    if len(parts) == 3:
        event = Event(parts[0], parts[1], parts[2])
        return event
    elif len(parts) == 4:
        event = Event(parts[0], parts[1], parts[2], parts[3])
        return event
    else:
        raise ApiException(f"invalid RAW event data {raw}")


API_ROOT = "/api/v1"
EVENT_API_ROOT = API_ROOT + "/calendar"


@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = _logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = _logic.list()
        raw_data = ""
        for event in events:
            raw_data += str(event) + '\n'
        return raw_data, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        event = _logic.read(_id)
        raw_data = str(event)
        return raw_data, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _logic.update(_id, event)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404

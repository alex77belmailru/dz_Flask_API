## запуск приложения

```
python server.py
```


## cURL тестирование

### добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "YYYY-MM-DD|title|text"
```

### получение всего списка событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление события по идентификатору / ID == 1 
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "new date|new title|new text"
```

### удаление события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-02-12|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-02-12|title1|text1"
failed CREATE operation with: Only one event per day

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2024-02-12|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2024-02-12|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-02-13|title|text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-02-13|title|loo .. oooong text"
failed to UPDATE with: text lenght > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-02-13|loo .. oong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --
```
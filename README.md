 ```docker run -d -p 8000:80 -v todo_data:/app/data rushawx/todo-service:latest```

TODO-сервис:
 <li> POST/items: Создание задачи (title, description?, completed=false) </li>
 <li> GET/items: Получение списка всех задач </li>
 <li> GET/items/{item_id}: Получение задачи по ID </li>
 <li> PUT/items/{item_id}: Обновление задачи по ID </li>
 <li> DELETE/items/{item_id}: Удаление задачи.</li>
 <li> Все операции должны работать с базой SQLite </li>
 <li> Перед запуском автоматически создается таблица, если она не
 существует </li>

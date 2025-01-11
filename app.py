from main import add  # Импортируем задачу из main.py

# Запуск задачи через Celery
result = add.delay(4, 6)  # Используем delay для асинхронного выполнения задачи
print(result.get())  # Получаем результат (блокирует выполнение до получения ответа)
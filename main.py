from celery import Celery

# Создание экземпляра Celery с настройками для брокера и результатного бэкенда
app = Celery("main", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

# Пример задачи
@app.task
def add(x, y):
    return x + y

# Для запуска Celery worker
if __name__ == '__main__':
    app.start()
    
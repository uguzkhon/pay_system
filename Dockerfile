#какой язык программирования
FROM python:latest



# копирования всех файлов во внутрь контейнера
COPY . /code

# Назначить основную папку
WORKDIR /code

# установка библиотек
RUN pip install -r requirements.txt

# Запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]
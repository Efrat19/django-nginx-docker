FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install Django psycopg2
COPY . /code/
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
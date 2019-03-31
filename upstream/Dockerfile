FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Django psycopg2
COPY . /code/
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

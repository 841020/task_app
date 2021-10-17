FROM python:3

WORKDIR /web
COPY requirements.txt /web/
COPY . /web/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
CMD gunicorn --bind 0.0.0.0:${PORT:-8000} "app:create_app()"
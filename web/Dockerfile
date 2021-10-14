FROM python:3

WORKDIR /web
COPY requirements.txt /web/
COPY . /web/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python models.py
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
CMD ["gunicorn","--bind", "0.0.0.0:8000" , "app:app"]
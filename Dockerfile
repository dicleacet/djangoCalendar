FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /djangoCalendar
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python:3.9.6

WORKDIR /opt/app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "slavik_test/manage.py", "runserver", "0.0.0.0:8000"]
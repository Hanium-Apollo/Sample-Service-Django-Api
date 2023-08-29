FROM python:3
WORKDIR /app/src

## Install packages
COPY requirements.txt ./
COPY .env ./
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

EXPOSE 8080

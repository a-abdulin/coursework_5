FROM python:3.11

WORKDIR /course5
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


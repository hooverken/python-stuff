FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY go.sh .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "bash", "go.sh" ]
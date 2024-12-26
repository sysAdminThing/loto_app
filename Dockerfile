FROM python:3.10
LABEL authors="AmalMuradov"

WORKDIR /LOTO_APP

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=6006"]


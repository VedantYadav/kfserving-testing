FROM python:3.8-buster

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR /app
COPY . ./

RUN pip install -r requirements.txt

ENV TF_CPP_MIN_LOG_LEVEL=2

CMD ["python", "./src/compute.py"]

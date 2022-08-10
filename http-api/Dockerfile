FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./settings.toml ./

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

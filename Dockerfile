FROM python:slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD uvicorn workout_api.main:app --reload

CMD ["uvicorn", "workout_api.main:app","--host", "0.0.0.0","--port", "8000", "--log-level", "info", "--reload"]


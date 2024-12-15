FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/app/data"]

ENV PYTHONUNBUFFERED=1

ENV DB_URL="sqlite:///app/data/items.db"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

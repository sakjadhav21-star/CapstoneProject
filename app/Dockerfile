FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 1. Point to the correct folder path on your repository
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the rest of the contents from the app folder into Docker's /app directory
COPY app/ .

EXPOSE 5000

# 3. Cleaned up CMD (Conflict markers removed)
CMD ["python", "app.py"]


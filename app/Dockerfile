FROM python:3.11-slim

WORKDIR /app

# Upgrade system packages to resolve base OS vulnerabilities
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel, and jaraco.context to resolve Python-specific vulnerabilities
RUN pip install --no-cache-dir --upgrade pip setuptools wheel jaraco.context

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

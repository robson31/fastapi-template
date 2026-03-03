# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for building packages
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only dependency file to cache
COPY pyproject.toml ./

# Upgrade pip/setuptools/wheel
RUN pip install --upgrade pip setuptools wheel

# Install dependencies non-editable (more reliable inside Docker)
RUN pip install ".[dev]"

# Copy all app code
COPY app ./app

# Expose port
EXPOSE 8000

# Run uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
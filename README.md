# Scalable FastAPI Service

A **scalable Python backend template** built with **FastAPI**.  
This project serves as a foundation for developing **robust, production-ready APIs** with a modular structure and clean architecture.

## Features
- Modular FastAPI application structure
- Example router and endpoint
- Dockerized deployment for easy setup
- Ready for extension into larger systems
- Auto-generated API docs via Swagger UI (`/docs`) and ReDoc (`/redoc`)

## Tech Stack
- **Python 3.11+**
- **FastAPI** – high-performance API framework
- **Uvicorn** – ASGI server
- **Docker** – containerization for portability and deployment

## Getting Started

### 1. Clone the repository
```bash
git clone git@github.com:robson31/fastapi-template.git
cd fastapi-template
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
uvicorn app.main:app --reload
```

### 4. Run with Docker
```bash
docker build -t fastapi-template .
docker run -p 8000:8000 fastapi-template
```

# FastAPI MySQL Docker Project

A FastAPI project blueprint with MySQL database running in Docker containers.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone repository:
```bash
git clone https://github.com/mario1870/fastapi-mysql-docker.git
cd fastapi-mysql-docker
```

2. Add a .env file
```bash
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_HOST=db
MYSQL_DATABASE=fastapi_db
MYSQL_ROOT_PASSWORD=root_password
```

3. Start application
```bash
make up
```

## Development Setup

1. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r src/requirements.txt
```

## API Endpoints
The API is available at http://localhost:8000.

- GET /users/: List all users  
- POST /users/: Create new user

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Useful Commands

- Stop containers:  
`make down`

- View logs:  
`make logs`

- Python Shell:  
`make shell`

- MySQL Shell:  
`make db-shell`

- Freeze dependencies:  
`make freeze`
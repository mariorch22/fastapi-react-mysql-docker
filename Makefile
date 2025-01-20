.PHONY: build run stop clean logs shell db-shell test

# Build the containers
build:
	docker-compose build

# Run the containers
up:
	docker-compose up --build -d

# Stop the containers
down:
	docker-compose down

# Remove all containers and volumes
clean:
	docker-compose down -v
	docker system prune -f

# View logs
logs:
	docker-compose logs

# Shell into web container
backend-shell:
	docker exec -it backend /bin/bash

frontend-shell:
	docker exec -it frontend bash

# Shell into MySQL container
db-shell:
	docker exec -it web_container mysql -uuser -ppassword fastapi_db

# Requirements
freeze:
	pip freeze > src/requirements.txt
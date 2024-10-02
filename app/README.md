# Project Title

## Description

This project is a Django application that provides an API for managing teams and people. It is built using Django Rest Framework and uses PostgreSQL as the database.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker
- Docker Compose

## Setup
с
To get started, follow these steps:

1. **Create a `.env` file** in the root directory of the project with the following variables:

   ```plaintext
   POSTGRES_HOST=your_postgres_host
   POSTGRES_USER=your_postgres_user
   POSTGRES_NAME=your_postgres_database_name
   POSTGRES_PASSWORD=your_postgres_password

2. **Build and run the application** using Docker Compose. Execute the following command in your terminal:

   ```bash
   docker-compose up --build

3. **Access the Swagger UI documentation** by visiting the following URL in your web browser:

   [http://127.0.0.1/api/schema/swagger-ui](http://127.0.0.1/api/schema/swagger-ui)

   This will allow you to explore the API endpoints and see the available functionalities provided by the application.

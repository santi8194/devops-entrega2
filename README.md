# Blacklist API Service

This project provides a simple and efficient microservice for managing a blacklist of email addresses. It is built with Python and Flask, offering a RESTful API to add and query blacklisted emails.

## Project Overview

The Blacklist API is designed to be a modular and scalable solution for applications that need to check against a list of blocked email addresses. It includes authentication for protected endpoints and provides a health check for monitoring.

## Features

- **Add to Blacklist**: Add an email to the blacklist with a reason.
- **Check Blacklist**: Verify if an email is on the blacklist.
- **Authentication**: Secure endpoints using token-based authentication.
- **Health Check**: A simple endpoint to monitor the service's status.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/santi8194/devops-entrega2.git
    cd devops-entrega2
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the Flask development server, run the following command:

```bash
python application.py
```

The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Health Check

- **GET /**: Checks the health of the service.
  - **Response (200 OK)**:
    ```json
    {
      "status": "ok"
    }
    ```

### Create Blacklist Entry

- **POST /blacklists**: Adds a new email to the blacklist.
  - **Headers**:
    - `Authorization`: `Bearer <token>`
  - **Body**:
    ```json
    {
      "email": "user@example.com",
      "reason": "Reason for blacklisting"
    }
    ```
  - **Response (201 Created)**:
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "reason": "Reason for blacklisting",
      "created_at": "2023-10-28T12:00:00Z"
    }
    ```

### Get Blacklist Status

- **GET /blacklists/<email>**: Retrieves the blacklist status for a specific email.
  - **Headers**:
    - `Authorization`: `Bearer <token>`
  - **Response (200 OK)**:
    ```json
    {
      "is_blacklisted": true,
      "reason": "Reason for blacklisting"
    }
    ```

## Project Structure

The project is organized into the following main components:

- `application.py`: The main Flask application entry point.
- `requirements.txt`: A list of Python dependencies.
- `blacklists/`: The core application module.
  - `src/blueprints/`: Contains Flask blueprints for routing.
  - `src/commands/`: Business logic for handling requests.
  - `src/models/`: Defines the database models.
  - `src/errors/`: Custom error handling.
- `tests/`: Contains unit and integration tests.

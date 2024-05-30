# E-Commerce Backend - File Upload API

## Overview

This project provides an API to upload static files (image, PDF, video, or any binary file) with encryption. The stored files are not directly readable from the public path.

## Features

- File upload API
- File encryption using AES
- Public URL generation for uploaded files
- Flask-based application
- Dockerized for easy deployment
- Unit tests for API and encryption

## Setup

### Prerequisites

- Docker
- Docker Compose

### Installation


    ```

!. Generate an encryption key:
    ```sh
    python -c "from app.encryption import generate_key, save_key; save_key(generate_key())"
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

4. The application will be available at `http://127.0.0.1:8000/`.

### Run this application
-uvicorn app.main:app

### Usage

- To upload a file, send a POST request to `http://localhost:5000/upload` with the file in the form-data.
- To download a file, send a GET request to `http://localhost:5000/files/<filename>`.

### Running Tests

To run the unit tests:

```sh
pytest

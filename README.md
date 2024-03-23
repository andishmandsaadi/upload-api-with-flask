# Flask File Upload API

This Flask API provides an endpoint for uploading files securely. It supports multiple file formats and ensures that only allowed file types are processed. The API is designed to be simple yet effective, with clear error messages and HTTP status codes for various outcomes.

## Features

- File upload via POST request.
- Support for multiple file extensions: webp, png, jpg, jpeg, gif, svg.
- Secure filename processing.
- JSON responses with appropriate HTTP status codes.
- UUID based unique naming for uploaded files.

## Requirements

- Flask
- Werkzeug
- Python 3.6+

## Getting Started

### Installation

First, clone the repository and navigate to the project directory:

`git clone [https://github.com/andishmandsaadi/upload-api-with-flask](https://github.com/andishmandsaadi/upload-api-with-flask)`

`cd upload-api-with-flask`


Install the required Python packages:

`pip install Flask Werkzeug`


### Running the Application

To run the application, execute:

`python uploadapi.py`


The API server will start, and you can access it via `http://localhost:8989`.

## Usage

To upload a file, send a POST request to `/upload` with the file included in the form data. The file form field should be named `file`.

Example using `curl`:

`curl -X POST -F "file=@path/to/your/file.jpg" http://localhost:8989/upload`


### Responses

- **Success**: Returns a JSON object with the URL of the uploaded file.
  - Status Code: 200
  - Example: `{"url": "uploadsNew/uniquefilename.jpg"}`
- **No file part**: If the file part is missing from the request.
  - Status Code: 400
  - Example: `{"error": "No file part"}`
- **No file name**: If no file name is provided.
  - Status Code: 400
  - Example: `{"error": "No file name"}`
- **File not allowed**: If the file extension is not in the allowed list.
  - Status Code: 400
  - Example: `{"error": "File not allowed"}`

## Deployment

For production environments, it's recommended to deploy the Flask application using a more robust WSGI server like Gunicorn or uWSGI behind a reverse proxy like Nginx.

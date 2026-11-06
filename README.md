# Lab 2: Web Server Lab

**Course:** Essentials of Health Informatics

## About

This project implements a TCP web server in Python as part of Lab 2 for Essentials of Health Informatics.

The server accepts HTTP GET requests over a TCP socket, parses the requested filename, reads the file from the server's own directory, and sends back an HTTP response with the file contents preceded by a `200 OK` header. If the requested file does not exist, the server replies with an `HTTP/1.1 404 Not Found` message.

## Features

- TCP communication using Python's `socket` module
- Parses the filename from the incoming HTTP GET request
- Serves any HTML file located in the server's directory
- Returns `HTTP/1.1 200 OK` with the file contents when the file exists
- Returns `HTTP/1.1 404 Not Found` when the file is missing
- Handles one HTTP request at a time
- Informative console messages for each request and response

## Project Structure

```text
web-server-lab/
├── server.py
├── HelloWorld.html
└── lab2-screenshot.png
```

## Requirements

- Python 3
- A web browser (for testing)

## How to Run

Open a terminal in the project directory.

### 1. Start the server

```bash
python server.py
```

The server will begin listening on port 6789.

### 2. Open the page in a browser

Navigate to:

```text
http://127.0.0.1:6789/HelloWorld.html
```

The browser will display the contents of HelloWorld.html.

### 3. Request a missing file

Navigate to:

```text
http://127.0.0.1:6789/DoesNotExist.html
```

The browser will display the 404 Not Found message.

## Example

For a successful request to /HelloWorld.html, the server sends:

```text
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head><title>Hello World</title></head>
<body><h1>Hello World!</h1></body>
</html>
```

For a request to a file that does not exist, the server sends:

```text
HTTP/1.1 404 Not Found

<html><body><h1>404 Not Found</h1></body></html>
```

## Technologies

- Python 3
- TCP sockets
- HTTP

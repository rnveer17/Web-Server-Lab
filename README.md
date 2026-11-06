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
└── HelloWorld.html
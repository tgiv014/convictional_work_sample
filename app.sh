#!/bin/sh

# Per Flask's documentation, using the built-in dev server to host is bad.
# We'll use gunicorn instead
gunicorn --chdir /app app:app -w 2 --threads 2 -b 0.0.0.0:5000

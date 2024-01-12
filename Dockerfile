FROM python:3.11-slim

# Define virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY . /app
WORKDIR /app
CMD gunicorn wsgi:app --bind 0.0.0.0:8080 --log-level=debug --workers=2

EXPOSE 8080
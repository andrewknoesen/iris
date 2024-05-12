FROM python:3.12
# FROM --platform=linux/arm64/v8 python:3.11

LABEL maintainer="Andrew Knoesen"

WORKDIR /app

# Installs python, removes cache file to make things smaller
RUN apt update -y
RUN rm -Rf /var/cache/apt

# Copy over poetry files
COPY ./pyproject.toml .
COPY ./poetry.lock .

# Install poetry
# RUN pip install poetry && poetry install --only main
RUN pip install poetry && poetry install --only main --no-root --no-directory

# Copy contents to root
COPY  ./iris_api/ ./iris_api/

# Copy over pickle file
COPY ./pkl ./pkl 

#Set up flask app
EXPOSE 5000
ENV FLASK_APP=./iris_api/app.py
CMD ["poetry", "run", "python", "./iris_api/app.py"]

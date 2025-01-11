FROM python:3.11.11-bullseye

# set workdir in docker
WORKDIR /app
COPY . .

# set env variables
# do not create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensures that the python output i.e. the stdout and stderr streams are sent straight to terminal without being first buffered
ENV PYTHONUNBUFFERED 1

# install requirements
RUN pip install -r requirements.txt --no-cache-dir

# Specify the command to run on container start
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
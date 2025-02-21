
FROM python:3.13

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY pubClient.py ./
COPY Sensors/ ./Sensors/
# COPY .env ./

# To install the dependencies
RUN pip install --no-cache-dir paho-mqtt python-dotenv loguru

# Ensure Logs directory exists
RUN mkdir -p ./Logs

CMD ["python", "pubClient.py"]
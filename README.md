# OrderFlow - Distributed Order Processing System

## Overview
OrderFlow is a scalable distributed system built using **Flask (Python), PostgreSQL, and Kafka**. It provides a microservices-based order management system, supporting **real-time data processing, inventory updates, and high availability** using asynchronous Kafka messaging.

## Features
- **Flask Microservices Architecture** with structured logging.
- **Kafka Integration** for real-time order and inventory updates.
- **PostgreSQL Database** for storing order details.
- **Docker & Docker Compose** for simplified deployment.
- **Kafka Consumer** for background order processing.

## Project Structure
```
OrderFlow/
├── app/
│   ├── __init__.py        # Flask app initialization
│   ├── routes.py         # Flask routes for order processing
│   ├── kafka_utils.py    # Kafka producer & consumer logic
│   ├── db_utils.py       # Database connection utilities
├── config/
│   ├── kafka_config.py   # Kafka configurations
│   ├── db_config.py      # PostgreSQL configurations
├── tests/
│   ├── test_routes.py    # Unit tests for routes
│   ├── test_kafka.py     # Unit tests for Kafka messaging
│   ├── test_db.py        # Unit tests for database interactions
├── docker-compose.yml    # Dockerized setup for Kafka, PostgreSQL
├── Dockerfile            # Dockerfile to containerize the app
├── requirements.txt      # Dependencies list
├── main.py               # Application entry point
└── README.md             # This file
```

## Installation
### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **Docker & Docker Compose**

### Setup & Run
```sh
git clone https://github.com/YOUR_GITHUB/OrderFlow.git
cd OrderFlow

# Install dependencies
pip install -r requirements.txt

# Start the services using Docker Compose
docker-compose up --build

# Alternatively, run the Flask app manually
python main.py
```

## API Endpoints
### 1. Create Order
**POST** `/order`
```json
{
    "order_id": "12345",
    "item": "Laptop",
    "quantity": 1
}
```
_Response:_
```json
{"message": "Order received, stored in DB, and sent to Kafka"}
```

### 2. Update Inventory
**POST** `/inventory`
```json
{
    "item": "Laptop",
    "stock": 100
}
```
_Response:_
```json
{"message": "Inventory update received and sent to Kafka"}
```

### 3. Get Orders
**GET** `/orders`
_Response:_
```json
[
    {"order_id": "12345", "item": "Laptop", "quantity": 1}
]
```

## Next Steps
- **Add JWT Authentication** for securing API endpoints.
- **Implement Kafka Retry Mechanism** for message failures.
- **Optimize Database Queries** for faster retrievals.

## Contributors
- [Hruthwik Krishnamurthy](https://github.com/hruthwikkk)


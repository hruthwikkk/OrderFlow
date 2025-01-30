from kafka import KafkaProducer, KafkaConsumer
import threading
import json

KAFKA_BROKER_URL = 'localhost:9092'
ORDER_TOPIC = 'order_topic'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

def order_consumer():
    consumer = KafkaConsumer(
        ORDER_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        process_order(message.value)

def process_order(order):
    print(f"Processing order: {order}")

# Run consumer in a separate thread
threading.Thread(target=order_consumer, daemon=True).start()

from flask import Blueprint, jsonify, request
from app.kafka_utils import producer
from app.db_utils import get_db_connection
import logging

bp = Blueprint('routes', __name__)

ORDER_TOPIC = 'order_topic'
INVENTORY_TOPIC = 'inventory_topic'

logging.basicConfig(level=logging.INFO)

@bp.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    producer.send(ORDER_TOPIC, bytes(str(order_data), 'utf-8'))

    # Save order to database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (order_id, item, quantity) VALUES (%s, %s, %s)",
        (order_data['order_id'], order_data['item'], order_data['quantity'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    logging.info(f"Order {order_data['order_id']} processed.")
    return jsonify({'message': 'Order received, stored in DB, and sent to Kafka'}), 200

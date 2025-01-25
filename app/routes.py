
from flask import Blueprint, jsonify, request
from app.kafka_utils import producer
from app.db_utils import get_db_connection

bp = Blueprint('routes', __name__)

ORDER_TOPIC = 'order_topic'
INVENTORY_TOPIC = 'inventory_topic'

@bp.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    producer.send(ORDER_TOPIC, bytes(str(order_data), 'utf-8'))
    return jsonify({'message': 'Order received and sent to Kafka'}), 200

@bp.route('/inventory', methods=['POST'])
def update_inventory():
    inventory_data = request.json
    producer.send(INVENTORY_TOPIC, bytes(str(inventory_data), 'utf-8'))
    return jsonify({'message': 'Inventory update received and sent to Kafka'}), 200

@bp.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders), 200

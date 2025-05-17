from flask import Flask, request, jsonify
from mt5_client import MT5Client
import threading

app = Flask(__name__)
mt5 = MT5Client()

@app.route('/api/order', methods=['POST'])
def handle_order():
    data = request.json
    result = mt5.place_order(
        symbol=data['symbol'],
        lot=data['lot'],
        order_type=data['type']
    )
    return jsonify({"status": "success", "result": result._asdict()})

if __name__ == '__main__':
    app.run(port=5000)
import os
from flask import Flask, jsonify, request
from ib_insync import IB, Stock
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
ib = IB()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/connect', methods=['POST'])
def connect_ib():
    try:
        host = request.json.get('host', '127.0.0.1')
        port = request.json.get('port', 7497)
        client_id = request.json.get('client_id', 1)
        
        ib.connect(host, port, clientId=client_id)
        return jsonify({"status": "connected"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disconnect', methods=['POST'])
def disconnect_ib():
    try:
        ib.disconnect()
        return jsonify({"status": "disconnected"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/quote/<symbol>', methods=['GET'])
def get_quote(symbol):
    try:
        if not ib.isConnected():
            return jsonify({"error": "Not connected to IB"}), 400
            
        stock = Stock(symbol, 'SMART', 'USD')
        ib.qualifyContracts(stock)
        ticker = ib.reqMktData(stock)
        ib.sleep(2)
        
        return jsonify({
            "symbol": symbol,
            "bid": ticker.bid,
            "ask": ticker.ask,
            "last": ticker.last
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
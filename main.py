import os
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GATEWAY_BASE_URL = os.getenv('GATEWAY_BASE_URL', 'http://localhost:5000/v1/api')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    try:
        # 1. Extract IBKR credentials from the request's Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Missing Authorization header"}), 401

        # 2. Prepare the request to the Gateway
        url = f"{GATEWAY_BASE_URL}/portfolio/accounts"
        
        # 3. Forward the auth header directly to the IBKR Gateway
        headers = {'Authorization': auth_header}
        
        # 4. Make the HTTP request to the Gateway
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        portfolio_data = response.json()

        return jsonify(portfolio_data)

    except requests.exceptions.HTTPError as e:
        # Handle IBKR authentication errors (e.g., 401 from the Gateway)
        return jsonify({"error": "IBKR Authentication failed"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
# Interactive Brokers API Gateway

A Flask-based API gateway for Interactive Brokers TWS/Gateway, designed for Google Cloud deployment.

## Setup

1. Copy `.env.example` to `.env` and configure your IB connection settings
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `python main.py`

## Docker

Build: `docker build -t ibkr-api-gateway .`
Run: `docker run -p 8080:8080 -e IB_HOST=host.docker.internal ibkr-api-gateway`

**Note**: The container runs IB Gateway headlessly. For initial setup, you may need to configure credentials outside the container first.

## Google Cloud Deployment

1. Set your project: `gcloud config set project YOUR_PROJECT_ID`
2. Deploy: `gcloud builds submit --config cloudbuild.yaml`

## API Endpoints

- `GET /health` - Health check
- `POST /connect` - Connect to IB TWS/Gateway
- `POST /disconnect` - Disconnect from IB
- `GET /quote/<symbol>` - Get market data for symbol
# Interactive Brokers API Gateway

A Flask-based API gateway for Interactive Brokers Client Portal Gateway, designed for multi-user support and Google Cloud deployment.

## Development Setup

### Docker Compose (Recommended)
```bash
docker-compose up --build
```
This starts both Client Portal Gateway (port 5000) and API service (port 8080) with live file mapping.

### Manual Setup
1. Copy `.env.example` to `.env`
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `python main.py`

## Docker Production

Build: `docker build -t ibkr-api-gateway .`
Run: `docker run -p 5000:5000 -p 8080:8080 ibkr-api-gateway`

## Authentication

1. Navigate to `https://localhost:5000` to authenticate with IBKR
2. Use the session for API calls with Authorization header

## Google Cloud Deployment

1. Set your project: `gcloud config set project YOUR_PROJECT_ID`
2. Deploy: `gcloud builds submit --config cloudbuild.yaml`

## API Endpoints

- `GET /health` - Health check
- `GET /portfolio` - Get portfolio data (requires Authorization header)
- Client Portal Gateway: `https://localhost:5000`
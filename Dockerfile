FROM openjdk:11-jre-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip wget unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Download Client Portal Gateway
RUN wget -O clientportal.gw.zip https://download2.interactivebrokers.com/portal/clientportal.gw.zip \
    && unzip clientportal.gw.zip \
    && rm clientportal.gw.zip

# Copy application files
COPY . .

EXPOSE 5000 8080

CMD ["bash", "start-services.sh"]
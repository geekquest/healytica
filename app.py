from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/health', methods=['GET'])
def health_check():
    try:
        # Simulate health check logic here
        logging.info("Performing health check")
        return jsonify({'status': 'healthy'}), 200
    except Exception as e:
        logging.error("Error during health check: %s", e, exc_info=True)
        return jsonify({'error': 'Health check failed'}), 500

if __name__ == '__main__':
    try:
        logging.info("Starting Healytica app on port 8080")
        app.run(host='0.0.0.0', port=8080)
    except Exception as e:
        logging.error("Failed to start Healytica app: %s", e, exc_info=True)
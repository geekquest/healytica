from sqlalchemy import create_engine
from pymongo import MongoClient
import redis
import logging
from config import POSTGRESQL_URI, MONGODB_URI, REDIS_URI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def test_postgresql_connection():
    try:
        engine = create_engine(POSTGRESQL_URI)
        connection = engine.connect()
        connection.close()
        logging.info("Connected to PostgreSQL successfully.")
    except Exception as e:
        logging.error("Failed to connect to PostgreSQL: %s", e, exc_info=True)

def test_mongodb_connection():
    try:
        client = MongoClient(MONGODB_URI)
        client.server_info()  # Forces a call.
        logging.info("Connected to MongoDB successfully.")
    except Exception as e:
        logging.error("Failed to connect to MongoDB: %s", e, exc_info=True)

def test_redis_connection():
    try:
        r = redis.Redis.from_url(REDIS_URI)
        r.ping()
        logging.info("Connected to Redis successfully.")
    except Exception as e:
        logging.error("Failed to connect to Redis: %s", e, exc_info=True)

def test_db_connections():
    test_postgresql_connection()
    test_mongodb_connection()
    test_redis_connection()

if __name__ == '__main__':
    test_db_connections()
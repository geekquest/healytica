import os

# PostgreSQL Configuration
POSTGRESQL_URI = os.getenv('POSTGRESQL_URI', 'postgresql://username:password@localhost/dbname')  # INPUT_REQUIRED {Replace 'username:password@localhost/dbname' with your actual PostgreSQL connection string}

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/dbname')  # INPUT_REQUIRED {Replace 'mongodb://localhost:27017/dbname' with your actual MongoDB connection string}

# Redis Configuration
REDIS_URI = os.getenv('REDIS_URI', 'redis://localhost:6379')  # INPUT_REQUIRED {Replace 'redis://localhost:6379' with your actual Redis connection URI}
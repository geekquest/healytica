const mongoose = require('mongoose');
const logger = require('../utils/logger');

// Load environment variables
require('dotenv').config();

const mongoURI = process.env.MONGO_URI || 'mongodb://localhost:27017/healytica_core_platform'; // INPUT_REQUIRED {Provide your MongoDB URI replacing the default URI if needed}

const connectToMongoDB = async () => {
  try {
    await mongoose.connect(mongoURI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
      useFindAndModify: false,
    });
    logger.info('Connected to MongoDB');
  } catch (error) {
    logger.error(`MongoDB connection error: ${error.message}`, error);
    // Exit process with failure
    process.exit(1);
  }
};

module.exports = connectToMongoDB;
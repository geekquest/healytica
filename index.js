require('dotenv').config();
const express = require('express');
const logger = require('./src/utils/logger');
const connectToMongoDB = require('./src/config/mongodb');
const routes = require('./src/api/routes/routes');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/ping', (req, res) => {
  logger.info('Ping route was called.');
  res.status(200).send('Server is running');
});

app.use(routes);

app.use((req, res, next) => {
  res.status(404).send("Sorry can't find that!");
  logger.warn(`404 - Not Found - ${req.originalUrl} - ${req.method} - ${req.ip}`);
});

app.use((err, req, res, next) => {
  logger.error(`500 - ${err.message} - ${req.originalUrl} - ${req.method} - ${req.ip}`);
  res.status(500).send('Something broke!');
  next(err);
});

connectToMongoDB().then(() => {
  app.listen(PORT, () => {
    logger.info(`Server is running on port ${PORT}`);
  });
}).catch((err) => {
  logger.error('Failed to connect to MongoDB', err);
  process.exit(1);
});
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const sampleMiddleware = require('../middlewares/sampleMiddleware');

router.use((req, res, next) => {
    console.log(`Incoming request: ${req.method} ${req.path}`);
    next();
});

router.post('/api/users/register', sampleMiddleware, userController.register);

module.exports = router;
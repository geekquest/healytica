module.exports = (req, res, next) => {
  console.log('Sample middleware in action');
  next(); // Pass control to the next middleware/function
};
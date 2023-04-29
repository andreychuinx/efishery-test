const jwt = require('jsonwebtoken')

module.exports = {
  generatePassword: (length) => {
    const charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let password = '';
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset[randomIndex];
    }
    return password;
  },
  generateJWT: async (data) => {
    return new Promise((resolve, reject) => {
      jwt.sign(data, process.env.JWT_SECRET, (err, token) => {
        if (err) reject(err);
        resolve(token)
      })
    })
  }

}
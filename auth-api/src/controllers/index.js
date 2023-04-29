const { readFile } = require('../models')

class AuthController {
  async register(req, res) {
    const data = await readFile()
    console.log(data)
  }
}

module.exports = AuthController
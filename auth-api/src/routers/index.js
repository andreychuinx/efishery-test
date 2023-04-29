const express = require('express')
const Router = express.Router()
const Controller = require('../controllers')

const authController = new Controller()

Router.post('/register', authController.register)

module.exports = Router;
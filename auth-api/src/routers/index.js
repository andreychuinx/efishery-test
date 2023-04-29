const express = require('express')
const Router = express.Router()
const AuthController = require('../controllers')

const authController = new AuthController()

Router.post('/register', authController.register)
Router.post('/login', authController.login)

module.exports = Router;
const express = require('express')
const Router = express.Router()
const AuthController = require('../controllers')

const authController = new AuthController('User')

Router.post('/register', authController.register)

module.exports = Router;
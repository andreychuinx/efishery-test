const express = require('express')
const Router = express.Router()

Router.post('/register', Controller.postRegister)

module.export = Router;
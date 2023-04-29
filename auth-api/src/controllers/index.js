const Joi = require('joi')
const { readFile, writeFile } = require('../models')
const { dataSet: { User } } = require('../config/enum')
const { generatePassword, generateJWT } = require('../helpers')
class AuthController {
  static registerValidation = Joi.object({
    phone: Joi.number().min(12).required(),
    name: Joi.string().required(),
    role: Joi.string().required().valid('admin', 'member').messages({
      'any.required': 'Role is required',
      'any.only': 'Roles not valid',
      'string.base': 'The type field must be a string',
    })
  })

  static loginValidation = Joi.object({
    phone: Joi.number().min(12).required(),
    password: Joi.string().required()
  })

  async register(req, res) {
    const body = req.body
    try {
      await AuthController.registerValidation.validateAsync(body)
      let data = await readFile(User)
      const checkPhone = data.findIndex(dt => dt.phone === body.phone)
      if (checkPhone === -1) {
        let result = { ...body, date_registry: new Date(), password: generatePassword(8) }
        data.push(result)
        await writeFile(User, data)
        res.status(200).json(result)
      } else {
        const { password, ...result } = data[checkPhone]
        res.status(200).json(result)
      }
    } catch (err) {
      let newErr = {}
      if (err.name && err.name === 'ValidationError') {
        newErr.code = 400
        newErr.message = err.details[0].message
      } else {
        newErr.code = 400
        newErr.message = err.message
      }
      res.status(newErr.code).json({ message: newErr.message })

    }
  }

  async login(req, res) {
    const body = req.body
    try {
      await AuthController.loginValidation.validateAsync(body)
      const data = await readFile(User)
      const checkPhone = data.findIndex(dt => dt.phone === body.phone)
      if (checkPhone === -1) throw new Error('Phone Not Found')
      if (data[checkPhone].password !== body.password) throw new Error ('Wrong Password')
      const jwt = await generateJWT(data[checkPhone])
      const { password, ...result } = data[checkPhone]
      res.status(200).json({
        ...result,
        token: jwt
      })
    } catch (err) {
      let newErr = {}
      if (err.name && err.name === 'ValidationError') {
        newErr.code = 400
        newErr.message = err.details[0].message
      } else {
        newErr.code = 400
        newErr.message = err.message
      }
      res.status(newErr.code).json({ message: newErr.message })

    }
  }

}

module.exports = AuthController
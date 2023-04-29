require('dotenv').config()
const express = require('express')
const app = express()
const bodyParser = require('body-parser')

const routes = require('./src/routers')

app.use(bodyParser.json())

app.get('/api', (req, res) => {
  res.json({
    test: 'test'
  })
})

app.use((req, res, next) => {
  res.status(404).send('Page not found')
  next()
})

app.listen(3000, () => {
  console.log('Server Started on port 3000')
})
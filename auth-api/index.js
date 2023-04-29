require('dotenv').config()
const express = require('express')
const app = express()
const bodyParser = require('body-parser')

const routes = require('./src/routers')
const middlewares = require('./src/middlewares')

app.use(bodyParser.json())

app.use('/api', routes)

app.use((req, res, next) => {
  res.status(404).send('Page not found')
  next()
})

const startServer = async () => {
  const port = process.env.PORT || 3000;
  app.listen(port, async () => {
    await middlewares.checkDataSet()
    /*no-console*/
    console.log(`Server started on port ${port}`)// eslint-disable-line
  } )
}

startServer()
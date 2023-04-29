const fs = require('fs').promises

const readFile = async () => {
  try {
    const readData = await fs.readFile('../databases/User.json', 'utf-8') 
    console.log(readData, 'ini')
    return readData
  } catch (error) {
    console.log(error)
    // return new Error(error)
  }
}

module.exports = {
  readFile
}
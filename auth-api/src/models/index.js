const fs = require('fs').promises

const readFile = async (dataSet) => {
  try {
    const readData = await fs.readFile(`./src/databases/${dataSet}.json`, 'utf-8')
    return JSON.parse(readData)
  } catch (error) {
    throw new Error(error)
  }
}

const writeFile = async (dataSet, data) => {
  try {
    await fs.writeFile(`./src/databases/${dataSet}.json`, JSON.stringify(data))
    return true
  } catch (err) {
    throw new Error(error)
  }
  
}

module.exports = {
  readFile,
  writeFile
}
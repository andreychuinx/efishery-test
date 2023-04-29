const fs = require('fs').promises
const { dataSet } = require('../config/enum')

const checkDataSet = async () => {
  for (let dataName in dataSet) {
    try {
      await fs.access(`./src/databases/${dataSet[dataName]}.json`)
    } catch (err) {
      await fs.writeFile(`./src/databases/${dataSet[dataName]}.json`, '[]')
    }
  }
  return;

}

module.exports = {
  checkDataSet
}
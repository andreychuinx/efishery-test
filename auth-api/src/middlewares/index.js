const fs = require('fs').promises

const checkUserDb = async () => {
  try {
    await fs.readFile('./src/databases/User.json', 'utf-8')
  } catch (err) {
    console.log(err.code)
    if (err.code === 'ENOENT') {
      console.log('kesini')
      await fs.writeFile('./src/databases/User.json', '{}')
    }
  } finally {
    return;
  }

}

module.exports = {
  checkUserDb
}
// implement a KV store then a transaction functionality


const DATA = {

}



// SET DELETE GET

// KV store
// { key: {} //value either string/integer }


function SET(key, value) {
  if (transactions.length === 0) {
    DATA[key] = value
  }
  const txn_dict = transactions[transactions.length - 1]
  txn_dict[key] = value
}

function DELETE(key) {
  if (transactions.length === 0) {
    DATA[key] = undefined
  }
  const txn_dict = transactions[transactions.length - 1]
  txn_dict[key] = "for_deletion"
}


function GET(key) {
  return DATA[key]
}



const transactions = []
let idx = 0

function BEGIN_TRANSACTION() {
  transactions.push({})
}

function COMMIT() {
  const curTxn = transactions[transactions.length - 1]
  // find out which keys to be deleted
  const needDeleteKeys = Object.keys(curTxn).map((key) => {
    if (curTxn[key] === "for_deletion") {
      return key
    } else {
      return null
    }
  }).filter(Boolean)

  // get rid of curTxn keys that are for_deletion
  needDeleteKeys.map((key) => {
    DATA[key] = undefined
    curTxn[key] = undefined
  })
  DATA = {
    ...DATA,
    ...curTxn
  }
}


function ROLLBACK() {
  transactions.pop()
}




// [V, B] => commit == [V] => rollback == []
GET("A")
SET("A", "123") // 123 = A
BEGIN_TRANSACTION() // call it V
SET("A", "456") // 456 = A
GET("A") // 456
BEGIN_TRANSACTION() // call it B
SET("A", "999") 
COMMIT() // commits everything that happened in B
GET("A") // 999
ROLLBACK() // rolls back everything that happened in V
GET("A") // should return 999

// no nested txn
// [a, b, c] commit => exectuting, [a, b, c]: pop if rollback

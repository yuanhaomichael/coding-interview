const https = require('https')
const url = "https://jsonmock.hackerrank.com/api/movies";
var glob_data = ''
https.get(url, res => {
  let data = '';
  res.on('data', chunk => {
    data += chunk;
  });
  res.on('end', () => {
    data = JSON.parse(data);
    console.log(data);
    console.log(data.data[2].Title)
    glob_data += data
  })
})
.on('error', err => {
  console.log(err.message);
})



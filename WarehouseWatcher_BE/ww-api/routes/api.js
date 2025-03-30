var express = require('express');
var router = express.Router();

const { InfluxDBClient, Point } = require('@influxdata/influxdb3-client');
const fs = require('fs');
const path = require('path');
var data = [];
const port = process.env.API_PORT;
const host = process.env.INFLUXDB_HOST
const token = process.env.INFLUXDB_TOKEN

async function getSensorData(query_params) {
  
  try {
    const client = new InfluxDBClient({host: host, token: token})
    
    const base_tpc = 'Waterloo/Warehouse/'
    const topic = base_tpc + query_params.topic
    const sdt = query_params.start
    const edt = query_params.end
    const fld = 'data_values'

    const query = `SELECT time, ${fld}
    FROM "${topic}"
    WHERE time >= '${sdt}' and time < '${edt}'
    AND ("${fld}" IS NOT NULL)`

    const rows = await client.query(query, 'test1')
    try{
      for await (const row of rows) {
        data.push(row)
        // console.log(row)
      }
    }catch(e)
    {
      console.log(e);
    }    
    client.close()
  } catch (e) {
    console.error(e)
  } 

}

router.get('/sensordata', function(req, res, next) {
  data = [];
  const param = req.query;
  const param_length = Object.keys(param).length;
  var response = undefined;
  // if (param_length === 3 && !new Date(param.start) && !new Date(param.end))
  if (param_length === 3)
  {
    getSensorData(param).then(
    () => {
      response = JSON.stringify(data)
      res.json(response).status(200)
    })
  } else {
    res.json("bad request, check params").status(400)
  }
  
})

// /* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('wwapi-respond with a resource');
});

module.exports = router;

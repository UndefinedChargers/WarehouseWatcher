// 1. user selects-type 
// - select options: a. environmental sensor, b. facility energy(tbd), c. facility assets(tbd)
// 2. user selects-object
// - select options: environmental sensor
// - sub options: a. room-temp sensor, b. fridge-temp, c. freezer-temp, d. airquality, e. humidity
// 2.1.2. user selects-minimum
// 2.1.3. user selects-maximum

export const thresholdselectoptions = [
  {
    type: "environmental sensor",
    minthreshold_field: "min_threshold",
    maxthreshold_field: "max_threshold",
    options: [
      {
        oid: "sensor1_temp",
        sensorname: "room-temp",
        selectionrangemin: 15,
        selectionrangemax: 40,
      },
      {
        oid: "sensor2_temp",
        sensorname: "fridge-temp", 
        rangemin: 0,
        rangemax: 15,
      },
      {
        oid: "sensor3_temp",
        sensorname: "freezer-temp", 
        rangemin: -35,
        rangemax: 0,
      },
      {
        oid: "sensor1_air",
        sensorname: "airquality-co2", 
        rangemin: 400,
        rangemax: 1000,
      },
      {
        oid: "sensor1_humidity",
        sensorname: "humidity-level", 
        rangemin: 30,
        rangemax: 60,
      },
    ]
  },
]
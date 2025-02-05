// FILE: ww-config.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-30

import { Vector3 } from "@babylonjs/core";

export const warehouseSceneConfig = {
    light: {
        direction: new Vector3(0, 1, 0),
        intensity: 1.2,
    },
    model: {
        filename: "warehouse_v2.glb",
    },
    camera: {
        initial_position: new Vector3(16.52, 10.24, 8.08),
        initial_target: new Vector3(-5.41, 0.972, -3.908),
    },
    sidepanel: {
        panel_width: "15%",
        font_color: "white",
        panel_background: "#44444420",
    } 
};

export const sensor_object = [{
    meshname: "sensor1_temp.001",
    topic: "Waterloo/Warehouse/Thermostat/Room",
},
{
    meshname: "sensor1_humidity.001",
    topic: "Waterloo/Warehouse/Thermostat/",
},
{
    meshname: "sensor1_air.001",
    topic: "Waterloo/Warehouse/Thermostat/Room",
},
]



export const inventory_data = {
    "WW-PD-A82": {Lot:"465829", Description:"Cheollian spectrometer", Quantity:25, ghs:"ghs07"},
    "WW-PD-X92":{Lot:"9657236", Description:"Jang-Goon litesizer", Quantity:37, ghs:"ghs02"},
    "WW-PD-B55": {Lot:"849562", Description:"Daum molecular analyzer", Quantity:25, ghs:"class62"},
    "WW-PD-J86":{Lot:"152648", Description:"Bora bipolar disector", Quantity:37, ghs:"ghs07"},
} 
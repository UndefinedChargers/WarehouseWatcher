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
        filename: "warehouse_v3.glb",
    },
    camera: {
        initial_position: new Vector3(16.52, 10.24, 8.08),
        initial_target: new Vector3(-5.41, 0.972, -3.908),
        exclude_obj: [ "plane", "wall", "stacker", "freezer", "coldroom" ],
        target_obj: [{
            name: "sensor1",
            position: new Vector3(12.104, 8.179, -0.609),
        },
        {
            name: "shelf1",
            position: new Vector3(0.232, 4.785, 8.537),
        },
        {
            name: "shelf2",
            position: new Vector3(-6.328, 4.785, 8.451),
        },
        {
            name: "shelf3",
            position: new Vector3(-12.847, 4.785, 8.449),
        },
        {
            name: "shelf4",
            position: new Vector3(-18.393, 4.785, 8.448),
        },
        {
            name: "shelf5",
            position: new Vector3(2.183, 3.670, -6.669),
        },
        {
            name: "shelf6",
            position: new Vector3(5.500, 3.578, -6.252),
        },
        {
            name: "shelf7",
            position: new Vector3(5.500, 3.578, -6.252),
        },
        {
            name: "shelf8",
            position: new Vector3(5.500, 3.578, -6.252),
        },
        {
            name: "shelf9",
            position: new Vector3(-0.046, 2.740, -2.163),
        },
        {
            name: "shelf10",
            position: new Vector3(-0.046, 2.740, -2.163),
        },
        {
            name: "shelf11",
            position: new Vector3(-0.046, 2.740, -2.163),
        },
        {
            name: "shelf12",
            position: new Vector3(-0.046, 2.740, -2.163),
        },
        {
            name: "shelf13",
            position: new Vector3(-0.03715, 3.8730, -15.35),
        },
        {
            name: "shelf14",
            position: new Vector3(-5.9975, 3.8730, -15.35),
        },
        {
            name: "shelf15",
            position: new Vector3(-12.50, 3.8730, -15.35),
        },
        {
            name: "shelf16",
            position: new Vector3(-18.393, 3.8730, -15.35),
        },
    ],
    },
    sidepanel: {
        panel_width: "15%",
        font_color: "white",
        panel_background: "#44444420",
    } 
};

export const sensor_object = [{
    meshname: "sensor1_temp",
    topic: "Waterloo/Warehouse/Thermostat/Room",
},
{
    meshname: "sensor1_humidity",
    topic: "Waterloo/Warehouse/Thermostat/Room",
},
{
    meshname: "sensor1_air",
    topic: "Waterloo/Warehouse/Thermostat/Room",
},
{
    meshname: "sensor2_temp",
    topic: "Waterloo/Warehouse/Thermostat/Refrigerator",
},
{
    meshname: "sensor2_humidity",
    topic: "Waterloo/Warehouse/Thermostat/Refrigerator",
},
{
    meshname: "sensor2_air",
    topic: "Waterloo/Warehouse/Thermostat/Refrigerator",
},
{
    meshname: "sensor3_temp",
    topic: "Waterloo/Warehouse/Thermostat/Freezer",
},
{
    meshname: "sensor3_humidity",
    topic: "Waterloo/Warehouse/Thermostat/Freezer",
},
{
    meshname: "sensor3_air",
    topic: "Waterloo/Warehouse/Thermostat/Freezer",
},
]



export const inventory_data = {
    "WW-PD-A82": {Lot:"465829", Description:"Cheollian spectrometer", Quantity:25, ghs:"ghs07"},
    "WW-PD-X92":{Lot:"9657236", Description:"Jang-Goon litesizer", Quantity:37, ghs:"ghs02"},
    "WW-PD-B55": {Lot:"849562", Description:"Daum molecular analyzer", Quantity:25, ghs:"class62"},
    "WW-PD-J86":{Lot:"152648", Description:"Bora bipolar disector", Quantity:37, ghs:"ghs07"},
} 
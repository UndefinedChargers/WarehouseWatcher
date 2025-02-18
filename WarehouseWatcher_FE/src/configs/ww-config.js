// FILE: ww-config.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-30

import { Vector3, Color3 } from "@babylonjs/core";

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
    },
    scenestatus: {
        status_topic: "WW/App/Front/Status",
        status_message: {
            app_name: "WW",
            request: "update_inventory",
            value: 0,
            timestamp: new Date(Date.now())
        }
    }
};

export const sensor_object = [{
    meshname: "sensor1_temp",
    topic: "Waterloo/Warehouse/Room",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: 20,
    max_threshold: 25,
    color_good: new Color3(0, 1, 0),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor1_humidity",
    topic: "Waterloo/Warehouse/Room",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: 20,
    max_threshold: 25,
    color_good: new Color3(0, 0, 1),
    color_warning: new Color3(1, 0.5, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor1_air",
    topic: "Waterloo/Warehouse/AirQuality_warehouse",
    targetval: "data",
    targetvalmem: "CO2",
    unit: 'ppm',
    min_threshold: 0,
    max_threshold: 850,
    color_good: new Color3(0, 0, 1),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor2_temp",
    topic: "Waterloo/Warehouse/Refrigerator",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: 2,
    max_threshold: 4.5,
    color_good: new Color3(0, 1, 0),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor2_humidity",
    topic: "Waterloo/Warehouse/Room",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: 2,
    max_threshold: 4.5,
    color_good: new Color3(0, 1, 0),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor2_air",
    topic: "Waterloo/Warehouse/AirQuality_warehouse",
    targetval: "data",
    targetvalmem: "CO2",
    unit: 'ppm',
    min_threshold: 0,
    max_threshold: 850,
    color_good: new Color3(0, 0, 1),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
{
    meshname: "sensor3_temp",
    topic: "Waterloo/Warehouse/Freezer",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: -20,
    max_threshold: -16,
    color_good: new Color3(1, 0, 0),
    color_warning: new Color3(0, 1, 0),
    color_bad: new Color3(0, 1, 0),
},
{
    meshname: "sensor3_humidity",
    topic: "Waterloo/Warehouse/AirQuality_warehouse",
    targetval: "data",
    targetvalmem: "Data",
    unit: 'C',
    min_threshold: -20,
    max_threshold: -16,
    color_good: new Color3(1, 0, 0),
    color_warning: new Color3(0, 1, 0),
    color_bad: new Color3(0, 1, 0),
},
{
    meshname: "sensor3_air",
    topic: "Waterloo/Warehouse/Room",
    topic: "Waterloo/Warehouse/AirQuality_warehouse",
    targetval: "data",
    targetvalmem: "CO2",
    unit: 'ppm',
    min_threshold: 0,
    max_threshold: 850,
    color_good: new Color3(0, 0, 1),
    color_warning: new Color3(1, 0.65, 0),
    color_bad: new Color3(1, 0, 0),
},
]



export const inventory_data = [{"location": "s2.l01", "product": "WW-PD-J85", "description": "Sola bipolar disector", "batch": "512648", "quantity": 50.0, "ghs": "ghs07"}, {"location": "s2.l01", "product": "WW-PD-A81", "description": "Cheollian spectrometer", "batch": "645829", "quantity": 57.0, "ghs": "ghs07"}, {"location": "s2.l01", "product": "WW-PD-K86", "description": "Poiee bipolar disector", "batch": "512648", "quantity": 46.0, "ghs": "ghs07"}]
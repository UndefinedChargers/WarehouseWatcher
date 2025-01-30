// FILE: ww-config.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-30

import { Vector3 } from "@babylonjs/core";

export const warehouseSceneConfig = {
    light: {
        direction: new Vector3(0, 1, 0),
        intensity: 1.8,
    },
    model: {
        filename: "warehouse_v0.glb",
    },
    camera: {
        initial_position: new Vector3(16.52, 10.24, 8.08),
        initial_target: new Vector3(-5.41, 0.972, -3.908),
    }

};
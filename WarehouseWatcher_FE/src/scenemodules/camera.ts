// FILE: camera.ts
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-25
// DESCRIPTION: ?? do we want another scene
// !! set min, max

import { warehouseSceneConfig } from "@/configs/ww-config";
import { WarehouseScene } from "@/scenes/WarehouseScene";
import { Scene, Vector3, UniversalCamera } from "@babylonjs/core";

export class Camera {
  _scene: Scene;
  _canvas: HTMLCanvasElement;
  _camera: UniversalCamera;

  constructor(obj: WarehouseScene) {
    this._scene = obj.scene;
    this._canvas = obj.canvas;
    this._camera = this.CreateCamera();
  }

  CreateCamera(): UniversalCamera {
    const camera = new UniversalCamera("unicam", warehouseSceneConfig.camera.initial_position, this._scene);
    camera.attachControl(this._canvas, true);
    camera.speed = 0.2;
    camera.angularSensibility = 12000;
    camera.minZ = 0.5;
    camera.maxZ = 100;
    camera.checkCollisions = true;
    camera.ellipsoid = new Vector3(1, 2, 1);
    // camera.applyGravity = true;
 
    // camera.inputs.addMouseWheel();
    // camera.inputs._mouseWheelInput.wheelPrecisionX = 0.1;
    // camera.inputs._mouseWheelInput.wheelPrecisionY = 0.1;
    // camera.inputs._mouseWheelInput.wheelPrecisionZ = 0.1;
    camera.setTarget(warehouseSceneConfig.camera.initial_target);
    camera.attachControl(true);
    // camera.keysUp = [38]; // arrow
    // camera.keysDown = [40]; //arrow
    // camera.keysRotateLeft = [37]; // arrow
    // camera.keysRotateRight = [39]; // arrow
    // camera.keysRight = [190]; // comma
    // camera.keysLeft = [188]; // dot
    camera.keysUpward = [33]; // pageup
    camera.keysDownward = [34]; // pagedown

    
    return camera;
  } 

}
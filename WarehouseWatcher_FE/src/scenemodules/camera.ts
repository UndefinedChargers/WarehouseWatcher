// FILE: camera.ts
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-25
// DESCRIPTION:

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
    const camera = new UniversalCamera("camera", warehouseSceneConfig.camera.initial_position, this._scene);
    camera.attachControl(this._canvas, true);
    camera.speed = 0.1;

    camera.minZ = 0.3;

    camera.checkCollisions = true;
    
    camera.inputs.addMouseWheel();
    camera.inputs._mouseWheelInput.wheelPrecisionX = 0.1;
    camera.inputs._mouseWheelInput.wheelPrecisionY = 0.1;
    camera.inputs._mouseWheelInput.wheelPrecisionZ = 0.1;
    camera.setTarget(warehouseSceneConfig.camera.initial_target);
    camera.attachControl(true);
    
    return camera;
  } 
}
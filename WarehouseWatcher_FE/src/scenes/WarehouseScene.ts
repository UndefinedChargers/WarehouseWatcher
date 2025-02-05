// FILE: WarehouseScene.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-10
// DESCRIPTION:
// References: 
// https://doc.babylonjs.com/communityExtensions/Babylon.js+ExternalLibraries/BabylonJS_and_Vue/BabylonJS_and_Vue_1#vue-3

import * as BABYLON from "@babylonjs/core";
import * as GUI from "@babylonjs/gui"
import "@babylonjs/loaders"
import { Camera } from '@/scenemodules/camera';
import { warehouseSceneConfig } from "@/configs/ww-config";
import { useEnvTopicStore } from '@/stores/envTopicStore';
import { GuiPanel } from "@/scenemodules/panel";
import { EnvironmentSensor } from "@/scenemodules/envsensor";
import { sensor_object } from "@/configs/ww-config";


export class WarehouseScene {
  canvas: HTMLCanvasElement;
  engine: BABYLON.Engine;
  scene: BABYLON.Scene;
  camera: BABYLON.UniversalCamera;

  constructor(private cnvs: HTMLCanvasElement) {
    this.canvas = cnvs;
    this._init();
  }
  
  private async _init(): Promise<void> {
    this.engine = new BABYLON.Engine(this.canvas, true);
    this.scene = this.CreateScene();
    this.camera = new Camera(this)._camera;
    
    await this._main();
  }

  private async _main(): Promise<void> {
    await this.LoadModels();
    this._CreatePickingRay();
    new GuiPanel();
    let envSensors = [];
    sensor_object.forEach((obj) => envSensors.push(new EnvironmentSensor(this, obj.meshname)));
    
    this.engine.runRenderLoop(() => {
      this.scene.render();
    });
  }

  //
  //
  //
  CreateScene(): BABYLON.Scene {
    this.engine.displayLoadingUI();

    const scene = new BABYLON.Scene(this.engine);
    const hemiLight = new BABYLON.HemisphericLight(
      "hemiLight",
      warehouseSceneConfig.light.dirrection,
      scene
    );
    hemiLight.intensity = warehouseSceneConfig.light.intensity;
        
    return scene;
  }
  
  //
  //
  //
  async LoadModels(): Promise<void> {
    const { meshes } = await BABYLON.SceneLoader.ImportMeshAsync(
      "",
      "./models/",
      warehouseSceneConfig.model.filename,
    );    
    this.engine.hideLoadingUI();
  }

  //
  //
  //
  private _CreatePickingRay(): void {
    // !! 3d btn set visibility on before render adn control? or just not use it... 
    this.scene.onPointerDown = () => {
      const ray = this.scene.createPickingRay(this.scene.pointerX, this.scene.pointerY, BABYLON.Matrix.Identity(), this.camera, false);
      const hit = this.scene.pickWithRay(ray);
      if (hit.pickedMesh != null)
      {
        console.log(hit.pickedMesh.name);
        // console.log(this.camera._currentTarget);
        // if (hit.pickedMesh.name == "thermo1")
        // {
        //   this.DisplayGUI(hit.pickedMesh.name);
        // }
      }
    };
  }

  //
  //
  //
  DisplayGUI(meshname: string): void {
    const topic = "Waterloo/Warehouse/Thermostat/Room"
    const envstore = useEnvTopicStore();
    let topicdata = envstore.individualTopicData(topic)?.data.Data;
    var mesh = this.scene.getMeshById(meshname);

    // 3D
    var manager = new GUI.GUI3DManager(this.scene);
    var button = new GUI.Button3D("button");
    manager.addControl(button);
    // button.linkToTransformNode(this.scene.getMeshById("SHELF1"));
    button.linkToTransformNode(mesh);
    button.scaling.set (8, 1, 8);
    button.node!.rotation.y += Math.PI*0.5;
    // console.log(mesh.position.x, mesh.position.y, mesh.position.z);
    button.position.y = 1.8;
  
    var text1 = new GUI.TextBlock();
    text1.text = topicdata;
    text1.color = "white";
    text1.fontSize = 50;
    button.content = text1;

    button.onPointerUpObservable.add(function(){
      // change this with visible later
      button.dispose();
      text1.dispose();
    })
  }
}
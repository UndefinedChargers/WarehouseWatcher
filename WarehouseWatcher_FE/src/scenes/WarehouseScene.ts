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
    this.CreateEnvironmentSensor();
    
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
  // !! make argument string aray later
  CreateEnvironmentSensor(): void {
    const topic = "Waterloo/Warehouse/Thermostat/Room"
    const envstore = useEnvTopicStore();
    const sensor = this.scene.getMeshById("thermo1");
    var sensor_material = new BABYLON.StandardMaterial("mat", this.scene);
    // var hl = new BABYLON.HighlightLayer("hl", this.scene);    
    // hl.addMesh(sensor.subMeshes[0].getRenderingMesh(), new BABYLON.Color3(0,1,0))
    var gl = new BABYLON.GlowLayer("gl", this.scene);
    gl.addIncludedOnlyMesh(sensor.subMeshes[0].getRenderingMesh());

    var adt = GUI.AdvancedDynamicTexture.CreateFullscreenUI("guitext");
    adt.useInvalidateRectOptimization = false;

    let sensor_text_rect = new GUI.Rectangle();
    adt.addControl(sensor_text_rect);
    sensor_text_rect.width = "150px";
    sensor_text_rect.height = "100px";
    sensor_text_rect.linkOffsetY = "-100px";
    sensor_text_rect.transformCenterY = 1;
    // sensor_text_rect.background = "red"
    sensor_text_rect.background = "#00000050";
    sensor_text_rect.color = "#02132450";
    sensor_text_rect.thickness = 1;
    // sensor_text_rect.alpha = 0.8;
    sensor_text_rect.scaleX = 0;
    sensor_text_rect.scaleY = 0;
    sensor_text_rect.linkWithMesh(sensor);

    let sensor_text = new GUI.TextBlock();
    sensor_text.fontSize = 50;
    sensor_text.color = "white";
    sensor_text.textWrapping = true;
    sensor_text.textVerticalAlignment = GUI.Control.VERTICAL_ALIGNMENT_CENTER;
    // sensor_text.textVerticalAlignment = GUI.Control.VERTICAL_ALIGNMENT_TOP;
    sensor_text_rect.addControl(sensor_text);

    let am_sesnor = new BABYLON.ActionManager(this.scene);
    sensor.actionManager = am_sesnor;
    console.log(this.scene);

    am_sesnor.registerAction(new BABYLON.ExecuteCodeAction(BABYLON.ActionManager.OnPointerOverTrigger, function(e){
      // console.log(e.meshUnderPointer.name);
      let topicdata = envstore.individualTopicData(topic)?.data.Data;
      sensor_text.text = topicdata;
      sensor_text_rect.scaleX = 0.5;
      sensor_text_rect.scaleY = 0.5;
      sensor_text.color = "green";

      // this.scene.beginAnimation(sensor_text_rect, 0, 10, false);
    }));

    am_sesnor.registerAction(new BABYLON.ExecuteCodeAction(BABYLON.ActionManager.OnPointerOutTrigger, function(e){
      // this.scene.beginAnimation(sensor_text_rect, 10, 0, false);
      sensor_text_rect.scaleX = 0;
      sensor_text_rect.scaleY = 0;
    }));


    this.scene.onAfterRenderObservable.add(() => {
      this.DisplayEnvironmentSensor(sensor, sensor_material);  
    }, 250)
  }
 
  //
  //
  //
  DisplayEnvironmentSensor(sensor: BABYLON.AbstractMesh | null, material: BABYLON.StandardMaterial): void {
    const topic = "Waterloo/Warehouse/Thermostat/Room"
    const envstore = useEnvTopicStore();
    let topicdata = envstore.individualTopicData(topic)?.data.Data;
    let val = parseFloat(topicdata);
        
    if (val >= 23) {
      material.emissiveColor = new BABYLON.Color3(1, 0, 0);
      sensor.material = material;
    } else if (val < 23) {
      material.emissiveColor = new BABYLON.Color3(0, 1, 0);
      sensor.material = material;
    } else { // null
      material.emissiveColor = new BABYLON.Color3(0, 1, 0);
      sensor.material = material;
    }     
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
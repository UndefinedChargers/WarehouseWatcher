// FILE: WarehouseScene.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-10
// DESCRIPTION:
// References: 
// https://doc.babylonjs.com/communityExtensions/Babylon.js+ExternalLibraries/BabylonJS_and_Vue/BabylonJS_and_Vue_1#vue-3

import * as BABYLON from "@babylonjs/core";
import "@babylonjs/loaders"
import { Camera } from '@/scenemodules/camera';
import { warehouseSceneConfig, inventory_data} from "@/configs/ww-config";
import { GuiPanel } from "@/scenemodules/panel";
import { EnvironmentSensor } from "@/scenemodules/envsensor";
import { sensor_object } from "@/configs/ww-config";
import { useAppStatusStore } from "@/stores/appStatusStore";
import { useInventoryStore } from "@/stores/inventoryStore";


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
    const panel = new GuiPanel();
    this._CreatePickingRay(panel);
    // panel.buildDetails(inventory_data);

    let envSensors = [];
    sensor_object.forEach((obj) => envSensors.push(new EnvironmentSensor(this, obj.meshname)));
    
    this.engine.runRenderLoop(() => {
      this.engine.resize();
      this.scene.render();
    });
  }

  CreateScene(): BABYLON.Scene {
    this.engine.displayLoadingUI();

    const scene = new BABYLON.Scene(this.engine);
    const hemiLight = new BABYLON.HemisphericLight(
      "hemiLight",
      warehouseSceneConfig.light.dirrection,
      scene
    );
    hemiLight.intensity = warehouseSceneConfig.light.intensity;
    scene.gravity = new BABYLON.Vector3(0, -0.1, 0);
    scene.collisionsEnabled = true;
    scene.freezeActiveMeshes();

    return scene;
  }
  
  async LoadModels(): Promise<void> {
    const { meshes } = await BABYLON.SceneLoader.ImportMeshAsync(
      "",
      "./models/",
      warehouseSceneConfig.model.filename,
    );    
    this.engine.hideLoadingUI();
  }

  // https://forum.babylonjs.com/t/double-click-for-an-event-rather-than-pointerdown/30907
  private _CreatePickingRay(guipanel: GuiPanel): void {
    var hl = new BABYLON.HighlightLayer("h1", this.scene);
    this.scene.onPointerObservable.add((pointerInfo) => {
      switch (pointerInfo.type) {
        case BABYLON.PointerEventTypes.POINTERDOUBLETAP:
          if (pointerInfo.pickInfo.hit) {
            if (pointerInfo.event.button === 0) {
              if (pointerInfo.pickInfo.hit) {
                var pickedmesh = pointerInfo.pickInfo.pickedMesh;
                console.log(pickedmesh.name);
                hl.removeAllMeshes();
                hl.addMesh(pickedmesh.subMeshes[0].getRenderingMesh(), new BABYLON.Color3(210, 180, 140));
                hl.blurVerticalSize = 1.5;
                hl.blurHorizontalSize = 1.5;
                this._MoveCamera(pickedmesh.name);

                const statusStore = useAppStatusStore();
                const inventoryStore = useInventoryStore();
                statusStore.setTargetObject(pickedmesh.name);
                
                // shelf only
                if (pickedmesh.name.includes("shelf")) {
                  const BASE = "WW/Waterloo/Warehouse/Inventory/"
                  var location = pickedmesh.name.split(/[.\/_]/);
                  let a = location[0].replace("helf", "");
                  let b = location[1].at(0);
                  let c = location[2].slice(1);
                  let loc = a.concat(".", b).concat(c);
                  console.log(BASE+loc);

                  const locationdata = inventoryStore.getLocationInventory(BASE+loc);
                  // console.log(locationdata);
                  guipanel.buildDetails(locationdata);
                }
              }
            }
         }
      }
    });
  }

  _MoveCamera(meshname): void {
    // console.log(mesh.name)
    var splitedname = meshname.split(/[_.]/) ;
    let targetmesh = this.scene.getMeshById(meshname);
    let excluded = warehouseSceneConfig.camera.exclude_obj.find(obj => obj === meshname);
    // console.log(excluded);
    if (excluded == undefined && targetmesh !== null) {
      var targetobject = warehouseSceneConfig.camera.target_obj.find(obj => obj.name === splitedname[0]);
      this.camera._position = targetobject.position;
      this.camera.setTarget(targetmesh.absolutePosition); 
    }    
  }
}
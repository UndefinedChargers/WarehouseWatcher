import { Scene } from "@babylonjs/core";
import { useEnvTopicStore } from '@/stores/envTopicStore';
import { ActionManager, AbstractMesh, Color3, ExecuteCodeAction, StandardMaterial, GlowLayer } from "@babylonjs/core";
import { AdvancedDynamicTexture, Image, Control, Rectangle, ScrollViewer, StackPanel, TextBlock } from "@babylonjs/gui"
import { sensor_object } from "@/configs/ww-config";
import { WarehouseScene } from "@/scenes/WarehouseScene";

// mesh name and its topic
export class EnvironmentSensor {
  _scene: Scene;
  _sensor: string;
  
  constructor(obj: WarehouseScene, meshname: string) {
    this._scene = obj.scene;
    this._sensor = meshname;
    this.CreateEnvironmentSensor();
  }
  
  CreateEnvironmentSensor(): void {
    const envstore = useEnvTopicStore();
    const index = sensor_object.findIndex(sensor => sensor.meshname === this._sensor)
    // console.log(sensor_object[index].topic);
    let topic = sensor_object[index].topic;
    const sensor = this._scene.getMeshById(this._sensor);
    var sensor_material = new StandardMaterial("mat", this._scene);
    // var hl = new BABYLON.HighlightLayer("hl", this.scene);    
    // hl.addMesh(sensor.subMeshes[0].getRenderingMesh(), new BABYLON.Color3(0,1,0))
    var gl = new GlowLayer("gl", this._scene);
    gl.addIncludedOnlyMesh(sensor.subMeshes[0].getRenderingMesh());
    gl.setEffectIntensity(sensor.subMeshes[0].getRenderingMesh(), 0.5);
    var adt = AdvancedDynamicTexture.CreateFullscreenUI("guitext");
    adt.useInvalidateRectOptimization = false;
  
    let sensor_text_rect = new Rectangle();
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
  
    let sensor_text = new TextBlock();
    sensor_text.fontSize = 50;
    // sensor_text.color = "white";
    sensor_text.textWrapping = true;
    sensor_text.textVerticalAlignment = Control.VERTICAL_ALIGNMENT_CENTER;
    // sensor_text.textVerticalAlignment = GUI.Control.VERTICAL_ALIGNMENT_TOP;
    sensor_text_rect.addControl(sensor_text);
  
    let am_sesnor = new ActionManager(this._scene);
    sensor.actionManager = am_sesnor;
    // console.log(this._scene);
  
    am_sesnor.registerAction(new ExecuteCodeAction(ActionManager.OnPointerOverTrigger, function(e){
      let topicdata = envstore.individualTopicData(topic)?.data.Data;
      sensor_text.text = topicdata;
      sensor_text_rect.scaleX = 0.5;
      sensor_text_rect.scaleY = 0.5;
      sensor_text.color = "white";
      // this.scene.beginAnimation(sensor_text_rect, 0, 10, false);
    }));
    am_sesnor.registerAction(new ExecuteCodeAction(ActionManager.OnPointerOutTrigger, function(e){
      // this.scene.beginAnimation(sensor_text_rect, 10, 0, false);
      sensor_text_rect.scaleX = 0;
      sensor_text_rect.scaleY = 0;
    }));
    
    this._scene.onAfterRenderObservable.add(() => {
      this.DisplayEnvironmentSensor(sensor, topic, sensor_material);}, 250)
  }
  
  DisplayEnvironmentSensor(sensor: AbstractMesh | null, topic: string, material: StandardMaterial): void {
    const envstore = useEnvTopicStore();
    let topicdata = envstore.individualTopicData(topic)?.data.Data;
    let val = parseFloat(topicdata);
    
    if (sensor.name?.includes("temp")){
      if (val >= 23) {
        material.emissiveColor = new Color3(1, 0, 0);
        sensor.material = material;
      } else if (val < 23) {
        material.emissiveColor = new Color3(0, 1, 0);
        sensor.material = material;
      } else { // null
        material.emissiveColor = new Color3(0, 1, 0);
        sensor.material = material;
      }
    }
    // change color values later
    if (sensor.name?.includes("humidity")) {
      if (val >= 0) {
      material.emissiveColor = new Color3(0, 0, 1);
      sensor.material = material; 
      } else if (val < 23) {
      material.emissiveColor = new Color3(0, 1, 0);
      sensor.material = material;
      } else { // null
      material.emissiveColor = new Color3(0, 0, 1);
      sensor.material = material;
      }
    }
    if (sensor.name?.includes("air")) {
      if (val >= 0) {
      material.emissiveColor = new Color3(0, 0, 1);
      sensor.material = material; 
      } else if (val < 23) {
      material.emissiveColor = new Color3(1, 0, 0);
      sensor.material = material;
      } else { // null
      material.emissiveColor = new Color3(0, 0, 1);
      sensor.material = material;
      }
    }
  }
}
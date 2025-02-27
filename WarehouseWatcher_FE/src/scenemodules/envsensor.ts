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
    let sensorobj = sensor_object[index];
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
    sensor_text_rect.width = "160px";
    sensor_text_rect.height = "90px";
    sensor_text_rect.linkOffsetY = "-100px";
    sensor_text_rect.transformCenterY = 1;
    sensor_text_rect.background = "#00000050";
    sensor_text_rect.color = "#02132450";
    sensor_text_rect.thickness = 1;
    // sensor_text_rect.alpha = 0.8;
    sensor_text_rect.scaleX = 0;
    sensor_text_rect.scaleY = 0;
    sensor_text_rect.linkWithMesh(sensor);
  
    let sensor_text = new TextBlock();
    sensor_text.fontSize = 32;
    sensor_text.textWrapping = true;
    sensor_text.textVerticalAlignment = Control.VERTICAL_ALIGNMENT_CENTER;
    sensor_text_rect.addControl(sensor_text);
  
    let am_sesnor = new ActionManager(this._scene);
    sensor.actionManager = am_sesnor;
    // console.log(this._scene);
  
    am_sesnor.registerAction(new ExecuteCodeAction(ActionManager.OnPointerOverTrigger, function(e){
      let topicdata
      if (sensorobj.targetvalmem === "Data") {
        topicdata = envstore.individualTopicData(sensorobj.topic)?.data.Data;
      }
      if (sensorobj.targetvalmem === "Humidity") {
        topicdata = envstore.individualTopicData(sensorobj.topic)?.data.Humidity;
      }
      if (sensorobj.targetvalmem === "CO2") {
        topicdata = envstore.individualTopicData(sensorobj.topic)?.data.CO2;
      }
      sensor_text.text = topicdata + sensorobj.unit;
      sensor_text_rect.scaleX = 0.5;
      sensor_text_rect.scaleY = 0.5;
      sensor_text.color = "white";
    }));
    am_sesnor.registerAction(new ExecuteCodeAction(ActionManager.OnPointerOutTrigger, function(e){
      sensor_text_rect.scaleX = 0;
      sensor_text_rect.scaleY = 0;
    }));
    
    this._scene.onAfterRenderObservable.add(() => {
      this.DisplayEnvironmentSensor(sensor, sensor_material);}, 250)
      
  }
  
  DisplayEnvironmentSensor(sensor: AbstractMesh | null, material: StandardMaterial): void {
    const envstore = useEnvTopicStore();
    const index = sensor_object.findIndex(sensor => sensor.meshname === this._sensor)
    let sensorobj = sensor_object[index];

    let topicdata = undefined;
    if (sensorobj.targetvalmem === "Data") {
      topicdata = envstore.individualTopicData(sensorobj.topic)?.data.Data;
    }
    if (sensorobj.targetvalmem === "Humidity") {
      topicdata = envstore.individualTopicData(sensorobj.topic)?.data.Humidity;
    }
    if (sensorobj.targetvalmem === "CO2") {
      topicdata = envstore.individualTopicData(sensorobj.topic)?.data.CO2;
    }
    let val = parseFloat(topicdata);
    
    if (val >= sensorobj.min_threshold && val < sensorobj.max_threshold) {
      material.emissiveColor = sensorobj.color_good;
      sensor.material = material;
    } else if (val == sensorobj.max_threshold) {
      material.emissiveColor = sensorobj.color_warning;
      sensor.material = material;
    } else { // null
      material.emissiveColor = sensorobj.color_bad;
      sensor.material = material;
    }
  }
}
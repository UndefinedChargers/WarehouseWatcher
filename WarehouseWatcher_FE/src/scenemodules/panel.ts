// FILE: panel.ts
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-30
// REFERENCE: https://playground.babylonjs.com/#4U4QH9#35

import { AdvancedDynamicTexture, Image, Control, Rectangle, ScrollViewer, StackPanel, TextBlock, Button } from "@babylonjs/gui"
import { warehouseSceneConfig, inventory_data } from "@/configs/ww-config";
import { publishMQTT } from "../helper/wwmqtt";

export class GuiPanel {
  _container: StackPanel;
  _detailsContainer: StackPanel;
  constructor() {
    this._container = new StackPanel();
    this._detailsContainer = new StackPanel();
    this.createGuiPannel();
  }
  
  createGuiPannel(): void {
    const data = inventory_data;
    
    // panelUI.panel
    const panelUI = AdvancedDynamicTexture.CreateFullscreenUI("panel");
    const panel = new Rectangle();
    panel.isPointerBlocker = true;
    panel.width = warehouseSceneConfig.sidepanel.panel_width;
    panel.height = "60%";
    panel.background = "#44444420";
    panel.color = "#02132450";
    panel.thickness = 1;
    panel.horizontalAlignment = Control.HORIZONTAL_ALIGNMENT_RIGHT;
    panel.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    panelUI.addControl(panel);
    
    // panelUI.panel.panelContainer
    const panelContainer = this._container;
    panelContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP; 
    panel.addControl(panelContainer);

    // panelUI.panel.panelContainer.TextBlock
    const location = "INVENTORY"
    const titleContainer = this.makeTitleContainer()
    panelContainer.addControl(titleContainer);

    panelContainer.addControl(this.space(0.001*window.innerWidth));
    panelContainer.addControl(this.textTitle(location));
    panelContainer.addControl(this.space(0.001*window.innerWidth));
    // const title = this.buildTitle("Warehouse-Waterloo");
    


    // panelUI.panel.panelContainer.StackPanel
    // const detailsContainer = new StackPanel();
    this._detailsContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    panelContainer.addControl(this._detailsContainer);
    
    // this.buildDetails(data);
  }

  makeTitleContainer() {
    const item_rect = new Rectangle();
    item_rect.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    item_rect.height = 0.02 * window.innerWidth + "px";
    item_rect.thickness = 0;

    const tb1 = new TextBlock();
    tb1.textVerticalAlignment = 1;
    tb1.textHorizontalAlignment = 0;
    tb1.top = "0px";
    tb1.left = 0.008*window.innerWidth + "px";
    tb1.text = "WW-Waterloo";
    tb1.color = warehouseSceneConfig.sidepanel.font_color;
    tb1.fontSize = 0.01 * window.innerWidth;
    item_rect.addControl(tb1);

    const reloadbtn = Button.CreateSimpleButton("reload", "Inventory");
    reloadbtn.fontSize = 0.01 * window.innerWidth + "px";
    reloadbtn.verticalAlignment = Control.VERTICAL_ALIGNMENT_CENTER;
    reloadbtn.horizontalAlignment = Control.HORIZONTAL_ALIGNMENT_RIGHT;
    reloadbtn.width = "30%";
    reloadbtn.height = 0.016 * window.innerWidth + "px";
    reloadbtn.thickness = 0;
    reloadbtn.cornerRadius = 10;
    reloadbtn.color = "white";
    reloadbtn.background = "#ffffff50";
    item_rect.addControl(reloadbtn);

    reloadbtn.onPointerClickObservable.add(function() {
      const result = publishMQTT(warehouseSceneConfig.scenestatus.status_topic, JSON.stringify(warehouseSceneConfig.scenestatus.status_message));
    });
    return item_rect;
}

  buildDetails(data: object) {
    if (data == undefined) {
      this._detailsContainer.clearControls();      
    } else {
      this._detailsContainer.clearControls();
      this._detailsContainer.clearControls();

      const top = this.getTop(this._detailsContainer);
      const height = window.innerHeight-top-100;
      const sv = new ScrollViewer();
      sv.barSize = 0.006 * window.innerWidth;
      sv.thickness = 0;
      sv.color = "grey";
      sv.height = height + "px";
      this._detailsContainer.addControl(sv);
  
      // sub container
      const subContainer = new StackPanel();
      subContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
      subContainer.width = 0.99;
      sv.addControl(subContainer);
  
      const items = Object.values(data);
      // const items = Object.keys(data);
      for (let i = 0; i < items.length; i++) {
        const item = items[i];
        // console.log(item);
        this.buildItemContaier(i, item, subContainer);
      }
    }
  }

  buildItemContaier(index, itemObj, container) {
    const item_rect = new Rectangle();
    item_rect.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    item_rect.height = 0.06 * window.innerWidth + "px";
    item_rect.thickness = 0;

    const tb1 = new TextBlock();
    tb1.textVerticalAlignment = 0;
    tb1.textHorizontalAlignment = 0;
    tb1.top = "0px";
    tb1.left = 0.008*window.innerWidth + "px";
    tb1.text = "Loc" + (index + 1) + " " + itemObj.location;
    tb1.color = warehouseSceneConfig.sidepanel.font_color;
    tb1.fontSize = 0.01 * window.innerWidth ;
    item_rect.addControl(tb1);

    const tb2 = new TextBlock();
    tb2.textVerticalAlignment = 0;
    tb2.textHorizontalAlignment = 0;
    tb2.top = 0.0121*window.innerWidth + "px";
    tb2.left = 0.008*window.innerWidth + "px";
    tb2.text = "Item: " + itemObj.description;
    tb2.color = warehouseSceneConfig.sidepanel.font_color;
    tb2.fontSize = 0.008 * window.innerWidth;
    item_rect.addControl(tb2);
    
    const tb3 = new TextBlock();
    tb3.textVerticalAlignment = 0;
    tb3.textHorizontalAlignment = 0;
    tb3.top = 0.022 * window.innerWidth + "px";
    tb3.left = 0.008 * window.innerWidth + "px";
    tb3.text = "Lot: " + itemObj.batch;
    tb3.color = warehouseSceneConfig.sidepanel.font_color;
    tb3.fontSize = 0.009 * window.innerWidth;
    item_rect.addControl(tb3);

    const tb4 = new TextBlock();
    tb4.textVerticalAlignment = 0;
    tb4.textHorizontalAlignment = 0;
    tb4.top = 0.033 * window.innerWidth + "px";
    tb4.left = 0.008 * window.innerWidth + "px";
    tb4.text = "Quantity: " + itemObj.quantity;
    tb4.color = warehouseSceneConfig.sidepanel.font_color;
    tb4.fontSize = 0.009 * window.innerWidth;
    item_rect.addControl(tb4);
    container.addControl(item_rect);

    const path = "../pictogram/"+(itemObj.ghs)+".gif";
    const image_rect = new Rectangle();
    image_rect.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    image_rect.horizontalAlignment = Control.HORIZONTAL_ALIGNMENT_RIGHT;
    image_rect.top = 0.005 * window.innerWidth + "px";
    image_rect.width = 0.035 * window.innerWidth + "px";
    image_rect.height = 0.035 * window.innerWidth + "px";
    image_rect.thickness = 0;
    const image = new Image("GHS" + itemObj.ghs, path);
    image_rect.addControl(image);
    item_rect.addControl(image_rect);
  }

  

  getTop(container: StackPanel){
    let top = 0;
    container.parent.children.forEach(function(con){
        if(con != container){
            top += con.heightInPixels;
        }
    })
    container.children.forEach(function(con){
        top += con.heightInPixels;
    })
    return top;
  }

  textTitle(text: string): TextBlock {
    const title = new TextBlock();
    title.height = (0.0275*window.innerWidth) + "px";
    title.text = text;
    title.color = warehouseSceneConfig.sidepanel.font_color;
    title.fontSize = (0.01*window.innerWidth);
    return title;
  }
  
  space(size: number): Rectangle {
    const rect = new Rectangle();
    rect.height = size + "px";
    rect.thickness = 0;
    const line = new Rectangle();
    line.height = "1px";
    line.thickness = 0;
    line.background = "#44444420";
    rect.addControl(line);
    return rect;
  }
}
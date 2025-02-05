// FILE: panel.ts
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-30
// DESCRIPTION: 
// REFERENCE: https://playground.babylonjs.com/#4U4QH9#35

import { AdvancedDynamicTexture, Image, Control, Rectangle, ScrollViewer, StackPanel, TextBlock } from "@babylonjs/gui"
import { warehouseSceneConfig, inventory_data } from "@/configs/ww-config";

export class GuiPanel {
  constructor() {
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
    const panelContainer = new StackPanel();
    panelContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP; 
    panel.addControl(panelContainer);

    // panelUI.panel.panelContainer.TextBlock
    panelContainer.addControl(this.textTitle("Warehouse-Waterloo"));
    panelContainer.addControl(this.space(0.003*window.innerWidth));
    panelContainer.addControl(this.textTitle("Inventory"));
    panelContainer.addControl(this.space(0.003*window.innerWidth));

    // panelUI.panel.panelContainer.StackPanel
    const detailsContainer = new StackPanel();
    detailsContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    panelContainer.addControl(detailsContainer);
    
    this.buildDetails(data, detailsContainer);
  }

  buildDetails(data: object, container: StackPanel) {
    container.clearControls();

    const top = this.getTop(container);
    const height = window.innerHeight-top-100;
    const sv = new ScrollViewer();
    sv.barSize = 0.006 * window.innerWidth;
    sv.thickness = 0;
    sv.color = "grey";
    sv.height = height + "px";
    container.addControl(sv);

    // sub container
    const subContainer = new StackPanel();
    subContainer.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    subContainer.width = 0.99;
    sv.addControl(subContainer);

    const items = Object.keys(data);
    for (let i = 0; i < items.length; i++) {
      console.log(items[i]);
      const item = items[i];
      this.buildItemContaier(i, item, data[item], subContainer);
    }
  }

  buildItemContaier(index, item, itemObj, container) {
    const item_rect = new Rectangle();
    item_rect.verticalAlignment = Control.VERTICAL_ALIGNMENT_TOP;
    item_rect.height = 0.06 * window.innerWidth + "px";
    item_rect.thickness = 0;

    const tb1 = new TextBlock();
    tb1.textVerticalAlignment = 0;
    tb1.textHorizontalAlignment = 0;
    tb1.top = "0px";
    tb1.left = 0.008*window.innerWidth + "px";
    tb1.text = "Loc" + (index + 1) + " " + (item);
    tb1.color = warehouseSceneConfig.sidepanel.font_color;
    tb1.fontSize = 0.01 * window.innerWidth ;
    item_rect.addControl(tb1);

    const tb2 = new TextBlock();
    tb2.textVerticalAlignment = 0;
    tb2.textHorizontalAlignment = 0;
    tb2.top = 0.0121*window.innerWidth + "px";
    tb2.left = 0.008*window.innerWidth + "px";
    tb2.text = itemObj.Description;
    tb2.color = warehouseSceneConfig.sidepanel.font_color;
    tb2.fontSize = 0.008 * window.innerWidth;
    item_rect.addControl(tb2);
    
    const tb3 = new TextBlock();
    tb3.textVerticalAlignment = 0;
    tb3.textHorizontalAlignment = 0;
    tb3.top = 0.022 * window.innerWidth + "px";
    tb3.left = 0.008 * window.innerWidth + "px";
    tb3.text = "Lot : " + itemObj.Lot;
    tb3.color = warehouseSceneConfig.sidepanel.font_color;
    tb3.fontSize = 0.009 * window.innerWidth;
    item_rect.addControl(tb3);

    const tb4 = new TextBlock();
    tb4.textVerticalAlignment = 0;
    tb4.textHorizontalAlignment = 0;
    tb4.top = 0.033 * window.innerWidth + "px";
    tb4.left = 0.008 * window.innerWidth + "px";
    tb4.text = "Quantity : " + itemObj.Quantity;
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
    const image = new Image("GHS" + item, path);
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
    title.fontSize = (0.013*window.innerWidth);
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
// FILE: subscriber.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-23
// DESCRIPTION: 
// https://yeees.tistory.com/475
// cloud works only wss https://community.hivemq.com/t/how-to-connect-to-websocket-with-wss/1681 

import mqtt from 'mqtt';
import { useEnvTopicStore } from '@/stores/envTopicStore';
import { useInventoryStore } from '@/stores/inventoryStore';
import { useAppStatusStore } from '@/stores/appStatusStore';

export const subscribeMQTT = () => {
    const client = mqtt.connect(import.meta.env.VITE_MQTT_HOST, {
        username: import.meta.env.VITE_MQTT_USER,
        password: import.meta.env.VITE_MQTT_PASSWORD,
    });
    
    client.on('connect', function () {
        console.log('Connected');
    });

    client.on('error', function (error) {
        console.log(error);
    });
    
    client.on('message', function (topic, message) {
        // console.log('Received message:', topic, message.toString());
        const obj = JSON.parse(message);
        // console.log(topic);
        if (topic.includes("Inventory")) {
            const invStore = useInventoryStore();
            invStore.setInvTopicData(topic, obj);
            const obj1 = invStore.getLocationInventory(topic);
            // console.log(obj1[0].quantity);
        } else if (topic.includes("Status")) {
            const statusStore = useAppStatusStore();
            statusStore.inventory_reload(true);
        } else {
            const envStore = useEnvTopicStore();
            envStore.setTopicData(topic, obj);
        }


    });
    
    client.subscribe('#');
};

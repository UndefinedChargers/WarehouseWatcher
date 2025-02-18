// FIRST VERSION: 2025-02-13
// DESCRIPTION: Reference https://github.com/mqttjs/MQTT.js

import mqtt from 'mqtt';

const pub_client = mqtt.connect(import.meta.env.VITE_MQTT_HOST, {
    username: import.meta.env.VITE_MQTT_USER,
    password: import.meta.env.VITE_MQTT_PASSWORD,
});

export const publishMQTT = (topic, message) => {
	let result;
	pub_client.publish(topic, message, { qos: 1, retain: true }, (err2) => {
		if (!err2) {
			// console.log(topic, message)
			result =  true
		} else {
			console.error(err2)
			result = false
		}
	})
	return result;
};


import { defineStore } from 'pinia'

export const useEnvTopicStore = defineStore('envDataStore', {
  state: () => ({
      envTopicData: new Map(),
  }),
  
  getters: {
    individualTopicData: (state) => {
      return (topic) => state.envTopicData.get(topic);
    },
  },

  actions: {
    setTopicData (topic, payload) {
      this.envTopicData.set(topic, payload);
    },
  },
})

// export const useEnvTopicStore = defineStore('envTopicStore', () => {
//   const count = ref(0)
//   const doubleCount = computed(() => count.value * 2)
//   function increment() {
//     count.value++
//   }

//   return { count, doubleCount, increment }
// })

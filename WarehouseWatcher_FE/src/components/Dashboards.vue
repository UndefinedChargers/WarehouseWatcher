<script>
export default {
  name: "GrafanaDashboardDisplay",
  data() {
    return {
      grafanaDashboards: {
        "Energy Consumption": [
          {
            name: "Energy Consumption Last 2 Days",
            link: "https://172.206.30.225:3000/d/beerjk87fqw3kc/energy-consumption-last-2-days?orgId=2&from=now-2d&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Energy Consumption Last 30 Days",
            link: "https://172.206.30.225:3000/d/eeff59kj7oav4c/energy-consumption-last-30-days?orgId=2&from=now-30d&to=now&timezone=browser&refresh=30m"
          }
        ],
        "Environment": [
          {
            name: "Environment Last 30 Days",
            link: "https://172.206.30.225:3000/d/aeffh96iz7bb4b/environment-last-30-days?orgId=2&from=now-30d&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Environment Last Hour",
            link: "https://172.206.30.225:3000/d/deffalkw79slcb/environment-last-hour?orgId=2&from=now-1h&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Environment Real-Time",
            link: "https://172.206.30.225:3000/d/eeffszsys7pc0d/environment-real-time?orgId=2&from=now-5m&to=now&timezone=browser&refresh=5m"
          }
        ]
      },
      selectedCategory: Object.keys(this.grafanaDashboards)[0] || "",
      selectedDashboard: "",
    };
  },
  methods: {
    formatCategoryName(category) {
      return category.replace(/([A-Z])/g, " $1").replace(/^./, str => str.toUpperCase());
    }
  }
};
</script>

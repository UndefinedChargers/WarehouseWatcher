<script>

</script>

<template>
  <div class="reportlist-container">
    <h1>Results</h1>
    <div>
      <v-container class="bg-surface-variant mt-6 rounded">
        <v-row>
          <v-col cols="12">
            <v-list>
              <v-list-item-group v-if="reportData && reportData.length">
                <v-list-item v-for="(item, index) in reportData" :key="index">
                  <v-list-item-content>
                    <v-list-item-title>{{ item.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ item.value }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
              <v-row v-else>
                <v-col>No data available</v-col>
              </v-row>
            </v-list>

            <v-btn @click="downloadCSV" color="primary">Download CSV</v-btn>
            <v-btn @click="downloadPDF" color="primary">Download PDF</v-btn>
            <v-btn @click="downloadExcel" color="primary">Download Excel</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import jsPDF from 'jspdf';
import { utils, writeFile } from 'xlsx';

// Sample report data => replace with queried data later
const reportData = ref([
  { name: '2025-03-12 8:00', value: 'Temperature: 22°C' },
  { name: '2025-03-13 8:00', value: 'Temperature: 22°C' },
  { name: '2025-03-14 8:00', value: 'Temperature: 22°C' },
  { name: '2025-03-15 8:00', value: 'Temperature: 22°C' },
]);

const formatDataToCSV = (data) => {
  const headers = ['Date', 'Temperature'];
  const rows = data.map(item => [item.name, item.value]);

  let csvContent = 'data:text/csv;charset=utf-8,';
  csvContent += headers.join(',') + '\n'; 
  rows.forEach(row => {
    csvContent += row.join(',') + '\n'; 
  });

  return csvContent;
};

const downloadCSV = () => {
  const csvContent = formatDataToCSV(reportData.value);
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', 'report.csv'); 
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link); 
};

const downloadPDF = () => {
  const doc = new jsPDF();
  doc.setFontSize(12);
  
  let y = 10;
  doc.text('Report', 10, y);
  y += 10;
  
  reportData.value.forEach(item => {
    doc.text(`${item.name}: ${item.value}`, 10, y);
    y += 10;
  });
  
  doc.save('report.pdf');
};

const downloadExcel = () => {
  const ws = utils.json_to_sheet(reportData.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, 'Report');
  writeFile(wb, 'report.xlsx');
};
</script>

<style scoped>
</style>

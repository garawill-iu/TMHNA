// Full updated dashboard.js with fixes for filters and real-time alerts

// Updated dashboard.js with additional hardcoded data for filters

document.addEventListener('DOMContentLoaded', function () {
    // Hardcoded data for filters
    const data = {
        '2024': {
            'TMH': {
                revenue: '$2.3B',
                maintenance: '$1.2M',
                utilization: '85%',
                overdue: '8',
                fleetUtilization: [75, 80, 85, 83, 87, 90],
                maintenanceCosts: [300000, 350000, 280000, 270000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [1000000, 800000, 400000],
                    regionB: [900000, 700000, 500000],
                },
                kaizen: [15, 20, 10, 25],
                inventoryTurnover: [5, 6, 4, 5],
                assetDowntime: [2, 3, 1, 4],
                policyProgress: [60, 70, 80, 90],
                realTimeAlerts: [5, 4, 6, 8],
            },
            'Raymond': {
                revenue: '$2.9B',
                maintenance: '$900K',
                utilization: '78%',
                overdue: '10',
                fleetUtilization: [70, 75, 78, 76, 80, 83],
                maintenanceCosts: [280000, 300000, 250000, 220000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [800000, 600000, 300000],
                    regionB: [700000, 500000, 400000],
                },
                kaizen: [10, 15, 8, 20],
                inventoryTurnover: [4, 5, 3, 4],
                assetDowntime: [3, 4, 2, 5],
                policyProgress: [50, 60, 70, 85],
                realTimeAlerts: [6, 5, 7, 9],
            },
            'TMHNA': {
            revenue: '$5.2B', // $2.3B + $2.9B
            maintenance: '$2.1M', // $1.2M + $900K
            utilization: '81.5%', // Average of 85% and 78%
            overdue: '18', // 8 + 10
            fleetUtilization: [145, 155, 163, 159, 167, 173], // Sum arrays
            maintenanceCosts: [580000, 650000, 530000, 490000], // Sum arrays
            revenueProductLine: {
                labels: ['Forklifts', 'Trucks', 'Maintenance'],
                regionA: [1800000, 1400000, 700000], // Sum arrays
                regionB: [1600000, 1200000, 900000], // Sum arrays
            },
            kaizen: [25, 35, 18, 45], // Sum arrays
            inventoryTurnover: [9, 11, 7, 9], // Sum arrays
            assetDowntime: [5, 7, 3, 9], // Sum arrays
            policyProgress: [55, 65, 75, 87.5], // Average of 60, 70, 80, 90 and 50, 60, 70, 85
            realTimeAlerts: [11, 9, 13, 17], // Sum arrays
            },
        },
        '2023': {
            'TMH': {
                revenue: '$2.1BM',
                maintenance: '$1.0M',
                utilization: '82%',
                overdue: '9',
                fleetUtilization: [73, 78, 82, 80, 85, 88],
                maintenanceCosts: [290000, 340000, 270000, 260000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [950000, 750000, 380000],
                    regionB: [880000, 680000, 480000],
                },
                kaizen: [13, 18, 12, 22],
                inventoryTurnover: [4.5, 5.5, 3.5, 4.5],
                assetDowntime: [3, 2.5, 2, 3.5],
                policyProgress: [50, 65, 75, 80],
                realTimeAlerts: [4, 6, 5, 7],
            },
            'Raymond': {
                revenue: '$2.8B',
                maintenance: '$2.1M',
                utilization: '75%',
                overdue: '11',
                fleetUtilization: [68, 72, 75, 73, 77, 80],
                maintenanceCosts: [270000, 290000, 240000, 210000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [750000, 570000, 280000],
                    regionB: [690000, 490000, 370000],
                },
                kaizen: [8, 12, 10, 18],
                inventoryTurnover: [3.5, 4.5, 2.5, 3.5],
                assetDowntime: [4, 3.5, 3, 4.5],
                policyProgress: [45, 60, 70, 75],
                realTimeAlerts: [5, 7, 6, 8],
            },
            'TMHNA': {
            revenue: '$4.9B', // $2.1B + $2.8B
            maintenance: '$3.1M', // $1.0M + $2.1M
            utilization: '78.5%', // Average of 82% and 75%
            overdue: '20', // 9 + 11
            fleetUtilization: [141, 150, 157, 153, 162, 168], // Sum arrays
            maintenanceCosts: [560000, 630000, 510000, 470000], // Sum arrays
            revenueProductLine: {
                labels: ['Forklifts', 'Trucks', 'Maintenance'],
                regionA: [1700000, 1320000, 660000], // Sum arrays
                regionB: [1570000, 1170000, 850000], // Sum arrays
            },
            kaizen: [21, 30, 22, 40], // Sum arrays
            inventoryTurnover: [8, 10, 6, 8], // Sum arrays
            assetDowntime: [7, 6, 5, 8], // Sum arrays
            policyProgress: [47.5, 62.5, 72.5, 77.5], // Average of 50, 65, 75, 80 and 45, 60, 70, 75
            realTimeAlerts: [9, 13, 11, 15], // Sum arrays
        },
        },
        '2022': {
            'TMH': {
                revenue: '$2.6B',
                maintenance: '$1.1M',
                utilization: '80%',
                overdue: '7',
                fleetUtilization: [72, 76, 80, 78, 83, 85],
                maintenanceCosts: [310000, 330000, 260000, 250000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [920000, 720000, 350000],
                    regionB: [850000, 650000, 450000],
                },
                kaizen: [12, 14, 11, 20],
                inventoryTurnover: [4, 5, 3, 4],
                assetDowntime: [2.5, 3.5, 1.5, 3],
                policyProgress: [40, 55, 65, 70],
                realTimeAlerts: [6, 5, 7, 8],
            },
            'Raymond': {
                revenue: '$2.7B',
                maintenance: '$4.2M',
                utilization: '73%',
                overdue: '12',
                fleetUtilization: [65, 70, 73, 71, 75, 78],
                maintenanceCosts: [260000, 280000, 230000, 200000],
                revenueProductLine: {
                    labels: ['Forklifts', 'Trucks', 'Maintenance'],
                    regionA: [720000, 560000, 260000],
                    regionB: [670000, 460000, 350000],
                },
                kaizen: [6, 10, 9, 15],
                inventoryTurnover: [3, 4, 2, 3.5],
                assetDowntime: [5, 4.5, 3.5, 5],
                policyProgress: [35, 50, 60, 65],
                realTimeAlerts: [7, 8, 6, 9],
            },
            'TMHNA': {
            revenue: '$5.3B', // $2.6B + $2.7B
            maintenance: '$5.3M', // $1.1M + $4.2M
            utilization: '76.5%', // Average of 80% and 73%
            overdue: '19', // 7 + 12
            fleetUtilization: [137, 146, 153, 149, 158, 163], // Sum arrays
            maintenanceCosts: [570000, 610000, 490000, 450000], // Sum arrays
            revenueProductLine: {
                labels: ['Forklifts', 'Trucks', 'Maintenance'],
                regionA: [1640000, 1280000, 610000], // Sum arrays
                regionB: [1520000, 1110000, 800000], // Sum arrays
            },
            kaizen: [18, 24, 20, 35], // Sum arrays
            inventoryTurnover: [7, 9, 5, 7.5], // Sum arrays
            assetDowntime: [7.5, 8, 5, 8], // Sum arrays
            policyProgress: [37.5, 52.5, 62.5, 67.5], // Average of 40, 55, 65, 70 and 35, 50, 60, 65
            realTimeAlerts: [13, 13, 13, 17], // Sum arrays
        },
        },
    };

    // DOM Elements
    const yearFilter = document.getElementById('yearFilter');
    const subsidiaryFilter = document.getElementById('subsidiaryFilter');
    const revenueText = document.getElementById('revenueText');
    const maintenanceText = document.getElementById('maintenanceText');
    const utilizationText = document.getElementById('utilizationText');
    const projectsText = document.getElementById('projectsText');

    // Chart Instances
    let fleetUtilizationChart;
    let maintenanceCostChart;
    let revenueChart;
    let kaizenChart;
    let inventoryTurnoverChart;
    let downtimeChart;
    let policyChart;
    let alertsChart;

    // Function to initialize charts
    function initializeCharts() {
        fleetUtilizationChart = createLineChart(
            'fleetUtilizationChart',
            'Fleet Utilization (%)',
            []
        );
        maintenanceCostChart = createBarChart(
            'maintenanceCostChart',
            'Maintenance Costs ($)',
            []
        );
        revenueChart = createStackedBarChart(
            'revenueChart',
            data['2024']['TMH'].revenueProductLine.labels,
            []
        );
        kaizenChart = createBarChart(
            'kaizenChart',
            'Kaizen Initiatives',
            []
        );
        inventoryTurnoverChart = createBarChart(
            'inventoryTurnoverChart',
            'Inventory Turnover Rate',
            []
        );
        downtimeChart = createBarChart(
            'downtimeChart',
            'Asset Downtime (Hours)',
            []
        );
        policyChart = createLineChart(
            'policyChart',
            'Policy Implementation Progress (%)',
            []
        );
        alertsChart = createBarChart(
            'alertsChart',
            'Real-Time Alerts',
            []
        );
    }

    // Create Line Chart
    function createLineChart(elementId, label, dataPoints) {
        return new Chart(document.getElementById(elementId), {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [
                    {
                        label: label,
                        data: dataPoints,
                        borderColor: '#ff5733',
                        tension: 0.4,
                        fill: false,
                    },
                ],
            },
        });
    }

    // Create Bar Chart
    function createBarChart(elementId, label, dataPoints) {
        return new Chart(document.getElementById(elementId), {
            type: 'bar',
            data: {
                labels: ['Q1', 'Q2', 'Q3', 'Q4'],
                datasets: [
                    {
                        label: label,
                        data: dataPoints,
                        backgroundColor: '#c70039',
                    },
                ],
            },
        });
    }

    // Create Stacked Bar Chart
    function createStackedBarChart(elementId, labels, datasets) {
        return new Chart(document.getElementById(elementId), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: datasets,
            },
            options: {
                scales: {
                    x: { stacked: true },
                    y: { stacked: true },
                },
            },
        });
    }

    // Update Charts based on filters
    function updateDashboard() {
        const year = yearFilter.value;
        const subsidiary = subsidiaryFilter.value;
        const selectedData = data[year][subsidiary];

        if (!selectedData) return; // Prevent errors for missing data

        // Update KPI Cards
        revenueText.textContent = selectedData.revenue;
        maintenanceText.textContent = selectedData.maintenance;
        utilizationText.textContent = selectedData.utilization;
        projectsText.textContent = selectedData.overdue;

        // Update Charts
        fleetUtilizationChart.data.datasets[0].data = selectedData.fleetUtilization;
        fleetUtilizationChart.update();

        maintenanceCostChart.data.datasets[0].data = selectedData.maintenanceCosts;
        maintenanceCostChart.update();

        revenueChart.data.datasets = [
            {
                label: 'Region A',
                data: selectedData.revenueProductLine.regionA,
                backgroundColor: '#ff5733',
            },
            {
                label: 'Region B',
                data: selectedData.revenueProductLine.regionB,
                backgroundColor: '#c70039',
            },
        ];
        revenueChart.update();

        kaizenChart.data.datasets[0].data = selectedData.kaizen;
        kaizenChart.update();

        inventoryTurnoverChart.data.datasets[0].data = selectedData.inventoryTurnover;
        inventoryTurnoverChart.update();

        downtimeChart.data.datasets[0].data = selectedData.assetDowntime;
        downtimeChart.update();

        policyChart.data.datasets[0].data = selectedData.policyProgress;
        policyChart.update();

        alertsChart.data.datasets[0].data = selectedData.realTimeAlerts;
        alertsChart.update();
    }

    // Initialize and Update
    initializeCharts();
    updateDashboard();

    // Add Event Listeners for Filters
    yearFilter.addEventListener('change', updateDashboard);
    subsidiaryFilter.addEventListener('change', updateDashboard);
});
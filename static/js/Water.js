$(document).ready(function(){
    $("#Goto").affix({
        offset: { 
            top: 200
     	}
    });


});

/* 折叠 Collapse */
/*
	Options: .collapse(options)		激活内容为可折叠元素。接受一个可选的 options 对象。
	Toggle:  .collapse('toggle')	切换显示/隐藏可折叠元素。
	Show:    .collapse('show')		显示可折叠元素。
	Hide:    .collapse('hide')		隐藏可折叠元素。
*/
$(function () { $('#').collapse({          
  	toggle: false          						/*.collapse(options)*/
})});
$(function () { $('#collapseOne').collapse('show')});
$(function () { $('#collapseTwo').collapse('hide')});
$(function () { $('#collapseThree').collapse('hide')});
$(function () { $('#collapseFour').collapse('hide')});
$(function () { $('#collapseFive').collapse('hide')});
$(function () { $('#collapseSix').collapse('hide')});


/* 仪表图 速度表改装为进度表 */
/* 服务类  */
$(function () {
    $('#container_Service').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

            /* 侯超群 20160306 */ 
            height: 180,
            width: 180
        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});

/* 运行类  */
$(function () {
    $('#container_Operation').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

			height: 180,
            width: 180          
        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});

/* 资源类 */
$(function () {
    $('#container_Resource').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

            height: 180,
            width: 180        
        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});

/* 资产类 */
$(function () {
    $('#container_Property').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

            height: 180,
            width: 180          
        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});

/* 财经类 */
$(function () {
    $('#container_Finance').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

            height: 180,
            width: 180

        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});

/* 人事类 */
$(function () {
    $('#container_Human').highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,

            height: 180,
            width: 180

        },
        
        title: {
            text: ' '
        },
        
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
           
        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
    
            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 60,
                color: '#aaaaff' // blue 1
            }, {
                from: 60,
                to: 80,
                color: '#4a4aff' // blue 2
            }, {
                from: 80,
                to: 100,
                color: '#000093' // blue 3
            }]        
        },
    
        series: [{
            name: '已完成',
            data: [0],
            tooltip: {
                valueSuffix: '%'
            }
        }]
    
    }, 
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
            setInterval(function () {
                /*
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);
                
                newVal = point.y + inc;
                if (newVal < 0 || newVal > 100) {
                    newVal = point.y - inc;
                }
                */
                var point = chart.series[0].points[0];
                newVal = 3.25;
                point.update(newVal);
                
            }, 3000);
        }
    });
});
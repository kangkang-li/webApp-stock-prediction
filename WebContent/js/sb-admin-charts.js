// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// -- uty: test Area Chart Example
function getFileFromServer(url, doneCallback) {
    var xhr;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = handleStateChange;
    xhr.open("GET", url, true);
    xhr.send();

    function handleStateChange() {
        if (xhr.readyState === 4) {
            doneCallback(xhr.status == 200 ? xhr.responseText : null);
        }
    }
}


/*var urlparameter;
if (null != window.location.hash) {
    var index = window.location.hash.indexOf("#");

    if (-1 != index) {
        urlparameter = window.location.hash.substring(1);
    }
    else {
        urlparameter = 'AMZN';
    }

    getFileFromServer("stockdata\\" + urlparameter + ".json", function(text) {

        if (text === null) {
            // An error occurred
            alert('cannot find test.json');
        }
        else {
            var obj;
            var stocklabel;

            // `text` is the file text
            //alert(text);
            obj = JSON.parse(text);

            var metaObj = obj['Meta Data'];
            stocklabel = metaObj['2. Symbol'];

            var data = obj['Time Series (Daily)'];

            var plotlabels = [], plotdata=[];

            for (x in data) {
                console.log(x);
                console.log(data[x]['4. close']);
                plotlabels.unshift(x);
                plotdata.unshift(data[x]['4. close']);
            }




            var ctx = document.getElementById("myAreaChart_test1");
            var myLineChart_test1 = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: plotlabels,
                    datasets: [{
                        data: plotdata,
                        label: stocklabel,
                        borderColor: "#3e95cd",
                        fill: false
                    }]
                },
            });
        }
    });
}*/


var myLineChart_test1;
var myVolumeChart_test1;
function updatechart (stock, obj) {

	if ("" == stock) {
		//document.getElementById("card mb-3").innerHTML = "TEST!";
		var items = document.getElementsByClassName("card mb-3");
		items[0].innerHTML = "<center>" +
				"<h1>Web Application of Stock Forecast</h1>" +
				"<br>" +
				"<h2>Group 8</h2>" +
				"<h3>Jia Xue, Jiawen Sun, Ke Xu, KangKang Li, Lang Liu, Mingbo Zhang</h3>" +
				"</center>";
		
		items[1].innerHTML = "";
		return;
	}
	if ('#' == stock[0]) {
		stock = stock.substring(1, stock.length);
	}
	
	alert("updatechart: " + stock);
	
	var loc = window.location.pathname;
	var dir = loc.substring(0, loc.lastIndexOf('/'));


    
	
	var plotlabels = [], plotdata = [], plotopen = [], plothigh = [], plotlow = [], plotvolume = [];
	for (x in obj) {
		plotlabels.push(x);
        plotdata.push(obj[x]['close']);
        plotopen.push(obj[x]['open']);
        plothigh.push(obj[x]['high']);
        plotlow.push(obj[x]['low']);
        plotvolume.push(obj[x]['volume']);
	}



    // if the chart is not undefined (e.g. it has been created)
    // then destory the old one so we can create a new one later
    if (myLineChart_test1) {
        myLineChart_test1.destroy();
    }
    
    if (myVolumeChart_test1) {
        myVolumeChart_test1.destroy();
    }

    var ctx = document.getElementById("myAreaChart_test1");
    var ctx2 = document.getElementById("myVolumeChart_test1");
    myLineChart_test1 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: plotlabels,
        	//labels: Object.keys(obj),
            datasets: [{
                type: 'line',
                data: plotdata,
                label:'close',
                borderColor: [
                              'rgba(255,99,132,1)',
                              'rgba(54, 162, 235, 1)',
                              'rgba(255, 206, 86, 1)',
                              'rgba(75, 192, 192, 1)',
                              'rgba(153, 102, 255, 1)',
                              'rgba(255, 159, 64, 1)'
                          ],
                borderWidth: 1,
                fill: true,
                pointDotRadius:3,
            }, 
            
            {
                type: 'line',
                data: plotopen,
                label:'open',
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
                fill: true,
                pointDotRadius:3,
            },
            {
                type: 'line',
                data: plothigh,
                label:'high',
                borderColor: [
                              'rgba(255,99,132,1)',
                              'rgba(54, 162, 235, 1)',
                              'rgba(255, 206, 86, 1)',
                              'rgba(75, 192, 192, 1)',
                              'rgba(153, 102, 255, 1)',
                              'rgba(255, 159, 64, 1)'
                          ],
                borderWidth: 1,
                fill: true,
                pointDotRadius:3,
            },
            {
                type: 'line',
                data: plotlow,
                label:'low',
                borderColor:[
                             'rgba(255,99,132,1)',
                             'rgba(54, 162, 235, 1)',
                             'rgba(255, 206, 86, 1)',
                             'rgba(75, 192, 192, 1)',
                             'rgba(153, 102, 255, 1)',
                             'rgba(255, 159, 64, 1)'
                         ],
                borderWidth: 1,
                fill: true,
                pointDotRadius:3,
            }
            
            /*{
                type: 'bar',
                data: plotvolume,
                fill: true
            }*/]
        },
        options: {
            //title: {
            //    display: true,
            //    text: 'World population per region (in millions)'
            //}
            //scales: {
            //    yAxes: [{
            //        scaleLabel: {
            //            display: true,
            //            labelString: 'Closing Price'
            //        }
            //    }]
            //}
        }
    });
    
    
    myVolumeChart_test1 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: plotlabels,
            datasets: [{
                type: 'line',
                label:'volume',
                data: plotvolume,

                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
                fill: true,
                pointDotRadius:3,
            }
            ]
        },
        options: {

        }
    });
}

function getprediction (stock) {
    document.predictionform.optionStockSymbol.value = stock;
    
    //document.getElementById("optionStockSymbol").value=stock; // it doesn't work this way
	document.forms['predictionform'].submit();

}

//window.onload = function() {
//	
//    updatechart(window.location.hash); // get #parameter
//    //alert(window.location.hash);
//};

// -- Area Chart Example
/*var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
        datasets: [{
            label: "Sessions",
            lineTension: 0.3,
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "rgba(2,117,216,1)",
            pointRadius: 5,
            pointBackgroundColor: "rgba(2,117,216,1)",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 20,
            pointBorderWidth: 2,
            data: [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
        }],
    },
    options: {
        scales: {
            xAxes: [{
                time: {
                    unit: 'date'
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 7
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 40000,
                    maxTicksLimit: 5
                },
                gridLines: {
                    color: "rgba(0, 0, 0, .125)",
                }
            }],
        },
        legend: {
            display: false
        }
    }
});*/
/*// -- Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [{
            label: "Revenue",
            backgroundColor: "rgba(2,117,216,1)",
            borderColor: "rgba(2,117,216,1)",
            data: [4215, 5312, 6251, 7841, 9821, 14984],
        }],
    },
    options: {
        scales: {
            xAxes: [{
                time: {
                    unit: 'month'
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 6
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 15000,
                    maxTicksLimit: 5
                },
                gridLines: {
                    display: true
                }
            }],
        },
        legend: {
            display: false
        }
    }
});
// -- Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ["Blue", "Red", "Yellow", "Green"],
        datasets: [{
            data: [12.21, 15.58, 11.25, 8.32],
            backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
        }],
    },
});*/

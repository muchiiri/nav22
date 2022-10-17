
	// ---------------names function-------------


// to check the value is hexa or not
const isValidHex = (hexValue) => /^#([A-Fa-f0-9]{3,4}){1,2}$/.test(hexValue)

const getChunksFromString = (st, chunkSize) => st.match(new RegExp(`.{${chunkSize}}`, "g"))
// convert hex value to 256
const convertHexUnitTo256 = (hexStr) => parseInt(hexStr.repeat(2 / hexStr.length), 16)
// get alpha value is equla to 1 if there was no value is asigned to alpha in function
const getAlphafloat = (a, alpha) => {
    if (typeof a !== "undefined") { return a / 255 }
    if ((typeof alpha != "number") || alpha < 0 || alpha > 1) {
        return 1
    }
    return alpha
}
// convertion of hex code to rgba code
function hexToRgba(hexValue, alpha) {
    if (!isValidHex(hexValue)) { return null }
    const chunkSize = Math.floor((hexValue.length - 1) / 3)
    const hexArr = getChunksFromString(hexValue.slice(1), chunkSize)
    const [r, g, b, a] = hexArr.map(convertHexUnitTo256)
    return `rgba(${r}, ${g}, ${b}, ${getAlphafloat(a, alpha)})`
}

let myVarVal 
function names(){

	let docStyle = getComputedStyle(document.documentElement);

	//get variable
	myVarVal  =  localStorage.getItem("primaryColor") || localStorage.getItem("darkPrimary") || localStorage.getItem("transparentPrimary") || localStorage.getItem("transparentBgImgPrimary") || "#4d65d9";

	if(document.querySelector('#salessummary') !== null){
        index2();
    }
	if(document.querySelector('#sales-summary') !== null){
        index();
    }
	if(document.querySelector('#revenuemorrischart') !== null){
        morrisFn();
    }


	let colorData = hexToRgba(myVarVal || "#4d65d9", 0.05)
	document.querySelector('html').style.setProperty('--primary005', colorData);

	let colorData1 = hexToRgba(myVarVal || "#4d65d9", 0.2)
	document.querySelector('html').style.setProperty('--primary02', colorData1);

	let colorData2 = hexToRgba(myVarVal || "#4d65d9", 0.3)
	document.querySelector('html').style.setProperty('--primary03', colorData2);

	let colorData5 = hexToRgba(myVarVal || "#4d65d9", 0.5)
	document.querySelector('html').style.setProperty('--primary05', colorData5);

	let colorData3 = hexToRgba(myVarVal || "#4d65d9", 0.7)
	document.querySelector('html').style.setProperty('--primary07', colorData3);

	let colorData4 = hexToRgba(myVarVal || "#4d65d9", 0.8)
	document.querySelector('html').style.setProperty('--primary08', colorData4);

	let colorData6 = hexToRgba(myVarVal || "#4d65d9", 0.1)
	document.querySelector('html').style.setProperty('--primary01', colorData6);


}
names()

// -------------------index charts------------------
function index() {

	/* Chartjs (#sales-summary) */
	var myCanvas = document.getElementById("sales-summary");
	myCanvas.height = "300";
	var myChart = new Chart(myCanvas, {
		type: 'bar',
		data: {
			labels: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"],
			datasets: [{
				label: 'Sales',
				data: [27, 16, 27, 22, 14, 18, 27, 21, 14, 27, 20, 27],
				backgroundColor: myVarVal,
				borderWidth: 1,
				hoverBackgroundColor: myVarVal,
				hoverBorderWidth: 0,
				borderColor: myVarVal,
				hoverBorderColor: myVarVal,
			}, {

				label: 'Profits',
				data: [44, 24, 39, 30, 31, 32, 39, 28, 24, 39, 31, 39],
				backgroundColor: hexToRgba(myVarVal, 0.2) ||'#9fa8e0',
				borderWidth: 1,
				hoverBackgroundColor: hexToRgba(myVarVal, 0.2) || '#9fa8e0',
				hoverBorderWidth: 0,
				borderColor: hexToRgba(myVarVal, 0.2) || '#9fa8e0',
				hoverBorderColor: hexToRgba(myVarVal, 0.2) ||'#9fa8e0',
			},

			]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
			layout: {
				padding: {
					left: 0,
					right: 0,
					top: 0,
					bottom: 0
				}
			},
			tooltips: {
				enabled: false,
			},
			scales: {
				yAxes: [{
					gridLines: {
						display: true,
						drawBorder: false,
						zeroLineColor: 'rgba(142, 156, 173,0.1)',
						color: "rgba(142, 156, 173,0.1)",
					},
					scaleLabel: {
						display: false,
					},
					ticks: {
						beginAtZero: true,
						stepSize: 10,
						max: 50,
						fontColor: "#8492a6",
						fontFamily: 'Hind Siliguri',
					},
				}],
				xAxes: [{
					barPercentage: 0.15,
					barValueSpacing: 3,
					barDatasetSpacing: 3,
					barRadius: 5,
					stacked: true,
					ticks: {
						beginAtZero: true,
						fontColor: "#8492a6",
						fontFamily: 'Hind Siliguri',
					},
					gridLines: {
						color: "rgba(142, 156, 173,0.1)",
						display: false
					},

				}]
			},
			legend: {
				display: true,
				
			},
			elements: {
				point: {
					radius: 0,
				}
			}
		}
	});
	/* Chartjs (#sales-summary) closed */



};
 function morrisFn(){

	// index CHART COLOR dOTS
	document.querySelector('.bg-primary-light-1').style.background = hexToRgba(myVarVal, 0.7) ;
	document.querySelector('.bg-primary-light-2').style.background = hexToRgba(myVarVal, 0.5) ;
	document.querySelector('.bg-primary-light-3').style.background = hexToRgba(myVarVal, 0.2) ;

	 	/*Morris chart */
	new Morris.Donut({

		element: 'revenuemorrischart',
		data: [
			{ label: "clients", value: 15 },
			{ label: "sales", value: 42 },
			{ label: "shares", value: 20 },
			{ label: "profits", value: 23 }
		],
		colors: [hexToRgba(myVarVal, 0.7) || "#7886d3", myVarVal, hexToRgba(myVarVal, 0.2) || "#d8dcf3", hexToRgba(myVarVal, 0.5) || "#9fa8e0"],
		labelColor: '#77778e',
		resize: true,
	});

	if (document.querySelectorAll('#revenuemorrischart svg').length >= 2) {
		let svgs = document.querySelectorAll('#revenuemorrischart svg')

		for (var i = 0; i <= svgs.length - 1; i++) {
			if (i == 0) {

			}
			else {
				svgs[i].remove()
			}
		}
	}
 }

//  -----------index2 charts------------

function index2() {
	'use strict'
	/* Apex Chart Start*/
	var options = {
		series: [{
			name: 'Net Profit',
			type: 'column',
			data: [22, 34, 56, 37, 35, 21, 34, 60, 78, 56, 53, 89],
		}, {
			name: 'Sales',
			type: 'column',
			data: [42, 50, 70, 57, 55, 58, 43, 80, 54, 23, 34, 77],
		}, {
			name: 'Total',
			type: 'line',
			data: [25, 36, 58, 39, 38, 25, 37, 62, 56, 25, 37, 79],
		}],
		chart: {
			height: 300,
			foreColor: 'rgba(142, 156, 173, 0.9)',
		},
		stroke: {
			width: [0, 2, 4],
			curve: "smooth"
		},
		grid: {
			borderColor: 'transparent',
		},
		colors: [myVarVal || "#4d65d9", "#d7d7d9", "#e4e7ed"],
		plotOptions: {
			bar: {
				endingShape: 'rounded',
				horizontal: false,
				columnWidth: '30%',
			},
		},
		dataLabels: {
			enabled: false,
		},
		legend: {
			show: true,
			position: 'top',
			labels: {
				color: 'rgba(142, 156, 173, 0.9)'
			},
			fontFamily: 'Hind Siliguri',
		},
		stroke: {
			show: true,
			width: 4,
			colors: ['transparent']
		},
		yaxis: {
			title: {
				style: {
					color: '#adb5be',
					fontSize: '14px',
					fontFamily: 'Hind Siliguri',
					fontWeight: 600,
					cssClass: 'apexcharts-yaxis-label',
				},
			},
			labels: {
				rotate: -90,
				style: {
					fontFamily: 'Hind Siliguri',
					cssClass: 'summaryyaxis',
				}
			}
		},
		xaxis: {
			type: 'month',
			categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
			axisBorder: {
				show: true,
				color: 'rgba(119, 119, 142, 0.05)',
				offsetX: 0,
				offsetY: 0,
			},
			axisTicks: {
				show: true,
				borderType: 'solid',
				color: 'rgba(119, 119, 142, 0.05)',
				width: 6,
				offsetX: 0,
				offsetY: 0
			},
			labels: {
				rotate: -90,
				style: {
					fontFamily: 'Hind Siliguri',
					cssClass: 'summaryxaxis',
				}
			}
		},
		markers: {
			size: 0
		}
	};

	document.getElementById('salessummary').innerHTML = ''
	var chart = new ApexCharts(document.querySelector("#salessummary"), options);
	chart.render();

	/* Apex Chart End*/

	// circle 1
	$('#circle1').circleProgress({
		value: 0.7,
		size: 60,
		fill: {
			color: ["#ff9b21"]
		}
	})
		.on('circle-animation-progress', function (event, progress) {
			$(this).find('strong').html(Math.round(70 * progress) + '<i>%</i>');
		});

	// circle 2
	$('#circle2').circleProgress({
		value: 0.85,
		size: 60,
		fill: {
			color: ["#19b159"]
		}
	})
		.on('circle-animation-progress', function (event, progress) {
			$(this).find('strong').html(Math.round(85 * progress) + '<i>%</i>');
		});

}

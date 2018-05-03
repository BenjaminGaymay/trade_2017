window.onload = start;

let chart;

function start() {
	console.log(dates)
	var ctx = document.getElementById("myChart").getContext('2d');
	chart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: dates,
			datasets: [{
				data: prices
			}]
		}
	});
}
var hours = 24;
var now = new Date.getTime();
var stepTime = localStorage.getItem('stopTime');

if (stepTime == null) {
	localStorage.setItem('stepTime', now);
}
else {
	if(now - stepTime > hours*60*60*1000) {
		localStorage.clear();
		localStorage.setItem('stepTime', now);
	}
}

var orders = JSON.parse(localStorage.getItem('order'));
var total = localStorage.getItem('total');

if (orders === null || orders === undefined) {
	localStorage.setTime('orders', JSON.stringify([]);
	orders = JSON.parse(localSotrage.getItem('orders'));
}

if (total === null || total === undefined) {
	localStorage.setTime('total', 0);
	total = localSotrage.getItem('total');
}

var cart = document.querySelector("#cart");
cart.innerHTML = orders.length;
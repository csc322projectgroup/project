var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

function addItem1(pid){
	itemID = '#it' + pid;
	var name = document.querySelector(itemID).innerHTML
	pcart.innerHTML += '<li>'+ name +'</li>';
	
	var orders = JSON.parse(localStorage.getItem('order'));
	var total = localStorage.getItem('total');
	total = Number(total) + Number(price);
	ptotal.innerHTML = 'Total: ' + total + '';
}
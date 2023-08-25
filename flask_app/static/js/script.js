var deliveryForm = document.getElementById("delivery-form");
deliveryForm.onsubmit = function (e) {
	e.preventDefault();

	var form = new FormData(deliveryForm);

	fetch("http://127.0.0.1:5000/create/delivery", { method: "POST", body: form })
		.then((response) => response.json())
		.then((data) => {
			populateCell(data);
			getDeliveries();
		});
};

function getDeliveries() {
	fetch("http://127.0.0.1:5000/deliveries")
		.then((res) => res.json())
		.then((data) => {
			for (let i = 0; i < data.length; i++) {
				populateCell(data[i]);
			}
		});
}
getDeliveries();

function populateCell(cellData) {
	let delCell = document.getElementById(`${cellData.schedule_id}${cellData.is_first_run}${cellData.stop_num}`);
	delCell.innerText = `${cellData.customer.company_name} | ${cellData.address.city}`;
	delCell.classList.add("bg-info");
}

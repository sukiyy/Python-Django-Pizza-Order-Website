function testCardNumber() {
	"use strict";
	var ccNum = document.getElementById("cardNumber").value;
	
	var namefield=document.getElementById("name");
	var cvvfield=document.getElementById("cvv");
	var cdfield = document.getElementById("cardNumber");	
	
    var visaRegEx = /^(?:4[0-9]{12}(?:[0-9]{3})?)$/;
    var mastercardRegEx = /^(?:5[1-5][0-9]{14})$/;
    var isValid = false;

	//test empty field
	if (namefield.length===0){
		alert("Please enter the name on card!");
	}
	if (cvvfield.length===0){
		alert("Please enter the CVV to complete your order!");
	}
	if (cdfield.length===0){
		alert("Please enter the credit card number to complete your order!");
	}
	//for visa and mastercard
	if (visaRegEx.test(ccNum)) {
		isValid = true;
    } else if(mastercardRegEx.test(ccNum)) {
        isValid = true;
    }
    if(isValid) {
		alert("Thank You for your order!");
    } else {
		alert("Please provide a valid Visa/Mastercard number!");
	}
	
	select();
}


function select() {
	"use strict";
	var x = document.getElementById("pizza").value;
	var output=document.getElementById("optionResult");
	if(x==="Hawaiian"){
		var para = document.createElement("P");
		var t = document.createTextNode("You select Hawaiian Pizza. Price:10$, Topping:cheese, pineapple, Canadian bacon, ham.");
        para.appendChild(t);
		output.appendChild(para);
	}else{
		var para2 = document.createElement("P");
		var t2 = document.createTextNode("You select Meat Lover Pizza. Price:12$, Topping:cheese, bacon, ham, pepperoni, hot sausage.");
        para2.appendChild(t2);
		output.appendChild(para2);
	}
}

function goBack()
{
	window.history.back()
}
function integrate_js()
{
	var upper = document.getElementById("upper").value
	var func = document.getElementById("function").value
	var lower = document.getElementById("lower").value
	//eel.generate_qr(data)(setImage)
	alert(upper,func,lower);
	eel.test(lower,func,upper)
	
}
/*
function factorise_js()
{
	var equation = document.getElementById("equation").value
	var variable = document.getElementById("variable").value
	var ans = eel.factorise(equation,variable);
	document.getElementById("ans_factorise").innerHTML=ans;
}
*/

async function factorise_js()
{
	var equation = document.getElementById("equation").value
	//alert(equation);
	let ans= await eel.factorise(equation)();
	document.getElementById("ans_factorise").innerHTML=ans;
}
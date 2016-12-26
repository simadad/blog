var logInBar = document.getElementById('logInBar');

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			};
		};
	};
	return cookieValue;
};

function u_long(str){
	if(str.length>20){
		document.getElementById('u_long').hidden=undefined;
	};
};

function p_short(str){
	if(str.length<5){
		document.getElementById('p_short').hidden=undefined;
	};
};

function login(ifNew, url){
	var username = document.getElementById('username').value;
	var password = document.getElementById('password').value;
	console.log(ifNew, username, password);
	var xmlhttp = new XMLHttpRequest();
	if(ifNew){
		xmlhttp.open('POST', url, true);
	}else{
		xmlhttp.open('POST', url, true);
	};
	var csrftoken = getCookie('csrftoken');
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			var info = xmlhttp.responseText;
			console.log('login', info);
			logInBar.innerHTML = info;
		};
	};
	xmlhttp.setRequestHeader('X-CSRFToken',csrftoken);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send('username='+username+'&password='+password);
};

function quit(url){
	console.log('aaaaaaa');
	var logInBar = document.getElementById('logInBar');
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('GET', url, true);
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState==4 && xmlhttp.status==200){
			var info = xmlhttp.responseText;
			console.log('logout', info);
			logInBar.innerHTML = info;
		};
	};
	xmlhttp.send();
};

function search_check(str)	
{
if (str.length>10)
	{
	alert('too long!');
	};
};
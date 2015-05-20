/*
 * Disclaimer terms e.t.c.
 */

//Some needed constants
var localUrl = ""; //ip address of the edison w.r.t. the user pc
var control = new Object();
control.state = 0;
//Functions 

function pause(){
	control.state = 0;
}

function play(){
	control.state = 1;
}


$().ready(function(){
	//On Window.Load variables
	var context = $("#canvas").getContext('2d');
	var fps = 0;
	var image = new Image();
	imgWidth = 512;
	imgHeight = 512;
	control.state = 0;

	
	//Setup websocket when window loaded
	connection = new WebSocket(localUrl); 
	
	connection.onopen = function(evt) { 
		alert("Connection Initiated!");
	}; 
	
	connection.onclose = function(evt) { 
		alert("Connection to Websocket Closed!");
	}; 
	
	connection.onmessage = function(evt) {
		if (control.state ==1){
			console.log(evt.data)//Debugging Purposes
			//Update canvas with image info
			context.drawImage(evt.data, imgWidth, imgHeight);
		}
	}; 
	
	connection.onerror = function(evt) {
		alert("Error on Connection!! : "+ evt.data);
	}; 
	
	//Button functions
	$("#START").click(function(){
		play();
	});//Start Button
	
	$("#STOP").click(function(){
		play();
	});//Stop Button

	
});
---
layout: default
title: JavaScript, Part I
nav_order: 5
---

## Javascript in DS
Javascript is one of the most important client side programming languages.  We use it very often in our projects, so some familiarity with the syntax and functionality of JS and common JS libraries is important. Mozilla offers a useful [tutorial on JS grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types).

The [W3 schools javascript tutorial](https://www.w3schools.com/js/) is an excellent place to start.

As an example, I will show you how to make some basic visualizations of our courses data using p5.js and D3.  

Much of our learning will utilize the [p5.js web editor](https://editor.p5js.org/)
We will also build on Princeton's [playing with data workshop](https://github.com/Princeton-CDH/playingwithdata)

We will also make use of the [D3 library](https://d3js.org/)

There are multiple examples of D3 on [codepen](https://codepen.io/tag/d3/) to work from. 

```HTML
<head>
  <!-- Plotly.js -->
   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

<body>
  <div id="myDiv" style="width: 100%; height: 700px;"><!-- Plotly chart will be drawn inside this DIV --></div>
  <script>
function makeplot() {
 	Plotly.d3.csv("https://raw.githubusercontent.com/HCDigitalScholarship/summer-django/master/department_counts.csv", function(data){ processData(data) } );

};
	
function processData(allRows) {

	console.log(allRows);
	var x = [], y = [], standard_deviation = [];

	for (var i=0; i<allRows.length; i++) {
		row = allRows[i];
		x.push( row['department'] );
		y.push( row['count'] );
	}
	console.log( 'X',x, 'Y',y, 'SD',standard_deviation );
	makePlotly( x, y, standard_deviation );
}

function makePlotly( x, y, standard_deviation ){
	var plotDiv = document.getElementById("plot");
	var traces = [{
		x: x, 
		y: y
	}];

	Plotly.newPlot('myDiv', traces, 
		{title: 'Number of Classes offered in Fall 2019 by Department'});
};
  makeplot();  </script>
</body>
```

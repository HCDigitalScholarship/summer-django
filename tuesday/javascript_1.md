---
layout: default
title: JavaScript
nav_order: 4
parent: Tuesday
---

## Javascript in DS
Javascript is one of the most important client side programming languages.  We use it very often in our projects, so some familiarity with the syntax and functionality of JS and common JS libraries is important. Mozilla offers a useful [tutorial on JS grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types).

The [W3 schools javascript tutorial](https://www.w3schools.com/js/) is an excellent place to start.

## For loops 
```javascript
//define an array
var fish_array = ["trout", "tuna", "cod", "herring", "salmon", "fry"];

var text = "";
var i;
for (i = 0; i < fish_array.length; i++) {
  text += fish_array[i] + "<br>";
}
document.getElementById("demo").innerHTML = text;
```
> As an exercise, right click on this page and then click on console.  Type in each line of the code above to get a feel for the syntax of javascript.
<p id="demo"></p>

It helps me to think of JS for loops as similar to a while loop in Python:
```python 
fish_list = ["trout", "tuna", "cod", "herring", "salmon", "fry"]
text = ''
i = 0
while i < len(fish_list):
    text += fish_list[i] + "<br>"
    i += 1
```


---

As an example, I will show you how to make some basic visualizations of our courses data using p5.js and D3.  

Much of our learning will utilize the [p5.js web editor](https://editor.p5js.org/)
We will also build on Princeton's [playing with data workshop](https://github.com/Princeton-CDH/playingwithdata)

We will also make use of the [D3 library](https://d3js.org/)

There are multiple examples of D3 on [codepen](https://codepen.io/tag/d3/) to work from. 

Here is an example using Plotly.js to create a chart of the number of courses offered by each department. 
Here is the [HTML](https://raw.githubusercontent.com/HCDigitalScholarship/summer-django/master/courses_by_department.html)


  <!-- Plotly.js -->
   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

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
  makeplot();  
  </script>

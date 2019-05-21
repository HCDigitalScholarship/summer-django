---
layout: default
title: JavaScript
nav_order: 4
parent: Tuesday
---

## Javascript in DS
Javascript is the most important client side programming languages we use in our projects.  Some familiarity with the syntax and functionality of JS and common JS libraries will help you make sense of existing code and to develop your own. 
- Mozilla offers a useful [tutorial on JS grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types).
- The [W3 schools javascript tutorial](https://www.w3schools.com/js/) is an excellent place to start.


It can be helpful for me to think of JS for-loops as similar to a while loop in Python:

```python 
fish_list = ["trout", "tuna", "cod", "herring", "salmon", "fry"]
text = ''
i = 0
while i < len(fish_list):
    text += fish_list[i] + "<br>"
    i += 1
```  

Of couse, we could just use a list comprehension,   
`''.join([fish+'<br>' for fish in fish_list])`, 
but it wouldn't work in the browser.  There are advantages and disadvantages to all languages and it's a good practice to learn more than one. 

- Short exercise, the for loop   

```
var fish_array = ["trout", "tuna", "cod", "herring", "salmon", "fry"];

var text = "";

var i;
// try entering console.log(i) in the console.  Note that it exists, but has no value. 

for (i = 0; i < fish_array.length; i++) {
  text += fish_array[i] + "<br>";
}
document.getElementById("demo").innerHTML = text;
```  

Right click on this page, click inspect and then click on console.  
- Type in each line of the code above (you can use something other than fish if you like) to get a feel for the syntax of javascript.  
- Use `console.log(fish_array)` to print its current value.  Note that the array can exist without any data.  It will simply show undefined. 
- If all goes well, you will see the names in the array printed on this page below:
<p id="demo"></p>

 
---
In the next section, you will learn how to draw, to create animations and data visualizations with p5.js. 

We also use the [D3 library](https://d3js.org/) very often for data visualizations. There are multiple examples of D3 on [codepen](https://codepen.io/tag/d3/) to work from.  The [plotly Python libary](https://plot.ly/python/) lets you create D3 visualizations in Python.  We also use [Dash](https://dash.plot.ly/) to generate interactive dashboards.    

As a quick exercise, here is an example using Plotly.js to create a chart of the number of courses offered by each department. 

Open up the source [HTML](https://raw.githubusercontent.com/HCDigitalScholarship/summer-django/master/courses_by_department.html) file here and have a look in the script section.  Where do you see a for loop in the script?  

Follow the script from function to function to get a feeling for how the graph is being generated. 

---

  <!-- Plotly.js -->
   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

  <div id="myDiv" style="width: 100%; height: 700px;"><!-- Plotly chart will be drawn inside this DIV --></div>
  <script>
function makeplot() {
 	Plotly.d3.csv("https://raw.githubusercontent.com/HCDigitalScholarship/summer-django/master/department_counts.csv", function(data){ processData(data) } );

};
	
function processData(allRows) {

	// console.log(allRows);
	var x = [], y = [], standard_deviation = [];

	for (var i=0; i<allRows.length; i++) {
		row = allRows[i];
		x.push( row['department'] );
		y.push( row['count'] );
	}
	// console.log( 'X',x, 'Y',y, 'SD',standard_deviation );
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

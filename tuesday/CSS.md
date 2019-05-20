---
layout: default
title: CSS
parent: Tuesday
nav_order: 3
---

## CSS (Cascading Style Sheets)

![Cascading waterfall](https://live.staticflickr.com/4883/45795354092_55b929688f_b.jpg)
                                                                                                                     
CSS is what makes the web pretty and more usable. It styles web pages so that the same application can be optimized for all devices (desktop, laptop, tablet, mobile, etc.) and applies aesthetic enhancements to pages of otherwise very plain text and images.

CSS rules are written by HTML element or class (we'll get into more case-specific CSS rules later). What do you think the following block does to the display of a web page?

```
p {
  font-family: Roboto;
  font-size: 14px;
  text-align: right;
  text-transform: lowercase;
  }
```

Let's look at the [Mozilla CSS Tutorial](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS) for some more on how to use CSS, and use some of these rules to style the HTML pages you created earlier.

## Inspect tools

We can actually see how this works in real time using the "Inspect" feature of most web browsers (Firefox and Safari call it "Inspect Element," Chrome calls it "Inspect." If you're using Safari, make sure the "Developer" menu is enabled in your preferences.) Right- or secondary-click on any part of a web page in your browser and open the Inspect tool. Start tinkering!

## HTML + CSS + Javascript libraries
Luckily, UI developers and experts have done _lots_ of heavy lifting for us already, and have created libraries that combine HTML, CSS, and Javascript (more on that this afternoon) to create beautiful and responsive web interfaces. [Bootstrap](https://getbootstrap.com/), developed at Twitter in 2011 to create consistency across internal tools, is one of the first and most popular front-end frameworks on the web today. Frameworks like these use a [grid](https://getbootstrap.com/docs/4.3/layout/grid/) system to create responsive sites, a combination of HTML elements and attributes with CSS rules that shape the layout of web pages that responds to window sizes. The grid is what allows for a 3-wide image gallery to render as a single column of images on a mobile device, or a top level navigation bar to become a "hamburger" menu on a tablet. 

The grid is a key concept of all responsive frameworks. It causes some headaches as you work through formatting your pages, but you'll be thankful for the grid when it all comes together!

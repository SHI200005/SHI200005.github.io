---
layout: post
title: (En) Save Plots in a Vector Format
categories: Coding-Issues
description: 
keywords: 
---

I use `matplotlib.pyplot` to generate plots. When you show the plots in my `Spyder` or `Jupyter Notebook` IDEs and save them by clicking, the default format is `.png`. However, in scientific publications, we use **vector images** to make sure they work well when embedded in text (i.e. the dots and captions do not blur when zooming in and zooming out).

In `Spyder` IDE, you can change the default format of image saving to `.svg`, but it seems that it does not work well when embedded in `LaTeX`, and some journals do not accept the format (???). The universal way is to save them as `.pdf` format. 

However, when the script for plotting stops running and the figures are already on the screen, it is hard to save them as `.pdf` format. It could be frustrating if it needed approx 10 hours to run the script. You do not want to re-run it! Therefore, it is important to develop a habit for embedding plot saving code in your script before you run it. Here is the hint. If your script output multiple images, use

``` 
import matplotlib.pyplot as plt

# Plot the first figure
def plot_first():
	fig, ax = plt.subplots() # create a figure object
	... i.e. ax.plot()
	plt.savefig('first.pdf', format='pdf')

# Plot the second figure
def plot_desond():
	fig, (ax1,ax2,ax3) = plt.subplots() # create a figure object
	... i.e. ax1.plot()
	plt.savefig('second.pdf', format='pdf')

plot_first()
plot_second()
```

Note that it is very important to create **figure objects** for multiple-figure saving!  

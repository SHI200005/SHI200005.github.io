---
layout: post
title: (En) Information Theory
categories: PhD-UT-Course-Review
description: 
keywords: quantum mechanics
mathjax: true 
---

> The math you get used to and the math you understand are different. You may first get used to some math, and then it may take years to understand. --Prof Frank Kschischang 

This is an informal oral statement from our lectures. I relate to this statement so much that I would like to put it down here.

## Relative entropy and Mutual Information



## Convex Function

### Convex Optimization



## Gaussian Channel

### Bandlimited Channels

#### Sampling Theorem

A continuous band-limited time-series (to *W* Hz) can be **perfectly** reconstructed, if uniformly (in time) sampled with a minimum frequency of 2*W*. Related theorem: [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem). A method is using sinc function, related theorem: [Whittaker–Shannon interpolation formula](https://en.wikipedia.org/wiki/Whittaker–Shannon_interpolation_formula). Math was elaborate in this online handout: [10.4: Perfect Reconstruction](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Signals_and_Systems_(Baraniuk_et_al.)/10%3A_Sampling_and_Reconstruction/10.04%3A_Perfect_Reconstruction), check the former section for unclear equations :-).

(Related to [复变函数](https://shi200005.github.io/2022/02/15/Complex-Functions/#%E5%82%85%E9%87%8C%E5%8F%B6%E7%A7%AF%E5%88%86), since the Fourier transform of the rect is sinc.)

#### White noise

Refer to **10.2.4 White Noise** in H. Pishro-Nik, "Introduction to probability, statistics, and random processes", available at https://www.probabilitycourse.com, Kappa Research LLC, 2014.

White noise means the power spectral density is a constant, usually denoted as $$\frac{N_0}{2}$$ (Watt/Hertz) as related to bandlimited channels (only let frequency in $$[-W,W]$$ pass through, and the noise power is thus $$N=\frac{N_0}{2}(2W)=N_0W$$). And the corresponding autocorrelation function (Fourier of power spectral, see 10.1.2 Mean and Correlation Functions of the above textbook) is a Dirac delta function. That means the noise sample at different time point is not correlated.

Gaussian White noise is when the noise sample obeys a Gaussian distribution, which can be generated from a Brownian motion (by Stirling's approximation, as concluded in [(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)). 

#### Channel Capacity

How to transmit signal using the Bandlimited Gaussian channel? We can send the signal by samples uniformly distributed in time (e.g., your voice message). 

Conclusion: $$C=\frac{1}{2}\log(1+\frac{P}{N})$$ bits / channel use -> $$C=\frac{1}{2}\log(1+\frac{P/2W}{N_0/2})$$ bits / sample -> $$C=W\log(1+\frac{P}{N_0W})$$ bits / second. My confusion was solved by figuring out $$N_0$$ is the quantity to specify the noise intensity, while for transmitting signals, the signal power is constrained as Watts, and if our sampling frequency is larger, we have to put less energy per sample on the signal... 

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

Symbols: random variables and the alphabet $$X\in\mathcal X$$, probability distribution $$\text{Pr}(X=x)$$, $$p_X(x)$$, $$p(x)$$.

## Information and Entropy

### Information

mainly comes from 2.7 of Kardar (particles) (a lot of direct copy... tell me whether it is appropriate and help me to improve!)

Consider a random variable with a discrete set of outcomes $$\mathbf{x}=\{x_i\}$$ (you use a language to write a letter and the language contains 5 letters, "a, b, c, d, e"), occurring with probabilities $$\{p(i)\}$$ (in that language, all words start with "a", making "a" the most frequent letter in texts), for $$i=1,...,M$$ ($$M$$ is the size of the alphabet, in the "letter" case, $$M=5$$).

Your message contains $$N$$ letters. There are $$M^N$$ kinds of different letter combinations. Choose the unit as "bits" means $$\ln_2(M^N)$$. The number of bits (**information**) to transmit your text precisely (imaging you are sending via email so the letters are coded in a binary way) is $$N\ln_2M$$ (the bits of two texts should be added, and the possibilities of the combined text should multiply, which could be reached in this logarithm way).

However, in the limit of large $$N$$, we expect the message to contain"roughly" $$\{N_i=Np_i\}$$ occurrences for each symbol. The number of typical messages thus corresponds to the number of ways of rearranging the $$\{N_i\}$$ occurrences of $$\{x_i\}$$, and is given by the multinomial coefficient $$\displaystyle g=\frac{N!}{\prod_{i=1}^M N_i!}$$, compared with $$M^N$$ before considering the non-uniform distribution. Using **Stirling's approximation**, we have $$\ln_2g\approx -N\displaystyle\sum_{i=1}^M p_i\ln_2p_i$$.

- It is interesting that statistical physicists use $$\ln_2$$ to indicate $$\log_2$$, while engineers use $$\log x$$ to indicate $$\log_2$$.

- Here, we start from "large $$N$$ gives $$\{N_i=Np_i\}$$" and then use [Stirling's approximation](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula).  Actually,


$$
  \text{The bound by the extreme value among distribution -> }
  \begin{cases}
  \text{The weak law of large number} \\
  \text{Stirling's approximation}
  \end{cases}
$$



### Shannon Entropy 

> Entropy is the unique measure of available information consistent with certain simple and plausible requirements. --- Shannon, 1948

The above was written before I took Information Theory, where $$H(X)=-\displaystyle\sum_{x}p(x)\log p(x)$$, the measure of **uncertainty**,  was derived from **three axioms** in Shannon's 1948 paper. In Shannon's argument, derivation for uniform distribution over $$n$$ elements, the entropy $$H_U(n)=H_2(n)\log n$$ was determined by a bound, and this sandwich just looks like what we did in Stirling's...

**Change the base of logarithm**: $$\text{log}_bp=(\text{log}_ba)(\text{log}_ab)$$, $$H_{\text{in bits}}(X)=(\text{log}_2e)H_{\text{in nats}}(X)$$.

For Bernoulli random variable $$X$$ with probability $$p$$, $$H(X)=\mathscr H(p)=-p\text{log}p-(1-p)\text{log}(1-p)$$. A tip: $$\displaystyle\frac{d}{dp}\mathscr H(f(p))=f^\prime\text{log}\frac{1-f}{f}$$.

### The Entropy of Mixing

Suppose mixing $$M$$ distinct components in the context of statistical mechanics. Consider characterizing the *distribution*, let alone the outcomes from different trials (how many samples taken and the sampling error...).

The *entropy* for *any probability distribution* as $$S=-\displaystyle\sum_{i=1}^Mp(i)\ln p(i)=-\langle\ln p(i)\rangle$$. 

The above is the entropy for a discrete probability distribution, for that of a continuous distribution, $$S=-\int dxp(x)\ln p(x)=-\langle \ln p(x)\rangle$$. The problem of scaling remains to be discussed.

### Joint & Conditional entropy

$$H(X,Y)=-\sum_{x,y}p(x,y)\log_2p(x,y)$$.

$$H(X\vert Y=y)=-\sum_xp(x\vert y)\log_2p(x\vert y)$$ -> $$H(X\vert Y)=-\sum_{x,y}p(x,y)\log_2(x\vert y)$$. Corollary: $$H(X\vert X)=0$$ no uncertainty.

**Chain rule**: $$H(X,Y)=H(X)+H(Y\vert X)=H(Y)+H(X\vert Y)$$, $$H(X_1,\cdots,X_n)=H(X_1)+H(X_2\vert X_1)+\cdots+H(X_n\vert X_1,\cdots,X_{n-1})$$.

If $$X,Y$$ are **independent**, then $$H(X\vert Y)=H(X)$$ is easy to prove. Then, follow the chain rule, $$H(X,Y)=H(X)+H(Y)$$.

### Asymptotic Equipartition Property (AEP)

As a result of [the weak law of large numbers](https://shi200005.github.io/2022/02/17/Probability/#大数定理), we have for i.i.d. $$\displaystyle-\frac{1}{n}\log_2(X1,X_2,\cdots,X_n)\to H(X)$$ w.r.t. $$p(x)$$.

## Relative entropy and Mutual Information



## Convex Function

### Convex Optimization



## Gaussian Channel

### Bandlimited Channels

#### White noise

Refer to **10.2.4 White Noise** in H. Pishro-Nik, "Introduction to probability, statistics, and random processes", available at https://www.probabilitycourse.com, Kappa Research LLC, 2014.

White noise means the power spectral density is a constant, usually denoted as $$\frac{N_0}{2}$$ (Watt/Hertz) as related to bandlimited channels (only let frequency in $$[-W,W]$$ pass through, and the noise power is thus $$N=\frac{N_0}{2}(2W)=N_0W$$). And the corresponding autocorrelation function (Fourier of power spectral, see 10.1.2 Mean and Correlation Functions of the above textbook) is a Dirac delta function. That means the noise sample at different time point is not correlated.

Gaussian White noise is when the noise sample obeys a Gaussian distribution, which can be generated from a Brownian motion (by Stirling's approximation, as concluded in [(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)). 

#### Channel Capacity

How to transmit signal using the Bandlimited Gaussian channel? We can send the signal by samples uniformly distributed in time (e.g., your voice message). 

Conclusion: $$C=\frac{1}{2}\log(1+\frac{P}{N})$$ bits / channel use -> $$C=\frac{1}{2}\log(1+\frac{P/2W}{N_0/2})$$ bits / sample -> $$C=W\log(1+\frac{P}{N_0W})$$ bits / second. My confusion was solved by figuring out $$N_0$$ is the quantity to specify the noise intensity, while for transmitting signals, the signal power is constrained as Watts, and if our sampling frequency is larger, we have to put less energy per sample on the signal... 

---
layout: post
title: (En) Biophysics
categories: PhD-UT-Course-Review
description: 
keywords: Biophysics
mathjax: true
---

This post covers several topics from PHY2707 and PHY2709 of UofT grad course. I will update whenever I need to teach or review the related materials. 

## References

1. Kardar, Mehran. *Statistical physics of particles*. Cambridge University Press, 2007.
2. Bialek, William. *Biophysics: searching for principles*. Princeton University Press, 2012.
3. [David Tong: Lectures on Kinetic Theory](http://www.damtp.cam.ac.uk/user/tong/kintheory/).

## Diffusion Equation

I hadn't really used the complex form of the Fourier integral before, but now I finally got to use it in the context of "diffusion starting from a single point". 

Let's start by considering the one-dimensional case. The well-posed problem is to solve a partial differential equation (PDE) with the **initial condition of a Dirac delta function**, which is challenging to handle. By employing the complex form of the Fourier transform, the Dirac delta function is transformed into a constant, and  the PDE becomes an ordinary differential equation (ODE). Reverting the solution of the ODE back through the Fourier transform yields the solution to the original PDE. Check my note [Biophysics_Diffusion](https://shi200005.github.io/download_file/Biophysics_Diffusion.pdf).

## Linear Response

>  Our purpose here is to explore the more general case of time dependent influences. --David Tong's Lecture 4

A time-invariant linear system: input $$\mathbf x(t)$$, response function $$h(t)$$ (causality requires $$h(t)=0$$ for $$t<0$$), output $$\mathbf y(t)$$.

Denote the linear operator $$L$$ where $$\mathbf y(t)=L[\mathbf x(t)]$$. Linear means $$L[\mathbf {a_1x_1}(t)+\mathbf{a_2x_2}(t)]=\mathbf{a_1}L[\mathbf x_1(t)]+\mathbf{a_2}L[\mathbf x_2(t)]$$.

From Dirac's delta function, $$\mathbf x(t)=\displaystyle\int_{-\infty}^t \mathbf x(t^\prime)\delta(t-t^\prime)dt^\prime$$. Denote $$h(t)=L[\delta(t)]$$.

Then apply $$L$$ on both sides, $$L[\mathbf x(t)]=L[\displaystyle\int_{-\infty}^t \mathbf x(t^\prime)\delta(t-t^\prime)dt^\prime]$$. Anyway, (slapped by mathematicians), $$=\displaystyle\int_{-\infty}^t \mathbf x(t^\prime)L[\delta(t-t^\prime)]dt^\prime$$. Then we get the **convolution theorem** $$\mathbf y(t)=\displaystyle\int_{-\infty}^t \mathbf x(t^\prime)h(t-t^\prime)dt^\prime$$.

How do species in a **genetic network** influence each other's dynamics? **Application in research**: Fan, R., & Hilfinger, A. (2023). The effect of microRNA on protein variability and gene expression fidelity. *Biophysical Journal*, *122*(5), 905-923. [online](https://www.sciencedirect.com/science/article/pii/S0006349523000437?via%3Dihub)

- Detailed solution: [(En) fan2023effect](https://shi200005.github.io/2023/10/30/fan2023effect/).

### Convolution Theorem

After applying convolution theorem, we get $$\tilde y(\omega)=\tilde x(\omega)\tilde h(\omega)$$. Look, 

> We learn the response is "local" in frequency space: if you shake something at frequency $$\omega$$, it responds at frequency $$\omega$$. Anything beyond this lies within the domain of non-linear response. --David Tong's Lecture 4

The transformed output function is a complex function. The **real part** is time reversible, called the ***reactive* part**; the **imaginary part** is not time reversible, called ***dissipative* part**. The causality requires the response function be analytic for Im$$\omega>0$$ (Kramers-Kronig Relation, see also Complex Functions ([复变函数](https://shi200005.github.io/2022/03/28/Complex-Functions/))). If you know the **dissipative** part of the response function, you know everything. Relating the response function and the imaginary part in Quantum Filed theory, then comes **Fluctuation-Dissipation theory**.

**Application in research**: Martin, Pascal, A. J. Hudspeth, and F. Jülicher. "Comparison of a hair  bundle's spontaneous oscillations with its response to mechanical  stimulation reveals the underlying active process." *Proceedings of the National Academy of Sciences* 98.25 (2001): 14380-14385. (**Ref 3 is a very good note for reading this paper!**)

## Vision

### Human eye photoreceptor cells are single-photon detectors

Reference: Hecht S, Shlaer S, Pirenne MH. ENERGY, QUANTA, AND VISION. *J Gen Physiol*. 1942;25(6):819-840. doi:10.1085/jgp.25.6.819

Question: What is the lower limit of the number of photons that enables human vision? Method: Use a very dim light source to shake it and see if the person being tested says it can be seen. Fact: There is no way to control the number of photons emitted each time (it is a random variable). Because 1. The light source is dim enough, and the emitted photons come from sparse sampling of a certain process (for related theories, see [Probability Theory](https://shi200005.github.io/2021/10/02/Probability/)), 2. In [Quantum Mechanics](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/), this process is actually a Poisson process. It can be considered that the random variable "number of photons emitted" conforms to the **Poisson distribution**.

If $$k$$ is the lower limit of the number of photons that can be seen, and the flash intensity is $$I$$, because each subject’s own eye parameters are different, the ratio of photons reaching the retina is $$\alpha$$, then in the test , the probability that the subject sees the light can be expressed by

$$P_{see}(I)=\Sigma_{n=k}^{\infty}P(n\vert M=\alpha I)=e^{-\alpha I}\Sigma_{n=k}^{\infty}\frac{(\alpha I)^n}{n!}$$

where $$\alpha$$ is unknown, but $$k$$ gives the shape of $$P_{see}(I)$$, $$\alpha$$ is just stretched on the $$M$$ axis, $$\alpha$$ requires curve fitting measured by a single person (varies from person to person). The figure below shows the test results published by Hecht, Shlaer, and Pirenne in 1942. It can be seen that the fit is quite good (William Bialek, Biophysics, 2.1).

![](/images/blog/Biophysics_Vision.jpg)

Note: The success of the experiment is that we first fit the $$\alpha$$ parameters of different testers, and then find the corresponding photon number threshold $$k$$ for each person. For the ensemble of the crowd, find Average of $$k$$. But if we first average the curves of three people, then fit an overall $$\alpha$$, and then get the overall $$k$$ value, I am afraid there will be no good results. In fact, this shows us finding what is reproducible can be difficult, and averaging across an ensemble of individuals can be qualitatively misleading.（William Bialek, Biophysics, 2.1）

---

The following will be rewrite...

## Information and Entropy

### Distribution of Maximum Entropy

As I have said in Probability ([概率论](https://shi200005.github.io/2021/10/02/Probability/)), we use probability to describe something because we lack information of the whole thing. Entropy quantifies the uncertainty of a distribution. When we don't know something, we cannot "bias" to pretend we know. Thus, given some information of a distribution, we plug in the information (usually use **Lagrange multipliers**, see Calculus([微积分](https://shi200005.github.io/2021/09/30/Calculus/)) and **maximize the entropy** of the distribution for estimation. 

If the mean is specified, the distribution of maximum entropy is **Boltzmann distribution**; if the mean and the standard deviation is specified, the distribution of maximum entropy is **Gaussian distribution**.

The following mainly comes from Bialek.

### Encoding Strategy

I read it but am too lazy to write

- How to encode information about a probability distribution using binary numbers (how many binary digits are used)?

- Kullback-Leibler divergence $$D_{KL}(\bold{p\vert\vert\bold{q})=\displaystyle\sum_n}p_slog_2(\frac{p_s}{q_s})$$    

  Describes the deviation between the probability distribution we guessed and the actual probability distribution. If we guess the probability distribution wrong, we need more space to encode a piece of data. This physical quantity quantifies how much more space we need to spend. 

- Correlations or order reduce the capacity to transmit information. 

The relationship with [Thermodynamics](https://shi200005.github.io/2021/10/11/Thermodynamics/): $$dS=\frac{\bar dQ}{T}$$, which describes the heat absorption caused by entropy change. Similarly, The entropy of a probability distribution also measures the amount of space needed to write down a description of the (microscopic) states drawn out of that distribution.

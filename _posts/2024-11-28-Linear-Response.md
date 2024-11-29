---
layout: post
title: (En) Linear Response
categories: Self-Study
description: 
keywords: classical mechanics, partial differential equations, Green's functions, linear response, electrodynamics
mathjax: true
---

> Our purpose here is to explore the more general case of time dependent influences. As we'll see, by studying the response of the system at different frequencies... --David Tong's Lecture 4

## The Damped Harmonic Oscillator

$$\ddot x+2\gamma\dot x+\omega_0^2x=f(t)$$. The $$f(t)$$ is the driving force, the **input**. We can observe $$x$$, the **output**. The left-hand side is a linear operator of $$x$$. This is an inhomogeneous linear system. We would like to know how the output $$x$$ responds to the input $$f(t)$$. Since $$\gamma$$ and $$\omega_0$$ are constants invariant in time, the system is invariant under time variance, so it is a **time-invariant system**.

First suppose $$f(t)$$ is a harmonic oscillation term $$C_0e^{i\omega t}$$. The question boils down to solving the particular solution of LHS=$$C_0e^{i\omega t}$$ and the general solution of LHS=$$0$$. The former is solved by guessing $$x(t)=Ae^{i\omega t}$$, or solving the characteristic function. The latter is the damped harmonic motion. Then we have 

$$\displaystyle x(t)=e^{-\gamma t}(Ae^{t\sqrt{\gamma^2-\omega_0^2}}+Be^{-t\sqrt{\gamma^2-\omega_0^2}})+(\frac{1}{-\omega^2+2i\gamma\omega+\omega_0^2})C_0e^{i\omega t}$$

The general solution will damped out and the particular solution will "go on". The latter describes the **amplitude** and **phase** of the output with regard to the frequency of the input. For the frequency that gives the largest amplitude, it is called **resonance**. We are usually concerned with weak damping, which means $$\gamma\ll\omega$$.

Using Fourier transform, every $$f(t)$$ can be written as a linear combination of $$C_0e^{i\omega t}$$. Since the dynamic equation is linear, the solution is the linear combination of solutions of each $$C_0e^{i\omega t}$$.

### Linear Response

A time-invariant linear system: input $$\mathbf x(t)$$, response function $$h(t)$$ (causality requires $$h(t)=0$$ for $$t<0$$), output $$\mathbf y(t)$$. Denote the linear operator $$L$$ where $$\mathbf y(t)=L[\mathbf x(t)]$$.  From Dirac's delta function, $$\displaystyle\mathbf x(t)=\int_{-\infty}^t \mathbf x(t^\prime)\delta(t-t^\prime)dt^\prime$$. Then apply $$L$$ on both sides, $$\displaystyle L[\mathbf x(t)]=L[\int_{-\infty}^t \mathbf x(t^\prime)\delta(t-t^\prime)dt^\prime]$$. Note that $$L$$ operates on $$t$$, and the system is time-invariant, so  $$\displaystyle L[\mathbf x(t)]=\int_{-\infty}^t \mathbf x(t^\prime)L[\delta(t-t^\prime)]dt^\prime$$. Denote $$h(t)=L[\delta(t)]$$, then we get the **convolution theorem** $$\displaystyle\mathbf y(t)=\int_{-\infty}^t \mathbf x(t^\prime)h(t-t^\prime)dt^\prime$$.

With this transform, the problem $$\ddot x+2\gamma\dot x+\omega_0^2x=f(t)$$ is converted to $$\displaystyle\frac{\partial^2\chi(t)}{\partial t^2}+2\gamma\frac{\partial\chi(t)}{\partial t}+\omega_0^2\chi(t)=\delta(t)$$, then $$\displaystyle x(t)=\int_{-\infty}^t \chi(t-t^\prime)f(t')dt^\prime$$.

Now solve $$\displaystyle\frac{\partial^2\chi(t)}{\partial t^2}+2\gamma\frac{\partial\chi(t)}{\partial t}+\omega_0^2\chi(t)=\delta(t)$$ with natural boundary conditions.

1. From causality, $$\chi(t)=0$$ when $$t<0$$.
2. If $$F(t)=\delta(t)$$, then $$x(t)=\chi(t)$$. Since $$x(t)$$ is continuous, then $$\chi(t)$$ is continuous. Therefore, $$\displaystyle\lim_{t\to 0}\chi(0)=0$$.
3. Finding $$\displaystyle\frac{\partial\chi(t)}{\partial t}$$ when $$t\to 0$$. For $$\epsilon>0$$ and take $$\epsilon\to 0$$, integrate the second-order PDE with $$t$$ from $$-\epsilon$$ to $$\epsilon$$ and we get $$\displaystyle [\frac{\partial\chi(t)}{\partial t}\vert_{t=\epsilon}-0] + \gamma[0-0] + \omega_0^2[0-0] =1$$, which is just $$\displaystyle \frac{\partial\chi(t)}{\partial t}\vert_{t=\epsilon}=1$$.

Having exercised to solve the PDE for $$t>0$$ in our first year (look above), the solution is $$\displaystyle \chi(t)=e^{-\gamma t}(Ae^{i\omega't}+Be^{-i\omega't})$$, where $$\omega'=\sqrt{\omega_0^2-\gamma^2}$$. Plugging in $$\chi(\epsilon)=0$$ and $$\displaystyle\frac{\partial\chi(t)}{\partial t}\vert_{t=\epsilon}=1$$, we can solve $$A$$ and $$B$$. The final answer is $$\displaystyle\chi(t)=e^{-\gamma t/2}\frac{\sin(\omega't)}{\omega'}$$. Then $$\displaystyle x(t)=\int_{-\infty}^t e^{-\gamma (t-t')}\frac{\sin(\omega'(t-t'))}{\omega'}f(t')dt^\prime$$.

Cross check: take $$\displaystyle x(t)=\int_{-\infty}^t e^{-\gamma (t-t')}\frac{\sin(\omega'(t-t'))}{\omega'}F(t')dt^\prime$$, using [Leibniz integral rule](https://en.wikipedia.org/wiki/Leibniz_integral_rule), we'll get back $$\ddot x+2\gamma\dot x+\omega_0^2x=f(t)$$ for sure.

### Fourier Transform

Note that $$\displaystyle x(t)=\int_{-\infty}^t \chi(t-t^\prime)f(t')dt^\prime$$. If $$\mathcal F[\chi(t)]=\tilde\chi(\omega)$$, $$\mathcal F[f(t)]=\tilde f(\omega)$$, $$\mathcal F[x(t)]=\tilde x(\omega)$$, then from **convolution theorem**, we have $$\tilde x(\omega)=\tilde\chi(\omega)\tilde f(\omega)$$. To calculate $$\tilde\chi(\omega)$$, we have $$\displaystyle\tilde\chi(\omega)=\int_{-\infty}^{\infty}\chi(t)e^{i\omega t}dt=\frac{1}{-\omega^2+2i\gamma\omega+\omega_0^2}$$, which is just the term when we solved LHS=$$C_0e^{i\omega t}$$ in our first year. Of course, it is a function telling us the amplitude and phase that the output in respond to the input, with regard of frequencies $$\omega$$.

### The Reactive Part and Dissipative Part

The Fourier transform of the response function is a complex function. The **real part** is time reversible (an even function), called the ***reactive* part** (see Figure 11 of [ref 2](http://www.damtp.cam.ac.uk/user/tong/kintheory/four.pdf)); the **imaginary part** is not time reversible (an odd function), called ***dissipative* part** (see Figure 12 of [ref 2](http://www.damtp.cam.ac.uk/user/tong/kintheory/four.pdf)). The causality requires the response function be analytic for $$\text{Im}\omega>0$$ (Kramers-Kronig Relation, see also Complex Functions ([复变函数](https://shi200005.github.io/2022/03/28/Complex-Functions/))). If you know the **dissipative** part of the response function, you know everything. Relating the response function and the imaginary part in Quantum Filed theory, then comes **Fluctuation-Dissipation theory**.

In the damped harmonic oscillator, consider $$f(t)=C_0\cos(\Omega t)$$.  We can show that the **work done** (power $$\displaystyle\frac{dW}{dt}=f(t)\dot x(t)$$) in a period ($$\displaystyle\frac{\overline{d W}}{dt}=\frac{\Omega}{2\pi}\int_{0}^{2\pi/\Omega}\frac{dW}{dt}dt$$)  is proportional to the **imaginary part**, that is, the **dissipative part**. Following [ref 2](http://www.damtp.cam.ac.uk/user/tong/kintheory/four.pdf)'s 4.2.2, we get $$\displaystyle\frac{\overline{d W}}{dt}=2C_0\Omega\text{Im}\tilde\chi(\Omega)$$. Given $$\Omega$$ and $$\gamma$$, the imaginary part peak at $$\omega_0=\Omega$$.

## Examples in Physics and Biophysics

### Lorenz Model of Dielectric Dispersion

Dielectric dispersion theory, based on the Lorenz model, provides  insights into how the dielectric constant varies with frequency due to  polarization dynamics. In this model, the electrons are bounded around the nuclear, and oscillated by the electric drive. (See [电动力学 - 绝缘体- Lorenz 模型](https://shi200005.github.io/2022/04/10/Electrodynamics/#%E7%BB%9D%E7%BC%98%E4%BD%93---lorenz-%E6%A8%A1%E5%9E%8B) or ref 3.) 

> Most of the time the index of refraction rises gradually with increasing frequency, consistent with our experience from optics (Fig. 9.19). However, in the immediate neighborhood of a resonance, the index of refraction drops sharply. Because this behavior is atypical, it is called anomalous dispersion. -- Griffiths, David. *Introduction to Electrodynamics*. Chapter 9.4.3.

### Calculating the covariances of Stochastic Genetic Networks

How do species in a **genetic network** influence each other's dynamics, for example, the covariances relationship between upstream and downstream components? **Application in research**: See ref 4 [online](https://www.sciencedirect.com/science/article/pii/S0006349523000437?via%3Dihub), derivation of equations 33 and 58. [Summary](https://shi200005.github.io/2023/10/30/fan2023effect/) and [detailed derivation](https://shi200005.github.io/download_file/Fan2023Effect_Supp.pdf).

### Active vs. Passive Biological Systems

**Application in research**: See ref 5.

> By comparing a hair bundle’s spontaneous oscillations with its response to small mechanical stimuli, we demonstrate a breakdown in a general principle of equilibrium thermodynamics, the fluctuation–dissipation theorem. We thus confirm that a hair bundle’s spontaneous movements are produced by energy-consuming elements within the hair cell.

## References

1. Morin, David. *Introduction to Classical Mechanics*. Cambridge University Press, 2008. Chapter 3.
2. [David Tong: Lectures on Kinetic Theory](http://www.damtp.cam.ac.uk/user/tong/kintheory/). Lecture 4.
3. Griffiths, David. *Introduction to Electrodynamics*. Cambridge University Press, 2024. Chapter 9.4.3.
4. Fan, R., & Hilfinger, A. (2023). The effect of microRNA on protein variability and gene expression fidelity. *Biophysical Journal*, *122*(5), 905-923. [online](https://www.sciencedirect.com/science/article/pii/S0006349523000437?via%3Dihub)
5. Martin, Pascal, A. J. Hudspeth, and F. Jülicher. "Comparison of a hair  bundle's spontaneous oscillations with its response to mechanical  stimulation reveals the underlying active process." *Proceedings of the National Academy of Sciences* 98.25 (2001): 14380-14385.

---
layout: post
title: (En) Stochastic Processes
categories: PhD-UT-Course-Review
description: 
keywords: stochastic processes, non-equilibrium statistical physics
mathjax: true
---

Prof Anton Zilman@UofT offered us great course on stochastic processes, starting with one-dimensional random walk, giving us good intuition on this topic. To make it work best for me, I will mainly refer to reference 1 below.

## References

1. Van Kampen, N. G. (1992). *Stochastic processes in physics and chemistry* (Vol. 1). Elsevier.
1. Haag, G. (2017). Modelling with the Master equation. *Solution Methods*.
1. My random post [(En) Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem](https://shi200005.github.io/2023/06/07/Network-Jump/#solution-of-linear-fokker-planck-equation).

## The Master Equation

For definitions set up in [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces), see [Definitions](https://shi200005.github.io/download_file/Stochastic_Processes_Definitions.pdf).

For derivation of the Master Equation, see [2](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces), as outlined below.

Given **Markov assumption**, we derive $$p(\vec n_2,t_2)=\displaystyle\sum_{\vec n_1}p(\vec n_2,t_2\vert \vec n_1,t_1)p(\vec n_1,t_1)$$ (Eqn.1) and **Chapman-Kolmogorov Equation** $$p(\vec n_3,t_3\vert \vec n_1,t_1)=\displaystyle\sum_{\vec n_2}p(\vec n_3,t_3\vert \vec n_2,t_2)p(\vec n_2,t_2\vert \vec n_1,t_1)$$.

Expand the Taylor series around $$t$$ with respect to $$t_2=t+\tau$$ yielding $$p(\vec n_2,t+\tau\vert \vec n_1,t)=p(\vec n_2,t\vert \vec n_1,t)p(\vec n_1,t_1)+\tau\frac{\partial p(\vec n_2,t_2\vert \vec n_1,t)}{\partial t_2}\vert_{t_2=t}+\mathscr O(\tau^2)$$.

... take the limit $$\tau\rightarrow 0$$ then the **Master Equation** is obtained $$\frac{dP(\vec n,t)}{dt}=\displaystyle\sum_{\vec m}w_t(\vec n,\vec m)P(\vec m,t)-w_t(\vec m,\vec n)P(\vec n,t)$$.

I also came across a nice link on **Chapman-Kolmogorov Equation** -> **Master Equation**: [Master Equation](https://statisticalphysics.leima.is/nonequilibrium/master-eqn.html).

Notes on "Markov" from Section IV.1 of [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

> In principle any closed isolated physical system can be described as a Markov process by introducing all microscopic variables as components of $$Y$$. In fact, the microscopic motion in phase space is deterministic and therefore Markovian, compare $$P_{1\vert 1}(x,t\vert x_0, t_0)=\delta[x-\phi(x_0,t-t_0)]$$. The physicist's question, however, is whether he can find a small set of variables whose behavior in time can be described as a multicomponent Markov process. The well-known, but still miraculous, experimental fact is that this is so far most many-body systems in nature. Of course, such a description is at best approximate and restricted to a macroscopic, coarse-grained level. This reduction to a much smaller number of variables is called "contraction" or "projection", but the justification of this approximation involves the fundamental problems of statistical mechanics and is still the subject of many discussions. 

### The Fokker-Planck Equation

The derivation (approximation) from the Master Equation to the Fokker-Planck Equation is in Section VIII.2 of [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

Express the transition probability $$W$$ as a function of the size $$r$$ of the jump and of the starting point: $$W(y\vert y')=W(y';r),r=y-y'$$.

Assumptions

- only small jumps occur, i.e., $$W(y';r)$$ is a sharply peaked function of $$r$$ but varies slowly with $$y'$$.
- the solution $$P(y,t)$$ also varies slowly with $$y$$.

Then expand the master equation according to the state-shift up to second order, we get the **Fokker-Planck Equation** $$\frac{\partial P(y,t)}{\partial t}=-\frac{\partial}{\partial y}\{a_1(y)P\}+\frac{1}{2}\frac{\partial^2}{\partial y^2}\{a_2(y)P\}$$, where $$a_\nu(y)=\displaystyle\int_{-\infty}^{\infty}r^\nu W(y;r)dr$$.

In the special case where $$a_1(y)=A_0+A_1y$$ and $$a_2(y)=B_0$$, the Fokker-Planck equation is linear. If $$A_1<0$$, the stationary solution is **Gaussian**. The stationary Markov process determined by the linear Fokker-Planck equation is the **Ornstein-Uhlenbeck** process. (to solve the Gaussian solution, use Fourier transform, also mentioned in [3](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces)).
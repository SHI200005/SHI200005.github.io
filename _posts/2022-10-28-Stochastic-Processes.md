---
layout: post
title: (En) Stochastic Processes
categories: PhD-UT-Course-Review
description: 
keywords: stochastic processes, non-equilibrium statistical physics
mathjax: true
---

Prof Anton Zilman@UofT offered us a great course on stochastic processes, starting with a one-dimensional random walk, which gave us good intuition on this topic. To make it work best for me, I will mainly refer to reference 1 below.

## References

1. Van Kampen, N. G. (1992). *Stochastic processes in physics and chemistry* (Vol. 1). Elsevier.
1. My random post [(En) Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem](https://shi200005.github.io/2023/06/07/Network-Jump/#solution-of-linear-fokker-planck-equation).

## The Master Equation

A system of linear first-order ODEs described probability evolution over time without memory of the history.

A nice note on integrating **Markov property** -> **Chapman-Kolmogorov Equation** -> **Master Equation**: [Master Equation](https://statisticalphysics.leima.is/nonequilibrium/master-eqn.html).

Notes on "Markov" from Section IV.1 of [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

> In principle any closed isolated physical system can be described as a Markov process by introducing all microscopic variables as components of $$Y$$. In fact, the microscopic motion in phase space is deterministic and therefore Markovian, compare $$P_{1\vert 1}(x,t\vert x_0, t_0)=\delta[x-\phi(x_0,t-t_0)]$$. The physicist's question, however, is whether he can find a small set of variables whose behavior in time can be described as a multicomponent Markov process. The well-known, but still miraculous, experimental fact is that this is so far most many-body systems in nature. Of course, such a description is at best approximate and restricted to a macroscopic, coarse-grained level. This reduction to a much smaller number of variables is called "contraction" or "projection", but the justification of this approximation involves the fundamental problems of statistical mechanics and is still the subject of many discussions. 

### The Fokker-Planck Equation

The derivation (approximation) from the Master Equation to the Fokker-Planck Equation is in Section VIII.2 of [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

Express the transition probability $$W$$ as a function of the size $$r$$ of the jump and starting point: $$W(y\vert y')=W(y';r),r=y-y'$$.

Assumptions

- only small jumps occur, i.e., $$W(y';r)$$ is a sharply peaked function of $$r$$ but varies slowly with $$y'$$.
- the solution $$P(y,t)$$ also varies slowly with $$y$$.

Then expand the master equation according to the state-shift up to second order, we get the **Fokker-Planck Equation** $$\displaystyle\frac{\partial P(y,t)}{\partial t}=-\frac{\partial}{\partial y}\{a_1(y)P\}+\frac{1}{2}\frac{\partial^2}{\partial y^2}\{a_2(y)P\}$$, where $$\displaystyle a_\nu(y)=\int_{-\infty}^{\infty}r^\nu W(y;r)dr$$.

In the special case where $$a_1(y)=A_0+A_1y$$ and $$a_2(y)=B_0$$, the Fokker-Planck equation is linear. If $$A_1<0$$​, the stationary solution is **Gaussian**. The stationary Markov process determined by the linear Fokker-Planck equation is the **Ornstein-Uhlenbeck** process. (to solve the Gaussian solution, use Fourier transform, also mentioned in [2](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces)).

#### e.g., Equilibrium of non-interacting particles

Suppose $$a_2(y)$$ is constant and $$\displaystyle\frac{1}{2}a_2(y)=D$$. Denote $$a_1(y)=v(y)$$ as we will see it is the *velocity*.

Define flux $$\displaystyle J(y,t)=-a_1(y)P+\frac{1}{2}\frac{\partial}{\partial y}\{a_2(y)P\}$$ so that $$\displaystyle\frac{\partial P(y,t)}{\partial t}=\frac{\partial J(y,t)}{\partial y}$$.

At equilibrium, $$J(y,t)=0$$ -> $$\displaystyle P^{\text{eq}}(y)=C\exp{\int^y\frac{v(y')dy'}{D}}$$. 

For Stokes flow where $$f=6\pi\eta Rv$$ (small round particles in honey), we get Einstein relation and Fluctuation-dissipation theorem.

### e.g., From the Simplest Random Walk

#### Simplest

$$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with all transition prob as $$1/2$$.

$$P(n,N\vert n_0=0,0)$$ obeys a symmetric binomial distribution. For large $$N$$, use Stirling's approximation, it becomes Gaussian distribution. Then, in the continuous limit, we associate the diffusion coefficient.

#### Asymmetric prob

 $$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with rightward transition prob as $$p$$ and leftward prob as $$q=1-p$$​.

$$P(n,N\vert n_0=0,0)$$ obeys a binomial distribution. 

#### Arbitrary

$$p$$​ varies at each grid. In the continuous limit, we obtain the Fokker-Planck Equation.

### e.g., Finite State Markov Chain

 States: $$i=1,2,...,n$$. Transition rate: $$r_{ij}:=r_{j\to i}$$.
$$
\begin{bmatrix}
	\dot P_1(t) \\ \dot P_2(t) \\ \vdots \\ \dot P_n(t)
\end{bmatrix}

=

\begin{bmatrix}
	-\displaystyle\sum_{j\neq 1} r_{j1} & r_{12} &\ldots  \\
    r_{21} & -\displaystyle\sum_{k\neq 2} r_{k2} &\ldots \\
    \ldots 
\end{bmatrix}

\begin{bmatrix}
	P_1(t) \\ P_2(t) \\ \vdots \\ P_n(t)
\end{bmatrix}
$$
Denote as $$\displaystyle\frac{\partial}{\partial t}\vec P(t)=\hat M\cdot\vec P(t)$$, check [Matrix exponential](https://shi200005.github.io/2021/09/30/Linear-Algebra/#matrix-exponential) in Linear Algebra. Steady-state exits: $$\hat M$$ has zero eigenvalues and negative real parts.
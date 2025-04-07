---
layout: post
title: (En) Stochastic Processes
categories: PhD-UT-Course-Review
description: 
keywords: 
mathjax: true
---

Prof Anton Zilman at UofT offered us a great course on stochastic processes. The course started with a one-dimensional random walk, which gave us good intuition on this topic. To make it work best for me, I will mainly refer to reference 1 below.

## References

1. Johan Paulsson, Lecture Notes, 10/15/2014, Systems Biology 200.
1. Van Kampen, N. G. (1992). *Stochastic processes in physics and chemistry* (Vol. 1). Elsevier.
1. My random post [(En) Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem](https://shi200005.github.io/2023/06/07/Network-Jump/#solution-of-linear-fokker-planck-equation).

## Introduction

### 1-D Random walk

$$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with all transition prob as $$p(n)$$ on each grid, calculate $$P(n,N\vert n_0=0,0)$$.

- Simplest random walk

  $$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with all transition prob as $$p(n)=1/2$$.

  $$P(n,N\vert n_0=0,0)$$ obeys a **symmetric binomial distribution**. 

  For large $$N$$, use **Stirling's approximation**, it becomes **Gaussian distribution** ([De Moivre-Laplace theorem](https://shi200005.github.io/2022/02/17/Probability/#de-moivre-laplace-%E5%AE%9A%E7%90%86) in Probability). 

  Then, in the **continuum limit**, we associate the diffusion coefficient $$\displaystyle D=\frac{a^2}{2\tau}$$, where $$a$$ is the distance between steps and $$\tau$$ is the time interval to take a step. $$\displaystyle P(r,t)=\frac{1}{\sqrt{4\pi Dt}}\exp\left(-\frac{r^2}{4Dt}\right)$$.

- Asymmetric random walk

   $$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with rightward transition prob as $$p(n)=p$$ and leftward prob as $$q(n)=1-p=q$$​.

  $$P(n,N\vert n_0=0,0)$$ obeys a **binomial distribution**. 

- General random walk 

  $$...-2\leftrightharpoons-1\leftrightharpoons0\leftrightharpoons1\leftrightharpoons2...$$ with rightward transition prob as $$p(n)$$ and leftward prob as $$q(n)=1-p(n)$$.

### Exponential lifetime

If we indicate the probability at state $$A$$ as $$P(A,t)$$, then we have $$P(A,t+dt)=P(A,t)-P_\text{jump}(t,t+dt)$$, while $$P_\text{jump}(t,t+dt)=P_\text{jump}(t,t+dt\vert A,t)P(A,t)$$, then $$\displaystyle\frac{dP(A,t)}{dt}=-\lim\limits_{dt→0}\frac{P_\text{jump}(t,t+dt\vert A,t)}{dt}P(A,t)$$. [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces)

Suppose the probability of jumping out per unit time $$\displaystyle\lim\limits_{dt→0}\frac{P_\text{jump}(t,t+dt\vert A,t)}{dt}=r$$ is a constant. Then the probability of **not** jumping out of $$A$$ by time $$t_A$$ is $$\displaystyle S(t_A)=\lim\limits_{dt→0}\prod_{dt}^{t_A/dt}(1-rdt)=e^{-rt_A}$$. Then the pdf of lifetime distribution in state $$A$$ is $$\displaystyle \lambda(t_A)=-\frac{\partial}{\partial t_A}S=re^{-rt_A}$$ , which obeys an [exponential distribution](https://shi200005.github.io/2022/02/17/Probability/#指数分布), with the mean $$\tau=1/r$$. 

### Equilibrium 

Zero flux between any two states $$J_{ij}=0$$. Transition rate: $$r_{ij}:=r_{j\to i}$$, then $$P_i^{\text{eq}}r_{ij}=P_j^{\text{eq}}r_{ji}$$ (if satisfied by all pairs -> **detailed balance**). 

## The Master Equation

$$\displaystyle\frac{\partial P(y,t)}{\partial t}=\int\{W(y\vert y^\prime) P(y^\prime,t)-W(y^\prime \vert y) P(y,t)\}$$, where $$W(y\vert y')$$ is the *transition probability per unit time*.

A system of ODEs described probability evolution over time **without memory of the history**, first-order w.r.g. time. 

A nice note on integrating **Markov property** -> **Chapman-Kolmogorov Equation** -> **Master Equation**: [Master Equation](https://statisticalphysics.leima.is/nonequilibrium/master-eqn.html).

Notes on "Markov" from Section IV.1 of [2](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

> In principle any closed isolated physical system can be described as a Markov process by introducing all microscopic variables as components of $$Y$$. In fact, the microscopic motion in phase space is deterministic and therefore Markovian, compare $$P_{1\vert 1}(x,t\vert x_0, t_0)=\delta[x-\phi(x_0,t-t_0)]$$. The physicist's question, however, is whether he can find a small set of variables whose behavior in time can be described as a multicomponent Markov process. The well-known, but still miraculous, experimental fact is that this is so far most many-body systems in nature. Of course, such a description is at best approximate and restricted to a macroscopic, coarse-grained level. This reduction to a much smaller number of variables is called "contraction" or "projection", but the justification of this approximation involves the fundamental problems of statistical mechanics and is still the subject of many discussions. 

#### e.g., Fixed jump time -> the master equation

Suppose the transition probability is $$T(y\vert y')$$ ($$y'$$ to $$y$$) and the current state is $$P(y,t)$$. Also for next state $$y$$ goes to $$y'$$ so $$\displaystyle \int T(y'\vert y)P(y,t)=P(y,t)$$.

Evolution: if the jumping time interval is $$\tau$$, then $$\displaystyle P(y,t+\tau)=\int T(y\vert y')P(y',t)$$. Now expand $$P$$ to **first-order in time**, $$\displaystyle P(y,t+\tau)=P(y,t)+\tau\frac{\partial}{\partial t}P(y,t)$$. Then $$\displaystyle \tau\frac{\partial}{\partial t}P(y,t)=\int \{T(y\vert y')P(y',t)-T(y'\vert y)P(y,t)\}$$. Transition probability per unit time: $$W(y\vert y')=T(y\vert y')/\tau$$, then we have the master equation above.

#### e.g., Exponential lifetime -> the master equation

Probability time of umping to state $$i$$ from $$A$$: $$p_i$$, per unit time: $$r_i=p_ir$$. $$\displaystyle \tau\frac{\partial}{\partial t}P(A)=\int p_iP(i)-P(A)$$. Plug in $$\tau=1/r$$, we have $$\displaystyle\frac{\partial}{\partial t}P(A)=\int r_iP(i)-rP(A)$$.

#### e.g., Finite State Markov Chain

 States: $$i=1,2,...,n$$. 
$$
\begin{bmatrix}
	\dot P_1(t) \\ \dot P_2(t) \\ \vdots \\ \dot P_n(t)
\end{bmatrix}

=

\begin{bmatrix}
	-\displaystyle\sum_{j\neq 1} r_{j1} & r_{12} &\ldots  \\
    r_{21} & -\displaystyle\sum_{k\neq 2} r_{k2} &\ldots \\
    \ldots &\ldots &\ldots
\end{bmatrix}

\begin{bmatrix}
	P_1(t) \\ P_2(t) \\ \vdots \\ P_n(t)
\end{bmatrix}
$$
Denote as $$\displaystyle\frac{\partial}{\partial t}\vec P(t)=\hat M\cdot\vec P(t)$$, check [Matrix exponential](https://shi200005.github.io/2021/09/30/Linear-Algebra/#matrix-exponential) in Linear Algebra. $$\hat M$$'s column elements sums to zero -> $$\hat M$$ is degenerate -> $$\det(\hat M)=0$$ -> at least one zero eigenvalue, at least one steady state. Stable steady-state: the eigenvalues have negative real parts.

Detailed-balance condition: **Kolmogorov condition** (in a loop...e.g., $$\displaystyle\frac{r_{12}r_{23}r_{31}}{r_{21}r_{32}r_{13}}=1$$).

Fokker-Planck equation only can be used in systems can be described by d-dimension (???).

### The Fokker-Planck Equation

The derivation (approximation) from the Master Equation to the Fokker-Planck Equation is in Section VIII.2 of [1](https://shi200005.github.io/2025/03/15/Stochastic-Processes/#references).

Express the transition probability $$W$$ as a function of the size $$r$$ of the jump and starting point: $$W(y\vert y')=W(y';r),r=y-y'$$.

Assumptions

- only small jumps occur, i.e., $$W(y';r)$$ is a sharply peaked function of $$r$$ but varies slowly with $$y'$$.
- the solution $$P(y,t)$$ also varies slowly with $$y$$.

Then expand the master equation according to the state shift up to the **second order**, we get the **Fokker-Planck Equation** $$\displaystyle\frac{\partial}{\partial t}P(y,t)=-\frac{\partial}{\partial y}\{a_1(y)P\}+\frac{1}{2}\frac{\partial^2}{\partial y^2}\{a_2(y)P\}$$, where $$\displaystyle a_\nu(y)=\int_{-\infty}^{\infty}r^\nu W(y;r)dr$$.

In the special case where $$a_1(y)=A_0+A_1y$$ and $$a_2(y)=B_0$$, the Fokker-Planck equation is linear. If $$A_1<0$$​, the stationary solution is **Gaussian**. The stationary Markov process determined by the linear Fokker-Planck equation is the **Ornstein-Uhlenbeck** process. (to solve the Gaussian solution, use Fourier transform, also mentioned in [2](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces)).

#### e.g., General 1-D random walk

Fixed jump time $$\tau$$ and interval $$a$$ as above. Expand to the second-order $$\displaystyle P(y\pm a)=P(y)\pm a\frac{\partial}{\partial y}P(y)+\frac{1}{2}a^2\frac{\partial^2}{\partial y^2}P(y)$$, same for $$p(y\pm a)$$ and $$q(y\pm a)$$. Then we have $$\displaystyle\frac{\partial}{\partial t}P(y,t)=-\frac{\partial}{\partial y}\{v(y)P\}+D\frac{\partial^2}{\partial y^2}P$$, where $$\displaystyle v(y)=\frac{a}{\tau}[p(y)-q(y)]=\epsilon\frac{a}{\tau}$$ is the *velocity*, $$\displaystyle D=\frac{a^2}{2\tau}$$ is the *diffusion coefficient*. In continuum limit, $$a,\tau\to0$$ and $$D=\text{const}$$, to keep $$v$$ finite, we should have $$\epsilon\to0$$ (small bias).

From **Continuity Equation** $$\displaystyle\frac{\partial}{\partial t} P(y,t)=\frac{\partial}{\partial y} J(y,t)$$, we get **Smoluchowski equation** $$\displaystyle J(y,t)=v(y)P(y,t)-D\frac{\partial}{\partial y}P(y,t)$$, which are "FLUX" and "[FICK'S LAW](https://shi200005.github.io/2022/02/24/Thermodynamics/#输运现象)".

##### Equilibrium of non-interacting particles

$$J(y,t)=0$$ -> $$\displaystyle P^{\text{eq}}(y)=C\exp{\int^y\frac{v(y')}{D}dy'}$$. 

[Boltzmann distribution](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/#近独立子系组成的系统): $$\displaystyle P^{\text{eq}}(y)=C\exp{\int^y\frac{u(y')}{k_BT}dy'}$$. Force $$\displaystyle F(y)=\frac{\partial}{\partial y}u(y)$$. For [overdamped](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#振动和波) system, we have $$v=\mu f$$, where $$\mu$$ is *mobility*, and we derive **Einstein relation** (a special case of Fluctuation-dissipation theorem) $$\displaystyle\mu=\frac{D}{k_BT}$$ for Brown particles. 

- Consider [Stokes' drag law]((https://shi200005.github.io/2022/02/24/Thermodynamics/#输运现象)), $$f=6\pi\eta Rv$$ (small round particles in honey), we get $$\displaystyle\mu=\frac{1}{6\pi\eta R}$$.


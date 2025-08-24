---
layout: post
title: (En) Stochastic Processes 1.0
categories: PhD-UT-Course-Review
description: 
keywords: 
mathjax: true
---

Prof Anton Zilman at UofT offered us a great course on stochastic processes. The course started with a one-dimensional random walk, which gave us good intuition on this topic. To make it work best for me, I will mainly refer to reference 1 below.

## References

1. Johan Paulsson, Lecture Notes, 10/15/2014, Systems Biology 200.
1. Van Kampen, N. G. (1992). *Stochastic processes in physics and chemistry* (Vol. 1). Elsevier.
1. Here, we focus on the one-variable case. For the multi-variable case, see my random post [(En) Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem](https://shi200005.github.io/2023/06/07/Network-Jump/#solution-of-linear-fokker-planck-equation).

## 1-D Random walk

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

## The Master Equation

$$\displaystyle\frac{\partial P(y,t)}{\partial t}=\int\{W(y\vert y^\prime) P(y^\prime,t)-W(y^\prime \vert y) P(y,t)\}$$, where $$W(y\vert y')$$ is the *transition probability per unit time*.

A system of ODEs described probability evolution over time **without memory of the history**, first-order w.r.g. time. 

A nice note on integrating **Markov property** -> **Chapman-Kolmogorov Equation** -> **Master Equation**: [Master Equation](https://statisticalphysics.leima.is/nonequilibrium/master-eqn.html).

Notes on "Markov" from Section IV.1 of [2](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces).

> In principle any closed isolated physical system can be described as a Markov process by introducing all microscopic variables as components of $$Y$$. In fact, the microscopic motion in phase space is deterministic and therefore Markovian, compare $$P_{1\vert 1}(x,t\vert x_0, t_0)=\delta[x-\phi(x_0,t-t_0)]$$. The physicist's question, however, is whether he can find a small set of variables whose behavior in time can be described as a multicomponent Markov process. The well-known, but still miraculous, experimental fact is that this is so far most many-body systems in nature. Of course, such a description is at best approximate and restricted to a macroscopic, coarse-grained level. This reduction to a much smaller number of variables is called "contraction" or "projection", but the justification of this approximation involves the fundamental problems of statistical mechanics and is still the subject of many discussions. 

### e.g., Fixed jump time -> the master equation

Suppose the transition probability is $$T(y\vert y')$$ ($$y'$$ to $$y$$) and the current state is $$P(y,t)$$. Also for next state $$y$$ goes to $$y'$$ so $$\displaystyle \int T(y'\vert y)P(y,t)=P(y,t)$$.

Evolution: if the jumping time interval is $$\tau$$, then $$\displaystyle P(y,t+\tau)=\int T(y\vert y')P(y',t)$$. Now expand $$P$$ to **first-order in time**, $$\displaystyle P(y,t+\tau)=P(y,t)+\tau\frac{\partial}{\partial t}P(y,t)$$. Then $$\displaystyle \tau\frac{\partial}{\partial t}P(y,t)=\int \{T(y\vert y')P(y',t)-T(y'\vert y)P(y,t)\}$$. Transition probability per unit time: $$W(y\vert y')=T(y\vert y')/\tau$$, then we have the master equation above.

### Exponential lifetime

If we indicate the probability at state $$A$$ as $$P(A,t)$$, then we have $$P(A,t+dt)=P(A,t)-P_\text{jump}(t,t+dt)$$, while $$P_\text{jump}(t,t+dt)=P_\text{jump}(t,t+dt\vert A,t)P(A,t)$$, then $$\displaystyle\frac{dP(A,t)}{dt}=-\lim\limits_{dt→0}\frac{P_\text{jump}(t,t+dt\vert A,t)}{dt}P(A,t)$$. [1](https://shi200005.github.io/2022/10/28/Stochastic-Processes/#refernces)

Suppose the probability of jumping out per unit time $$\displaystyle\lim\limits_{dt→0}\frac{P_\text{jump}(t,t+dt\vert A,t)}{dt}=r$$ is a constant. Then the probability of **not** jumping out of $$A$$ by time $$t_A$$ is $$\displaystyle S(t_A)=\lim\limits_{dt→0}\prod_{dt}^{t_A/dt}(1-rdt)=e^{-rt_A}$$. Then the pdf of lifetime distribution in state $$A$$ is $$\displaystyle \lambda(t_A)=-\frac{\partial}{\partial t_A}S=re^{-rt_A}$$ , which obeys an [exponential distribution](https://shi200005.github.io/2022/02/17/Probability/#指数分布), with the mean $$\tau=1/r$$. 

#### e.g., Exponential lifetime -> the master equation

Probability time of umping to state $$i$$ from $$A$$: $$p_i$$, per unit time: $$r_i=p_ir$$. $$\displaystyle \tau\frac{\partial}{\partial t}P(A)=\int p_iP(i)-P(A)$$. Plug in $$\tau=1/r$$, we have $$\displaystyle\frac{\partial}{\partial t}P(A)=\int r_iP(i)-rP(A)$$.

### e.g., Finite State Markov Chain

 States: $$i=1,2,...,n$$.

$$
\begin{pmatrix}
	\dot P_1(t) \\ \dot P_2(t) \\ \vdots \\ \dot P_n(t)
\end{pmatrix}

=

\begin{pmatrix}
	-\displaystyle\sum_{j\neq 1} r_{j1} & r_{12} &\ldots  \\
    r_{21} & -\displaystyle\sum_{k\neq 2} r_{k2} &\ldots \\
    \ldots &\ldots &\ldots
\end{pmatrix}

\begin{pmatrix}
	P_1(t) \\ P_2(t) \\ \vdots \\ P_n(t)
\end{pmatrix}
$$

Denote as $$\displaystyle\frac{\partial}{\partial t}\vec P(t)=\hat M\cdot\vec P(t)$$, check [Matrix exponential](https://shi200005.github.io/2021/09/30/Linear-Algebra/#matrix-exponential) in Linear Algebra. $$\hat M$$'s column elements sums to zero -> $$\hat M$$ is degenerate -> $$\det(\hat M)=0$$ -> at least one zero eigenvalue, at least one steady state. Stable steady-state: the eigenvalues have negative real parts.

Fokker-Planck equation can only be used in systems that can be described by d-dimension (???).

#### Equilibrium

Zero flux between any two states $$J_{ij}=0$$. Transition rate: $$r_{ij}:=r_{j\to i}$$, then $$P_i^{\text{eq}}r_{ij}=P_j^{\text{eq}}r_{ji}$$ (if satisfied by all pairs -> **detailed balance**). 

Detailed-balance condition: **Kolmogorov condition** (in a loop...e.g., $$\displaystyle\frac{r_{12}r_{23}r_{31}}{r_{21}r_{32}r_{13}}=1$$).

## The Fokker-Planck Equation (FP)

The derivation (approximation) from the Master Equation to the Fokker-Planck Equation is in Section VIII.2 of [1](https://shi200005.github.io/2025/03/15/Stochastic-Processes/#references).

Express the transition probability $$W$$ as a function of the size $$r$$ of the jump and starting point: $$W(y\vert y')=W(y';r),r=y-y'$$.

Assumptions

- only small jumps occur, i.e., $$W(y';r)$$ is a sharply peaked function of $$r$$ but varies slowly with $$y'$$.
- the solution $$P(y,t)$$ also varies slowly with $$y$$.

Then expand the master equation according to the state shift up to the **second order**, we get the **Fokker-Planck Equation** $$\displaystyle\frac{\partial}{\partial t}P(y,t)=-\frac{\partial}{\partial y}\{a_1(y)P\}+\frac{1}{2}\frac{\partial^2}{\partial y^2}\{a_2(y)P\}$$, where $$\displaystyle a_\nu(y)=\int_{-\infty}^{\infty}r^\nu W(y;r)dr$$.

### Linear FP: $$a_1$$ is linear

In the special case where $$a_1(y)=A_0+A_1y$$ and $$a_2(y)=B_0$$, the Fokker-Planck equation is linear. 

#### e.g., General 1-D random walk ($$A_1=0$$)

Fixed jump time $$\tau$$ and interval $$a$$ as above. Expand to the second-order $$\displaystyle P(y\pm a)=P(y)\pm a\frac{\partial}{\partial y}P(y)+\frac{1}{2}a^2\frac{\partial^2}{\partial y^2}P(y)$$, same for $$p(y\pm a)$$ and $$q(y\pm a)$$. Then we have $$\displaystyle\frac{\partial}{\partial t}P(y,t)=-\frac{\partial}{\partial y}\{v(y)P\}+D\frac{\partial^2}{\partial y^2}P$$, where $$\displaystyle v(y)=\frac{a}{\tau}[p(y)-q(y)]=\epsilon\frac{a}{\tau}$$ is the *velocity*, $$\displaystyle D=\frac{a^2}{2\tau}$$ is the *diffusion coefficient*. In continuum limit, $$a,\tau\to0$$ and $$D=\text{const}$$, to keep $$v$$ finite, we should have $$\epsilon\to0$$ (small bias).

From **Continuity Equation** $$\displaystyle\frac{\partial}{\partial t} P(y,t)=\frac{\partial}{\partial y} J(y,t)$$, we get **Smoluchowski equation** $$\displaystyle J(y,t)=v(y)P(y,t)-D\frac{\partial}{\partial y}P(y,t)$$, which are "FLUX" and "[FICK'S LAW](https://shi200005.github.io/2022/02/24/Thermodynamics/#输运现象)".

##### Equilibrium of non-interacting particles

$$J(y,t)=0$$ -> $$\displaystyle P^{\text{eq}}(y)=C\exp{\int^y\frac{v(y')}{D}dy'}$$. 

[Boltzmann distribution](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/#近独立子系组成的系统): $$\displaystyle P^{\text{eq}}(y)=C\exp{\int^y\frac{u(y')}{k_BT}dy'}$$. Force $$\displaystyle F(y)=\frac{\partial}{\partial y}u(y)$$. 

Brown particle: $$m\ddot x=f+\xi$$. For the [overdamped](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#振动和波) system, $$m\ddot x$$ is negligible, and we have $$v=-\mu f$$, where $$\mu$$ is *mobility*. Then, we derive the **Einstein relation** (a special case of the Fluctuation-dissipation theorem for Brown particles) $$\displaystyle\mu=\frac{D}{k_BT}$$. 

- Consider [Stokes' drag law]((https://shi200005.github.io/2022/02/24/Thermodynamics/#输运现象)), $$f=6\pi\eta Rv$$ (small round particles in honey), we get $$\displaystyle\mu=\frac{1}{6\pi\eta R}$$.

#### Ornstein-Uhlenbeck processes

If $$A_1<0$$, the stationary solution is **Gaussian** (to solve the Gaussian solution, use the Fourier transform, check [3](https://shi200005.github.io/2025/03/15/Stochastic-Processes/#references), where we talk about the special case of $$A_0=0$$ by moving the coordinate to the mean). 

## Langevin equation

Equivalence of FP and Langevin: $$\displaystyle\frac{\partial}{\partial t}P(y,t)=-\frac{\partial}{\partial y}\{a_1(y)P\}+\frac{1}{2}\frac{\partial^2}{\partial y^2}\{a_2(y)P\}$$ <-> $$dy=a_1(y)dt+\sqrt{a_2(y)}dW(t)$$ (**Stochastic differential equation**, **SDE**), where $$B_t$$ is a [Wiener process](https://en.wikipedia.org/wiki/Wiener_process#Characterisations_of_the_Wiener_process).

[Itô's lemma](https://en.wikipedia.org/wiki/Itô%27s_lemma#Derivation) is important in the derivation: $$dX_t=\mu_tdt+\sigma_tdB_t$$, where $$B_t$$ is a [Wiener process](https://en.wikipedia.org/wiki/Wiener_process#Characterisations_of_the_Wiener_process) -> function $$f(t,x)$$ by expanding the Taylor series we have $$\displaystyle df=\lim_{dt\to0}\left(\frac{\partial f}{\partial t}+\mu_t\frac{\partial f}{\partial x}+\frac{\sigma^2}{2}\frac{\partial^2 f}{\partial x^2}\right)dt+\sigma_t\frac{\partial f}{\partial x}dB_t$$.

$$\dot x(t)=\mu(F(x)+\xi(t))$$ ([overdamped](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#振动和波)) <-> $$\displaystyle\frac{\partial}{\partial t}p(x,t)=-\frac{\partial}{\partial x}(\mu f(x)p(x,t))+D\frac{\partial^2}{\partial x^2}p(x,t)$$, where $$\displaystyle\mu=\frac{D}{k_BT}$$ and $$\displaystyle\langle\xi(t)\xi(t')\rangle=\frac{k_BT}{\sqrt D}\delta(t-t')$$.

### Brown particle

The external force $$F(x)=0$$, then $$m\dot v=-v/\mu+\xi$$, use the multiplier to solve $$v$$, when $$t\to0$$, $$\displaystyle\frac{1}{2}m\langle v(t)^2\rangle\to\frac{k_BT}{2}$$, consistent with statistical mechanics from assuming [Boltzmann distribution](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/#近独立子系组成的系统).

## First Passage Processes

$$n=0\leftarrow...\leftrightharpoons n_0-1\leftrightharpoons n_0\leftrightharpoons n_0+1\leftrightharpoons...\rightarrow n=L$$ with rightward transition prob as $$p(n)=p$$ and leftward prob as $$q(n)=1-p=q$$. $$n=0$$ and $$n=L$$ are absorbing boundaries. When $$L\to\infty$$, <span style="color: blue;">You are a gambler. When you lose all your money, you have to quit. Every gambler is too addictive that they don't quit... </span>

Consider this step and the next step, $$P(0,\infty\vert n_0,0)=pP(0,\infty\vert n_0+1,0)+qP(0,\infty\vert n_0-1,0)$$. Try $$P(0,\infty\vert n_0,0)=\lambda^{n_0}$$ -> $$\displaystyle P(0,\infty\vert n_0,0)=\frac{(q/p)^L-(q/p)^{n_0}}{(q/p)^L-1}$$. 

- $$q>p$$ -> $$P(0,\infty\vert n_0,0)=1$$; <span style="color: blue;">The probability of losing this gambling game is higher than the probability of winning; should you play it? No! </span>
- $$q<p$$ -> $$\displaystyle P(0,\infty\vert n_0,0)=\left(\frac{q}{p}\right)^{n_0}<1$$. <span style="color: blue;">The probability of winning this gambling game is higher than the probability of losing **on average**. You either win or get broke. </span>

**Mean first passage time**  $$T(0\vert n_0,0)=pP(0\vert n_0+1,0)+qP(0\vert n_0-1,0)+\tau$$. Try $$T(0\vert n_0,0)=\lambda^{n_0}$$ -> $$\displaystyle T(0\vert n_0,0)=\frac{\tau L}{p-q}(-\frac{n_0}{L}+\frac{(q/p)^{n_0}-1}{(q/p)^L-1})$$.

- $$q>p$$ -> $$\displaystyle T(0\vert n_0,0)=\frac{\tau n_0}{q-p}$$; <span style="color: blue;">The expected time for you to get broke (as we can see, you are doomed to get broke if you keep gambling, just sooner or later, but we have an estimation of average "get broke" time). </span>
- $$q<p$$ -> $$T(0\vert n_0,0)\to\infty$$. <span style="color: blue;">**On average** players won't get broke; should you play it? But you can be the unfortunate guy ruined in this ensemble... </span>

[(Zh) 为何赌徒心态终究输光？非遍历性系统中的生存法则](https://mp.weixin.qq.com/s/TDdOlND6zjvVZqCEChm-Aw)

<span style="color: blue;">Conclusion: being a physicist is more rewarding than being a gambler.</span>

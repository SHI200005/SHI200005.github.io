---
layout: post
title: (En) How is the Significance of Fluctuations near Chemical Instability Captured by Gillespie Algorithm?
categories: Self-Study
description: 
keywords: Gillespie, fluctuations
mathjax: true
---

I have been applied Gillespie algorithm for about three years to simulate stochastic chemical reactions, or more coarse-grained gene regulatory networks. I think it is a good point to check Gillespie's important original papers and write a report about some of my thoughts...

Here, I used the model of **excitable gene regulatory network** I discussed in my undergraduate thesis as an example to illustrate how is **the significance of fluctuations near chemical instability** captured by **Gillespie Algorithm**.

Given that the algorithm is so well-known and basic for biophysics researchers, the computation steps which I have been taught twice in courses will not be included (but links to example codes below :wink:), but only the physics assumptions behind I learnt from Gillespie's paper by myself is included.

> An **exact** method is presented for numerically calculating, within the framework of the stochastic formulation of chemical kinetics, the time evolution of any **spatially homogeneous** mixture of molecular species which interreact through a specified set of coupled chemical reaction channels. The method is a compact, computer-based, Monte Carlo simulation procedure. [1](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references)

## On Gillespie Algorithm

D.T. Gillespie's 1976 paper [1](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references) described a mile-stone computer algorithm to simulate the **Markov process** of stochastic chemical reactions, which is **fully equivalent to the master equation**. It is very powerful for theorists to check their derived analytical statistical properties by numerical results. 

The paper is elegant and enjoyable to read (and easy). Here I used the example in the paper (see below) to quickly summarize the physical ideas (just for my own understanding, for you, it is better to read the original paper :wink:). My aim for this post is to combine it with a 2014 paper. Suppose there is a reaction

$$R_\mu: S_1+S_2\rightarrow2S_3 $$

### Deterministic Approach and its Limitations

For $$N$$ molecular species, a system of $$N$$ ODEs describes the time evolution of molecular concentration. The reaction constants are viewed as reaction "rates".

In the example, $$x_i$$ represent the concentrations of $$S_i$$, and the ODEs are

$$\frac{dx_1}{dt}=-k_\mu x_1x_2 \\ \frac{dx_2}{dt}=-k_\mu x_1x_2 \\ \frac{dx_3}{dt}=2k_\mu x_1x_2$$

where $$k$$ is the reaction rate and compared with the stochastic formulation, approximations are involved in the deterministic approach (see below).

### Physical Basis of Gillespie Algorithm

The only “assumption” is that the reaction parameter $$c_\mu$$, which characterizes reaction $$R_\mu$$, can be defined as follows. 

$$c_\mu\delta t \equiv \text{average probability, to first order in } \delta t\text{, that a }\\ \text{particular combination of }R_\mu \text{ reactant molecules } \\\text{will react accordingly in the next time interval }\delta t$$

<img src="\images\blog\Gillespie_Collision.JPG" alt="Gillespie_Collision" width="400px;" />

Figure from [2](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references).

Apart from the species involved ($$S_i$$) and the form of reactions ($$R_\mu$$), we need to specify the reaction parameter ($$c_\mu$$). How $$c_\mu$$ is specified was described elegantly in the text. 

In short, given **spatial homogeneity**, the *average probability* that a particular l-2 molecular pair will *collide* in the next time interval $$\delta t$$ is, to first order in $$\delta t$$, $$\langle V_{coll}/V\rangle=\pi d_{12}^2\langle v_{12}\rangle\delta t/V$$, where the brackets denote an average over the velocities of all $$S_1-S_2$$ molecular pairs.  <span style="color: gray;">The condition that nonreactive molecular collisions occur much more frequently than reactive molecular collisions is thus a convenient criterion for applicability of the stochastic formulation of chemical kinetics.</span>

Given **thermal (not chemical) equilibrium** at temperature $$T$$, $$\langle v_{12}\rangle$$ can be obtained from Maxwell-Boltzmann distributions $$\langle v_{12}\rangle=(8kT/\pi m_{12})^{1/2}$$, where $$m_{12}$$ is the reduced mass. Consider only when the kinetic energy of collision exceed the activation energy $$u_u^*$$, the reaction occurs, we get $$c_\mu=V^{-1}\pi d_{12}^2(8kT/\pi m_{12})^{1/2}\exp(-u_u^*/kT)$$.

### Gillespie Algorithm, Compared with the Deterministic Approach

In the example, representing the abundances of species are $$X_i$$, there will be $$X_1X_2$$ distinct combinations of reactant molecules inside $$V$$. Thus, the *average rate* of $$R_\mu$$ that occurs inside $$V$$ is $$\langle X_1X_2\rangle c_\mu$$.

The relationship with reaction rate in the deterministic approach is $$k_\mu=\langle x_1x_2\rangle Vc_\mu/\langle x_1\rangle\langle x_2\rangle$$.

> For “ordinary” chemical systems in which fluctuations and correlations play no significant role, the method stands as an alternative to the traditional procedure of numerically solving the deterministic reaction rate equations. For nonlinear systems **near chemical instabilities**, where fluctuations and correlations may invalidate the deterministic equations, the method constitutes an efficient way of numerically examining the predictions of the stochastic master equation. [1](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references)

In the deterministic approach, we take $$k_\mu\doteq Vc_\mu$$. It works well when $$\langle x_1x_2\rangle=\langle x_1\rangle\langle x_2\rangle$$ is almost true.

The following part of mathematical derivation from probability is so basic in a course that I don't bother to include it. 

### Probability, Markov Chains, and Monte Carlo Method

This part was elegantly explained in the lecture note my supervisor gave me (Johan Paulsson, 10/15/2014, Systems Biology 200), and I don't think I have any better ideas to rewrite. I just summarized some key points. (I don’t know whether the staff I show here violate copyright. If so, I will sincerely すみません…)

Regarding the chemical reaction as the random walk on the discrete lattice in the phase space, If we indicate the probability at state $$A$$ as $$P(A,t)$$, then we have $$P(A,t+dt)=P(A,t)-P_\text{jump}(t,t+dt)$$, while $$P_\text{jump}(t,t+dt)=P_\text{jump}(t,t+dt\vert A,t)P(A,t)$$, then $$\displaystyle\frac{dP(A,t)}{dt}=-\lim\limits_{dt→0}\frac{P_\text{jump}(t,t+dt\vert A,t)}{dt}P(A,t)$$. 

#### First-order degradation and life time

If the probability of jumping out per time is a constant $$\beta$$, then $$\displaystyle\frac{dP(A,t)}{dt}=-\beta P(A,t)$$. That means the life time of an molecule obeys the **exponential distribution**, with a **life time** of $$\tau=1/\beta$$.

### Output of Gillespie Algorithm

Simulating the Markovian random walk on the grid of species abundances (the phase space) can give us the time traces of the time evolution of the system (example here [3a](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references)). For complex reaction networks, the analytical solution of the stationary probability distribution on the phase space cannot be written down explicitly, and the Gillespie Algorithm gives us the result from numeric computation (example here [4]((https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references))).

## On Fluctuations near Instability

### Nonlinear Rates and Fluctuations

I would like to show an example of a one-variable dimer degradation to show the relationship between the master equation and the deterministic approach. From Gillespie's paper [1](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references), we set up a toy model, where the molecule is produced with a constant rate and degraded in a dimer form,

$$
x \stackrel{\lambda}{\longrightarrow} x+1 \\x \stackrel{\gamma x(x-1)}{\longrightarrow} x-2
$$
<img src="\images\blog\Gillespie_Dimer.jpg" alt="Gillespie_Dimer" style="zoom:100%;" />

Note that nonlinear rates prohibit exact **moment closure** [5](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references).  In the linear case, $$\displaystyle\frac{d\langle x\rangle}{dt}$$ contains terms no higher than the first moment, and you can solve it by given conditions. Then, $$\displaystyle\frac{d\langle x^2\rangle}{dt}$$ contains terms no higher than the second moment, and you can solve it by the solved first moment... But in the nonlinear case, as I have written, $$\displaystyle\frac{d\langle x\rangle}{dt}$$ contains the second-order term and can't be solved analytically.

Let's see something more interesting in my undergrad thesis - there are different types of fixed points in a nonlinear networks!!! The full English abstract of the thesis can be found [here](https://github.com/SHI200005/Examples/Excitability).

### The Excitable Gene Regulatory Network

**Interlinked positive and negative feedback loops** are universal in biological systems, for example, the network of Cyclin B and the network of MAPK. Different behaviors can be achieved, such as mono-stability, bi-stability, oscillation, and excitability. **A hallmark of excitability is that a transient input is sufficient for triggering a large response.** In electrophysiology, the neurons can transmit signals when the potential is raised above a threshold. Proteins regulated by genetic networks also fit the features of excitability. For example, when E. coli is under stress, it will likely switch to competence from vegetative growth.

The fast positive feedback loop drives the system further away from the stable node/focus, and then the slow negative feedback loop drives the system back to the stable node/focus. My thesis is to determine the parameters and dynamics of the 3-node gene regulatory network, which can achieve excitable behavior.

### Fixed Point Analysis

Fixed points analysis in the excitable gene regulatory networks appears in [6](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references), a model of *B. subtilis* competence. Excitable networks are defined when the ODEs have three fixed points: **a stable node/focus, a saddle, and an unstable focus**. Take the network in Figure.1.b and the ODEs in Box.1 (parameter given by Figure.S3.D), I plotted the three fixed points and the trajectories of the **deterministic approach given by the ODEs** (the MATLAB code attached [3b](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references)!). The saddle defines a manifold. If the initial point starts from the "node" side of the stable manifold, it will flow to the node. If you start from the "unstable focus" side of the stable manifold, it will flow across the unstable focus and then return to the node, and this is an excitement event. (Whether there will be excitement is totally determined by the initial condition. Similar to the bistable case of the Lotka-Volterra competition model, where there are two stable nodes and a saddle...)

![image](https://raw.githubusercontent.com/SHI200005/Examples/tree/main/Excitability/annex/3.2/3_2.jpg)

 ### Stochastic Model and Reduced Model

In the case that the stable node/focus is **close enough** to the saddle (**chemical instability**), taking stochasticity into account when the trajectory is bouncing around the stable node/focus, it might cross the saddle's stable manifold and trigger **auto-excitement**! **Gillespie simulations can capture this auto-excitement!** I will elaborate it by two examples.

### Fluctuation Caused Auto-Excitements Forms a Genetic Timer

The excitable network and auto-excitement were also discussed in 8, where the auto-excitement can be regarded as "a genetic timer." My math understanding of the fixed points in excitable networks mainly came from this short paper.

<img src="https://raw.githubusercontent.com/SHI200005/Examples/tree/main/Excitability/annex/nocode/5_6.jpeg" alt="Figure1" width="350px;" />

This is the figure 1 in the paper. **A** shows a two-node gene regulatory network consisting of interlinked positive and negative feedback loops. **B** is the deterministic model. The filled red circle is the stable focus, the open red circle is the saddle, and the open red diamond is the unstable focus. If the initial state is on the "excitement" side of the stable manifold defined by the saddle. **D** is from Gillespie simulations. The saddle is very close to the stable focus. When the trajectory bounces due to the stochasticity, it might cross the stable manifold and trigger an auto-excitement.

Note that, if we adjust the parameter set of the network, **making the real-part of the eigenvalue of the unstable focus sufficient close to zero**, instead of going to the stable focus directly, the trajectory might circle the unstable focus around for several times before returning! The time spent for each circle is similar, and that's why it is called the genetic timer!

<img src="https://www.pnas.org/cms/10.1073/pnas.0806349105/asset/45618616-ee9d-4ae5-b7c6-9d0d5cf22f4b/assets/graphic/zpq9990851480002.jpeg" alt="Figure1" width="350px;" />

### Transcription and Translation Rates Affects the Level of Intrinsic Noise

In 2002, Ozbudak et al. showed that in a stochastic gene regulatory network model, **When the transcription rate is high, variability in protein levels is low, but when the transcription rate is lowered and the translation rate is raised, gene expression is far noisier, even at the same mean.** (Summarized in [7](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#references))

![image2](https://raw.githubusercontent.com/SHI200005/Examples/tree/main/Excitability/annex/nocode/5.4.jpg)

This statement is explicitly shown in my simulations. Refer to pages 18-20 in [3c](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/Eng.pdf), the corresponding figures and codes in [3a](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/Eng.pdf). In my excitable networks, auto-excitement can be triggered with a larger probability with smaller transcription rates and larger translation rates (at the same mean). Visualized on pages 19-20, [3c](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/Eng.pdf).

## References

[1] Gillespie, D. T. (1976). A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. *Journal of computational physics*, *22*(4), 403-434. [online](https://www.sciencedirect.com/science/article/abs/pii/0021999176900413?via%3Dihub#preview-section-cited-by)

[2] Gillespie, D. T. (1977). Exact stochastic simulation of coupled chemical reactions. *The journal of physical chemistry*, *81*(25), 2340-2361. [online](https://pubs.acs.org/doi/10.1021/j100540a008)

[3] My undergraduate thesis [repository](https://github.com/SHI200005/Examples/Excitability).

  - [a] [Figure 5.5](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/5.5), [Figure 5.6](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/5.6)

  - [b] [Figure 3.2](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/3.2)

- [c] [Brief introduction](https://github.com/SHI200005/Examples/tree/main/Excitability/annex/Eng_copyright.pdf)

[4] [Paper repository](https://github.com/t-wittenstein/quantify-biochemical-rates/tree/master/Simulation)

[5] Hilfinger, A., Norman, T. M., Vinnicombe, G., & Paulsson, J. (2016). Constraints on fluctuations in sparsely characterized biological  systems. *Physical review letters*, *116*(5), 058101. [online](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.058101)

[6] Süel, G. M., Garcia-Ojalvo, J.,  Liberman, L. M., & Elowitz, M. B. (2006). An excitable gene  regulatory circuit induces transient cellular differentiation. *Nature*, *440*(7083), 545-550. [online](https://www.nature.com/articles/nature04588)

[7] Raj, A., & Van Oudenaarden, A. (2008). Nature, nurture, or chance: stochastic gene expression and its consequences. *Cell*, *135*(2), 216-226. [online](https://www.cell.com/fulltext/S0092-86740801243-9)

[8] Turcotte, M., Garcia-Ojalvo, J., & Süel, G. M. (2008). A genetic  timer through noise-induced stabilization of an unstable state. *Proceedings of the National Academy of Sciences*, *105*(41), 15732-15737. [online](https://www.pnas.org/doi/abs/10.1073/pnas.0806349105)

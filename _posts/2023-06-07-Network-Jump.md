---
layout: post
title: (En) Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem
categories: Self-Study
description: 
keywords: fluctuations, Markov, Master Equation
mathjax: true
---

The content of this post is closely linked to the research conducted by [A. Hilfinger](https://www.hilfinger.group/), [J. Paulsson](https://paulsson.med.harvard.edu/), and [J. Elf](https://elflab.icm.uu.se/), etc. As a mathematical rookie, I will introduce the models and mathematics in the most accessible way. You need a second-year undergrad level of mathematics to read this. 

At the starting point, [3](https://shi200005.github.io/2023/06/07/Network-Jump/#references), [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references) and [10](https://shi200005.github.io/2023/06/07/Network-Jump/#references) in the references are three papers can be read in details.

## Noise in Gene Regulatory Networks

In 2002, Elowitz et al. provided experimental evidence that gene regulatory networks inherently exhibit noise [1](https://shi200005.github.io/2023/06/07/Network-Jump/#references). How to analyze the noise then? In **Molecular Biology** (a course I took as an undergrad, and I will write something in Chinses, but haven't started yet...), we've already learned how complicated the mechanisms of transcription and translation could be. However, physicists are people having good intuition of extracting from facts and making up models to describe the world. They have tried to use **Markov processes** to describe the network with intrinsic noise (discussed in van Kampen's IV.1 [2](https://shi200005.github.io/2023/06/07/Network-Jump/#references), also quoted in [(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)). We describe the dynamics of the number (integers) of molecules (mRNAs, proteins...) as discrete **birth and death** jump between the grids of the whole phase space. 

More about the model construction, see **Appendix of [3](https://shi200005.github.io/2023/06/07/Network-Jump/#references)** and the main text of [4](https://shi200005.github.io/2023/06/07/Network-Jump/#references), also quoted in [(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/).

## One-Variable Case

Always start from the simplest. Let's consider a molecule $$X$$'s probability (per unit time) of production  and degradation are $$f(x)$$ and $$g(x)$$ (also refer to transition rates). As a Markovian process, we take the transition rates merely depends on where the current state is. We write it as


$$
x \stackrel{f(x)}{\longrightarrow} x+1 \\
x \stackrel{g(x)}{\longrightarrow} x-1
$$


which the probability distribution on different grids is $$P(x,t)$$. The time evolution of the probability distribution $$\displaystyle\frac{dP(x,t)}{dt}$$ is described by a **master equation**, which can be interpreted as "plus the probability in and minus the probability out of that state". It should be conditioned on the initial state, but we'll drop it, because we're interested in the stationary state, which all initial states will evolve to. From $$\displaystyle\frac{dP(x,t)}{dt}$$, using the "index shift" trick, we can get the evolution of statistical quantities of $$X$$ (average over the ensemble). (This is from Hilfinger's lecture note of PHY2707, and I don't know whether there is a copyright. If there is, I will sincerely すみません...)

<img src="\images\blog\Network_Jump_1var.jpg" alt="Network_Jump_1var" style="zoom:50%;" />

### Special case: constant birth and first-order degradation

Now, let's look at an intuitive and simple case where the molecule has a constant production rate and a first-order degradation rate. The steady-state (also detailed balance in this case) of the probability distribution on grids forms a **Poisson distribution**. (from Hilfinger's lecture note...)


$$
x \stackrel{\lambda}{\longrightarrow} x+1 \\
x \stackrel{\beta x}{\longrightarrow} x-1
$$

<img src="\images\blog\Network_Jump_1var_Special.jpg" alt="Network_Jump_1var_Special" style="zoom:50%;" />

Note that for the stationary state, for each $$x>0$$ grid, the two ways in and two ways out should sum up to zero. while for the $$x=0$$ grid, there is only one way in and out from/to $$x=1$$ grid. Then we know ways $$x=m$$ to $$x=m+1$$ should equal $$x=m+1$$ to $$x=m$$. 

## Multi-variable Case

Gene regulatory networks consist of many interacting molecule species. We consider a biochemical system with $$n$$ molecular species and $$m$$ elementary reactions. 


$$
x(t) \stackrel{W_i(x(t))}{\longrightarrow} x(t)+r_i, \quad i=1,2,...,m
$$


For this network, use the "index shift" trick to calculate mean, variances, and covariances with the master equation. **The detailed steps are in [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references)**, equation (1)-(3). I don't bother to type the results here.

In these jump models, the **diffusion** and **drift** coefficients are related, using a **Lyapunov equation** [6](https://shi200005.github.io/2023/06/07/Network-Jump/#references), to the **steady-state covariance** matrix [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references). If all the transition rates are **linear** functions, the Lyapunov equation is the *exact* result of the master equation and **no** Gaussian approximation is needed. If the transition rates are **nonlinear**, **van Kampen's $$\Omega$$ expansion** (leads to **linear noise approximation**) is needed to derive the equation.

We follow the content in [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references). Define the vector of transition rate as $$f(x):=\sum_ir_iW_i(x)$$.

### Linear Case

We can write the transition rate as $$f(x(t))=Ax(t)+f_0$$, where $$A$$ is an n*n real constant matrix (**drift**) and $$f_0$$ is an n-dimensional constant vector.

Define the **covariance** matrix $$\Sigma(t):=\langle x(t)x^T(t)\rangle-\langle x(t)\rangle\langle x^T(t)\rangle$$, **autocorrelation** $$R_{xx}(t_1,t_2):=\langle x(t_1)x^T(t_2)\rangle-\langle x(t_1)\rangle\langle x^T(t_2)\rangle$$. **Following [4](https://shi200005.github.io/2023/06/07/Network-Jump/#references)**, there are some important *exact* results.

$$\displaystyle\frac{d\Sigma(t)}{dt}=A\Sigma(t)+\Sigma A(t)^T+D(t)$$. (5 in text, where $$D(t):=\sum_ir_iW_i(\langle x(t)\rangle)r_i(t)$$)

$$\displaystyle\frac{\partial R_{xx}(t_1,t_2)}{\partial t_1}=AR_{xx}(t_1,t_2)$$. (7 in text)

For steady state, 

$$AR_{xx}(0)+R_{xx}(0)A^T+D=0$$. (9 in text) This is the **Lyapunov equation**, and often called the **fluctuation-dissipation** theorem, a balance between the tendency of particles to diffuse and mechanisms such as negative feedback that bring them back to equilibrium (Remark 3 in text).

$$\displaystyle\frac{\partial R_{xx}(\tau)}{\partial\tau}=AR_{xx}(\tau)$$. (10 in text) And how to solve this system of ODEs? Use **matrix exponential**, which involves **diagonalizing** the matrix; see Linear Algebra ([线性代数 - Matrix Exponential](https://shi200005.github.io/2021/09/30/Linear-Algebra/#matrix-exponential)).

#### The Classical Model of mRNA and Protein

This is an example of a linear case with the classical mRNA-protein model [3](https://shi200005.github.io/2023/06/07/Network-Jump/#references). You can regard $$X_1$$ as the mRNA and $$X_2$$ as the protein. (In many cases, the protein degradation rate is very small compared with cell growth [7](https://shi200005.github.io/2023/06/07/Network-Jump/#references), and the dilution effects are often described as first-order degradation.) You will come across this model from time to time when you are reading Paulsson Group related things... For example, model [4] in [8](https://shi200005.github.io/2023/06/07/Network-Jump/#references), and equation [7] is the exact result of this linear rates model. See below how to derive.


$$
x_1 \stackrel{\lambda}{\longrightarrow} x_1+1 \quad x_2 \stackrel{\alpha x_1}{\longrightarrow} x_2+1 \\
x_1 \stackrel{\beta_1 x_1}{\longrightarrow} x_1-1 \quad x_2 \stackrel{\beta_2x_2}{\longrightarrow} x_2-1
$$

![Network_Jump_2var_Linear](\images\blog\Network_Jump_2var_Linear.jpg)

#### The Classical Model with Additional Complex Formation and Disassociation

In [9](https://shi200005.github.io/2023/06/07/Network-Jump/#references), the role of the miRNA-mRNA complex in regulating noise at the protein level was considered. In the following figure, I showed the matrix $$D$$ of the reaction involving more than one species. 

![Network_Jump_Complex](\images\blog\Network_Jump_Complex.jpg)

#### The "Normalized" Form

Well, I base the above derivation on [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references). In the well-known paper [9](https://shi200005.github.io/2023/06/07/Network-Jump/#references), where the author set up a "standard procedure", they are in a **normalized** form (example papers using the "normalized" form: [9](https://shi200005.github.io/2023/06/07/Network-Jump/#references), [10](https://shi200005.github.io/2023/06/07/Network-Jump/#references), [11](https://shi200005.github.io/2023/06/07/Network-Jump/#references)). I show the procedure to normalize them. Note that "Little's Law" is applied here.

 ![Network_Jump_Complex](\images\blog\Network_Jump_Normalize.jpg)

#### From Langevin Equation

For the linear case, the Lyapunov equation, or the fluctuation-dissipation theorem, can also be derived from the Langevin equation $$\displaystyle\frac{d \vec{a}}{dt}=\hat H\vec{a}+\vec{\tilde{f}}$$, where $$\vec{\tilde f}(t)$$ is a **white noise** vector. The steps can be found in chapter 1.8 from [12](https://shi200005.github.io/2023/06/07/Network-Jump/#references). You can also find my note [Network_Langevin_Lyapunov](https://shi200005.github.io/download_file/Network_Langevin_Lyapunov.pdf) here.

The relationship between the master equation, the Fokker-Planck approximation, and the Langevin approach will be discussed in the following part.

### Nonlinear Case

In the nonlinear case, we cannot simply drag the drift matrix $$A$$ out as $$f(x(t))-\langle f(x(t))\rangle=A(x(t)-\langle x(t)\rangle)$$ (above equation 5 in [5](https://shi200005.github.io/2023/06/07/Network-Jump/#references)), and get the nice Lyapunov equation. To quantify the variances and covariances (second-moment properties), we must make some approximations...

#### Van Kampen's $$\Omega$$ expansion and Linear Noise Approximation

The $$\Omega$$-expansion means the Master equation is Taylor expanded **near macroscopic system trajectories** or **stationary solutions** in powers of $$1/\sqrt{\Omega}$$, where $$\Omega$$ is the system volume. When the Master equation is approximated near a macroscopically stable stationary solution, terms of first order in $$1/\sqrt{\Omega}$$ give the macroscopic rate equations, and terms of second order in $$1/\sqrt{\Omega}$$  give the **Linear Noise Approximation (LNA)**. The rationale behind this approach is that relative fluctuations will tend to decrease for constant average concentrations with the inverse of the square root of the volume [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references).

P.S. In most papers, researchers look at the stationary properties. A **cyclostationary** case (not stationary) case where Linear Noise Approximation is applied **near macroscopic system trajectories** can be found in [14](https://shi200005.github.io/2023/06/07/Network-Jump/#references).

You can find a formal explanation in chapter X of [2](https://shi200005.github.io/2023/06/07/Network-Jump/#references). If you are looking for a shorter and closely related to gene regulatory network text, check **the supplementary material of [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references) ** (after "Derivation of the LNA," go to "Example 3: Coupled fluctuations in a two-component system" starting from page 6).

I would like to explain it as "changing the variables from several species to the rescaled fluctuations of species." We start from the nonlinear master equation and species' corresponding joint probability distribution (equation A3 in supplementary materials of [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references)). After approximation, we end at the **linear Fokker-Planck equation** about the joint probability distributions of the fluctuations $$\displaystyle\frac{\partial\Pi(\xi,t)}{\partial t}=-\sum_{ik}A_{ik}\frac{\partial}{\partial \xi_i}\xi_k\Pi(\xi)+\frac{1}{2}\sum_{ik}[BB^T]_{ik}\frac{\partial^2\Pi(\xi)}{\partial\xi_i\partial\xi_k}$$ (equation A9 in supplementary materials of [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references)). 

**P.S.** An alternative perspective of **LNA** can be found in Section A.3 of the Supplemental Information in [15](https://shi200005.github.io/2023/06/07/Network-Jump/#references), which is $$R_i^+(x)\approx R_i^+(\langle x\rangle)+\nabla R_i^+(\langle x\rangle)\cdot(x-\langle x\rangle)$$. Clearly, the physical meaning is expanded **near macroscopic system trajectories** or **stationary solutions** where matrix $$\nabla R_i^+(\langle x\rangle)$$ can be used as the rate matrix as in the linear case.

#### Solution of Linear Fokker-Planck Equation

The stationary solution is equation A11(in supplementary materials of [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references)), **the multidimensional Normal/Gaussian distribution**, and the detailed steps in chapter 6.5 Ornstein-Uhlenbeck Process from [16](https://shi200005.github.io/2023/06/07/Network-Jump/#references). Generally speaking, the **Fourier transform** will be applied to solve this multivariable PDE. First have a taste by my note [Biophysics_Diffusion](https://shi200005.github.io/download_file/Network_Langevin_Lyapunov.pdf) (diffusion equation from [Biophysics](https://shi200005.github.io/2022/12/30/Biophysics/) on the simplest case and see how Fourier transform works).

#### Lyapunov Equation of Linear Fokker-Planck Equation

From $$\displaystyle\frac{\partial\Pi(\xi,t)}{\partial t}=-\sum_{ik}A_{ik}\frac{\partial}{\partial \xi_i}\xi_k\Pi(\xi)+\frac{1}{2}\sum_{ik}[BB^T]_{ik}\frac{\partial^2\Pi(\xi)}{\partial\xi_i\partial\xi_k}$$, multiply by $$\xi_j\xi_l$$ and integrate over the whole phase space, and we will get the Lyapunov equation $$\displaystyle\frac{\partial \Xi(\xi,t)}{\partial t}=A\Xi+\Xi A+BB^T$$, where the covariance matrix $$\Xi=\langle \xi\xi^T\rangle$$ is the covariance matrix of rescaled fluctuations. In stationary, $$0=A\Xi+\Xi A+BB^T$$

The hint is from VIII.6 [2](https://shi200005.github.io/2023/06/07/Network-Jump/#references).

![Network_Jump_2var_Linear](\images\blog\Network_Jump_Lyapunov.jpg)

#### Example of Nonlinear Case

Check "Example 3: Coupled fluctuations in a two-component system" in supplementary materials of [13](https://shi200005.github.io/2023/06/07/Network-Jump/#references).

Using the Lyapunov equation to compute the variance and covariance of species is frequently employed in the research of A. Hilfinger, J. Paulsson, J. Elf, etc. You can read [9](https://shi200005.github.io/2023/06/07/Network-Jump/#references), the famous paper by J. Paulsson where the Lyapunov equation is presented intuitively (and my post derived Equation (S4) rigorously). 

### Master Equation, Fokker-Planck Approximation, and Langevin Approach

We describe the stochastic process by the master equation $$\displaystyle\frac{\partial P(y,t)}{\partial t}=\int\{W(y\vert y^\prime P(y^\prime,t)-W(y^\prime \vert y) P(y,t)\}$$, corresponding to a stationary joint statistical properties (mean, variances, covariances...). However, it is impossible to solve the statistical properties directly from the master equation unless the transition rates are linear.

To solve it approximately, the Fokker-Planck equation is based on the assumption that the jumps are relatively very small. N. G. van Kampen's $$\Omega$$ expansion is a formal method when the system is large (jumps are relatively small). Intuitively, we get a solvable linear Fokker-Planck from the expansion. The Langevin approach is mathematically equivalent to the linear Fokker-Planck equation (the former is a continuous system). I derived the Lyapunov equation from the Langevin approach in the linear case. To read more, check chapters V. VII. and VIII. from [2](https://shi200005.github.io/2023/06/07/Network-Jump/#references).

## Wrap up

I sincerely thank **everyone** in my group, especially B Kell and A. Hilfinger. You can regard this post as my first-year progress in theory, although it should not have taken that long.... I feel like I'm just crossing the critical point. I completed a phase transition of "being defeated by the equations from the beginning of papers" to "understand the basic math and have a better sense of deriving statistical properties."

## References

[1] Elowitz, Michael B., Arnold J. Levine, Eric D. Siggia, and Peter S. Swain. “Stochastic Gene Expression in a Single Cell.” *Science* 297, no. 5584 (August 16, 2002): 1183–86. [online](https://doi.org/10.1126/science.1070919).

[2] Van Kampen, Nicolaas Godfried. *Stochastic processes in physics and chemistry*. Vol. 1. Elsevier, 1992.

[3] Thattai, Mukund, and Alexander Van Oudenaarden. "Intrinsic noise in gene regulatory networks." *Proceedings of the National Academy of Sciences* 98.15 (2001): 8614-8619. [online](https://www.pnas.org/doi/full/10.1073/pnas.151588598)

[4] Paulsson, Johan. "Models of stochastic gene expression." *Physics of life reviews* 2.2 (2005): 157-175. [online](https://scholar.google.ca/scholar?q=Models+of+stochastic+gene+expression&hl=en&as_sdt=0&as_vis=1&oi=scholart#d=gs_cit&t=1686243281386&u=%2Fscholar%3Fq%3Dinfo%3AgTxTbE6bWKAJ%3Ascholar.google.com%2F%26output%3Dcite%26scirp%3D0%26hl%3Den)

[5] I. Lestas, J. Paulsson, N. E. Ross and G. Vinnicombe, "Noise in Gene Regulatory Networks," in *IEEE Transactions on Automatic Control*, vol. 53, no. Special Issue, pp. 189-200, Jan. 2008, doi: 10.1109/TAC.2007.911347. [online](https://ieeexplore.ieee.org/document/4439816)

[6] Lyapunov equation. (2023, February 7). In [*Wikipedia*](https://en.wikipedia.org/wiki/Lyapunov_equation).

[7] Koch, A L, and H R Levy. “Protein turnover in growing cultures of Escherichia coli.” *The Journal of biological chemistry* vol. 217,2 (1955): 947-57.

[8] Hilfinger, Andreas, and Johan Paulsson. "Separating intrinsic from extrinsic fluctuations in dynamic biological systems." *Proceedings of the National Academy of Sciences* 108.29 (2011): 12167-12172. [online](https://www.pnas.org/doi/abs/10.1073/pnas.1018832108)

[9] Paulsson, J. Summing up the noise in gene networks. *Nature* **427**, 415–418 (2004). [online](https://doi.org/10.1038/nature02257)

[10] Fan, Raymond, and Andreas Hilfinger. "The effect of microRNA on protein variability and gene expression fidelity." *Biophysical Journal* 122.5 (2023): 905-923. [online](https://www.sciencedirect.com/science/article/pii/S0006349523000437)

[11] Pedraza, J. M., & Paulsson, J. (2008). Effects of molecular memory and bursting on fluctuations in gene expression. *Science*, *319*(5861), 339-343.

[12] Keizer, Joel. *Statistical thermodynamics of nonequilibrium processes*. Springer Science & Business Media, 2012.

[13] Elf, J., & Ehrenberg, M. (2003). Fast evaluation of fluctuations in  biochemical networks with the linear noise approximation. *Genome research*, *13*(11), 2475-2484. [online](https://genome.cshlp.org/content/13/11/2475.short)

[14] Huh, D., Paulsson, J. Non-genetic heterogeneity from stochastic partitioning at cell division. *Nat Genet* **43**, 95–100 (2011). [online](https://doi.org/10.1038/ng.729)

[15] Hilfinger, A., Norman, T. M., Vinnicombe, G., & Paulsson, J. (2016). Constraints on fluctuations in sparsely characterized biological  systems. *Physical review letters*, *116*(5), 058101. [online](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.058101)

[16] Risken, H., and T. K. Caugheyz. "The fokker-planck equation: Methods of solution and application." (1991): 860-860.


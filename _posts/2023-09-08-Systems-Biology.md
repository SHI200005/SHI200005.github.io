---
layout: post
title: (En) Systems Biology
categories: BS-NJU-Course-Review-Other
description: 
keywords: 
mhchem: true
---

I love this course offered by Prof Xiao-Peng Zhang the Kuang Ya Ming Honors School at NJU. The course were delivered in Chinese but all the lecture slides are in English. I also finished my course thesis in English. This great course leaded us to understand research papers in this field by teaching us crucial math involved.

After taking this course, I got extremely interested in systems biology and chose to write my [undergraduate thesis](https://github.com/SHI200005/UndergradThesis_Excitability) on systems biology. My thesis supervisor asked me to read B. Ingalls' **Mathematical Modeling in Systems Biology**, which is a helpful reference. This post include both materials from the textbook and my notes for my undergrad thesis.

I will also include some points when I continued studying systems biology for my undergrad thesis. There will be a **Nonlinear Physics** part, which was moved to [(En) Nonlinear Dynamics](https://shi200005.github.io/2023/09/07/Nonlinear-Dynamics/).

| 课程名                       | 系统生物学导论                                                               |
| 学习时间                   | 大三下                                                                               |
| 周课时                       | 2                                                                                        |
| 本人成绩                   | 95                                                                                      |
| 课程教材                   | 无                                                                                       |
| 建议参考教材           | **B. Ingalls, Mathematical Modeling in Systems Biology**   |
| 先修课程                   | 微积分 线性代数 概率论 计算物理导论                         |

## References

1. Ingalls, B. P. (2013). *Mathematical modeling in systems biology: an introduction*. MIT press.
1. Strogatz, S. H. (2018). *Nonlinear dynamics and chaos with student solutions manual: With applications to physics, biology, chemistry, and engineering*. CRC press.

## Modeling of Chemical Reaction Networks

Assumption: reactions are approximately **irreversible** (not exactly true according to thermodynamics (refer to [大学化学](https://shi200005.github.io/2023/02/10/General-Chemistry/#%E5%8C%96%E5%AD%A6%E5%B9%B3%E8%A1%A1%E6%9D%A1%E4%BB%B6))). If all reactions are regarded irreversible, when the closed reaction network reaches equilibrium, "nothing happens anymore". However, biological systems usually have open networks far from thermodynamics equilibrium, and we study their dynamics, such as dynamic equilibrium properties and robustness.  

### The Law of Mass Action

(Ingalls 2.1.3) **The rate of a chemical reaction is proportional to the product of the concentrations of the reactions**, coming from the probability of collisions. 

- For the physics basis of rate constants based on probability of collisions, check the link of my review below.

- How does the second order rate come from approximation of exact collision scenario? Check [Nonlinear Rates and Fluctuations](https://shi200005.github.io/2023/05/15/Gillespie-Fluctuations/#nonlinear-rates-and-fluctuations).

Assumptions: 1. spatial homogeneity; 2. continuously varying concentrations.

The dynamics leads to ODEs of continuous concentration of molecular species, e.g. $\overset{k_0}\rightarrow A \overset{k_1}\rightarrow{}$ leads to $\frac{d}{dt}a(t)=k_0-k_1a(t)$.

### Model Reduction Assumptions

#### The Rapid Equilibrium Assumption

The above are all elementary reactions. If reactions have distinct timescale, we can reduce our network by approximation.

(Ingalls 2.2.1) **If we choose to neglect the fast timescale, we can make use of the fact that the equilibrium is maintained to relate the two concentrations**. It addresses individual reaction processes.

e.g. $\ce{A<=>[k_1][k_{-1}]B->[k_2]}$ given that $k_1+k_{-1}\gg k_2$, equilibrium condition gives $\tilde b(t)=\tilde a(t)\frac{k_1}{k_{-1}}$... set $\tilde c(t)=\tilde a(t)+\tilde b(t)$ reduced to $\ce{C->[\frac{k_2k_1}{k_{-1}k_1}]}$. 

Will exhibit a persistent error if the system relaxes to dynamic steady state but out of equilibrium, e.g. $\ce{->[k_0]A<=>[k_1][k_{-1}]B->[k_2]}$.

#### The Quasi-Steady-State Assumption (QSSA)

(Ingalls 2.2.2) e.g., $\ce{->[k_0]A<=>[k_1][k_{-1}]B->[k_2]}$ given that $k_1+k_{-1}\gg k_2$, assume species $A$ comes rapidly to its steady-state concentration, introduce the quasi-steady state $a^{qss}(t)$ satisfies $0=k_0+k_{-1}b(t)-k_1a^{qss}(t)$, more complex but leads to better approximations over long times. 

- As far as I know, the QSSA assumption is what I always come across in systems biology literature, instead of the rapid equilibrium assumption.
- Note that setting the left hand side $\frac{da(t)}{dt}=0$ and substitute the right hand side with $a^{qss}(t)$ doesn't mean $\frac{da^{qss}(t)}{dt}=0$. Other time-varying variables like $b(t)$ change with time and thus $a^{qss}(t)$ changes with time. The approximation is that $a^{qss}(t)$ keep up with the corresponding stationary value of other values at every time point $t$.

## Biochemical Kinetics

**Elementary reactions**, using separation of timescale methods.

### Michaelis-Menten Kinetics

(Ingalls 3.1.1)

$$\ce{S + E<=>C_1<=>C_2<=>P +E }$$

Assumptions: 1. $\ce{C_1<=>C_2}$ is fast compared to the association and dissociation events; 2. $P$ never binds free enzyme, which lead to 

$\ce{S + E<=>[k_1][k_{-1}]C->[k_2]P + E}$.

Assumption: For many reactions in the cell, the substract is far more abundant than the enzyme, then complex $C$ is considered in **quasi-steady state**.

Result: $\text{Rate of S → P}=\frac{k_2k_1e_Ts}{k_{-1}+k_2+k_1s}=\frac{V_{max}s}{K_M+s}$, where $$e_T$$ denote the total enzyme concentration, $$s$$ denote the substrate concentration, $V_{max}=k_2e_T$ is the limiting (or maximal) rate, $K_M=(k_{-1}+k_2)/k_1$ is the Michaelis (or half-saturating) constant.

![Sys_Bio_Michaelis_Menten](\images\blog\Sys_Bio_Michaelis_Menten.JPG)

Figure from Ingalls' book. There is a first order and a zero-order regime. **When deciding the reaction rate in our biological network, how can we decide the rate functions? We need to consider the regime the reactions happens.**

#### Regulation of Enzyme Activity

(Ingalls 3.2)

**Competitive Inhibition**


$$
\ce{S + E<=>[k_1][k_{-1}]C->[k_2]E + P} 
\\ \ce{I + E<=>[k_3][k_{-3}]C_I}
$$


$\text{Rate of S → P}=\frac{V_{max}s}{K_M(1+i/K_i)+s}$ , where $K_i=k_{-3}/k_3$.

**Allosteric Regulation**

Check Ingalls' book for an excellent explanation. 


$$
\ce{S + E<=>[k_1][k_{-1}]C->[k_2]E + P} \\ 
\ce{I + E<=>[k_3][k_{-3}]EI} \\
\ce{I + ES<=>[k_3][k_{-3}]ESI} \\
\ce{S + EI<=>[k_1][k_{-1}]ESI}.
$$


$\text{Rate of S → P}=\frac{V_{max}s}{(1+i/K_i)(K_M+s)}$ , where $K_i=k_{-3}/k_3$.

**Cooperativity**

To describe potentially independent binding events that have a significant influence on one another, leading to **nonlinear** behaviors. Famous example: the binding of oxygen to the protein *hemoglobin*.

For the binding sites are identical but cooperative effects occur between them,


$$
\ce{P + X<=>[4k_1][k_{-1}]PX_1} \\ 
\ce{PX_1 + X<=>[3k_2][2k_{-2}]PX_2} \\
\ce{PX_2 + X<=>[2k_3][3k_{-3}]PX_3} \\
\ce{PX_3 + X<=>[k_4][4k_{-4}]PX_4}.
$$

(For instance, there are four sites available for the first ligand to bind, so the overall reaction rate is $4k_1$ . There are only three sites available for the second ligand to bind, so the rate is $3k_2$.) When the binding events are in equilibrium, write down the fractional saturation...

##### Hill Function

If the final binding event has a much higher affinity than the earlier binding events (i.e., $K_4\ll K_1,K_2,K_3,K_4$), then the fractional saturation can be approximated by $Y=\frac{[X]^4/(K_1K_2K_3K_4)}{1+[X]^4/(K_1K_2K_3K_4)}$, formalized in the **Hill function** $Y=\frac{[X]^n}{K^n+[X]^n}$.

## Gene Regulatory Networks

(Ingalls 7) **A set of genes whose protein products regulate one another's expression rates is refereed to as a *gene regulatory network*.** Now we will consider coarse-grained model, which compresses a bunch of elementary reactions together onto a "transcription and translation" level.

The **stochastic model** of unregulated gene expression in Ingalls' 7.1.1 was analyzed in [this post](https://shi200005.github.io/2023/06/07/Network-Jump/#the-classical-model-of-mrna-and-protein). It is an easy linear model so the continuous approximated version is more easy...

(Ingalls 7.1.2) *The majority of gene regulation occurs through control of the initiation of transcription*. Transcription factors bind on DNA (*promotor region* in prokaryotes), as *activator* when it activate RNA polymerase binding and then activate protein production, as *repressor* otherwise.

Approximation: *the association-dissociation event occurs on a much faster timescale than gene expression, so it can be treated in equilibrium when modeling gene expression*.

(Ingalls Eqn(7.7)) When the $$N$$ transcription factors bind with strong cooperativity, promoter occupancy can be written as $\frac{[P]^N}{K^N+[P]^N}$, where $K$ is the half-saturating concentration. The fraction calculation is similar to michaelis-menten kinetics model above, and **nonlinear** rates emerged from strong **cooperativity**. In short, in the **activator** case, the rate of transcription is "proportional to the bounded fraction + leak"; in the **repressor** case, that is "proportional to the unbounded fraction + leak". 

If nonlinear, there might be multiple fixed points in the system. For fixed point analysis, see below, **nonlinear physics**. Then, we will get back to interesting network behaviors!

## Nonlinear Dynamics

For details, check [(En) Nonlinear Dynamics](https://shi200005.github.io/2023/09/07/Nonlinear-Dynamics/).

Example: bistable network (cooperative inhibition with balanced inhibition strength) in Ingalls' Model (4.2), the phase portrait as Figure 4.8 (B). In this example, the eigenvalues of the Jacobian at three fixed points are all real numbers.

As the figure I put in the "similarity matrix" part of the post [线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/#%E7%9B%B8%E4%BC%BC%E7%9F%A9%E9%98%B5),

![Linear_Algebra_Similar](\images\blog\Linear_Algebra_Similar.jpg)

Can you get the intuition of what eigenvalues mean in this bistable system? :kissing_heart:

![Sys_Bio_Bistable](\images\blog\Sys_Bio_Bistable.jpg)

In this figure, $A$ and $C$ are stable nodes, and $B$ is a saddle. For a specific fixed point, the Jacobian describes how the trajectory evolves (the Jacobian as a transformation of the displacement). If diagonalize the Jacobian, the basis transformation matrix describes a new coordinate that the direction of eigenvalues falls on the basis. Starting from the direction with negative eigenvalue of the saddle $B$'s Jacobian, a curve can be sketched that separates the "destination" of the system - for initial state on the upper left of that curve, the system will converge to $A$; for initial state on the lower right of that curve, the system will converge to $C$.

For an example of eigenvalues with imaginary part, check my [undergraduate thesis](https://github.com/SHI200005/UndergradThesis_Excitability).

## Noisy Models

### Noise from a noisy signal

### Noise from the Stochastic Nature of Chemical Reactions

Fine.

---
layout: post
title: (En) hilfinger2011separating
categories: Supp-of-Supp
description: 
keywords: 
mhchem: true
---

I started an interesting new category - supplementary mathematics of supplementary information of selected papers, abbr. as "Supp-of-Supp". I am writing down page-after-page detailed but non-trivial mathematical derivations for the non-intuitive equation that suddenly appears and kills me when reading the papers, which are closely related to my research topics and similar crucial mathematical skills.

I always receive blame, saying that I emphasize too much on details. I argue that details are important for "rigorous success". I only emphasize crucial details while being clear enough about the whole picture. Of course, this is my personal opinion. I might be wrong...

## Supplemental Mathematics

The paper is [1](https://shi200005.github.io/2023/10/02/hilfinger2011separating/#references).

For convenience, for the bracket of averaging, I add the subscript to denote whether it is the (time-dependent) ensemble average, $\langle ...\rangle_e$, or the average over all histories (of a time-dependent ensemble average), $\langle ...\rangle_{\vec Z[0,t]}$. 

For ergodic and non-diverging systems, $\langle\langle\vec  X_t\vert \vec Z[0,t]\rangle_e\rangle_{\vec Z[0,t]}=\langle \vec x\rangle$ (we denote the average without subscripts).

The linear two-stage stochastic model (usually taken as mRNA-protein model),


$$
\ce{z ->[\lambda_z] z + 1} \quad \ce{x ->[\lambda_x] x + 1}\\
\ce{z ->[\beta_zz] z - 1} \quad \ce{x ->[\beta_xx] x - 1}
$$


detailed steps of derivations, please refer to the handwritten [note](https://shi200005.github.io/download_file/Hil11Sep_Supp.pdf), which covers

-  The conditional mean $\langle x\vert z\rangle$; variance of the conditional average of $X$ given $Z$, $\sigma^2_{\langle x\vert z\rangle}$;
- the variance of $X_t$ in a group of cells sharing an environmental history $\vec Z[0,t]$ averaged over all possible histories $\langle\sigma^2_{X_t\vert\vec Z[0,t]}\rangle$.

The derivations of results noted as [2](https://shi200005.github.io/2023/10/02/hilfinger2011separating/#references) can be found in another post.

Also a quick note on the part **Modeling intrinsic noise - multiplicative environments**. 

- When step size = 1
  
  
  $$
  \ce{x ->[\lambda(z)] x + 1} \\
  \ce{x ->[\beta(z)x] x - 1}
  $$
  
  
  For this system, as the supplemental material shows, fortunately, we have $\langle\sigma^2_{X_t\vert\vec Z[0,t]}\rangle=\langle\langle\vec  X_t\vert \vec Z[0,t]\rangle_e\rangle_{\vec Z[0,t]}$.

The black-square term $\frac{b+1}{2}\frac{1}{\langle x\rangle}$ comes from assuming static environment (no correlations between the environment and the variable).

- the flux balance (first-order property) $0=b\langle\lambda(\vec z)\rangle-\langle\beta(\vec z)\rangle\langle x\rangle$ and 
- the Lyapunov equation $0=b^2\langle\lambda(\vec z)\rangle+\langle\beta(\vec z)\rangle\langle x\rangle-2\langle\beta(\vec z)\rangle\sigma^{2}_{xx,\text{black -squares}}$.

## Brief summary

**Can each noise term be compared to models that account only for either intrinsic or extrinsic mechanisms rather than the whole complex system that is subject to both types of noise?**

In a stochastic system with species abundances vector $\vec x$ and stochastic environmental influences $\vec z$. The rate of reaction $k$ is denoted as $r_k(\vec x,\vec z)$, where actually $\vec x$ and $\vec z$ are time variables. The jump processes are $\ce{\vec{x}->[r_k(\vec{x},\vec{z})]\vec{x}+\vec{s}_k}$.

Note that the environment is dynamic, when using the law of total variances to decompose noise, decomposing according to the **current environment** state **underestimates the extrinsic noise** and **exaggerates the intrinsic noise**, showed by the linear two-stage model. That is because the current $x$ is not at the stationary value of current $z$. It needs time to catch up! The noise should be decomposed, not according to the current state of the environment, but **the full history of the environment**.

- When the **extrinsic** noise of the full system thus indeed equals the noise of the intrinsically deterministic system subjected to the fluctuating environment:

  If the total fluxes follow $\hat R(\vec x,\vec z)=\vec a(\vec z)+\hat J(\vec z)\vec x$ (**linear in intrinsic variables**), denote $\vec{\bar x}(t)=\langle\vec  X_t\vert \vec Z[0,t]\rangle_e$, then we have $\frac{d }{dt}\vec{\bar x}(t)=\displaystyle\sum_k\vec s_k r_k(\vec{\bar x})$. 

  Since the covariance of the **dual-reporter** satisfies $\text{Cov}(X,Y)=\langle(\bar x(t))^2\rangle_{\vec Z\vert[0,t]}-\langle\bar x(t)\rangle_{\vec Z\vert[0,t]}^2=\sigma_{ext}^2$, then the extrinsic noise from the dual-reporter method can be rigorously analyzed using models that ignore intrinsic stochasticity. Note that there is a type in the last line of Eq.[8] in the paper!

- When the **intrinsic** noise can be rigorously analyzed using models that ignore extrinsic stochasticity: 

  although under some special cases it might hold, but generally it holds when the Jacobian matrix $\hat J(\vec z)$ is independent of $\vec z$ ($J_{ij}=\displaystyle\sum_k s_{ki}\frac{dr_k}{dx_j}$), which was called "**additive noise**" model. 

  For the **Lyapunov equation** $\frac{d\hat c}{dt}=\hat J\hat C+(\hat J\hat C)^T+\hat B$, where the covariance matrix $C_{ij}=\langle X_{i,t}X_{j,t}\vert \vec Z[0,t]\rangle-\langle X_{i,t}\vert \vec Z[0,t]\rangle\langle X_{j,t}\vert \vec Z[0,t]\rangle$ and the diffusion matrix $B_{ij}=\displaystyle\sum_k r_k(\langle \vec X_t\vert \vec Z[0,t]\rangle,\vec z(t))s_{ki}s_{kj}$. Taking infinitely long time integral, we get $0=\hat J\langle\hat C\rangle+(\hat J\langle \hat C\rangle)^T+\langle\hat B\rangle$. Thus, $\sigma_{int}^2=\langle\hat C_{nn}\rangle$ (*this hold when the probability of a state is always a continuous time variable*, and my on-going research focus on segregation models).

  Even if the species is driven by a periodically varying signal, for example
  
  
  $$
  \ce{x ->[A(sin(\omega t) + 1)] x + 1}\\
  \ce{x ->[\beta x] x - 1}
  $$
  
  
  the intrinsic noise is equivalent to 
  
  
  $$
  \ce{y ->[A] y + 1}\\
  \ce{y->[\beta y] y - 1}
  $$
  
  
  where $\langle x\rangle=\langle y\rangle$.

## References

[1] Hilfinger, A., & Paulsson, J. (2011). Separating intrinsic from extrinsic fluctuations in dynamic biological systems. *Proceedings of the National Academy of Sciences*, *108*(29), 12167-12172. [online](https://www.pnas.org/doi/abs/10.1073/pnas.1018832108)

[2] My random post. [Gene Regulatory Networks Described by Jump Process and Fluctuation Dissipation Theorem](https://shi200005.github.io/2023/06/07/Network-Jump/).

## Acknowledgement

Prof Andreas Hilfinger told me some secrets. Thank him very much.

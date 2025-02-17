---
layout: post
title: (En) Biophysics
categories: PhD-UT-Course-Review
description: 
keywords: Biophysics
mathjax: true
---

This post covers several topics from PHY2707 and PHY2709 of UofT grad course. I will update whenever I need to teach or review the related materials. I also included something I learned as an undergrad but I believe they're too difficult for undergrads...

## References

1. Bialek, William. *Biophysics: searching for principles*. Princeton University Press, 2012.

## Vision

### Human eye photoreceptor cells are single-photon detectors

Reference: Hecht S, Shlaer S, Pirenne MH. ENERGY, QUANTA, AND VISION. *J Gen Physiol*. 1942;25(6):819-840. doi:10.1085/jgp.25.6.819

Question: What is the lower limit of the number of photons that enables human vision? Method: Use a very dim light source to shake it and see if the person being tested says it can be seen. Fact: There is no way to control the number of photons emitted each time (it is a random variable). Because 1. The light source is dim enough, and the emitted photons come from a sparse sampling of a certain process (for related theories, see [Probability Theory](https://shi200005.github.io/2021/10/02/Probability/)), 2. In [Quantum Mechanics](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/), this process is actually a Poisson process. It can be considered that the random variable "number of photons emitted" conforms to the **Poisson distribution**.

If $$k$$ is the lower limit of the number of photons that can be seen, and the flash intensity is $$I$$, because each subject’s eye parameters are different, the ratio of photons reaching the retina is $$\alpha$$, then in the test , the probability that the subject sees the light can be expressed by

$$\displaystyle P_\text{see}(I)=\sum_{n=k}^{\infty}P(n\vert M=\alpha I)=e^{-\alpha I}\sum_{n=k}^{\infty}\frac{(\alpha I)^n}{n!}$$

where $$\alpha$$ is unknown, but $$k$$ gives the shape of $$P_\text{see}(I)$$, $$\alpha$$ is just stretched on the $$M$$ axis, $$\alpha$$ requires curve fitting measured by a single person (varies from person to person). The figure below shows the test results published by Hecht, Shlaer, and Pirenne in 1942. It can be seen that the fit is quite good (William Bialek, Biophysics, 2.1).

![](/images/blog/Biophysics_Vision.jpg)

Note: The success of the experiment is that we first fit the $$\alpha$$ parameters of different testers, and then find the corresponding photon number threshold $$k$$ for each person. For the ensemble of the crowd, find Average of $$k$$. But if we first average the curves of three people, then fit an overall $$\alpha$$, and then get the overall $$k$$ value, I am afraid there will be no good results. In fact, this shows us finding what is reproducible can be difficult, and averaging across an ensemble of individuals can be qualitatively misleading.（William Bialek, Biophysics, 2.1）

---

The following will be rewrite...





















The following mainly comes from Bialek.

### Encoding Strategy

I read it but am too lazy to write

- How to encode information about a probability distribution using binary numbers (how many binary digits are used)?

- Kullback-Leibler divergence $$D_{KL}(\bold{p\vert\vert\bold{q})=\displaystyle\sum_n}p_slog_2(\frac{p_s}{q_s})$$    

  Describes the deviation between the probability distribution we guessed and the actual probability distribution. If we guess the probability distribution wrong, we need more space to encode a piece of data. This physical quantity quantifies how much more space we need to spend. 

- Correlations or order reduce the capacity to transmit information. 

The relationship with [Thermodynamics](https://shi200005.github.io/2021/10/11/Thermodynamics/): $$dS=\frac{\bar dQ}{T}$$, which describes the heat absorption caused by entropy change. Similarly, The entropy of a probability distribution also measures the amount of space needed to write down a description of the (microscopic) states drawn out of that distribution.

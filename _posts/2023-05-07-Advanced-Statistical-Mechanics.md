---
layout: post
title: (En) Advanced Statistical Mechanics
categories: PhD-UT-Course-Review
description: 
keywords: Advanced Statistical Mechanics
mathjax: true
---

.

版本 2023/09/08 Ver0.1

## References

1. Kardar, Mehran. *Statistical physics of particles*. Cambridge University Press, 2007.

## Essential Math

### Probability - Multi-var

In Kardar (particle) 2.4, **Many random variables**, everything is so clear that I don't want to elaborate. For *the joint Gaussian distribution*, the *Wick's theorem* is important in the course.

Recall what we've learnt from 2.2 **One random variable** (also in [概率论](https://shi200005.github.io/2021/10/02/Probability/)), and *Symmetric matrices diagonalization by unitary matrices* in [线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/).

### d-Dimensional Space Gaussian Integrals

In Kardar (particle) 4.4. In Calculus ([微积分](https://shi200005.github.io/2021/09/30/Calculus/)), we've learnt $$I_d≡(\displaystyle\int_{-\infty}^{\infty}dxe^{-x^2})^d=\pi^{d/2}$$ by changing coordinates. We can also "drag a surface out", as $$I_d=\displaystyle\int_0^{\infty}dRS_dR^{d-1}e^{-R^2}=\frac{S_d}{2}(d/2-1)!$$. Then we get $$S_d=\frac{2\pi^{d/2}}{(d/2-1)!}$$.
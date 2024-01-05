---
layout: post
title: (En-Zh) Nonlinear Dynamics
categories: BS-NJU-Course-Review-Others
description: 
keywords: 
mhchem: true
---

...

<span style="font-size: 25px;">(En) Part I: Basic</span>

## References

1. Ingalls, B. P. (2013). *Mathematical modeling in systems biology: an introduction*. MIT press.
1. Strogatz, S. H. (2018). *Nonlinear dynamics and chaos with student solutions manual: With applications to physics, biology, chemistry, and engineering*. CRC press.

## Stability of Fixed Points

For this part, I mainly talk on nonlinear gene networks. Check [(En) Systems Biology](https://shi200005.github.io/2023/09/08/Systems-Biology/) for the context and examples.

Take a nonlinear network of species interaction with each other, the dynamics of the system consists of species are described as **a system of ODEs**. How to mathematically solve (or describe) them? For this part, check Strogatz's book (ref 2).

### One-Dimensional Case

$\frac{dx(t)}{dt}=f(x(t))$ is an ODE. How to solve it is described in [微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B). As we can see, we can only solve some very specific ODEs analytically. If we can't solve analytically, it is helpful to sketch **the trend of the evolution** without a lot of detail.

If the solution of $\frac{dx(t)}{dt}=0$ is $x=x_i$ (if nonlinear, there can be multiple solutions, and we call them **fixed points**), then $$x=x_i$$ might be a candidate that finally the system will rest at this point. Will this happen?

We focus on the local part near the fixed points. Place your state near a fixed point, will it go to the fixed point or diverge further away? And then, can we sketch the how phase plane by this?

> (Ingalls' 4.2) The long-time (i.e., asymptotic) behavior of biochemical and genetic networks will be either
>
> - convergence to a steady state; or
> - convergence to a sustained periodic oscillation, referred to as limit-cycle oscillation. (Shi's comment: sorry for the messy structure but this only works for multi-dimensional case)

Other dynamic behaviors (divergence and chaos, for example) do not often occur in systems biology models.

Keep only the first-order term, we have $\frac{dx(t)}{dt}\vert_{x=x_i}=f'(x_i)(x(t)-x_i)$. As the (Example 2.2.1) shown in Strogatz's book ($f(x)=x^2-1$), the **stability of fixed points** are determined by the symbols of $f(x_i)$. If negative, go to the fixed point (stable); if positive, diverge away (unstable). More tricky case that $f(x_i)=0$, see Strogatz's book, not this post.

![Sys_Bio_Nonlinear_1D](\images\blog\Sys_Bio_Nonlinear_1D.JPG)

### Multi-dimensional Case

For the example, check Ingalls' model (4.2). For a general expression, $\mathbf{x(t)}=(x_1(t),...,x_n(t))^{T}$ is an $$n\times 1$$ vector, and $\mathbf{f}(\mathbf x(t))=(f_1(x_1(t)),...,f_n(x_n(t))^T$ is an $n\times 1$ vector, the system of ODEs is therefore $\frac{d}{dt}\mathbf{x}(t)=\mathbf{f}(\mathbf x(t))$. Fixed points are $\mathbf x_i$. Consider the local properties near the fixed points, only keep the first-order terms, we have $\frac{d}{dt}\mathbf{x}(t)\vert_{\mathbf x=\mathbf x_i}=\mathbf{J}(\mathbf x_i)\cdot (\mathbf x(t)-\mathbf x_i)$, where $J_{mn}(\mathbf x_i)=[\frac{\partial f_m(\mathbf x)}{\partial x_n}]\vert_{\mathbf x=\mathbf x_i}$ is the **Jacobian matrix**.

As in 1D case, the stability is determined by the symbols of the first derivatives of $f(x)$ at the fixed points, what criteria we use in the multi-dimensional case? The **eigenvalues** of the Jacobian matrix at the fixed points!

Read Ingalls' 4.2 for the great mathematical explanation. To summarize,

> **Linearized Stability Criterion**
>
> - If both eigenvalues of the Jacobian have negative real part, then the state is stable.
> - If *either* eigenvalue has positive real part, then the steady state is *unstable*.
>

... not addressed the case of eigenvalues with zero real part ... rarely encountered...

## Bifurcation

Check Strogatz's related sections.

If we change the value of a parameter (parameters) in ODEs, the structure of the flow diagram can change. The number and the stability of fixed points can change. **Qualitative** changes in the dynamics are called **bifurcations**.

Example: Saddle-node bifurcation, transcritical bifurcation and pitchfork bifurcation, hopf bifurcation...



<span style="font-size: 25px;">(Zh) Part II: Intermediate</span>

## References

1. 梁昆淼，高等教育出版社《理论力学（第四版）》，第十章。

线性 $f$：$f(ax_1+bx_2)=af(x_1)+bf(x_2)$。

> 物理学中的叠加原理是系统具有线性性质的体现。在该情况下，系统的整体性质可以由组成该系统的所有子系统的性质叠加尔得到，这也表明各子系统之间是没有相互作用的，或者这种相互作用对所讨论的性质而言是可以忽略不计的。

## 微扰法

用小参数展开进行主机近似的方法。

逐级近似—— e.g., 非线性振动的求解。求越来越高阶的振动方程，每次求解的时候舍弃更高阶小量，然后逐级求解。

参数共振—— e.g., 秋千越荡越高。共振不是通过驱动力实现的，而是通过参数的变化而实现的。参数共振与受迫振动的不同。

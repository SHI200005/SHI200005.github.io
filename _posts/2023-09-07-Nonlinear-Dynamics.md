---
layout: post
title: (En) Nonlinear Dynamics
categories: BS-NJU-Course-Review-Other
description: 
keywords: 
mhchem: true
---

...

## References

1. Ingalls, B. P. (2013). *Mathematical modeling in systems biology: an introduction*. MIT press.
1. Strogatz, S. H. (2018). *Nonlinear dynamics and chaos with student solutions manual: With applications to physics, biology, chemistry, and engineering*. CRC press.

## Stability of Fixed Points

For this part, I mainly talk about nonlinear gene networks. Check [(En) Systems Biology](https://shi200005.github.io/2023/09/08/Systems-Biology/) for the context and examples.

Take a nonlinear network of species interacting; the system's dynamics consists of species described as **a system of ODEs**. How do you mathematically solve (or describe) them? For this part, check Strogatz's book (ref 2).

### One-Dimensional Case

$\displaystyle\frac{dx(t)}{dt}=f(x(t))$ is an ODE. How to solve it is described in [微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B). As we can see, we can only solve some very specific ODEs analytically. If we can't solve the problem analytically, sketching the **evolution trend** without a lot of detail is helpful.

If the solution of $\displaystyle\frac{dx(t)}{dt}=0$ is $x=x_i$ (if nonlinear, there can be multiple solutions, and we call them **fixed points**), then $$x=x_i$$ might be a candidate for the system to finally rest at this point. Will this happen?

We focus on the local part near the fixed points. Place your state near a fixed point. Will it go to the fixed point or diverge further away? And then, can we sketch the how phase plane by this?

> (Ingalls' 4.2) The long-time (i.e., asymptotic) behavior of biochemical and genetic networks will be either
>
> - convergence to a steady state; or
> - convergence to a sustained periodic oscillation, referred to as limit-cycle oscillation. (Shi's comment: sorry for the messy structure but this only works for multi-dimensional case)

Other dynamic behaviors (divergence and chaos, for example) do not often occur in systems biology models.

Keep only the first-order term, and we have $\displaystyle\frac{dx(t)}{dt}\vert_{x=x_i}=f'(x_i)(x(t)-x_i)$. As Example 2.2.1 shows in Strogatz's book ($f(x)=x^2-1$), the **stability of fixed points** is determined by the symbols of $f(x_i)$. If negative, go to the fixed point (stable); if positive, diverge away (unstable). A trickier case that $f(x_i)=0$, see Strogatz's book, not this post.

![Sys_Bio_Nonlinear_1D](\images\blog\Sys_Bio_Nonlinear_1D.JPG)

**No limit cycles** (Bendixson).

### Multi-dimensional Case

For example, check Ingalls' model (4.2). For a general expression, $\mathbf{x(t)}=(x_1(t),...,x_n(t))^{T}$ is an $$n\times 1$$ vector, and $\mathbf{f}(\mathbf x(t))=(f_1(x_1(t)),...,f_n(x_n(t))^T$ is an $n\times 1$ vector, the system of ODEs is therefore $\displaystyle\frac{d}{dt}\mathbf{x}(t)=\mathbf{f}(\mathbf x(t))$. Fixed points are $\mathbf x_i$. Consider the local properties near the fixed points, only keep the first-order terms, and we have $\displaystyle\frac{d}{dt}\mathbf{x}(t)\vert_{\mathbf x=\mathbf x_i}=\mathbf{J}(\mathbf x_i)\cdot (\mathbf x(t)-\mathbf x_i)$, where $\displaystyle J_{mn}(\mathbf x_i)=[\frac{\partial f_m(\mathbf x)}{\partial x_n}]\vert_{\mathbf x=\mathbf x_i}$ is the **Jacobian matrix**.

As in 1-D case, the stability is determined by the symbols of the first derivatives of $f(x)$ at the fixed points, what criteria we use in the multi-dimensional case? The **eigenvalues** of the Jacobian matrix at the fixed points!

Read Ingalls' 4.2 for the great mathematical explanation. To summarize,

> **Linearized Stability Criterion**
>
> - If both eigenvalues of the Jacobian have negative real part, then the state is stable.
> - If *either* eigenvalue has positive real part, then the steady state is *unstable*.
>

... not addressed the case of eigenvalues with zero real part ... rarely encountered...

Limit cylces are possible, e.g., Van der Pol.

### Category of fixed points

- Node: real eigenvalues (no oscillation) with the same sign

  - Stable node: negative eigenvalues

  - Unstable node: posotive eigenvalues.

- Saddle: real eigenvalues (no oscillation) with different signs, not stable

- Spiral: contains conjungate complex eigenvalues (with oscillation, see Ingalls' page 105)

  - spiral sink: all eigenvalues have negative real part 
  - spiral source: with positive real part

## Bifurcation

Check Strogatz's related sections.

If we change the value of a parameter (parameters) in ODEs, the structure of the flow diagram can change. The number and the stability of fixed points can change. **Qualitative** changes in the dynamics are called **bifurcations**.

Example: Saddle-node bifurcation, transcritical bifurcation and pitchfork bifurcation, hopf bifurcation...

---
layout: post
title: (En) Statistical Mechanics (Graduate Level)
categories: Self-Study
description: 
keywords: 
mathjax: true
---

I also self-learnt a lot of probability theory from Kardar's book, which makes what we had to memorized for our second year undergrad course under good intuition and now I don't need to *know* them by memorizing. Check [随机变量的 fancy 数字特征 - 概率论](https://shi200005.github.io/2021/10/07/Probability/#%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E7%9A%84-fancy-%E6%95%B0%E5%AD%97%E7%89%B9%E5%BE%81).

## References

1. Kardar, Mehran. *Statistical physics of particles*. Cambridge University Press, 2007.

## Information and Entropy

The content for this part mainly comes from 2.7 of Kardar (particles) (a lot of direct copy... tell me whether it is appropriate and help me to improve!)

### Information

Consider a random variable with a discrete set of outcomes $$\mathbf{x}=\{x_i\}$$ (you use a language to write a letter and the language contains 5 letters, "a, b, c, d, e"), occurring with probabilities $$\{p(i)\}$$ (in that language, all words start with "a", making "a" the most frequent letter in texts), for $$i=1,...,M$$ ($$M$$ is the size of the alphabet, in the "letter" case, $$M=5$$).

Your message contains $$N$$ letters. There are $$M^N$$ kinds of different letter combinations. Choose the unit as "bits" means $$\ln_2(M^N)$$. The number of bits (**information**) to transmit your text precisely (imaging you are sending via email so the letters are coded in a binary way) is $$N\ln_2M$$ (the bits of two texts should add, and the possibilities of the combined text should multiply, which could be reached in this logarithm way).

However, in the limit of large $$N$$, we expect the message to contain"roughly" $$\{N_i=Np_i\}$$ occurrences for each symbol. The number of typical messages thus corresponds to the number of ways of rearranging the $$\{N_i\}$$ occurrences of $$\{x_i\}$$, and is given by the multinomial coefficient $$g=\frac{N!}{\prod_{i=1}^M N_i!}$$, compared with $$M^N$$ before considering the non-uniform distribution. Using **Stirling's approximation**, we have $$\ln_2g\approx -N\displaystyle\sum_{i=1}^M p_i\ln_2p_i$$.

- It is interesting that statistical physicists use $$\ln_2$$ to indicate $$\log_2$$, while engineers use $$\log x$$ to indicate $$\log_2$$.

- Here, we start from "large $$N$$ gives $$\{N_i=Np_i\}$$"  (introduced in [概率论](https://shi200005.github.io/2022/02/17/Probability/#%E5%A4%A7%E6%95%B0%E5%AE%9A%E7%90%86-1))) and then use Stirling's approximation (introduced in [统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)).  Actually,

  
  $$
  \text{The bound by the extreme value among distribution -> }
  \begin{cases}
  \text{The weak law of large number} \\
  \text{Stirling's approximation}
  \end{cases}
  $$
  

  The above was written before I took [(En) Information Theory](https://shi200005.github.io/2023/10/03/Information-Theory/), where $$H(X)=-\displaystyle\sum_{x}p(x)\log p(x)$$ was derived from three axioms in Shannon's 1948 paper. In Shannon's argument, derivation for uniform distribution over $$n$$ elements, the entropy $$H_U(n)=H_2(n)\log n$$ was determined by a bound, and this sandwich just look like what we did in Stirling's...

### The Entropy of Mixing

Suppose mixing $$M$$ distinct components in the context of statistical mechanics. Consider characterizing the *distribution*, let alone the outcomes from different trials (how many samples taken and the sampling error...).

The *entropy* for *any probability distribution* as $$S=-\displaystyle\sum_{i=1}^Mp(i)lnp(i)=-\langle lnp(i)\rangle$$. 

The above is the entropy for a discrete probability distribution, for that of a continuous distribution, $$S=-\int dxp(x)lnp(x)=-\langle lnp(x)\rangle$$. The problem of scaling remains to be discussed.

## The BBGKY hierarchy

Scan-reading the irreversibility parts from Kardar's book (particles)...

To find out how the probability evolves with time...

In the previous posts, we considered $$N$$-particle ideal gas, with no interacting terms in the Hamiltonian. Now we take **two-body interactions** into account (but not the ignorable higher-body interaction terms), and get the Hamiltonian of the **weakly interacting gas** 

$$\mathcal{H}(\mathbf{p},\mathbf{q})=\displaystyle\sum_{i=1}^N[\frac{\vec{p_i}^2}{2m}+U(\vec{q_i})]+\frac{1}{2}\displaystyle\sum_{(i,j)=1}^N\mathcal{V}(\vec{q_i}-\vec{q_j})$$.

Consider $$f_s(\vec p_1,...,\vec q_s,t)$$ as the expectation value of finding $$S$$ of the $$N$$ particles at point $$(\vec p_1,...,\vec q_s)$$ in the phase space at time $$t$$.

With the help of dividing the Hamiltonian..., after tedious mathematical derivations... (and some more elaborate math can be find here [PHY526_Sussman](https://www.dmsussman.org/assets/teaching/phys526/3_kineticTheory.pdf)), we have the **time evolution of $$f_s$$** as 

$$\frac{\partial f_s}{\partial t}-\{\mathcal{H_s,f_s}\}=\displaystyle\sum_{n=1}^N\int dV_{s+1}\frac{\partial \mathcal{V(\vec{q_n}-\vec{q}_{s+1})}}{\partial \vec{q}_n}·\frac{\partial f_{s+1}}{\partial\vec{p}_n}$$. 

This is the BBGKY hierarchy.

## The Boltzmann Equation

The above BBGKY hierarchy is too complicated to tell us anything. Consider the **time scales** of different terms under **short-range interactions**, cancel something, 

and the final result is a **closed form equation for $$f_1$$**, as equation (3.41) in Kardar's book. I don't bother to write down.

## The H-theorem and irreversibility

If $$f_1(\vec p,\vec q,t)$$ satisfies the Boltzmann equation, then $$d\Eta/dt\leq 0$$, where

$$\Eta(t)=\int d^3\vec pd^3\vec qf_1(\vec p,\vec q,t)lnf_1(\vec p,\vec q,t)$$,

which is related to the **information content of the one-particle PDF** (for information of a distribution, see [Biophysics](https://shi200005.github.io/2022/12/30/Biophysics/)). Proved by plugging in the Boltzmann equation.

Key mathematical step for introducing time irreversibility: check Kardar Eq.(3.40). *The assumption of molecular chaos* (factorizing $$f_2$$ as the product of two $$f_1$$) is applied to the "before collision term", but not the "after collision term", since when out of equilibrium, after collision, the coordinates are likely to be more correlated!

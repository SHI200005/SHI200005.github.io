---
layout: post
title: (En) Information Theory
categories: PhD-UT-Course-Review
description: 
keywords: quantum mechanics
mathjax: true 
---

> The math you get used to and the math you understand are different. You may first get used to some math, and then it may take years to understand. --Prof Frank Kschischang 

This is an informal oral statement from our lectures. I relate to this statement so much that I would like to put it down here.

Symbols: random variables and the alphabet $$X\in\mathcal X$$, probability distribution $$\text{Pr}(X=x)$$, $$p_X(x)$$, $$p(x)$$.

## Information and Entropy

### Information

mainly comes from 2.7 of Kardar (particles) (a lot of direct copy... tell me whether it is appropriate and help me to improve!)

Consider a random variable with a discrete set of outcomes $$\mathbf{x}=\{x_i\}$$ (you use a language to write a letter and the language contains 5 letters, "a, b, c, d, e"), occurring with probabilities $$\{p(i)\}$$ (in that language, all words start with "a", making "a" the most frequent letter in texts), for $$i=1,...,M$$ ($$M$$ is the size of the alphabet, in the "letter" case, $$M=5$$).

Your message contains $$N$$ letters. There are $$M^N$$ kinds of different letter combinations. Choose the unit as "bits" means $$\ln_2(M^N)$$. The number of bits (**information**) to transmit your text precisely (imaging you are sending via email so the letters are coded in a binary way) is $$N\ln_2M$$ (the bits of two texts should be added, and the possibilities of the combined text should multiply, which could be reached in this logarithm way).

However, in the limit of large $$N$$, we expect the message to contain"roughly" $$\{N_i=Np_i\}$$ occurrences for each symbol. The number of **typical** messages thus corresponds to the number of ways of rearranging the $$\{N_i\}$$ occurrences of $$\{x_i\}$$, and is given by the multinomial coefficient $$\displaystyle g=\frac{N!}{\prod_{i=1}^M N_i!}$$, compared with $$M^N$$ before considering the non-uniform distribution. Using **Stirling's approximation**, we have $$\ln_2g\approx -N\displaystyle\sum_{i=1}^M p_i\ln_2p_i$$.

- It is interesting that statistical physicists use $$\ln_2$$ to indicate $$\log_2$$, while engineers use $$\log x$$ to indicate $$\log_2$$.

- Here, we start from "large $$N$$ gives $$\{N_i=Np_i\}$$" and then use [Stirling's approximation](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula).  Actually,


$$
  \text{The bound by the extreme value among distribution -> }
  \begin{cases}
  \text{The weak law of large number} \\
  \text{Stirling's approximation}
  \end{cases}
$$



### Shannon Entropy 

> Entropy is the unique measure of available information consistent with certain simple and plausible requirements. --- Shannon, 1948

The above was written before I took Information Theory, where $$H(X)=-\displaystyle\sum_{x}p(x)\log p(x)$$, the measure of **uncertainty**,  was derived from **three axioms** in Shannon's 1948 paper. In Shannon's argument, derivation for uniform distribution over $$n$$ elements, the entropy $$H_U(n)=H_2(n)\log n$$ was determined by a bound, and this sandwich just looks like what we did in Stirling's...

**Change the base of logarithm**: $$\text{log}_bp=(\text{log}_ba)(\text{log}_ab)$$, $$H_{\text{in bits}}(X)=(\text{log}_2e)H_{\text{in nats}}(X)$$.

For Bernoulli random variable $$X$$ with probability $$p$$, $$H(X)=\mathscr H(p)=-p\text{log}p-(1-p)\text{log}(1-p)$$. A tip: $$\displaystyle\frac{d}{dp}\mathscr H(f(p))=f^\prime\text{log}\frac{1-f}{f}$$.

### The Entropy of Mixing

Suppose mixing $$M$$ distinct components in the context of statistical mechanics. Consider characterizing the *distribution*, let alone the outcomes from different trials (how many samples taken and the sampling error...).

The *entropy* for *any probability distribution* as $$S=-\displaystyle\sum_{i=1}^Mp(i)\ln p(i)=-\langle\ln p(i)\rangle$$. 

The above is the entropy for a discrete probability distribution, for that of a continuous distribution, $$S=-\int dxp(x)\ln p(x)=-\langle \ln p(x)\rangle$$. The problem of scaling remains to be discussed.

### Joint & Conditional entropy

$$H(X,Y)=-\sum_{x,y}p(x,y)\log_2p(x,y)$$.

$$H(X\vert Y=y)=-\sum_xp(x\vert y)\log_2p(x\vert y)$$ -> $$H(X\vert Y)=-\sum_{x,y}p(x,y)\log_2(x\vert y)$$. Corollary: $$H(X\vert X)=0$$ since no uncertainty.

**Chain rule**: $$H(X,Y)=H(X)+H(Y\vert X)=H(Y)+H(X\vert Y)$$, $$H(X_1,\cdots,X_n)=H(X_1)+H(X_2\vert X_1)+\cdots+H(X_n\vert X_1,\cdots,X_{n-1})$$.

If $$X,Y$$ are **independent**, then $$H(X\vert Y)=H(X)$$ is easy to prove. Then, follow the chain rule, $$H(X,Y)=H(X)+H(Y)$$.

### Asymptotic Equipartition Property (AEP)

As a result of [the weak law of large numbers](https://shi200005.github.io/2022/02/17/Probability/#大数定理), we have for i.i.d. $$\displaystyle-\frac{1}{n}\log_2(X1,X_2,\cdots,X_n)\to H(X)$$ w.r.t. $$p(x)$$.

Typical set $$A_\epsilon^{(n)}$$: some most observed sequences ($$\vert A_\epsilon^{(n)}\vert\sim2^{nH}$$ sequences) that occupy most probability ($$1-\epsilon$$ for sufficiently large $$n$$), within all sequences ($$X^n$$ sequences). Similar to the "typical messages" talked above!

## Mutual information and relative entropy

### Mutual information

$$\displaystyle I(X;Y)=H(X)-H(X\vert Y)=H(X)+H(Y)-H(X,Y)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}$$, $$I(X;Y)=I(Y;X)$$ symmetric.

<img src="/images/blog/Information_Theory_Mutual_Information.png" alt="Information_Theory_Mutual_Information" style="zoom:25%;" />

$$I(X;X)=H(X)$$ self-information, $$H(X,Y)=H(Y)+H(X\vert Y)$$.

### Relative entropy / Kullback-Leibler divergence

$$\displaystyle D(p\Vert q)=\sum_xp(x)\log_2\frac{p(x)}{q(x)}\ge0$$, **not symmetric**.

- "=" iff $$p=q$$ proved using $$x-1\ge\ln x$$;
- a measure of the differences between two p.m.f., relative entropy of $$p$$ w.r.t. $$q$$; the penalty we should pay if we assume $$q$$ to design code but actually it is $$p$$;
- $$D(p(x,y)\Vert p(x)p(y))=I(X;Y)$$ -> $$I(X;Y)\ge0$$, "=" iff $$p(x),p(y)$$ are independent, $$p(x,y)=p(x)p(y)$$. 
  - -> $$H(X)\ge H(X\vert Y)$$. Some apriori knowledge (information, $$I(X;Y)$$) can reduce uncertainty **on average**.  If the knowledge is bullshit ($$I(X;Y)=0$$), then it doesn't reduce the uncertainty.
- -> $$H(X)\le\log_2\vert X\vert$$, given the alphabet, uniformly distributed -> the largest entropy (**Maximum entropy**).

### Chain rule

$$I((X_1,X_2,X_3);Y)=I(X_1;Y)+I((X_2;Y)\vert X_1)+I((X_3;Y)\vert(X_1,X_2))$$

## Data processing inequality (DPI)

### Markov chain

$$p(x,y,z)=p(x)p(y\vert x)p(z\vert(x,y))$$ -**Markovian**-> $$p(x,y,z)=p(x)p(y\vert x)p(z\vert y)$$ (only keep your neighbor in your condition), also denote as $$X\to Y\to Z$$

- -> $$p((x,z)\vert y)=p(x\vert y)p(z\vert y)$$, which means $$I((X;Z)\vert Y)=0$$;
- $$X\to Y\to Z$$ <-> $$Z\to Y\to X$$.

P.S. $$X_1\to X_2\to X_3\to X_4$$ -> $$p(x_1\vert(x_3,x_4))=p(x_1\vert x_3)$$, only keep your nearest neighbour.

### DPI

$$X\to Y\to Z$$ -> $$I(X;Y)\ge I(X;Z)$$ and $$I(X;Y)\ge I((X;Y)\vert Z)$$, using $$I(X;(Y,Z))=I(X;Z)+I((X;Y)\vert Z)=I(X;Y)+I((X;Z)\vert Y)=I(X;Y)$$.

---

## Prefix codes

$$X$$ has an alphabet $$\mathscr X$$, to code $$X$$, we use anrepresentation alphabet $$\mathscr D=\{0,1,\cdots, D-1\}$$. E.g., binary representation $$D=2$$, $$\mathscr D=\{0,1\}$$.

### Prefix code & Kraft's inequality (KI)

Uniquely decodable; furthermore, you don't need to decode it backward. Generated by a "tree".

<img src="/images/blog/Information_Theory_Prefix.png" alt="Information_Theory_Prefix" style="zoom:30%;" />

The codeword lengths of any prefix code must satisfy KI. (McMillan) The codeword lengths of any uniquely decodable code must satisfy KI. -> Prefix code can achieve optimality code lengths. -> We'll focus on prefix codes.

### Huffman codes

Prefix codes achieve KI with equality, not unique.



E.g., a *prefix code* 

alphabet $$\mathscr X$$ | a      | b    | c      | d     |

p.m.f. $$p(x)$$    | 1/2 | 1/4 | 1/8  | 1/8  |

code $$C(x)$$     | 0     | 10  | 110 | 111 |

Average length: $$E(l_c(x))=1*1/2+2*1/4+3*1/8+3*1/8=1.75$$ (bits / letter)

$$H(X)=1/2*\log_2(1/2)+1/4*\log_2(1/4)+1/8*\log_2(1/8)+1/8*\log_2(1/8)=1.75$$  (bits / letter)

## Convex Function

### Convex Optimization



## Gaussian Channel

### Bandlimited Channels

#### White noise

Refer to **10.2.4 White Noise** in H. Pishro-Nik, "Introduction to probability, statistics, and random processes", available at https://www.probabilitycourse.com, Kappa Research LLC, 2014.

White noise means the power spectral density is a constant, usually denoted as $$\frac{N_0}{2}$$ (Watt/Hertz) as related to bandlimited channels (only let frequency in $$[-W,W]$$ pass through, and the noise power is thus $$N=\frac{N_0}{2}(2W)=N_0W$$). And the corresponding autocorrelation function (Fourier of power spectral, see 10.1.2 Mean and Correlation Functions of the above textbook) is a Dirac delta function. That means the noise sample at different time point is not correlated.

Gaussian White noise is when the noise sample obeys a Gaussian distribution, which can be generated from a Brownian motion (by Stirling's approximation, as concluded in [(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)). 

#### Channel Capacity

How to transmit signal using the Bandlimited Gaussian channel? We can send the signal by samples uniformly distributed in time (e.g., your voice message). 

Conclusion: $$C=\frac{1}{2}\log(1+\frac{P}{N})$$ bits / channel use -> $$C=\frac{1}{2}\log(1+\frac{P/2W}{N_0/2})$$ bits / sample -> $$C=W\log(1+\frac{P}{N_0W})$$ bits / second. My confusion was solved by figuring out $$N_0$$ is the quantity to specify the noise intensity, while for transmitting signals, the signal power is constrained as Watts, and if our sampling frequency is larger, we have to put less energy per sample on the signal... 


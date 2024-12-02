---
layout: post
title: 量子力学
categories: BS-NJU-Course-Review-Physics
description: 薛定谔的猫猫
keywords: quantum mechanics
mathjax: true
---

> I think I can safely say that nobody understands quantum mechanics.--Richard Feynman

| 课程名                       | 量子力学                                                                           |
| 学习时间                   | 大三上                                                                               |
| 周课时                       | 4                                                                                        |
| 本人成绩                   | 85                                                                                      |
| 课程教材                   | 曾谨言 《量子力学》[?](https://www.zhihu.com/question/25922245/answer/240334225)                                                     |
| 个人建议参考教材    | D. J. Griffiths Introduction to Quantum Mechanics  |
| 先修课程                   | 微积分 线性代数 理论力学  数学物理方法                      |

注意：本文讨论**非相对论**量子力学。

## 波函数

这一节讨论**坐标表象**、一维空间。

波函数： $$\Psi(x,t)$$​. 薛定谔方程： $$\displaystyle i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi$$. 定态薛定谔方程见下文。

- 三维空间中薛定谔方程的一种导出角度（也不知道当年老薛是不是这样导出的）：

  德布罗意的自由粒子波函数 $$\Psi(\vec{r},t)=\psi_0e^{i(\vec{p}\cdot\vec{r}-Et)/\hbar}$$ 对时间微分  ->  拉普拉斯算子、非相对论动量能量替换  ->  自由粒子（质量 $$m$$）的运动所满足的薛定谔方程。

  再推广到有外力作用的其概况：粒子 m 在势场 $$V(\vec r,t)$$ 中的运动所满足的薛定谔方程。$$V(\vec r,t)=V(r)$$ 的定态情况下，把波函数分离变量，得到**定态薛定谔方程**。

- **定态薛定谔**的另一种导出角度：参见梁昆淼老师《理论力学》9.6 - 从“几何力学”到“波动力学”

> 经典力学中的牛顿方程不是从理论上推导出来的，而是对自然现象的观察和总结，并经过实验验证，因而是一条经验规律。量子力学中薛定谔方程的得到与牛顿方程有相似之处，也不是从理论上推导出来的。然而两者也有不同之处，那就是薛定谔方程不是一条经验规律，它实质上是一个公设，当然这个公设与前面讨论的德布罗意波函数假说是一致的。它的正确性是由在各种具体情况下从它导出的各个结论与实验结果相符合的事实而确立的。——徐克尊 《近代物理学（第4版）》中科大出版社 2019

统计解释：$$\vert\Psi(x,t)\vert^2dx$$：时刻 $$t$$ 在 $$x$$ 到 $$x+dx$$ 之间找到该粒子的**概率** -> 归一化条件 $$\displaystyle \int_{-\infty}^{\infty}\vert\Psi(x,t)\vert^2dx=1$$.

- 波函数可以被归一化的条件： $$x$$ 趋向于正负无穷时，波函数趋向于零快于$$\displaystyle\frac{1}{\sqrt{\vert x\vert}}$$.
- 可以证明，若某一时刻的波函数是归一化的，则薛定谔方程给出任意时刻的波函数都是归一化的。

### 观测量的期望

$$\displaystyle\langle x\rangle=\int_{-\infty}^{\infty}{x\vert\Psi(x,t)\vert^2dx}$$.

> Rather, $$\langle x\rangle$$ is the average of measurments performed on particles all in the state $\Psi$, which means that either you must find some way of returning the particle to its original state after each measurement, or else you prepare a whole ensemble of particles, each in the same state $\Psi$, and measure the positions of all of them: $\lang x\rang$ is the average of these results.

由$$\displaystyle\langle p\rangle=m\frac{d\langle x\rangle}{dt}$$，将薛定谔方程带入$$\displaystyle\frac{d\langle x\rangle}{dt}=\int{x\frac{\partial}{\partial t}\vert\Psi\vert^2dx}$$，推出$$\langle p\rangle$$。

结论：$$\displaystyle\langle x\rangle=\int{\Psi^*(x)\Psi dx}, \langle p\rangle=\int{\Psi^*(\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx}$$. 在坐标表象下，$$x$$ 的**算符**是 $$x$$，$$p$$ 的**算符**是 $$\displaystyle\frac{\hbar}{i}\frac{\partial}{\partial x}$$。

对于其他力学量 $$Q(x,p)$$ 的期望，$$\displaystyle\langle Q(x,t)\rangle=\int{\Psi^*Q(x,\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx}$$。形式理论那里会用到。

### 定态薛定谔方程

如果 $$V$$ 与 时间无关，也就是 $$V(x,t)=V(x)$$，则可以将波函数分离变量为 $$\Psi(x,t)=\psi(x)f(t)$$，带入薛定谔方程，分离为空间部分 $$\displaystyle-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+V\psi=E\psi$$，和时间部分 $$f(t)=e^{-iEt/\hbar}$$。

备注：在[理论力学](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E8%AF%BA%E7%89%B9%E5%AE%9A%E7%90%86)中，哈密顿量为 $$\displaystyle H(x,p)=\frac{p^2}{2m}+V(x)$$，在量子力学中，坐标表象下，把坐标和动量换成相应的算符，则得到哈密顿算符 $$\displaystyle\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)$$。则定态薛定谔方程可以写作 $$\hat H\psi=E\psi$$。

定态解的性质：

1. $$\vert\Psi(x,t)\vert^2=\vert\psi(x)\vert^2$$, $$\displaystyle\langle Q(x,t)\rangle=\int{\psi^*Q(x,\frac{\hbar}{i}\frac{\partial}{\partial x})\psi dx}$$.

2. $$\langle\hat H\rangle=E, \langle\hat H^2\rangle=E^2$$ 有确定的能量。
3.  $$\displaystyle\Psi(x,t)=\sum_{n=1}^{\infty}c_n\psi_n(x)e^{-iE_nt/\hbar}$$（[施图姆-刘维尔本征值问题]()）。

波函数满足的条件：

- 一般情况下要求 $$\psi(x)$$ 连续——在 $$V(x)$$ 的衔接处使用。对于一维无限深方势阱，有两端 $$\psi(x)=0$$. 波函数的一阶导如何，请结合牛顿 - 莱布尼兹公式。
- 束缚态 $$E<V(\infty)$$
  1. 利用无限远处波函数有限的条件。
  2. 对于对称势场，可以证明（好像是 Griffiths 一道习题来着？）波函数要么是奇宇称，要么是偶宇称，所以可以先假定宇称再求解。
- 散射态 $$E>V(\infty)$$：透射区没有反射波。可以计算**反射系数**和**透射系数**。

例子见[量子力学 - 绪论](https://shi200005.github.io/download_file/Quantum_Mechanics_Wave_Functions.pdf)。一维无限高方势阱和零点能（波函数连续 -> 边界波函数是$$0$$）-> 基态能量，是不确定原理必然导致的结果。一维方势垒和隧道效应（波函数连续）。即使粒子能量低于势垒，一部分粒子讲穿透势垒达到另一边，称为隧道效应，俗称能穿墙的*崂山道士*。应用：扫描隧道电镜（STM）。

#### 谐振子 

$$\displaystyle-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+\frac{1}{2}m\omega^2x^2\psi=E\psi$$ 形式可以说来源于经典胡克定律。因为势能项是平方的，所以可以用复数分解一下，然后得到**梯子算符** $$\displaystyle a_±=\frac{1}{\sqrt{2m}}(\frac{\hbar}{i}\frac{d}{dx}±im\omega x)$$ ，省略很多很多数学，最终解得 $$\psi(x)=A_n(a_+)^ne^{-\frac{m\omega}{2\hbar}x^2}$$, $$E=(n+\frac{1}{2})\hbar\omega$$，其中 $$n=0,1,...$$。之所以把谐振子单拿出来说，是因为[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)气体热容那里用到了，但是那篇气体热容部分我好像没写这部分。

## 形式理论

主要引出量子力学中特有的表示形式、之前没怎么见过的**厄米共轭**、**力学量的期望**以及**动量表象**。

简要介绍量子力学中特有的表示形式。向量：$$\vert\alpha\rangle$$，向量的内积（点乘）：$$\langle\beta\vert\alpha\rangle=\langle\alpha\vert\beta\rangle^*$$，向量的模长：$$\Vert\alpha\Vert=\sqrt{\langle\alpha\vert\alpha\rangle}$$。

只介绍 **Schwarz 不等式** $$\vert\langle f\vert g\rangle\vert^2≤\langle f\vert f\rangle\langle g\vert g\rangle$$，因为会在**不确定性关系**的证明中用到，见下文。这个不等式的证明可以在[微积分](https://shi200005.github.io/2021/09/30/Calculus/)的绪论部分查阅。

线性变换

- 两组基向量：$$\vert e_i\rangle, \vert f_i\rangle$$ ，基变换矩阵 $$\boldsymbol{S}$$ 也就是 $$\displaystyle\vert e_j\rangle=\Sigma_{i=1}^{n}S_{ij}\vert f_i\rangle$$。这两组基向量下向量分别表示为$$\boldsymbol{a^e}$$, $$\boldsymbol{a^f}$$，两组基下的向量分量关系为 $$\displaystyle a_i^f=\sum_{j=1}^{n}S_{ij}a_j^e$$，也就是 $$\boldsymbol{a}^f=\boldsymbol{Sa^e}$$。

- 在基$$\vert e_i\rangle$$下有线性变换  $$\vert\alpha\rangle\stackrel{\hat T}\longrightarrow\vert\alpha\prime\rangle$$，即$$\boldsymbol{a}^{e\prime}=\boldsymbol{T^ea^e}$$，则不难推出 $$\boldsymbol{a}^{f\prime}=\boldsymbol{T^fa^f}$$，其中 $$\boldsymbol{T^f}=\boldsymbol{ST^eS^{-1}}$$。

请结合[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)理解“**相似矩阵**是同一个线性变换在两个不同基下的表示矩阵。”

### 厄米变换和厄米共轭

法语小知识：厄米 Hermitian 来自法语，H 不发音。

符号：矩阵上加波浪取转置，右上加星号取共轭，就是**厄米共轭**，即 $$\boldsymbol{T^\dagger}≡\boldsymbol{\tilde{T}^*}$$，向量同理。

Hermitian 厄米矩阵:  $$\boldsymbol{T^\dagger}≡\boldsymbol{T}$$. Unitary 酉矩阵/幺正算符: $$\boldsymbol{U^\dagger}≡\boldsymbol{U^{-1}}$$.

厄米变换：如果 $$\boldsymbol{T}$$ 是厄米矩阵，则$$\langle\alpha\vert\hat{T}\beta\rangle=\langle \hat{T}^\dagger\alpha\vert\beta\rangle=\langle \hat{T}\alpha\vert\beta\rangle$$。厄米变换有几个很好的性质：

1. 特征值为实数。意义：力学量都是厄米算符，测量值一定是实数（请不要告诉我你的坐标含有虚数单位
2. 不同特征值的特征向量正交。
3. 特征向量张成线性空间。

厄米变换的这些好性质承袭[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)中提及“实对称矩阵”的好性质。其实**实对称矩阵**就是**厄米矩阵**元素都是实数的特殊形式。而**正交矩阵**就是**酉矩阵**元素都是实数的特殊形式。

### 统计表示

参见 Griffiths 3.3 The Generalized Statisticcal Interpertation

> Classical dynamical quantities (such as position, velocity, momentum and kinetic energy) can be expressed as functions of the "canonical" variables $$x$$ and $$p$$ (and, in rare cases, t): $$Q(x,p,t)$$. To each such classical observable we associate a quantum-menchanical *operator*, $$\hat Q$$, obtained from $$Q$$ by substitution $$\displaystyle p\rightarrow\frac{\hbar}{i}\frac{\partial}{\partial x}$$...... $$\hat Q$$ must be a *Hermitian* operator.

>1. Observable quantities, $$Q(x,p,t)$$, are represented by Hermitian operators, $$\displaystyle \hat Q(x,\frac{\hbar}{i}\frac{\partial}{\partial t},t)$$; the expectation value of $$Q$$, in the state $$\vert\Psi\rangle$$, is $$\langle\Psi\vert\hat Q\Psi\rangle$$.
>2. If you measure an observable $$Q$$ on a particle in the state $$\vert\Psi\rangle$$, you are certain to get one of the eigenvalues of $$\hat Q$$. The probability of getting the particular eigenvalue $$\lambda$$ is equal to the absolute square of the $$\lambda$$ comonent of  $$\vert\Psi\rangle$$, when expressed in the orthonormal basis of eigenvectors.

此节也给出了**动量表象**与**坐标表象**下的波函数与互为**傅里叶变换**关系（此前我们谈论的波函数都在坐标表象下）。$$\displaystyle \Phi(p,t)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}e^{-ipx/\hbar}\Psi(x,t)dx$$。

### 对易

$$[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$$ 是**算符对易式**。如果$$[\hat A,\hat B]=0$$ 则称它们**对易**。拓展阅读：[量子力学 对易关系](https://zhuanlan.zhihu.com/p/382891349)。

可以证明：对角算符互相一定对易。如果两个算符对易，用同一个基变换矩阵对其进行相似变换后得到的矩阵仍然对易。因此可以同时对角化的两个算符一定对易。如果两个算符$$\hat A,\hat B$$ 对易，$$\vert\alpha\rangle$$ 是 $$\hat A$$ 的特征向量，且 $$\hat A$$ 的特征向量谱不简并，那么 $$\vert\alpha\rangle$$ 也是$$\hat B$$ 的特征向量。应用：[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)中 $$\hat L$$, $$\hat L_z$$ 就是同时把球谐函数作为特征向量的两个对易算符。

### 不确定性关系

对于可观测量 $$A$$ 和 $$B$$，利用 **Schwaz 不等式**，省略具体的数学，可以得到 $$\displaystyle \sigma_A^2\sigma_B^2≥(\frac{1}{2i}\langle[\hat A,\hat B]\rangle)$$，其中 

不难证明$$[\hat x,\hat p]=i\hbar$$，如果带入 $$\hat A=x$$, $$\displaystyle \hat B=\frac{\hbar}{i}\frac{d}{dx}$$，就得到了大名鼎鼎的 $$\displaystyle \Delta x\Delta  p≥\frac{\hbar}{2}$$，

> There will be an "uncertainty principle" for *any pair of observables whose corresponding operators* do not commute. We call them **incompatible observables**.

何时位置动量的不确定关系可以取等号？参见 Griffiths 3.4.2。当波函数是高斯波包时。

### 可观测量随时间的演化

不难推出 $$\displaystyle\frac{d}{dt}\langle\hat Q\rangle=\frac{i}{\hbar}\langle[\hat H,\hat Q]\rangle+\langle\frac{\partial \hat Q}{\partial t}\rangle$$（[经典对应](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E6%B3%8A%E6%9D%BE%E6%8B%AC%E5%8F%B7)）

来自 Griffiths 3.4.3，感觉 sloppy：若 $$\hat Q$$ 不显含时间，若我们规定 $$\Delta E≡\sigma_H$$, $$\displaystyle\Delta t≡\frac{\sigma_Q}{\vert d\langle Q\rangle\vert}dt$$，则有 $$\displaystyle\Delta E\Delta  t≥\frac{\hbar}{2}$$。注意：在**非相对论量子力学**中，两对不确定关系是不可以互推的。（[经典对应](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E5%93%88%E5%AF%86%E9%A1%BF-%E9%9B%85%E5%8F%AF%E6%AF%94%E6%96%B9%E7%A8%8B)）

## 三维空间中的量子力学

波函数： $$\Psi(\vec r,t)$$. 薛定谔方程： $$\displaystyle i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi$$. 定态薛定谔方程：$$\displaystyle-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi=E\psi$$. 动量算符：$$\displaystyle\frac{\hbar}{i}\nabla$$. 我们研究 $$V(\vec r)=V(r)$$, $$\Psi(\vec r,t)=\Psi(r,t)$$ 的[情况](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E6%9C%89%E5%BF%83%E5%8A%9B)。

通过分离变量 $$\psi(r,\theta,\varphi)=R(r)Y(\theta,\varphi)$$。后者为[球函数](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E4%B8%80%E8%88%AC%E7%9A%84%E7%90%83%E5%87%BD%E6%95%B0)，前者的方程形式视势函数的具体形式而定。

### 角动量算符

由 $$\vec{L}=\vec{r}\times\vec{p}$$ 得到 $$\displaystyle\hat L_x=\frac{\hbar}{i}(y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y})$$，不难证明 $$[\hat L_x,\hat L_y]=i\hbar L_z$$。以及设 $$\hat L=\hat L_x+\hat L_y+\hat L_z$$，不难证明 $$[\hat L,\hat L_i]=0$$，也就意味着 $$\hat L,\hat L_z$$ 对易，有共同的本征函数，能同时有确定的本征值或量子数。

如果用纯代数方法讨论特征值和特征向量，构造梯子算符 $$\hat L_±=\hat L_x±i\hat L_y$$， $$L_±f_l^m=\hbar\sqrt{l(l+1)-m(m±1)}L_±f_l^{m±1}$$，一顿操作猛如虎，得到结论：记特征向量为 $$f_l^m$$，则 $$\hat L^2f_l^m=\hbar l(l+1)f_l^m,\hat L_z^2f_l^m=\hbar mf_l^m$$，其中 $$l=0,1/2,1,3/2...,m=-l,-l+1,...,l-1,l$$。注意：利用纯代数方法解出的 $$l$$ 是半整数。为什么纯代数方法能解出半整数？我也不知道怎么解释。

在[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E7%90%83%E5%87%BD%E6%95%B0)中已经讨论过，$$Y$$ 是球函数，本征函数是 $$Y_{lm}$$。$$Y$$ 为角动量平方算符作用在 $$Y$$上的本征方程，角动量平方的大小为 $$L^2=l(l+1)\hbar$$，其中 $$l=0,1,2...$$。把角动量在 $$z$$ 方向上的算符作用在 $$Y$$ 上得到角动量在 $$z$$ 方向分量的本征值 $$L_z=m\hbar$$。$$l$$：**角量子数**，$$z$$：**磁量子数**。

【intuition】这里插播一个曾困扰我的点：为什么空间上有 $$x,y,z$$ 三个轴，我们偏偏就要选择讨论 **$$z$$ 方向上的分量**呢？我记得当时老师的解释是“3 个方向都是一样的，大家只是都选了 $$z$$ 方向”。我个人认为或许这样解释更好：三个方向在物理上是一样的，但是在球坐标的描述下，$$\theta$$ 正好是与 $$z$$ 轴的夹角，有特殊性，导致我们利用分离变数法求解微分方程时，$$z$$ 轴一定程度上能够独立出来（$$\hat L_z$$ 作用在球谐函数能得到简洁漂亮的结果）。如果我们的球坐标用与 $$x$$ 轴的夹角，和 $$yOz$$ 平面上投影和 $$y$$ 轴的夹角描述，或许我们就会转而讨论角动量的 $$x$$ 轴分量了。

### 无限深球形势阱

此时球内定态薛定谔方程是[亥姆霍兹方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E6%96%BD%E5%9B%BE%E5%A7%86-%E5%88%98%E7%BB%B4%E5%B0%94%E6%9C%AC%E5%BE%81%E5%80%BC%E9%97%AE%E9%A2%98)。归结为求解径向边界条件为中心不发散、边缘为 0 的[球贝塞尔方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E7%90%83%E8%B4%9D%E5%A1%9E%E5%B0%94%E5%87%BD%E6%95%B0)。中心不发散，排除球诺伊曼函数。参加 Griffiths 4.1.3 Example.

### 氢原子的量子力学解

$$\displaystyle V(r)=-\frac{e^2}{4\pi\epsilon_0}\frac{1}{r}$$ 我们关注 $$E<0$$ 的[束缚态](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E5%BC%95%E5%8A%9B-%E5%BC%80%E6%99%AE%E5%8B%92%E8%A1%8C%E6%98%9F%E8%BF%90%E5%8A%A8%E5%AE%9A%E5%BE%8B)，此时本征值是分立的，有分立能级。

诡异的 $$R(r)$$ 方程采用[级数法](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E6%96%BD%E5%9B%BE%E5%A7%86-%E5%88%98%E7%BB%B4%E5%B0%94%E6%9C%AC%E5%BE%81%E5%80%BC%E9%97%AE%E9%A2%98)暴力求解（Griffiths 的量子力学第四章给出用 $$r$$ 为 $$0$$ 和无穷远的两种极限情况求解），与能量有关的参数只能取 $$n=1,2,3,...$$，$$l$$ 被限制为 $$l=0,1,2,...n-1$$，从此得到的能量本征值与玻尔理论 $$\displaystyle E_n=-[\frac{m}{2\hbar^2}(\frac{e^2}{4\pi\epsilon_0})^2]\frac{1}{n^2}$$ 中给出的相同。$$n$$：**主量子数**。由此可见，类氢原子体系的能量仅由量子数 $$n$$，直接来源于非相对论的薛定谔方程，无需任何人为量子化假设，只要存在束缚势阱就必然导致量子化。

### 自旋

轨道磁矩在 $$z$$ 方向的分量如何观测？原子与外磁场相互作用。[电磁学](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E5%AE%89%E5%9F%B9%E5%8A%9B)中已经得到结论：在不均匀磁场中，受力 $$\vec{F}=-\nabla U_m$$。**斯特恩-盖拉赫实验**：使银原子束穿过 $$z$$ 方向有很大梯度的非均匀磁场，如果原子轨道磁矩 $$z$$ 方向上是量子化的，则探测屏上出现分立的斑束。不过分立斑束的位置和数量很出乎意料，以及原子光谱的精细结构和反常塞满分裂现象，暗示原子中除了轨道磁矩外还有其他形式的磁矩。

为了解释各种轨道磁矩还不能解释的问题，1925 年两个荷兰青年提出了扯淡的**电子自旋**理论。$$S^2=s(s+1)\hbar^2$$, $$S_z=m_s\hbar$$, $$s=1/2$$, $$m_s=±1/2$$。其中 $$s$$ 是电子**自旋角动量**量子数，简称**自旋量子数**......用于解释**斯特恩-盖拉赫实验**的反常分裂结果。后来 1929 年狄拉克建立了相对论量子力学之后，从数学上可以自然地赋予电子自旋自由度。自旋是电子的**内禀**属性，是相对论量子力学特有的，不能做经典的对应。

自旋相关算符的特征值特征向量（也就是本征态）的建立完全类比上文角动量相关算符的代数算法。自旋是粒子的**内禀**属性，我们也不能用类似于球谐函数的坐标函数描述。本征值 $$s=0,1/2,1,3/2,...$$; $$m=-s,-s+1,...,s-1,s$$，由于没有关于本征值的先验知识，我们无法排除非整数的存在了。只要粒子的类型确定了，它的自旋就是确定的，例如 pi 介子是 $$0$$，质子、中子和电子等实物粒子是 $$1/2$$，光子是 $$1$$......

#### 拥有 1/2 自旋的粒子

考虑 $$\hat S$$, $$\hat S_z$$ 的共同本征态。设 $$s=1/2,m_s=1/2$$ 为 spin up 态  $$\chi_+=\pmatrix{1\\0}$$， $$s=1/2,m_s=-1/2$$ 为 spin down 态  $$\chi_-=\pmatrix{0\\1}$$。可以紧凑地由**泡利矩阵**表示：$$\vec{S}=\displaystyle\frac{\hbar}{2}\vec{\sigma}$$。

例：若 $$\hat S_z$$ 的本征态 $$\chi_+=\pmatrix{1\\0}$$ (eigenvalue $$+\hbar/2$$), $$\chi_-=\pmatrix{0\\1}$$ (eigenvalue $$-\hbar/2$$). 则 $$\hat L_x$$ 的本征态则为 $$\chi_+^{(x)}=\pmatrix{\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}}$$ (eigenvalue $$+\hbar/2$$), $$\chi_-^{(x)}=\pmatrix{\frac{1}{\sqrt{2}}\\-\frac{1}{\sqrt{2}}}$$ (eigenvalue $$-\hbar/2$$). $$\hat S$$, $$\hat S_z$$ 对易，拥有共同本征态，$$\hat S_x$$, $$\hat S_z$$ 不对易，本征态不同。见 Griffiths 4.4.1。

例：拉莫尔进动的量子力学表示。见 Griffiths 4.4.2。

#### 两个自旋为 1/2 的粒子体系

四个状态：$$\uparrow\uparrow:m=1$$；$$\uparrow\downarrow:m=0$$；$$\downarrow\uparrow:m=0$$；$$\downarrow\downarrow:m=-1$$。

$$\hat S_-\vert11\rangle=\hbar\sqrt2\vert10\rangle$$；$$\hat S_-\vert\uparrow\uparrow\rangle=(\hat S_-\vert\uparrow\rangle)\vert\uparrow\rangle+\vert\uparrow\rangle(\hat S_-\vert\uparrow\rangle)=\hbar(\downarrow\uparrow+\uparrow\downarrow)$$ -> $$\displaystyle\vert10\rangle=\frac{1}{\sqrt2}(\downarrow\uparrow+\uparrow\downarrow)$$.

于是得到 $$s=1$$ 的三重态：$$\vert11\rangle=\uparrow\uparrow$$；$$\displaystyle\vert10\rangle=\frac{1}{\sqrt{2}}(\uparrow\downarrow+\downarrow\uparrow)$$；$$\vert1(-1)\rangle=\downarrow\downarrow$$；$$s=0$$ 的单重态：$$\displaystyle\vert00\rangle=\frac{1}{\sqrt{2}}(\uparrow\downarrow-\downarrow\uparrow)$$。

## 全同粒子

全同性原理：微观粒子如电子、质子、中子、光子等具有静止质量、电荷、自旋、磁矩等固有属性，称为粒子的内禀属性。内禀属性都相同的微观粒子称为**全同粒子**，差异不能通过实验观测到。在量子力学中，对于两个全同粒子，在波函数重叠的区域本质上无法分辨它们（由于微观粒子具有**波粒二象性**，用确定的轨道描述粒子的运动已失去意义，陈老师：你无法在这些粒子上粘上标签1,2,3...来分辨它们），交换任意两个粒子不会引起物理状态的变化，称为**全同性原理**。

费米子与玻色子：全同粒子的交换对称性于粒子的内禀自旋有关。自旋量子数为**半整数**的粒子组成的全同粒子体系(如电子、质子等)，其波函数一定是**交换反对称**的，称为**费米子**（遵从泡利不相容原理）。自旋量子数为**零或整数**的粒子组成的全同粒子体系（例如光子、pi 介子等），其波函数一定是**交换对称**的，称为**玻色子**（不遵从泡利不相容原理）。

对于统计物理人，我们更关心费米子和玻色子在统计学行为上的区别。根据 Griffiths 5.1.2 如果计算 $$\langle(x_1-x_2)^2\rangle$$，不难发现 "identical bosons tend to be somewhat closer together, and identical fermions somewhat farther apart, than distinguishable particles in the same two states. 同时也提醒我们，离得太远的两个电子**波函数根本不交叠**，就算电子是费米子，直接按可分辨粒子处理就可以。后续[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)中也提到过，定域子系，包括可分辨的玻色子和费米子，也按玻尔兹曼统计处理。

## 不含时微扰理论



## WKB 近似



## 含时微扰理论



## 散射

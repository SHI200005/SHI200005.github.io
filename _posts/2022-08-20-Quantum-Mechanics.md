---
layout: post
title: 量子力学
categories: BS-NJU-Course-Review-Physics
description: 薛定谔的猫猫
keywords: quantum mechanics
mathjax: true
---

> I think I can safely say that nobody understands quantum mechanics.--Richard Feynman

事实上，这是我 2022.12.24 开始写的，但是因为文章在每个分类是按日期降序排列的，我希望它排在《统计物理》之前，按计划也实在应该在那之前完成，故杜撰了一个更合适的完成日期。在我这里，这并不算篡改实验数据和学术不端。

| 课程名                       | 量子力学                                                                           |
| 学习时间                   | 大三上                                                                               |
| 周课时                       | 4                                                                                        |
| 本人成绩                   | 85                                                                                      |
| 课程教材                   | 曾谨言 《量子力学》                                                       |
| 个人建议参考教材    | D. J. Griffiths Introduction to Quantum Mechanics  |
| 先修课程                   | 微积分 线性代数 理论力学  数学物理方法                      |

注意：**线性代数**对于量子力学的重要性必须被强调。

注意：本文讨论**非相对论**量子力学。

注意：在整个网站中，凡是我声称“不难推出”的，并不一定能一眼看出怎么推，并不一定你抓到我让我赤手空拳推导我就能推出来——但是推导过程很容易在各种教科书上查到，尤其是我推荐的教科书。

教材评论：本人并不在科研中使用量子力学（因为我处理的作用量比一个普朗克常数大很多），对于我这种在量子力学方面没有追求的人，我强烈建议使用 Griffiths 的教材自学，而不要使用曾谨言老师那一版，前者简单易懂——[一些关于教材的八卦](https://www.zhihu.com/question/25922245/answer/240334225)。不过 PhD 阶段和办公室做 Quantum Optics 的同学交流时，他认为 Griffiths 的书充满浅显的概念，对于这个领域真正的科研还是太浅了。所以得出结论：或许 Griffiths 这本书最适合我这种不搞量子的。

## 波函数

这一节讨论**坐标表象**。

波函数： $$\Psi(x,t)$$. 波函数的导出：[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)-量子力学初步-薛定谔方程及其应用例子部分写了一种导出方式。

薛定谔方程： $$i\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}+V\Psi$$. 可类比为量子力学中的牛顿第二定律(?

统计解释：$$\vert\Psi(x,t)\vert^2dx$$：时刻 $$t$$ 在 $$x$$ 到 $$x+dx$$ 之间找到该粒子的**概率** -> 归一化条件 $$\int_{-\infty}^{\infty}\vert\Psi(x,t)\vert^2dx=1$$.

- 波函数可以被归一化的条件： $$x$$ 趋向于正负无穷时，波函数趋向于零快于$$\frac{1}{\sqrt{\vert x\vert}}$$.
- 可以证明，若某一时刻的波函数是归一化的，则薛定谔方程给出任意时刻的波函数都是归一化的。

### 观测量的期望

$$\langle x\rangle=\int_{-\infty}^{\infty}{x\vert\Psi(x,t)\vert^2dx}$$.

> Rather, $$\langle x\rangle$$ is the average of measurments performed on particles all in the state $\Psi$, which means that either you must find some way of returning the particle to its original state after each measurement, or else you prepare a whole ensemble of particles, each in the same state $\Psi$, and measure the positions of all of them: $\lang x\rang$ is the average of these results.

由$$\langle p\rangle=m\frac{d\langle x\rangle}{dt}$$，将薛定谔方程带入$$\frac{d\langle x\rangle}{dt}=\int{x\frac{\partial}{\partial t}\vert\Psi\vert^2dx}$$，推出$$\langle p\rangle$$。

结论：$$\langle x\rangle=\int{\Psi^*(x)\Psi dx}, \langle p\rangle=\int{\Psi^*(\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx}$$. 在坐标表象下，$$x$$ 的**算符**是 $$x$$，$$p$$ 的**算符**是 $$\frac{\hbar}{i}\frac{\partial}{\partial x}$$。

这一部分波函数的处理感觉和我做的[随机过程](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)里面的 Master equation 的概率有异曲同工之妙呢~

对于其他力学量 $$Q(x,p)$$ 的期望，$$\langle Q(x,t)\rangle=\int{\Psi^*Q(x,\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx}$$。形式理论那里会用到。

## 定态薛定谔方程

如果 $$V$$ 与 时间无关，也就是 $$V(x,t)=V(x)$$，则可以将波函数分离变量为 $$\Psi(x,t)=\psi(x)f(t)$$，带入薛定谔方程，分离为空间部分 $$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+V\psi=E\psi$$，和时间部分 $$f(t)=e^{-iEt/\hbar}$$。

备注：在[理论力学](https://shi200005.github.io/2022/01/25/Theoretical-Mechanics/)中，哈密顿量为 $$H(x,p)=\frac{p^2}{2m}+V(x)$$，在量子力学中，坐标表象下，把坐标和动量换成相应的算符，则得到哈密顿算符 $$\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)$$。则定态薛定谔方程可以写作 $$\hat H\psi=E\psi$$。

定态解的性质：

1. $$\vert\Psi(x,t)\vert^2=\vert\psi(x)\vert^2, \langle Q(x,t)\rangle=\int{\psi^*Q(x,\frac{\hbar}{i}\frac{\partial}{\partial x})\psi dx}$$.

2. $$\langle\hat H\rangle=E, \langle\hat H^2\rangle=E^2$$ 有确定的能量。
3.  $$\Psi(x,t)=\Sigma_{n=1}^{\infty}c_n\psi_n(x)e^{-iE_nt/\hbar}$$。

接下来便是解很多与时间无关的势场下的定态薛定谔方程，因为跟我之后做的没关系，就不详细描述了。只是描述一下怎么解的，然后稍微多描述一下谐振子。

波函数满足的条件：

- 一般情况下要求 $$\psi(x)$$ 连续——在 $$V(x)$$ 的衔接处使用。对于一维无限深方势阱，有两端 $$\psi(x)=0$$.
- 1. $$V(x)$$ 不发散时要求$$\frac{d}{dx}\psi(x)$$ 连续——在 $$V(x)$$ 的衔接处使用。
  2. $$V(x)$$ 发散时不要求$$\frac{d}{dx}\psi(x)$$ 连续。在 delta 函数势中使用 $$\frac{d}{dx}\psi(x)\vert_{x=0^+}^{x=0^-}=\frac{2m\gamma}{\hbar^2}\psi(0)$$（来自对薛定谔方程积分）。
- 束缚态 $$E<V(\infty)$$
  1. 利用无限远处波函数有限的条件。
  2. 对于对称势场，可以证明（好像是 Griffiths 一道习题来着？）波函数要么是奇宇称，要么是偶宇称，所以可以先假定宇称再求解。
- 散射态 $$E>V(\infty)$$：透射区没有反射波。可以计算**反射系数**和**透射系数**。

自由粒子波函数介绍了不少，但没啥用，我就不写。

**谐振子**的薛定谔方程 $$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+\frac{1}{2}m\omega^2x^2\psi=E\psi$$ 形式可以说来源于经典胡克定律。因为势能项是平方的，所以可以用复数分解一下，然后得到**梯子算符** $$a_±=\frac{1}{\sqrt{2m}}(\frac{\hbar}{i}\frac{d}{dx}±im\omega x)$$ ，省略很多很多数学，最终解得 $$\psi(x)=A_n(a_+)^ne^{-\frac{m\omega}{2\hbar}x^2}, E=(n+\frac{1}{2})\hbar\omega$$，其中n=0,1,...。之所以把谐振子单拿出来说，是因为[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)气体热容那里用到了，但是那篇气体热容部分我好像没写这部分。

## 形式理论

这一部分用来考验你的[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)功底。因为我自己功底不错，所以很多东西就不详述了。主要引出量子力学中特有的表示形式、之前没怎么见过的**厄米共轭**、**力学量的期望**以及**动量表象**。

### 线性代数

简要介绍量子力学中特有的表示形式。向量：$$\vert\alpha\rangle$$，向量的内积（点乘）：$$\langle\beta\vert\alpha\rangle=\langle\alpha\vert\beta\rangle^*$$，向量的模长：$$\Vert\alpha\Vert=\sqrt{\langle\alpha\vert\alpha\rangle}$$。

只介绍 **Schwarz 不等式** $$\vert\langle f\vert g\rangle\vert^2≤\langle f\vert f\rangle\langle g\vert g\rangle$$，因为会在**不确定性关系**的证明中用到，见下文。这个不等式的证明可以在[微积分](https://shi200005.github.io/2021/09/30/Calculus/)的绪论部分查阅。

1. 线性变换

   两组基向量：$$\vert e_i\rangle, \vert f_i\rangle$$ ，基变换矩阵 $$\boldsymbol{S}$$ 也就是 $$\vert e_j\rangle=\Sigma_{i=1}^{n}S_{ij}\vert f_i\rangle$$。这两组基向量下向量分别表示为$$\boldsymbol{a^e}, \boldsymbol{a^f}$$，两组基下的向量分量关系为 $$a_i^f=\Sigma_{j=1}^{n}S_{ij}a_j^e$$，也就是 $$\boldsymbol{a}^f=\boldsymbol{Sa^e}$$。

   在基$$\vert e_i\rangle$$下有线性变换  $$\vert\alpha\rangle\stackrel{\hat T}\longrightarrow\vert\alpha\prime\rangle$$，即$$\boldsymbol{a}^{e\prime}=\boldsymbol{T^ea^e}$$，则不难推出 $$\boldsymbol{a}^{f\prime}=\boldsymbol{T^fa^f}$$，其中 $$\boldsymbol{T^f}=\boldsymbol{ST^eS^{-1}}$$。

   请结合[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)理解“**相似矩阵**是同一个线性变换（在同一线性空间中）在两个不同基下的表示矩阵。”

2. 特征值和特征向量：很简单，不详述。参见[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)。

### 厄米变换和厄米共轭

法语小知识：厄米 Hermitian 来自法语，H 不发音。

符号：矩阵上加波浪取转置，右上加星号取共轭，就是**厄米共轭**，即 $$\boldsymbol{T^\dagger}≡\boldsymbol{\tilde{T}^*}$$，向量同理。

Hermitian:  $$\boldsymbol{T^\dagger}≡\boldsymbol{T}$$. Unitary: $$\boldsymbol{U^\dagger}≡\boldsymbol{U^{-1}}$$.

厄米变换：如果 $$\boldsymbol{T}$$ 是厄米矩阵，则$$\langle\alpha\vert\hat{T}\beta\rangle=\langle \hat{T}^\dagger\alpha\vert\beta\rangle=\langle \hat{T}\alpha\vert\beta\rangle$$。厄米变换有几个很好的性质：

1. 特征值为实数。意义：力学量都是厄米算符，测量值一定是实数（请不要告诉我你的坐标含有虚数单位
2. 不同特征值的特征向量正交。
3. 特征向量张成线性空间。

厄米变换的这些好性质承袭[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)中提及“实对称矩阵”的好性质。其实**实对称矩阵**就是**厄米矩阵**元素都是实数的特殊形式。而**正交矩阵**就是**酉矩阵**元素都是实数的特殊形式。

### 函数空间

**可将函数作为向量**（例如[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)中的球谐函数就是角动量算符的特征向量），$$\langle f\vert g\rangle=\int{f(x)^*g(x)}dx$$（要求$$\int\vert f(x)^2\vert dx<\infty$$）。i.e. 勒让德多项式就可以作为函数向量空间的基......

- 希尔伯特(Hilbert)空间

  印象里考试和作业都没怎么考察过，调查了身边数学/物理相关方向人士也有大量人对此含义不清。完备的内积空间是**希尔伯特(Hilbert)空间**。我没学过数学，除了 Griffiths 3.2.3 讲的内容我都看不懂......像我一样完全不会数学的就去看这部分吧......

  完备性关系：对于一组完备的标准正交基，有$$\Sigma_n\vert\phi_n\rangle\langle\phi_n\vert=\boldsymbol{1}$$。事实上，这个概念非常重要(!!)，不论是对于**一维伊辛模型严格解**（详见以后会有的**高等统计物理**），还是**矩阵 SVD 分解**（详见[机器学习](https://shi200005.github.io/2022/12/05/Machine-Learning/)）。

  相关讨论-[What is meant by the term "completeness relation"](https://physics.stackexchange.com/questions/251803/what-is-meant-by-the-term-completeness-relation) P.S. "From my humble (physicist) mathematics training" 真是笑死我啦！俺也一样！

### 统计表示

参见 Griffiths 3.3 The Generalized Statisticcal Interpertation

> Classical dynamical quantities (such as position, velocity, momentum and kinetic energy) can be expressed as functions of the "canonical" variables $$x$$ and $$p$$ (and, in rare cases, t): $$Q(x,p,t)$$. To each such classical observable we associate a quantum-menchanical *operator*, $$\hat Q$$, obtained from $$Q$$ by substitution $$p\rightarrow\frac{\hbar}{i}\frac{\partial}{\partial x}$$...... $$\hat Q$$ must be a *Hermitian* operator.

>1. Observable quantities, $$Q(x,p,t)$$, are represented by Hermitian operators, $$\hat Q(x,\frac{\hbar}{i}\frac{\partial}{\partial t},t)$$; the expectation value of $$Q$$, in the state $$\vert\Psi\rangle$$, is $$\langle\Psi\vert\hat Q\Psi\rangle$$.
>2. If you measure an observable $$Q$$ on a particle in the state $$\vert\Psi\rangle$$, you are certain to get one of the eigenvalues of $$\hat Q$$. The probability of getting the particular eigenvalue $$\lambda$$ is equal to the absolute square of the $$\lambda$$ comonent of  $$\vert\Psi\rangle$$, when expressed in the orthonormal basis of eigenvectors.

此节也给出了**动量表象**与**坐标表象**下的波函数与互为**傅里叶变换**关系（此前我们谈论的波函数都在坐标表象下）。$$\Phi(p,t)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}e^{-ipx/\hbar}\Psi(x,t)dx$$。

### 对易

$$[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$$ 是**算符对易式**。如果$$[\hat A,\hat B]=0$$ 则称它们**对易**。这个妹妹我曾在[理论力学](https://shi200005.github.io/2022/01/25/Theoretical-Mechanics/)中的**泊松括号**见过的~拓展阅读：初级：[泊松括号（Poisson bracket）是怎么量子化到对易子（commutator）的？ - Rac苏的回答 - 知乎 ](https://www.zhihu.com/question/27463344/answer/1390822940)；进阶：[量子力学 对易关系](https://zhuanlan.zhihu.com/p/382891349)。

可以证明：对角算符互相一定对易。如果两个算符对易，用同一个基变换矩阵对其进行相似变换后得到的矩阵仍然对易。因此可以同时对角化的两个算符一定对易。如果两个算符$$\hat A,\hat B$$对易，$$\vert\alpha\rangle$$ 是 $$\hat A$$ 的特征向量，且 $$\hat A$$ 的特征向量谱不简并，那么 $$\vert\alpha\rangle$$ 也是$$\hat B$$ 的特征向量。应用：[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)中 $$\hat L,\hat L_z$$ 就是同时把球谐函数作为特征向量的两个对易算符。

### 不确定性关系

对于可观测量 $$A$$ 和 $$B$$，利用 **Schwaz 不等式**，省略具体的数学，可以得到 $$\sigma_A^2\sigma_B^2≥(\frac{1}{2i}\langle[\hat A,\hat B]\rangle)$$，其中 

不难证明$$[\hat x,\hat p]=i\hbar$$，如果带入 $$\hat A=x, \hat B=\frac{\hbar}{i}\frac{d}{dx}$$，就得到了大名鼎鼎的 $$\Delta x\Delta  p≥\frac{\hbar}{2}$$，未完......

> There will be an "uncertainty principle" for *any pair of observables whose corresponding operators* do not commute. We call them **incompatible observabels**.

### 可观测量随时间的演化

不难推出 $$\frac{d}{dt}\langle Q\rangle=\frac{i}{\hbar}\langle[\hat H,\hat Q]\rangle+\langle\frac{\partial \hat Q}{\partial t}\rangle$$（关于对易与守恒的推论......）。

......利用上式，若 $$\hat Q$$ 不显含时间，若我们规定 $$\Delta E≡\sigma_H, \Delta t≡\frac{\sigma_Q}{\vert d\langle Q\rangle\vert}dt$$，则有 $$\Delta E\Delta  t≥\frac{\hbar}{2}$$。注意：在**非相对论量子力学**中，$$\Delta x\Delta  p≥\frac{\hbar}{2}, \Delta E\Delta  t≥\frac{\hbar}{2}$$ 是不可以互推的。

## 三维空间中的量子力学

### 氢原子的量子力学解

详见[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)-氢原子的量子力学解。

### 角动量算符

由 $$\vec{L}=\vec{r}\times\vec{p}$$ 得到 $$\hat L_x=\frac{\hbar}{i}(y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y})$$，不难证明 $$[\hat L_x,\hat L_y]=i\hbar L_z$$。以及设 $$\hat L=\hat L_x+\hat L_y+\hat L_z$$，不难证明 $$[\hat L,\hat L_i]=0$$，也就意味着 $$\hat L,\hat L_z$$ 对易，有相同的特征向量（[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)-氢原子的量子力学解部分用分离变量法和级数法可以解出是球谐函数）。但此处对于特征值和特征向量的讨论，用了纯代数方法，构造梯子算符 $$\hat L_±=\hat L_x±i\hat L_y$$，一顿操作猛如虎（以及 $$L_±f_l^m=\hbar\sqrt{l(l+1)-m(m±1)}L_±f_l^{m±1}$$），得到结论：记特征向量为 $$f_l^m$$，则 $$\hat L^2f_l^m=\hbar l(l+1)f_l^m,\hat L_z^2f_l^m=\hbar mf_l^m$$，其中 $$l=0,\frac{1}{2},1,\frac{3}{2}...,m=-l,-l+1,...,l-1,l$$。注意：利用纯代数方法借出的 $$l$$ 是半整数，而球谐函数中的 $$l$$ 是整数，这是为什么呢......

不过来个小总结：波函数作为三个对易力学量的特征函数的特征方程在此！$$\hat H\psi=E\psi, $$$$ L^2\psi=\hbar^2l(l+1)\psi, $$$$ \hat L_z\psi=\hbar m\psi$$.

### 自旋

自旋的相关背景在[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)中已经有所讨论。自旋相关算符的特征值特征向量（也就是本征态）的建立完全类比上文角动量相关算符。自旋是粒子的**内禀**属性，我们也不能用类似于球谐函数的坐标函数描述，因此 Griffiths 书中采用了 $$\vert sm\rangle$$。结论可以紧凑地由泡利矩阵表示：$$\vec{S}=\frac{\hbar}{2}\vec{\sigma}$$，其中 $$\sigma_x,\sigma_y,\sigma_z$$ 随便翻翻书就能查到，不赘述了。

本征值 $$s=0,\frac{1}{2},1,\frac{3}{2},...$$; $$m=-s,-s+1,...,s-1,s$$，由于没有关于本征值的先验知识，我们无法排除非整数的存在了。只要粒子的类型确定了，它的自旋就是确定的，例如 pi 介子是 0，质子、中子和电子等实物粒子是 1/2，光子是 1......拥有 1/2 自旋的粒子的性质是我们重点研究的。

- 拥有 1/2 自旋的粒子

  结论：用 $$\hat S,\hat S_z$$ 的共同本征态 $$\chi_+=\pmatrix{1\\0}$$,(eigenvalue +$$\frac{\hbar}{2}$$), $$\chi_-=\pmatrix{0\\1}$$,(eigenvalue -$$\frac{\hbar}{2}$$). 但 $$\hat L_x$$ 的本征态则为 $$\chi_+^{(x)}=\pmatrix{\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}}$$,(eigenvalue +$$\frac{\hbar}{2}$$), $$\chi_-^{(x)}=\pmatrix{\frac{1}{\sqrt{2}}\\-\frac{1}{\sqrt{2}}}$$,(eigenvalue -$$\frac{\hbar}{2}$$).

  这部分书里用长文解释了不确定性关系，我就不总结了，反正费曼很怀疑我能在物理上正确总结的能力呢。但是我在这里想谈一下对易。$$\hat S,\hat S_z$$ 对易，拥有共同本征态，$$\hat S_x,\hat S_z$$ 不对易，本征态不同。但是 $$\hat S,\hat S_x$$ 对易，为什么本征态不同？如果你一开始寻找的是 $$\hat S,\hat S_x$$ 的共同本征态，则 $$\hat S_x$$ 的本征态形式又不同了。和你一开始找哪一对算符的共同本征态有关。

- 拉莫尔进动

  自旋为 1/2 的粒子在匀强磁场中，自旋角动量绕磁场方向以恒定的角度“旋转”，称为拉莫尔进动。关于经典进动：见[力学](https://shi200005.github.io/2021/10/07/Classcal-Mechanics/)-刚体力学-刚体的定点运动；关于拉莫尔进动：见 Griffiths 4.4.2。

- 斯特恩-盖拉赫实验

  见[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)，见 Griffiths 4.4.2。

- 两个自旋为 1/2 的粒子体系

  四个状态：$$\uparrow\uparrow:m=1$$,$$\uparrow\downarrow:m=0$$,$$\downarrow\uparrow:m=0$$, $$\downarrow\downarrow:m=-1$$.

  我们希望对于 $$s=1$$ 有 $$m=-1,0,1$$ 三个态，但是这里 $$m=0$$ 有俩，咋办？如果用 $$\vert sm\rangle$$ 的形式写状态，那么 $$\vert\uparrow\uparrow\rangle$$ 就是 $$\vert11\rangle$$，而之前角动量的梯子算符可以实现 $$\hat S_-\vert11\rangle=const\vert10\rangle$$，于是用下降梯子得到 $$\hat S_-\vert11\rangle=\hbar(\downarrow\uparrow+\uparrow\downarrow)$$。

  于是得到 s=1 的三重态：$$\vert11\rangle=\uparrow\uparrow$$;$$\vert10\rangle=\frac{1}{\sqrt{2}}(\uparrow\downarrow+\downarrow\uparrow)$$;$$\vert1-1\rangle=\downarrow\downarrow$$. 三重态的角动量算符本征值是 $$2\hbar$$.

  还有一个单重态：$$\vert00\rangle=\frac{1}{\sqrt{2}}(\uparrow\downarrow-\downarrow\uparrow)$$ 说实话我突然就不太明白这玩意怎么写出来的。大概是因为角动量算符本征值是 $$0$$？

## 全同粒子

概念见[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)-多电子原子的能级和光谱-泡利不相容原理。两个粒子的系统...交换算符 $$P$$...时间无关势下的定态波函数 $$\psi(\vec{r_1},\vec{r_2})=±\psi(\vec{r_2},\vec{r_1})$$，其中正号是费米子，负号是玻色子（要么交换对称，要么交换反对称）。

对于统计物理人，我们更关系费米子和玻色子在统计学行为上的区别。根据 Griffiths 5.1.2 如果计算 $$\langle(x_1-x_2)^2\rangle$$，不难发现 "identical bosons tend to be somewhat closer together, and identical fermions somewhat farther apart, than distinguishable particles in the same two states. 同时也提醒我们，离得太远的两个电子**波函数根本不交叠**，就算电子是费米子，直接按可分辨粒子处理就可以。后续[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)中也提到过，定域子系，包括可分辨的玻色子和费米子，也按玻尔兹曼统计处理。

## 不含时微扰理论



## WKB近似



## 含时微扰理论



## 散射

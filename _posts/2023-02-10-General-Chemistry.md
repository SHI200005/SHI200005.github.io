---
layout: post
title: 大学化学
categories: BS-NJU-Course-Review-Other
description: 其实还是热力学
keywords: College Chemistry
mathjax: true
---

《大学化学》是一门鸡肋的水课，学了将近两个月的配位化学，只是觉得崩溃，对于有机物的介绍也停留在给老年人科普的科学水平，需要记忆的枯燥知识点远比带来的知识体系提升更多。

这门课有点用的理论根本没打算让我们学会——对于物理系学生，并不需要学习任何配位化学——既不需要具体知识，也对知识体系架设无用。而当时我们学习这门课的时候，需要《热力学与统计物理》的知识，但我们还没有学这门课。

在此节中，从[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)出发，推导了理想气体热力学平衡描述，与**质量作用定律**相联系。至于质量作用定律与化学反应动力学的关系，需要用到部分[概率论](https://shi200005.github.io/2021/10/02/Probability/)和[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)的结论，我将放在**随机过程**（还没写）一文中。

2023.02.10,Ver0.0 2023.04.28,Ver0.1 2023.05.29,Ver1.0

| 课程名称                  | 大学化学                                             |
| 学习时间                  | 大三上                                                 |
| 周课时                      | 3                                                          |
| 本人成绩                  | 85                                                        |
| 课程教材                  | 《新大学化学》忘了谁写的 别看     |
| 个人建议参考教材   | 《热力学与统计物理学》林宗涵      |
| 先修课程                  | 微积分 热力学                                    |

## 多元系的复相平衡

### 多元均匀系

1. 组元和化学变量

   设系统包含 $$k$$ 种不同的分子，每一种分子在热力学上称为一个组元。令 $$N_1,N_2,...,N_k$$ 代表各种组元的摩尔数，称为化学变量。把变量 $$(N_1,N_2,...,N_k)$$ 简记为 $$\{N_i\}$$。因为各个组元之间可以发生化学反应，所以化学变量之间并不是独立的。

2. 偏摩尔量

   数学背景：若一个函数 $$f(x_1,...,x_n)$$ 满足下列关系：$$f(\lambda x_1,...,\lambda x_n)=\lambda^mf(x_1,...,x_n)$$，则称 $$f$$ 为 $$(x_1,...,x_n)$$ 的 $$m$$ 次齐次函数。齐次函数满足**欧拉定理**：$$\displaystyle\sum_{i=1}^nx_i\frac{\partial f}{\partial x_i}=mf$$。

   热力学函数里面的化学变量作为广延量，从吉布斯函数 $$G=U-TS+pV$$ 导出偏摩尔势（从其他函数导出其他偏摩尔量，但是生物物理狗一般只用吉布斯函数，所以我只提吉布斯函数）。$$G=G(T,p,N_1,...,N_k)$$， $$G=\displaystyle\sum_{i}N_i(\frac{\partial G}{\partial N_i})_{T,p,{N_{j≠i}}}=\displaystyle\sum_{i}N_i\mu_i$$，其中 $$\mu_i≡(\frac{\partial G}{\partial N_i})_{T,p,{N_{j≠i}}}$$ 是组元 $$i$$ 的偏摩尔吉布斯函数，称为组元 $$i$$ 的**化学势**。

   **!ACHTUNG!** 一般而言，组元 $$i$$ 的偏摩尔量不等于纯 $$i$$ 组元的摩尔量，只有分子之间相互作用可以忽略时才相等。

3. 吉布斯关系

   联立 $$dG=-SdT+Vdp+\displaystyle\sum_i\mu_idN_i$$ 和 $$dG=\displaystyle\sum_iN_id\mu_i+\displaystyle\sum_i\mu_i dN_i$$（看前面 $$G=\displaystyle\sum_iN_i\mu_i$$），得 $$SdT-Vdp+\displaystyle\sum_iN_id\mu_i=0$$，称为**吉布斯关系**，表明 $$k+2$$ 个强度变量 $$T,P,\mu_1,...,\mu_k$$ 之间存在一个约束关系，独立变量只有 $$k+1$$ 个。（见[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)）

### 多元系的复相平衡

多元复相系的每一项是一个均匀系，之前的公式仍适用，对于第 $$\alpha$$ 相，可以用 $$T^\alpha,p^\alpha，N_1^\alpha,...,N_k^\alpha$$ 为变量表示这个相的热力学函数。对于广延量热力学函数的可加性（把所有相加起来是总量），应该指出 $$V,U,S,N_i$$ 的可加性无需条件，但 $$H$$ 需要各相的压强相同，$$F$$ 需要各相的温度相同，$$G$$ 需要各相的温度与压强相同（参看林书65页）。

平衡条件：热、力学、相变平衡条件。若相变平衡条件不满足，过程应向着 $$dG<0$$ 的方向进行，组元 $$i$$ 从化学势高的相向化学势低的相转变。

### 化学平衡条件

热力学中，一般的化学反应写作 $$\displaystyle\sum_{i=1}^k\nu_iA_i=0$$。i.e. 化学反应 $$CO+\frac{1}{2}O_2\rightleftharpoons CO_2$$，热力学中改写为 $$CO_2-CO-\frac{1}{2}O_2=0$$，则 $$k=3$$，$$A_1=CO_2, \nu_1=1$$，$$A_2=CO, \nu_2=-1$$，$$A_3=O_2, \nu_3=-\frac{1}{2}$$。注意，把生成物写成正的，反应物写成负的。

联立 $$\delta G=\displaystyle\sum_i\mu_i\delta N_i$$ 和化学反应的约束条件 $$\delta N_i=\nu_i\epsilon$$，则 $$\delta G=\epsilon(\displaystyle\sum_i\nu_i\mu_i)$$。应用吉布斯自由能最小的条件判断化学反应的方向：若 $$\displaystyle\sum_i\nu_i\mu_i<0$$，则 $$\epsilon>0$$，正组元 $$dN_i=\nu_i\epsilon>0$$，生成物组元数量增加。

### 吉布斯相律

关于多元复相平衡的普遍性结论。已经在[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)中得到**约束条件** $$SdT+\boldsymbol{x}· d\boldsymbol{J}+\boldsymbol{N}·d\boldsymbol{\mu}=0$$。Quite generally, if there are $$n$$ ways of performing work on a system that can also change its internal energy by transformations between $$c$$ chemical constituents, the number of independent intensive parameters is $$n+c$$. Of course, including thermal exchanges there are $$n+c+1$$ displacement-like variables in 热力学基本方程，but the intensive variables are constrained by 上面那个式子。如果两相共存，就再加一个约束——两相化学势相等；如果三相共存，再加的就是两个约束——三相化学势都相等。

The Gibbs phase rule states that quite generally, if there are $$p$$ phases in coexistence, the dimensionality (number of degrees of freedom) of the corresponding loci in the space of intensive parameters is $$f=n+c+1-p$$.

### 混合理想气体的性质

[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)结论：设纯组元 $$i$$ 的理想气体的压强和化学势为 $$p_i^\prime$$ 和 $$\mu_i^\prime$$，则 $$\mu_i^\prime=RT\{\varphi_i(T)+lnp_i^\prime\}$$，其中 $$\varphi_i(T)=\frac{h_{i0}-Ts_{i0}}{RT}+\frac{1}{RT}\int c_{p_i}dT-\frac{1}{R}\int c_{p_i}\frac{dT}{T}$$（见林宗涵 2.5.1）。经半透壁实验证实，混合理想气体的分压和化学势 $$p_i$$ 和 $$\mu_i$$ 满足$$p_i=p_i^\prime$$ 和 $$\mu_i=\mu_i^\prime$$。

推论1：混合理想气体的内能只是温度的函数。

推论2：混合理想气体的熵 -> 吉布斯佯谬 -> 只能通过量子力学粒子全同性解决。

### 理想气体的化学平衡

将 $$\mu_i=RT\{\varphi_i(T)+lnp_i\}$$ 带入化学平衡条件 $$\displaystyle\sum_i\nu_i\mu_i=0$$，得 $$\displaystyle\sum_i\nu_ilnp_i=-\displaystyle\sum_i\nu_i\varphi_i(T)$$，记右边为 $$lnK_p(T)$$，得到 $$\displaystyle\prod_{i}p_i^ {\nu_i} =K_p(T)$$ 是**质量作用定律**的一种表达形式。

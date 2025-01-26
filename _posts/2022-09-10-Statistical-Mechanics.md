---
layout: post
title: 统计物理 1.0
categories: BS-NJU-Course-Review-Physics
description: 生物物理方向相当重要的课
keywords: statistical mechanics
mathjax: true
---

> Ludwig Boltzmann, who spent much of his life studying Statistical Mechanics, died in 1906,  by his own hand. Paul Ehrenfest, carrying on the work, died similarly in 1933. Now it is our  turn to study Statistical Mechanics. Perhaps it will be wise to approach the subject cautiously. --in *States of Matter*, by David. L. Goodstein, 1975, Dover N.Y. 

华人科学家张天蓉所写的关于玻尔兹曼和埃伦费斯特的文章：[量子英雄传-玻尔兹曼和埃伦菲斯特](https://wap.sciencenet.cn/blog-677221-1222685.html?mobile=1)。

作为业余钢琴家的玻尔兹曼也将其对音乐的热爱融入科学研究，见 [(De) Zum Gedenken an in Wien lebende Berühmtheiten](https://shi200005.github.io/2023/08/30/Wien/)。

如果你对埃伦费斯特没有那么熟悉（那是因为你对大学物理不熟悉，就像我），则这里列举几个埃伦费斯特的重要理论

- [相变的分类](https://shi200005.github.io/2022/02/24/Thermodynamics/#热动平衡判据)：将相变分为一级相变（如熔化、汽化）和二级相变（如超导相变、铁磁相变）。
- [量子力学浸渐近似](https://shi200005.github.io/2022/08/25/Modern-Physics/#浸渐近似)：提出量子系统在缓慢变化的哈密顿量下，其量子数保持不变。
- 热力学中的扩散问题：他与妻子塔季扬娜·埃伦费斯特（Tatiana Ehrenfest）共同提出了著名的“埃伦费斯特模型”。

| 学习时间                | 大三下                                                                        |
| 周课时                    | 4                                                                                 |
| 本人成绩                | 74 本来是61 :sweat_smile:                                                        |
| 课程教材                | 汪志诚 《统计物理学》                                            |
| 个人建议参考教材 | **Mehran Kardar, Statistical Physics of Particles**; R. K. Pathria, Statistical Mechanics 林宗涵《热力学与统计物理》 |
| 先修课程                | 微积分 概率论 热学 量子力学  |

> As we shall demonstrate, for discussing equilibrium properties of a macroscopic system, full knowledge of the behavior of its constituent particles is not necessary. All that is required is the *likelihood* that the particles are in a particular microscopic state.

统计物理学从物体的微观组成和结构出发，把宏观的性质看成**微观性质的统计平均**，采用统计平均的方法。所以说，这门课的基础是[概率论](https://shi200005.github.io/2021/10/02/Probability/)，不幸的是，概率论上得太 crappy。

## 统计物理学的基本概念

**子系**：一般把组成宏观物体的基本单元称为子系，可以是气体中的分子，固体中的原子，金属中的传导电子，热辐射场中的光子等；也可以是粒子的某一个自由度，如双原子分子的振动自由度，磁性原子的自旋自由度等等；还可以把系统分成许多宏观大小的部分，把每一个部分看成一个子系。

1. 经典描写：对于 $$r$$ 个自由度的**子系**，微观状态用 $$2r$$ 个变量描写，通常用广义坐标 $$q_1,q_2,...,q_r$$ 和广义动量 $$p_1,p_2,...,p_r$$ （正则形式经典力学，见[理论力学](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#哈密顿正则方程)）。相空间/相体积 $$d\omega=dq_1...dq_rdp_1...dp_r$$。对于 $$N$$ 个子系构成的整个**系统**，就是把所有子系放一块，用 $$2Nr$$ 个变量描写。
2. 量子描写：用量子态/量子数描写。子系量子态与子系相体积的对应关系：子系的一个量子态 $$\leftrightarrow$$ 大小为 $$h^r$$ 的子相体积。
3. **定域子系**：全同多粒子系统在各个粒子的波函数分别局限在空间不同的范围内，彼此没有交叠的情况下，可以从粒子所处的不同位置对它们加以区分，这种子系统称为定域子系。

---

## 统计系综理论

- [德语小知识](https://shi200005.github.io/2023/11/02/Language/#physics-1)：配分函数为什么用 $$Z$$ 表示？来自于德语 $$\mathfrak{Zustandssumme}$$ 的第一个字母 Z，英译为 “the sum over states”，很直观地表明了**微观性质的统计平均**这个概念。
- [刘维尔定理](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#刘维尔定理) $$\displaystyle\frac{d\rho}{dt}=\frac{\partial\rho}{\partial t}+\{\rho,H\}=0$$.

### 微正则系综

 - 如何描述系统达到了平衡态？需要相应的系综满足 $$\displaystyle\frac{\partial\rho_\text{eq}}{\partial t}=0$$ 以及 $$\displaystyle\frac{\partial H}{\partial t}=0$$，代入刘维尔定理也就是 $$\{\rho_\text{eq},H\}=0$$。如何实现 $$\{\rho_\text{eq},H\}=0$$？一个实现方式是如果 $$\rho_\text{eq}$$ 是 $$H$$ 的函数（泊松括号里整个求导链式法则推出 $$\rho^\prime(H)\{H,H\}=0$$）。于是，对于**微正则系综**，考虑 **mechanically and adiabatically isolated system**， 也就是 specify 物理量 $$E$$，也就是 $$H=E=\text{const}$$，于是 $$ρ_\text{eq}$$ 在相空间两个相邻的能量曲面 $$E$$ 和 $$E+ΔE$$ ($$\Delta E\rightarrow 0$$) 之间是一个**常数**（为啥能整出个 $$\Delta E$$？Justified by thermodynamic limit.）这是统计物理的基本**假说**，无法证实，但是从这个基础上推导的结果和实验符合得挺好。Refer to Kardar 3.2 Consequences of Liouville's theorem. The third consequence.

 - 于是，微正则系综为，宏观态 $$M$$ 由总能量 $$E$$ 和位形坐标 $$\vec x$$ 表示（比如粒子数、体积），$$M\equiv(E,\vec x)$$。

 - 如何把统计力学角度的熵（$$S=k_B\ln\Omega$$）和热力学角度的熵（$$\displaystyle dS=\frac{\bar dQ}{T}$$）联系起来？参见 Pathria 1.3。统计系综理论是不是 self-consistent（从统计物理出发导出的结论是否和[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)经验结论相符）？参见 Kardar 4.2。此处用到了 [saddle point approximation](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula)。

 - 微正则系综理论和热力学定律一致。与[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)第零定律：两个系统处于热平衡，则 $$\displaystyle\frac{\partial S_1}{\partial E_1}\vert_{\vec x_1}=\frac{\partial S_2}{\partial E_2}\vert_{\vec x_2}$$，对应于 $$\displaystyle\frac{\partial S}{\partial E}\vert_{\vec{x}}=\frac{1}{T}$$. 与[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)第一定律：若外界对系统做功为 $$\bar dW=\vec J·\delta \vec x$$，则 $$\displaystyle\frac{\partial S}{\partial x_i}\vert_{E,x_{j\neq i} }=-\frac{J_i}{T}$$，导出热力学基本方程。 与[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)第二定律：若系统从非平衡态演化到平衡态，$$\delta S\geq0 $$.

 - 应用：我感觉接触的其他几本教材里最大的败笔就是完全回避用微正则系综的例子，至少二能级系统和理想气体在数学上毫无难度，而仅仅一句“微正则系综计算过于复杂”让学生错失了很多理解系综理论的机会。

   思路：**考虑宏观状态对应的所有微观状态**（微正则系综复杂性来源），写出熵的表达式，导出热力学量，如平衡态温度 $$\displaystyle\frac{\partial S}{\partial E}\vert_{\vec x}=\frac{1}{T}$$。The internal energy is specified and the temperature is deduced.

   1. 二能级系统（Kardar 4.3）

      有 $$N$$ 个近独立的定域子系构成的系统，处于平衡态，只有两个能级，每个能级只有一个量子态。例子：非磁性固体中含有密度很低（相互作用可以忽略 -> 近独立子系）的磁性原子，磁性原子的总自旋为 1/2。

      特性：热容在高温区以幂次形式趋于零，在某一有限温度达到极大，并在 $$T→0$$ 时以指数形式趋于零，是一种**肖特基热容行为**。只要粒子能级的激发态于其基态（最低能级）之差为有限值时，都会呈现肖特基热容行为，是一种**量子效应**（[热力学](https://shi200005.github.io/2021/10/11/Thermodynamics/)第三定律所基于的事实）。在 $$T→\infty$$ 时，以幂律形式趋于零，是一种**饱和效应**，在微观状态数作为能量的函数有最大值的系统中见到。

      P.S. 同样的热容行为可以在**高等统计物理**最后的一维**伊辛模型**严格解部分找到，虽然自旋之间有了相互作用，但仍然具有量子效应和饱和效应（还没开始写，老鸽王了）。
   
      其实应用微正则系综后就能直接导出二能级系统**子系的玻尔兹曼分布**┭┮﹏┭┮
   
   2. 理想气体
   
      （Kardar 4.4）用微正则系综处理时数学上比较难的一点就是利用高斯积分的结论（$$\displaystyle S_d=\frac{2\pi^{d/2}}{(d/2-1)!}$$）写出整个相空间的体积。但是这玩意就算你现在不会，到了 [(En) Advanced Statistical Mechanics](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/) 也得学会，何乐而不学。然后也可以从微正则系综描述的理想气体导出单个分子的玻尔兹曼分布，也就是麦克斯韦速度分布率┭┮﹏┭┮（这些都不需要考虑全同性）
   
      （Kardar 4.5）混合理想气体的熵 -> 吉布斯佯谬 -> 只能通过量子力学粒子全同性解决 -> 经典极限下的连续相空间与量子化相空间 $$\displaystyle d\Gamma_N=\frac{1}{h^{3N}N!}\prod_{i=1}^Nd^3\vec{q_i}d^3\vec{p_i}$$ 

### 正则系综

微正则系综里面，我们 specify 了内能，deduce 了温度。其实也可以 specify 温度，deduce 内能。记得从刘维尔尔定理得出结论，平衡态只要 $$\rho_\text{eq}$$ 是哈密顿量 $$H(\vec p,\vec q)$$ 的函数即可，如果我们选择 $$\rho_\text{eq}(\mu)\propto e^{-\beta H}$$，就是正则系综分布函数了。更进一步说，只要概率密度是与哈密顿量对易的力学量（即任意守恒量）的函数即可。

 - 宏观条件：**小系统**与**大热源**接触达到平衡（注意这里的“小”和“大”的假设在推导过程中的作用，展开与恒定温度），两者构成的整体是一个**大孤立系**，相当于小系统的 $$(T,\vec x,N)$$ 一定。

   笨人当时就很疑惑，如果系统和大热源能交换能量，能量变了，系统的温度为啥是个 specified constant 呢？我现在的理解是这样的。拿出一个大孤立系，比如近独立自旋磁子，考虑其中的一小部分磁子，这一部分磁子的总能量是有涨落的。这里温度 $$T$$ 描述的是这个处于平衡态的大孤立系的温度。推导正则系综概率分布的过程中，参见 Kardar Eq.(4.55)，使用的是比起我们观察的小系统大很多的大热源满足的 $$\displaystyle\frac{\partial S_R}{\partial E_R}=\frac{1}{T}$$，整体和大热源的温度都可以用 $$T$$ 描述，也没关小系统什么事。

   但是，这个大孤立系的温度怎么能代表小系统的温度呢？如果用正则系综导出热力学量，这个小系统比起大热源要足够小，同时也要足够大，大到在数学上可以满足 thermodynamic limit。小系统能量有涨落但是概率分布峰值足够尖锐，平均能量相当于最概然能量，就是小系统的能量。

- 概率分布 $$\displaystyle\rho_{(T,\vec{x})}(\mu)=\frac{e^{-\beta H(\mu)}}{Z(T,\vec{x})}$$，**配分函数** $$Z(T,\boldsymbol{x})=\displaystyle\sum _{\mu}e^{-\beta H(\mu)}$$。

- 用配分函数表示热力学量 $$\displaystyle\bar E=-\frac{\partial}{\partial\beta}\ln Z$$，$$\displaystyle\bar Y_\lambda=\frac{1}{\beta}\frac{\partial}{\partial y_\lambda}\ln Z$$，$$\displaystyle S=k(lnZ-\beta\frac{\partial}{\partial\beta}\ln Z)$$，$$F=-kT\ln Z$$。对比热力学基本微分方程得 $$\displaystyle\beta=\frac{1}{kT}$$。

  【intuition】用配分函数表示热力学函数，和用 Generator Operator 求统计量的矩，在本质上是一件事情。详见[(En) Stochastic Processes](https://shi200005.github.io/2022/10/28/Stochastic-Processes/)。

- 能量涨落 $$\displaystyle\frac{\sqrt{\overline{(E-\bar E^2)}}}{\bar E}=\frac{\sqrt{kT^2C_V}}{\bar E}\sim\frac{1}{\sqrt{N}}$$.

- 应用：为啥说正则系综使用起来更简单呢？比如[高等统计物理](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/)里面的伊辛模型（无外磁场情况）也用正则系综。大概是因为写出一个宏观态对应的所有微观态相空间比较困难吧（详见微正则系综处理理想气体）。

  1. 二能级系统（Kardar 4.7）略
  2. 理想气体（Kardar 4.7）略
  
  这两个例子中，构成系统的子系都是近独立子系，系统的概率函数，也就子系的联合概率函数，就是各个子系概率函数的乘积。结论：构成系统的近独立子系满足**玻尔兹曼统计**。P.S. 二能级系统的子系是**定域子系**，理想气体的子系是**非定域非简并子系**，它们都满足玻尔兹曼统计。
  
- 如何从微正则系综出发推导出正则系综的配分函数？我们在推导过程中采用了“大热源比起小系统非常大”的假设以及相应的近似。我遇到了两种近似方法：

  1. 大热源微观状态数的泰勒展开近似：我所学习的方法， 也是林、Kardar、Pathria 等教材使用的方法。
  2. $$\Omega_\text{total}=\Omega_\text{system}*\Omega_\text{reservior}$$：参考教材：[Stowe, Keith. *An introduction to thermodynamics and statistical mechanics*. Cambridge University Press, 2007.]（个人认为这本教材语言严谨性不够）。注意，在没有特定假设的时候我们不能 take this equation for granted——微正则系综总能量不变，若小系统中有能量涨落，大热源能量的涨落是相应的——小系统和大热源是耦合而非独立的。然而，如果大热源足够大，最终数学上可以近似视为两者独立。
  3. 这两种形式不同的假设，说的都是”大热源比起小系统非常大“或者”大热源和小系统可以解耦“这句人话。应用在推导中，推导出的结果在数学上也是一致的。注意，见 Kardar Eq.(4.54)，整个系统的微观状态数严谨地写为 $$\Omega_{S\bigoplus R}(E_{Tot})$$，是大热源和小系统微观状态数的直和，而非直接 factorize 相乘，到后面用到大系统很大的近似条件，才把两个部分 decouple。
  

###  The Gibbs canonical ensemble

这个 ensemble 我之前学这门课的时候没听说过。见 Kardar 4.8. 

> The macrostates $$M\equiv(T,\vec J)$$ are speified in terms of the external temperature and forces acting on the system; the thermodynamic coordinates $$\boldsymbol x$$ appear as addtirional random variables. The system is maintained at constant force through external elements (e.g., pistons or magnets)...The microstates of this combined system occur with the (canonical) probabilities $$\displaystyle p(\mu_s,\vec x)=\frac{e^{-\beta H(\mu_s)+\beta\vec J\cdot \vec x}}{Z(T,N,\vec J)}$$, 配分函数就是 sum over 一下，懒得写了。

注意 $$\vec J\cdot \vec x$$ 在配分函数里的正负号┭┮﹏┭┮ 配分函数指数的来源：热力学基本微分方程（“能量守恒”）。统计物理中与微观状态数对应时，以熵为中心考虑分别对系统能量和外界功的偏导。推荐参考 Pathria 3.9。

- 应用

  1. 理想气体 略

  2. 恒定外场中的自旋磁子

     这一张讨论的都是近独立子系，如果这些自旋磁子之间有相互作用，也就是[高等统计物理](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/)里的伊辛模型，哈密顿量就是这么写的。请一定注意正负号！

### 巨正则系综

 - 宏观条件：**小系统**与**大热源兼大粒子源**接触达到平衡。相当于小系统的 $$(T,\vec x,μ)$$ 一定。

- 将系统与大热源绑定为微正则系综推导出巨正则系综配分函数，具体过程详见林书 8.4.1。结论：几率分布 $$\displaystyle\rho_{Ns}=\frac{1}{\Xi}e^{-\alpha N-\beta E_s}$$，归一化条件 $$\displaystyle\sum_{N=0}^\infty\sum_s\rho_{Ns}=1$$，**巨配分函数** $$\displaystyle\Xi=\sum_{N=0}^\infty\sum_se^{-\alpha N-\beta E_s}=\sum_{N=0}^\infty e^{-\alpha N}Z_N(\beta,\{y_\lambda\})$$。启示：为什么这玩意叫巨配分函数？大概是因为里面套着一个配分函数，对很多很多配分函数求和，所以比较“巨”（给巨佬递茶）。记忆配分函数的指数因子每一项的正负号还是回忆来自热力学基本微分方程。

- 用配分函数表示热力学量懒得写。只写一个巨势 $$\Psi=F-G=-kT\ln\Xi$$。

- 能量涨落 $$\displaystyle\frac{\sqrt{\overline{(E-\bar E^2)}}}{\bar E}=\frac{\sqrt{kT^2C_V}}{\bar E}\sim\frac{1}{\sqrt{N}}$$. 粒子数涨落同理。

- 经典极限下的形式：e.g. 单原子分子理想气体的热力学函数（跟用正则系综求得的完全一致）。e.g. 固体表面的吸附率（林书8.9）。

  用巨正则系综推导费米分布与玻色分布：$$\displaystyle\Xi=\sum_{N=0}^\infty\sum_se^{-\alpha N-\beta E_s}$$ 
  
  参见下面的近独立子系：--冗长的数学推导（林书8.10）--> $$\displaystyle\bar\alpha_\lambda=-\frac{w_\lambda}{e^{\alpha+\beta\epsilon_\lambda}±1}$$. 推导过程中使用了 $$\displaystyle E_N=\sum_\lambda a_\lambda\epsilon_\lambda$$ 的近独立关系。不需要先求最可几分布，而是直接求出平均分布。注意，用巨配分函数推导这俩分布确实要用近独立假设，但是系综理论是可以处理相互作用粒子的（见 [(En) Advanced Statistical Mechanics](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/)）。

### 三种系综之间的关系

 - 微正则系综是平衡态统计理论唯一的基本假设。从微正则系综出发，代入热力学基本方程，导出其他系综。

 - 从应用的角度，三种系综是等效的。条件：**热力学极限 Thermodynamic limit**。

 - 对于满足热力学极限的平衡系综，不必拘泥于宏观条件，哪个方便用哪个。就算粒子数不变，也可以想象粒子数变化，采用巨正则系综，最后用 $$\bar N$$ 代表粒子数就可以。[如何区分正则分布和巨正则分布？ - andrew shen的回答 - 知乎](https://www.zhihu.com/question/22187611/answer/21234177)

---

后面主要是描述系统中**近独立子系**的麦克斯韦-玻尔兹曼分布、费米-狄拉克分布和玻色-爱因斯坦分布的。如果组成系统的子系没有相互作用（相互作用很小），则配分函数可以拆成组成系统的相关子系配分函数的乘积。

## 近独立子系组成的系统

**近独立子系**：独立：组成系统的粒子之间相互作用能忽略不计，系统总能量等于各粒子能量之和 $$\displaystyle E=\sum_{i=1}^N\epsilon_i$$。近：假如粒子之间完全没有相互作用，粒子之间就不可能交换能量，系统就不可能达到平衡并保持平衡。

（也可见 Griffiths 5.4.2）如果给定各个能级 $$E_i$$ 简并度为 $$d_i$$，则对于 $$N_i$$ 个粒子具有 $$E_i$$ 能量的一群粒子，有几种 $$Q(N_1,N_2,N_3,...)$$ 不同的构型？统计物理的基本假说是热力学平衡下给定 $$E$$ 各量子态（微观状态）出现的概率相同。如果给定总粒子数和总能量，$$Q$$ 取最大值时，就是这群粒子最有可能的构型（$$E_i$$ 态上占了 $$N_i$$ 个粒子）。总粒子数和总能量作为约束，用[拉格朗日乘子法](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0)处理 $$Q$$ 在约束下的极值问题（粒子数乘子为 $$\alpha$$，能量约束为 $$\beta$$），$$Q$$ 涉及超大阶乘，用 [Stirling's approximation](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula) 处理（热力学极限：用最概然分布代替平均分布），得到能量为 $$\epsilon$$ 的能级占据数 $$n(\epsilon)$$ 为
$$
n(\epsilon)=
\begin{cases}
\displaystyle\frac{1}{e^{-(\epsilon-\mu)/k_BT}},\text{可分辨粒子的麦克斯韦 - 玻尔兹曼分布} \\
\displaystyle\frac{1}{e^{-(\epsilon-\mu)/k_BT}+1},\text{费米子的费米 - 波色分布} \\
\displaystyle\frac{1}{e^{-(\epsilon-\mu)/k_BT}-1} ,\text{玻色子的波色 - 爱因斯坦分布}\\
\end{cases}
$$
通过简单例子验证（没有根据更一般的情况说明），$$\beta=1/k_BT$$，$$\displaystyle e^{-\alpha}=\frac{N}{V}(\frac{2\pi\beta\hbar^2}{m})^{3/2}$$，定义化学势 $$\mu=-\alpha k_BT$$。

![](/images/blog/Statistical_Mechanics_Distribution.jpg)

## 玻尔兹曼统计

用于可分辨粒子和定域系统（包括可分辨的玻色子和费米子），可以从正则系综里拆出来。

引入**子系配分函数** $$\displaystyle Z=\sum_\lambda g_\lambda e^{-\beta\epsilon_\lambda}$$ 之后可以用于确定定域子系统的一切热力学函数！

### 用配分函数表示热力学函数

定域子系内能 $$\displaystyle U=-N\frac{\partial}{\partial\beta}\ln Z_1$$、外界对系统的作用力 $$\displaystyle Y_\lambda=-\frac{N}{\beta}\frac{\partial}{\partial y_\lambda}\ln Z_1$$ 

- -(热力学第一定律)-> 热量的统计表达式 $$\displaystyle\bar dQ=\sum_\lambda\epsilon_\lambda d\bar a_\lambda$$ 

  结论：绝热过程中，外参量的变化导致粒子能级的变化，但不改变平均分布。（[浸渐近似](https://shi200005.github.io/2022/08/25/Modern-Physics/#浸渐理论)）

- -(热力学基本微分方程)-> 熵的统计表达式 $$\displaystyle S=Nk(\ln Z_1-\beta\frac{\partial}{\partial\beta}\ln Z_1)$$ -> 参数 $$β$$ 是微分式的积分因子，与 $$T$$ 成反比，$$k$$ 称为**玻尔兹曼常数**

  结论：由熵的统计表达式得出对比微观状态数得 $$S=k\ln W(\{\bar a_\lambda\})$$ 玻尔兹曼墓碑上的公式。由此可见，熵代表系统的混乱度(或无序度)。热力学几率越大，即相应的围观状态数越多，代表系统越混乱。

### 玻尔兹曼统计的应用

1. 二能级系统

   略

2. 普朗克的热辐射理论。

   研究对象：达到平衡时空窖内的辐射场，称为平衡热辐射或简称热辐射（也叫做黑体辐射）。

   瑞利-金斯经典统计理论，由能均分定理得到振子的平均能量为 $$kT$$，公式只在低频区符合。维恩公式只在高频区符合。

   普朗克采用**唯象拟合**的办法得到正确的谱密度公式：放弃能量连续的传统观念，假设振子的能量是间断的。普朗克及瑞利-金斯的理论都是采用波的观点来处理的：空窖中的辐射场相当于无穷多个**简谐振子**组成的系统，各个振子的频率从$$0$$ 到 $$∞$$，按频谱 $$g(ν)$$ 变化。振子频谱不变，但**能量均分定理不适用**。假设对于频率为 $$ν$$ 的振子，其能量只能取 $$hν$$ 的**整数倍**，然后用**麦克斯韦-玻尔兹曼分布**求平均。[统计物理-平衡热辐射的统计理论](https://shi200005.github.io/download_file/Statistical_Mechanics_Black_Body_Radiation.pdf)

3. 固体热容的统计理论。

   见**固体物理**，还没写捏。

### 定域子系的经典极限条件

 - 量子性质可以归结为两条，一是能量的取值不连续，二是粒子全同性原理。
 - 定域系统粒子可分辨，无全同性。能量量子化决定了定域系统量子统计与经典统计的区别。**能级间隔**远小于 $$kT$$ 时，则能量量子化效应可以忽略，量子统计的结果还原为经典统计。常把**高温**称为经典极限。一定温度下，高频区振子不满足经典极限条件，是瑞利-金斯公式只适用于低频区的道理。
 - 在经典极限条件下，$$\displaystyle Z=\sum_{n=0}^\infty e^{-\beta\epsilon_n}$$$$\rightarrow$$$$\displaystyle Z=\int...\int\frac{dq_1...dq_rdp_1...dp_r}{h^{r}}e^{-\beta\epsilon}$$.

## 玻色统计和费米统计

**非定域子系**粒子有全同性，要区分费米子还是玻色子。费米子和玻色子的概念[近代物理](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/#费米子和玻色子)里面提过了。

### 用配分函数表示热力学函数

与上面那一节相似，引入**巨配分函数** $$\displaystyle \Xi_1=\prod_\lambda(1±e^{-\alpha-\beta\epsilon_\lambda})^{-g_\lambda}=\Xi_1(\alpha,\beta,{y_\lambda})$$. （其中 $$\epsilon_\lambda$$ 依赖于外参量 $$\{y_\lambda\}$$，并不需要是孤立系）。$$\displaystyle \ln\Xi_1=±\sum_\lambda g_\lambda \ln(1-e^{-\alpha-\beta\epsilon_\lambda})$$. （+为费米分布，-为玻色分布）

用巨配分函数表示热力学函数 $$\displaystyle \bar N=-\frac{\partial}{\partial\alpha}\ln\Xi_1$$, $$\displaystyle \bar E=-\frac{\partial}{\partial\beta}\ln\Xi_1$$, $$\displaystyle \bar Y_\lambda=-\frac{1}{\beta}\frac{\partial}{\partial y_\lambda}\ln\Xi_1$$, $$F,G,\Psi$$ 懒得写了。

熵 $$\displaystyle S=k(\ln\Xi_1-\alpha\frac{\partial}{\partial\alpha}\ln\Xi_1-\beta\frac{\partial}{\partial \beta}\ln\Xi_1)$$ 与最大热力学几率的玻尔兹曼关系仍然成立。

### 非定域子系的非简并条件

 - 在 $$e^α\gg 1$$ 情况下，玻色 - 爱因斯坦分布与费米 - 狄拉克分布都还原为麦克斯韦-玻尔兹曼分布。意义：$$e^α\gg 1$$ -> 每一个量子态上平均占据的粒子数远远小于 1，泡利不相容原理对费米子的限制可以忽略；费米分布和玻色分布的微观状态数彼此相等，只与麦克斯韦-玻尔兹曼分布差一个 $$1/N!$$ 项（$$\displaystyle W_{BE}=W_{FD}=\frac{1}{N!}W_{MB}$$）。
 - 满足非简并条件的非定域系统，把**巨配分函数**改写为 $$\ln\Xi=e^{-α}Z_1$$，其中 $$Z_1$$ 是定域系统里**配分函数**的形式。热力学量 $$\bar N=e^{-\alpha}Z_1$$, $$\displaystyle \bar E=-\bar N\frac{\partial}{\partial\beta}\ln Z_1$$, $$\displaystyle \bar Y_\lambda=-\frac{\bar N}{\beta}\frac{\partial}{\partial y_\lambda}\ln Z_1$$, $$\displaystyle \mu=-kT\ln\frac{Z}{\bar N}$$  。然而熵 $$\displaystyle S=\bar Nk(\ln Z_1-\beta\frac{\partial}{\partial\beta}\ln Z_1)-k\ln\bar N!$$. 最后一项表明**全同性原理**的影响！不会消失！
 - 粒子质量越大，温度越高，数密度越低，越容易满足非简并条件。亦即粒子平均热波长远远小于粒子之间的平均距离。除了低温下质量很轻的理想气体分子，**理想气体**分子都满足非简并条件，遵从麦克斯韦 - 玻尔兹曼分布。低温下的 He 气，4He 是玻色子（偶数个核子），3He 是费米子（奇数个核子）。金属中迅游电子组成的电子气体是强简并费米气体，热辐射的光子气体是强简并玻色气体。
 - 定域系统经典极限条件只有能量量子化不起作用，而非定域系统经典极限条件需要能量量子化和粒子全同性都不起作用。

## 非简并非定域子系

### 理想气体物态方程

[统计物理-理想气体物态方程](https://shi200005.github.io/download_file/Statistical_Mechanics_Ideal_Gas.pdf)

### 麦克斯韦速度分布律

麦克斯韦分布是气体分子**质心运动**的速度分布，它满足**非简并条件**（$$e^\alpha\gg1$$）的**理想气体**所遵从的麦克斯韦-玻尔兹曼分布的一种特殊情形。

![](/images/blog/Statistical_Mechanics_Maxwell_Velocity_Dist.jpg)

### 能量均分定理

只在满足**经典极限**的条件下成立，系统微观能量表达式中的每一个**正平方项**的平均值等于 $$(1/2)kT$$。

1. 应用：非简并理想气体分子质心平动动能、分子转动动能。这一部分对比理想气体状态方程定出玻尔兹曼常数 $$k$$。[统计物理-能量均分定理与理想气体内能](https://shi200005.github.io/download_file/Statistical_Mechanics_Maxwell_Velocity_Dist.pdf)

   小结

   - 对非简并理想气体，由于已满足 $$e^\alpha\gg1$$，只需要考察能级间隔与 $$kT$$ 之比，就可确定是否满足经典极限条件。由于分子的平动、转动、振动和束缚电子运动的能级间隔不同，需要分别对待。一般而言，对以气态存在的一切温度，平动自由度都满足经典极限条件。对大多数分子，转动自由度也满足经典极限条件。振动由于能级间隔大，必须用量子公式处理，束缚电子运动在绝大多数情况下被冻结。热容是平动、转动和振动各部分贡献之和，只有个别特殊情况下，束缚电子部分才有贡献。
   - 一切非简并理想气体的物态方程都满足 $$pV=NkT$$ 的经典形式，内部运动对压强无影响。
   - 内能只是温度的函数，与体积无关。
   - 熵可以分成平动、转动、振动与束缚电子运动四部分贡献之和。

2. 应用：理想固体模型中原子的振动。**固体物理**

## 弱简并非定域子系

弱简并：$$e^\alpha>1$$。介绍了弱简并理想费米/玻色气体的热力学函数和热容对于理想气体物态方程的偏离。处理巨配分函数，利用**粒子态密度** $$\displaystyle D(\epsilon)d\epsilon=\frac{2\pi V}{h^3}(2m)^{3/2}\epsilon^{1/2}d\epsilon$$ 代换。记 $$\displaystyle y=\frac{1}{g_s}n\lambda_T$$，其中 $$\displaystyle \lambda_T=\frac{h}{(2\pi mkT)^{1/2}}$$ 是热波长，$$g_s$$ 是自旋简并因子。有 $$\displaystyle \frac{pV}{NkT}=1±\frac{1}{2^{5/2}}y+O(y^2)$$，其中 + 为理想费米气体，- 为理想玻色气体。

### 统计关联

统计关联起源于粒子全同性原理，它是纯粹量子力学性质的。当 $$y→0$$，亦即 $$\lambda_T=\bar{\delta r}$$（$$\bar{\delta r}$$~$$n^{-1/3}$$），统计关联完全可以忽略。根据量子力学，每个粒子相当于一个波包，波包的平均大小为 $$\lambda_T$$，粒子之间的平均距离为 $$\bar{\delta r}$$，因此，当$$y→0$$ 时，可以完全忽略波包之间的重叠。

但当 $$y$$ 的值虽小但已不可忽略时，粒子的波包之间开始重叠，统计关联开始表现出来。尽管理想气体粒子之间的相互作用可以忽略，但对于**费米子**，由于不能有两个粒子处于同一个粒子量子态，它的波函数必须是**反对称**的，产生一 种有效的排斥作用；而**玻色子**的波函数是**对称**的，产生有效的吸引作用。

根据 Griffiths 5.1.2，对于可分辨粒子 $$\langle(x_1-x_2)^2\rangle=\langle x^2\rangle_a+\langle x^2\rangle_b-2\langle x^2\rangle_a\langle x^2\rangle_b$$；对于全同粒子 $$\langle(x_1-x_2)^2\rangle=\langle x^2\rangle_a+\langle x^2\rangle_b-2\langle x^2\rangle_a\langle x^2\rangle_b\mp2\vert\langle x\rangle_{ab}\vert$$。不难发现 "identical bosons tend to be somewhat closer together, and identical fermions somewhat farther apart, than distinguishable particles in the same two states. 同时也提醒我们，离得太远的两个电子**波函数根本不交叠**（$$\psi_a$$ 和 $$\psi_b$$ 中必有一个为 0，导致 $$\langle x\rangle_{ab}=0$$），就算电子是费米子，直接按可分辨粒子处理就可以。定域子系，包括可分辨的玻色子和费米子，也按玻尔兹曼统计处理。

## 强简并非定域子系

### 理想玻色气体

1. 玻色-爱因斯坦凝聚(BEC)

   **理想玻色气体**在强简并条件下的一种新**相变**。

   **未完待续**

2. 光子气体

   黑体辐射的粒子观点

   **未完待续**

---

## The BBGKY hierarchy

Scan-reading the irreversibility parts from Kardar's book (particles)...

To find out how the probability evolves with time...

In the previous posts, we considered $$N$$-particle ideal gas, with no interacting terms in the Hamiltonian. Now we take **two-body interactions** into account (but not the ignorable higher-body interaction terms), and get the Hamiltonian of the **weakly interacting gas** 

$$\displaystyle\mathcal{H}(\mathbf{p},\mathbf{q})=\sum_{i=1}^N[\frac{\vec{p_i}^2}{2m}+U(\vec{q_i})]+\frac{1}{2}\sum_{(i,j)=1}^N\mathcal{V}(\vec{q_i}-\vec{q_j})$$.

Consider $$f_s(\vec p_1,...,\vec q_s,t)$$ as the expectation value of finding $$S$$ of the $$N$$ particles at point $$(\vec p_1,...,\vec q_s)$$ in the phase space at time $$t$$.

With the help of dividing the Hamiltonian..., after tedious mathematical derivations... (and some more elaborate math can be find here [PHY526_Sussman](https://www.dmsussman.org/assets/teaching/phys526/3_kineticTheory.pdf)), we have the **time evolution of $$f_s$$** as 

$$\displaystyle\frac{\partial f_s}{\partial t}-\{\mathcal{H_s,f_s}\}=\sum_{n=1}^N\int dV_{s+1}\frac{\partial \mathcal{V(\vec{q_n}-\vec{q}_{s+1})}}{\partial \vec{q}_n}·\frac{\partial f_{s+1}}{\partial\vec{p}_n}$$. 

This is the BBGKY hierarchy.

## The Boltzmann Equation

The above BBGKY hierarchy is too complicated to tell us anything. Consider the **time scales** of different terms under **short-range interactions**, cancel something, 

and the final result is a **closed form equation for $$f_1$$**, as equation (3.41) in Kardar's book. I don't bother to write down.

## The H-theorem and irreversibility

If $$f_1(\vec p,\vec q,t)$$ satisfies the Boltzmann equation, then $$d\Eta/dt\leq 0$$, where

$$\displaystyle\Eta(t)=\int d^3\vec pd^3\vec qf_1(\vec p,\vec q,t)\ln f_1(\vec p,\vec q,t)$$,

which is related to the **[information]() content of the one-particle PDF**. Proved by plugging in the Boltzmann equation.

Key mathematical step for introducing time irreversibility: check Kardar Eq.(3.40). *The assumption of molecular chaos* (factorizing $$f_2$$ as the product of two $$f_1$$) is applied to the "before collision term", but not the "after collision term", since when out of equilibrium, after collision, the coordinates are likely to be more correlated!

## 致谢

感谢多伦多大学物理学院 Yuzheng Xie, Yuchong Li。 

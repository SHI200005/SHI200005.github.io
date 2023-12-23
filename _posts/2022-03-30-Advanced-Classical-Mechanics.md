---
layout: post
title: 理论力学 1.0
categories: BS-NJU-Course-Review-Physics
description: 对于理论力学的回顾
keywords: theoretical mechanics
mathjax: true
---

> 分析力学给出了力学系统在完全一般性的广义坐标下具有不变性是的动力学方程组，并突出了能量函数的意义。分析力学甚至概括了比牛顿力学广泛得多的系统，例如在电气系统、控制系统中的应用就是一个明显的例子。分析力学的数学形式有着极好的性质，它不仅提供了解决天体力学及一系列动力学问题的较佳途径，同时给量子力学的发展提供了启示，最适宜于成为引向现代物理的跳板。其最小作用量原理提供了建立相对论量子力学最简练而富有概括性的出发点。——梁昆淼

才疏学浅的笔者认为这是本科物理学专业必修课中最晦涩的，远超《量子力学》《电动力学》等！

| 学习时间                 | 大二上                                                                    |
| 周课时                     | 3                                                                              |
| 本人成绩                 | 83                                                                            |
| 课程教材                 | 梁昆淼,理论力学(第四版),高等教育出版社,2009 |
| 个人建议参考教材 | 同上                                                                         |
| 先修课程                 | 微积分 力学 电磁学                                                |

其他推荐教材：

1. 鞠国兴,理论力学学习指导与习题解析(第二版),?,? 
2. 朗道,力学(第五版),高等教育出版社,2007 
3. 鞠国兴,朗道《力学》解读,高等教育出版社,2014

本人学习成果评论：本人的理论力学学得简直就是个笑话。脱离了牛顿力学的直观，所谓“虚”“广义”“拉格朗日”“哈密顿”“勒让德”“泊松”等字样令我十分痛苦。在课堂上我自我评价 80% 的时间不知道老师在说什么，所幸课下反复阅读、思考、抄作业答案，终于有了些进步。感谢老师不挂之恩！

**我们为什么还要学习经典力学这种有局限性的结论？**

> 任何逻辑上封闭的的、其真实性再一定精确程度上被实验所证实的理论永远不会失去价值，二是作为特殊情况下成立的近似结果被所有后来更为精确的理论所包含。当然，这不包括那些存在内在矛盾的理论，它们仅在理论物理发展的某一个阶段具有价值。——朗道

注意：鞠老师的习题解与课本习题在序号上并不是对应的，还请看具体指出是课本习题序号还是习题解序号。

版本 2022.03.16,Ver0.1 2022.03.18,Ver0.2 2023.12.20,Ver1.0

## 虚功原理 达朗贝尔原理

### 虚功原理  <span style="color: red;">甩掉约束力</span>

- 概念：几何约束、运动约束、（非）完整约束、（非）定常约束、约束力、主动力。

  **完整约束**：可积分的运动约束与几何约束在物理实质上没有区别，合称为完整约束，e.g. 无滑动的滚动。

- 带有约束的力学问题，按“牛顿方式”来求解时，未知数增多，方程个数相应地增多。

自由度

- 总结：$$n$$ 个质点（位矢为 $$\mathbf r_i$$）的力学系统，若存在着 $$m$$ 个完整约束和 $$k$$ 个非完整约束，那么，质点的直角坐标数 $$N=3n$$，**广义坐标** $$q_i(t)$$ 个数等于 $$s=N-m$$，自由度等于 $$N-m-k$$。对于只存在完整约束的系统（$$k=0$$），广义坐标的个数就是自由度。如果存在非完整约束（$$k>0$$），广义坐标的个数大于自由度。运用广义坐标后，不再需要考虑完整约束，但非完整约束仍需考虑，并应将它用相应的广义速度表示。
- 基础课处理重点：完整系统——约束全是完整约束的系统。

虚位移

- 一切想象的符合约束条件的无限小可能位移定义为虚位移（时间被冻结）

理想约束（以下处理的重点）

- 满足系统**约束力**的**虚功**为 $$0$$（约束力针对系统所有约束力）。$$\delta W=\displaystyle\sum_{i=1}^n\mathbf N_i\cdot\delta \mathbf r_i=0$$.
- 举例：光滑性、刚性、不可伸长性。

**虚功原理**

- 当一个只有理想约束的力学系统处于**平衡**状态时，作用于该系统所有的**主动力**的虚功之总和为零。$$\delta W=\displaystyle\sum_{i=1}^n\mathbf F_i\cdot\delta \mathbf r_i=0$$
- 虚位移有很大任意性 -> 甩掉虚位移  -> 虚位移不独立 换成广义坐标 -> 广义坐标的虚位移 $$\delta\mathbf r_i=\displaystyle\sum_{\alpha=1}^s\frac{\partial\mathbf r_i}{\partial q_\alpha}\delta q_\alpha$$ -> 广义坐标下的虚功原理 -> 广义力（广义力对应广义坐标，而非单个主动力） $$Q_\alpha=\displaystyle\sum_{i=1}^n\mathbf F_i\cdot\frac{\partial\mathbf r_i}{\partial q_\alpha}=0$$ -> 完整约束广义虚位移相互独立 $$Q_\alpha=0$$.
- 解题步骤：判断是否满足理想约束，识别主动力，确定自由度和广义坐标。列所有主动力的虚功为 $$0$$（真实坐标微分），用广义坐标表示真实坐标，算出用广义坐标微分表示的真实坐标微分。若广义坐标相互独立，则令每个广义坐标微分的系数为 $$0$$，解方程。

约束力的求解——[拉格朗日乘子法](https://shi200005.github.io/2021/09/30/Calculus/#%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E4%B9%98%E5%AD%90%E6%B3%95)（虚功原理中约束力被甩掉了，如果要求怎么办？）

- 一开始可以不承认相应的约束条件。换句话说，在选取广义坐标时，可以暂不考虑相应的约束条件。这样选取的广义坐标实际上并不独立，他们之间有相应的约束条件相联系。具体见相关笔记。

  评论：实操起来计算量巨大，我没有一次能独立算对的（逃

### 达朗贝尔原理

- 以上研究的是静力学问题，现在转到动力学问题。代入牛顿第二定律，
- 在理想约束作用下，主动力和达朗贝尔力的虚功之总和为零。$$\displaystyle\sum_{i=1}^n(\mathbf F_i-m_i\ddot{\mathbf r}_i)\cdot\delta \mathbf r_i=0$$.

例：[虚功原理 达朗贝尔原理](https://shi200005.github.io/download_file/ACM_dAlembert.pdf)。

## 拉格朗日动力学

上文把约束力甩掉了，但是我们还想把虚位移甩掉。力学系统在广义坐标描述下所具有的最一般形式的动力学方程——拉格朗日动力学。拉格朗日动力学中，一个力学系统的性质可用单个函数——拉格朗日函数——来概括。

### 拉格朗日方程 <span style="color: red;">甩掉虚位移</span>

对于**静力学**问题，虚位移中的位矢不独立，我们引入与广义坐标相关的**广义力**。在**动力学**问题中，达朗贝尔原理带来的 $$\ddot{\mathbf{r}}_i$$ 怎么处理？

- 拉格朗日关系：对位矢 $$\mathbf r_i=\mathbf r_i(q_1,q_2,...,q_s,t)=\mathbf r_i(q,t)$$ 求导，得 
  
  
  $$
  \frac{\partial\mathbf{\dot{r}_i}}{\partial\dot q_\beta}=\frac{\partial\mathbf{r}_i}{\partial q_\beta}, \\
  \frac{\partial}{\partial q_\beta}(\frac{d}{dt}\mathbf{r}_i)=\frac{d}{dt}(\frac{\partial\mathbf{\dot{r}_i}}{\partial q_\beta}).
  $$
  
- 坐标变换带入达朗贝尔原理，再用拉格朗日关系做变换。对于**完整系统**，广义虚位移独立，每个广义坐标对应的方程为零，得到**拉格朗日方程** $$\frac{d}{dt}\frac{\partial T}{\partial\dot q_\alpha}-\frac{\partial T}{\partial q_\alpha}=Q_\alpha$$，其中 $$T=\displaystyle\sum_{i=1}^n \frac{1}{2}m_i\vert \mathbf{\dot{r}_i}\vert^2$$ 是动能。

- 把广义坐标、广义速度和 $$t$$ 当作**独立**变量，因为考虑的不是实际运动，而是虚幻的所有可能的运动。

拉格朗日函数

- 如果主动力全是**保守力**，存在**势能函数** $$V$$，与广义力的关系为 $$Q_\alpha=-\frac{\partial V}{\partial q_\alpha}$$。定义**拉格朗日函数**（不可观测量）$$L=T-V$$。得到**拉格朗日方程** $$\frac{d}{dt}\frac{\partial L}{\partial\dot q_\alpha}-\frac{\partial L}{\partial q_\alpha}=0$$（您要是实在学不会，把放进大脑 RAM 上考场，应该能混个总评及格）。

  这种类型的拉格朗日方程还可以通过哈密顿原理得到，它是**哈密顿作用量** $$S=\displaystyle\int_{t_1}^{t_2}Ldt$$ 取极值时的欧拉-拉格朗日方程。详见后文变分法。

- **[广义动量](https://shi200005.github.io/download_file/ACM_Generalized_Momentum.pdf)** $$p_\alpha=\frac{\partial L}{\partial\dot q_\alpha}$$ 

  基础课程内主要考虑 $$V$$ 与 $$\dot q_\alpha$$ 无关的情况，于是 $$p_\alpha=\frac{\partial T}{\partial\dot q_\alpha}$$）。这时，类比牛顿力学，拉格朗日方程可读作：广义动量的时间变化率等于广义力。

  广义动量包含了通常的动量、角动量等物理量，它的量纲取决于广义坐标的量纲。
  
- 彩蛋 [为什么拉格朗日量是动能减势能，而不是动能加势能？ - 王俊凯的回答 - 知乎](https://www.zhihu.com/question/544323036/answer/2708198213)

例：[拉格朗日动力学](https://shi200005.github.io/download_file/ACM_Lagrangian.pdf)。

### 诺特定理

运动积分

- 在系统运动过程中，存在 $$q_\alpha$$ 和 $$\dot q_\alpha$$ 的某些函数，它们**不随时间而变**，这些函数成为系统的**运动积分**（守恒律概念的推广）。
  
  广义动量积分
  
  - $$\frac{\partial L}{\partial q_\beta}=0$$（$$q_\beta$$ 是可遗坐标）-> $$\frac{d}{dt}\frac{\partial L}{\partial \dot q_\beta}=0$$ -> 广义动量守恒 $$p_\beta=\text{const}$$ 成为广义动量积分
  
  - 拉格朗日系统并不以牛顿第三定律为先决条件，而是根据某广义坐标是否为可遗坐标，也可以处理电磁场问题（其中质点机械运动动量并不守恒，在拉格朗日函数中计入广义势之后，广义动量包括电磁场的动量，广义动量守恒）。
  
  [广义能量积分](https://shi200005.github.io/download_file/ACM_Generalized_Energy.pdf) $$H=\displaystyle\sum_{\alpha=1}^sp_\alpha\dot q_\alpha-L$$
  
  - $$\frac{dH}{dt}=\frac{\partial L}{\partial t}=0$$.
  - 若 $$\frac{\partial\mathbf r_i}{\partial t}=0$$（定常约束）-> 动能是广义速度的二次齐次式 -> $$H$$ 就是机械能  （齐次函数的欧拉定理参见[多元函数微分学-微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0%E5%BE%AE%E5%88%86%E5%AD%A6)）
  - 关于矢量力学和拉格朗日力学关于机械能守恒条件的区别，见教材 73-74 页。

**诺特定理**

- 德语小知识：th 中的 h 不发音。[Amalie Emmy Noether](https://en.wikipedia.org/wiki/Emmy_Noether), German mathematician.

入门级材料阅读 David Morin "Introduction to Classical Music" Chapter 5 5.6 Noether's Theorem

守恒量 $$I(q,\dot q)=\displaystyle\sum_{k=1}^n\frac{\partial L}{\partial\dot q_k}\frac{d}{d\epsilon}\Phi(q,\epsilon)\vert_{\epsilon=0}$$.

教材原话对于一直到大四的我来说都是相当晦涩和不可接近的，不如直接看 tangible 的[例子](https://shi200005.github.io/download_file/ACM_Noether.pdf)：鞠老师《习题解》的讲义 3.1.2 部分和习题 3.30 3.31（两质点间有势力相互作用，时间平移、空间平移、空间转动拉格朗日函数守恒）。注意诺特定理在变换后与原来不相等的**推广形式**。其中习题 3.31 就是诺特定理的推广形式，时间平移变换所对应的守恒量守恒量就是机械能。

**非完整系统的动力学**在 3.3 节讲解，我懒得看，喜欢花样滑冰的同学可以看一看。

### 拉格朗日力学的推广

例如，带电粒子在电磁场中所受的洛伦兹力 $$\vec v\times\vec B$$ 与速度有关，可以定义磁失势 $$\vec A$$，从而定义广义势能 $$U(q,\dot q,t)=e\varphi-e\vec A\cdot\vec v$$，拉格朗日函数成为 $$L=T-U$$，原来的拉格朗日方程仍成立。此时，研究的守恒量，如广义动量守恒，是不以牛顿第三定律为基础的。

## 有心力 散射问题

关于有心力作用下运动的性质，见[力学 - 有心力](https://shi200005.github.io/2021/10/02/Classical-Mechanics/#%E6%9C%89%E5%BF%83%E5%8A%9B)。

我们关心**两体问题**，因为三体问题是邪恶的（见下文哈密顿力学-泊松括号-泊松定理）。如何在拉格朗日动力学的框架下简化两题问题？重点：理解《力学》中讨论过的[质心系](https://shi200005.github.io/2021/10/02/Classical-Mechanics/#%E8%B4%A8%E7%82%B9%E7%B3%BB%E5%8A%A8%E5%8A%9B%E5%AD%A6%E7%9A%84%E8%BF%90%E5%8A%A8%E5%AE%9A%E7%90%86)。

> 采用直角坐标系研究质心的运动，采用极坐标系研究第二个质点相对于第一个质点的相对运动......得到拉格朗日函数 $$L=\frac{1}{2}m_0(\dot x_0^2+\dot y_0^2+\dot z_0^2)+\frac{1}{2}m^\prime(\dot\rho^2+\rho^2\dot\varphi^2)-V(\rho)$$.  其中 $$m_0$$ 是质心质量，$$m^\prime$$ 是约化质量。

观察拉格朗日函数，显然质心动量能量守恒，甩掉。相对运动具有

- $$\varphi$$ 是可遗坐标，质点相对于极点的角动量守恒 $$h=\rho^2\dot\varphi$$.
- $$L$$ 不显含时间，机械能守恒 $$E^\prime=\frac{1}{2}m^\prime\dot\rho^2+\frac{1}{2}m^\prime\frac{h^2}{\rho^2}+V(\rho)$$. 通常称 $$V_{\text{eff}}(\rho)=\frac{1}{2}m^\prime\frac{h^2}{\rho^2}+V(\rho)$$ 为有效势能，用于研究相对径向的运动。

> 与可遗坐标对应的广义动量守恒，给解算带来不少方便，可遗坐标的个数越多，自然就越方便。同一个问题，由于广义坐标选取方法不同，可遗坐标的有无或个数随之就不同。例如，研究有心力问题时，如果选用直角坐标，那就没有一个可遗坐标，但如果变化到平面极坐标系，则极角 $$\varphi$$ 就是可遗坐标。（9.1.1 正则变换的条件）

有了这两个关系，参见 4.1 节，不难求出**轨道方程**，但是我们也不必从有效势能出发，可以用**比内公式**做个转化，直接从相互作用力的形式出发，求出轨道方程。

平方反比力给出的轨道方程是圆锥曲线。

### 引力 开普勒行星运动定律

著名平方反比引力：万有引力。引力情况离心率大于还是小于 1 对应相对运动机械能是正还是负。轨道方程 $$\rho=\frac{p}{1+\epsilon\text{cos}(\sigma+C)}$$，其中离心率 $$\epsilon=\sqrt{1+\frac{2E^\prime h^2m^\prime}{m^2k^4}}$$

平方反比引力下的椭圆轨道：半长轴 $$a=\frac{mk^2}{2\vert E^\prime\vert}$$、半短轴 $$b=h\sqrt{\frac{m^\prime}{2\vert E^\prime\vert}}$$、能量 $$E^\prime=-\frac{mk^2}{2a}$$。

引力下的圆轨道：稳定性 $$\frac{F^\prime(r_0)}{F(r_0)}+\frac{3}{r_0}>0$$ -> 稳定。星际航行怎么行。

### 斥力 散射问题

斥力情况（由于在两题问题中规定距离无穷远相互作用势能为 0）相对运动机械能必为正，离心率必大于 1，也就对应双曲线轨道。

卢瑟福 α 粒子散射实验：先用套路在质心系求解相对运动散射角 $$\theta$$，然后转化到静止（实验室）坐标系求散射角 $$\Theta$$。关于散射后的例子关于散射角 $$\theta$$ 的分布，导出**散射截面**的**卢瑟福公式** $$\sigma(\theta)=\frac{1}{4}(\frac{ZZ^\prime e^2}{2eE^\prime})\frac{1}{\text{sin}^4\frac{\theta}{2}}$$。然后问题来了，怎么转化成实验室坐标系下的散射截面 $$\sigma(\Theta)$$？太复杂了！不过别担心，卢瑟福的实验里金原子核和 $$\alpha$$ 粒子的质量差别很大，来个近似。

### 位力定理（Virial Theorem）

> The word **virial** for the right-hand side of the equation derives from *vis*, the [Latin](https://en.wikipedia.org/wiki/Latin) word for "force" or "energy", and was given its technical definition by [Rudolf Clausius](https://en.wikipedia.org/wiki/Rudolf_Clausius) in 1870.[[1\]](https://en.wikipedia.org/wiki/Virial_theorem#cite_note-1) ---[Wikipedia](https://en.wikipedia.org/wiki/Virial_theorem)

梁老师书中把这个定理放在哈密顿力学刘维尔定理之后，但我不是很明白和哈密顿动力学有什么关联，我个人把它放在这里。

$$S=\displaystyle\sum_{i=1}^n\mathbf K_i\cdot\mathbf r_i$$ 有界（$$\mathbf K_i$$ 指动量），取 $$\displaystyle\lim_{\tau\rightarrow\infty}\langle\frac{dS}{dt}\rangle$$，得 $$\langle T\rangle=-\frac{1}{2}\langle\displaystyle\sum_{i=1}^n\mathbf F_i\cdot\mathbf r_i\rangle$$。

【GRAD-UPDATE】研究随机过程统计量的系综平均用到的数学手段也很像，详见 [(En) hilfinger2011separating](https://shi200005.github.io/2023/10/02/hilfinger2011separating/)。

例：两粒子有心力 $$r^n$$ 作用，势能满足 $$V=kr^{n+1}$$，位力定理给出 $$\langle T\rangle=\frac{n+1}{2}\langle V\rangle$$。对于平方反比有心力，$$T=-\frac{1}{2}\langle V\rangle$$。解答了我高中时代的疑惑。

例：推导[理想气体压强方程](https://shi200005.github.io/2022/02/24/Thermodynamics/#%E7%83%AD%E5%8A%9B%E5%AD%A6%E7%AC%AC%E9%9B%B6%E5%AE%9A%E5%BE%8B) $$pV=nkT$$。

## 小振动

相对简单的一章。

把拉格朗日函数在平衡位置附近展开，保留二阶近似（现在不是很明白教材里“拉格朗日方程缺只是一阶近似”是啥意思）。

概念：简正坐标、简正频率、模式。无需赘述。

[小振动的一般理论 - 矩阵表述](https://shi200005.github.io/download_file/ACM_Oscillations.pdf)。其中教材 5.3.5 节写道，$$\hat M$$ 与 $$\hat K$$ 是两个对称矩阵，而且 $$\hat M$$ 是正定的，于是按照**矩阵理论**，一定可以找到一个实的非奇异满秩代换使 $$\hat M$$ 和 $$\hat K$$ 同时对角化。请问这个矩阵理论在哪？参见 Theorem 7.6.1, Horn, Roger A.; Johnson, Charles R. (2013). *Matrix Analysis, second edition*. Cambridge University Press。

## 哈密顿力学

>拉格朗日动力学用广义坐标和广义速度描写力学系统的运动，哈密顿动力学则用**广义坐标**和**广义动量**描写力学系统的运动，后者与广义坐标的量纲无关，总是作用量（能量 $$\times$$ 时间的量纲）。而量子论的量子化条件正是把**作用量**加以量子化。可见哈密顿动力学可作为从经典力学到量子力学的“跳板”。

### 哈密顿正则方程

<span style="color: red;">此部分下文均讨论只有**完整约束**，并且**主动力**都是**具有势能或广义势能**的，</span>即拉格朗日方程为 $$\frac{d}{dt}\frac{\partial L}{\partial\dot q_\alpha}-\frac{\partial L}{\partial q_\alpha}=0$$。

**勒让德变换**：利用复合函数微分法则（参见[微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0%E5%BE%AE%E5%88%86%E5%AD%A6)），$$L(q,\dot q,t)$$ -> $$\bar L(q,p,t)$$，运动规律微分方程（原为拉格朗日方程）如何改变？构造 $$H=\displaystyle\sum_{\beta=1}^sp_\beta\dot q_\beta-L$$，这个 $$H$$ 我们曾在“运动积分”见过的，然而独立变量的选择发生了改变。运动规律成为看起来很好看的**哈密顿正则方程**。哈密顿力学中，以广义动量、广义坐标、时间为变量的系统中，运动规律由哈密顿正则方程给出。
$$
\begin{cases}
\frac{\partial H}{\partial q_\alpha}=-\dot p_\alpha \\
\frac{\partial H}{\partial p_\alpha}=\dot q_\alpha	\quad(\alpha=1,2,...,s).
\end{cases}
$$

- P.S. “正则”的意思是形式简单而对称。对称到打字靠复制粘贴再改改都很方便。
- 勒让德变换请见教材 7.1.2，在[热力学 - 麦克斯韦关系](https://shi200005.github.io/2022/02/24/Thermodynamics/#%E5%9D%87%E5%8C%80%E7%B3%BB%E7%9A%84%E5%B9%B3%E8%A1%A1%E6%80%A7%E8%B4%A8)的推导中很重要。

例：[哈密顿力学](https://shi200005.github.io/download_file/ACM_Hamiltonian.pdf)。

### 刘维尔定理

在经典力学问题求解中，如果用哈密顿力学求解，总是逃不开拉格朗日函数的求解。那么我们为什么要用哈密顿力学呢？对于这个问题，梁昆淼老师在其《理论力学》教材第 7-9 章深入探讨。从一切可能运动的拉格朗日函数 $$L(q,\dot q,t)$$ 出发（拉格朗日动力学）或从一切可能运动的哈密顿函数 $$H(q,p,t)$$ 出发（哈密顿动力学），此时 $$q$$ 和 $$\dot q$$ 相互独立，$$q$$ 和 $$p$$ 也相互独立。但是进入虚位移求实际运动时 $$\dot q$$ 就不再独立于 $$q$$（我的理解是”关联“指的就是拉格朗日方程？），然而 $$p$$ 却独立于 $$q$$（这句话详见下文**哈密顿原理**部分）。于是拉格朗日动力学在 $$s$$ 维位形空间研究，哈密顿力学在 $$2s$$ 维位形空间中研究。

[统计物理 - 统计系综理论](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/#%E7%BB%9F%E8%AE%A1%E7%B3%BB%E7%BB%BC%E7%90%86%E8%AE%BA)（刘维尔定理）。把广义坐标和广义动量当作直角坐标而构成 $$2s$$ 维的空间叫做相空间。哈密顿正则方程的重要性：刘维尔定理是 $$2s$$ 维的相空间中的定理，在普通空间或 $$s$$ 维的位形空间中并不存在类似的定理。

### 泊松括号

把任意力学量用广义坐标和广义动量表示，$$\varphi(p,q,t)$$。两个力学量的**泊松括号**为 $$[\varphi,\psi]=\displaystyle\sum_{\alpha=1}^s(\frac{\partial\varphi}{\partial q_\alpha}\frac{\partial\psi}{\partial p_\alpha}-\frac{\partial\varphi}{\partial p_\alpha}\frac{\partial\psi}{\partial q_\alpha})$$。

于是，力学量随时间变化率 $$\frac{d\varphi}{dt}=\frac{\partial\varphi}{\partial t}+[\varphi,H]$$。

基本泊松括号 $$[q_\alpha,q_\beta]=0$$，$$[p_\alpha,p_\beta]=0$$，$$[q_\alpha,p_\beta]=\delta_{\alpha\beta}$$。

#### 泊松定理 可积系统

运动积分 $$\varphi$$ 满足 $$\frac{d\varphi}{dt}=0$$ 即 $$[\varphi,H]=-\frac{\partial\varphi}{\partial t}$$。

雅可比恒等式 $$[\varphi,[\psi,\theta]]+[\psi,[\theta,\varphi]]+[\theta,[\varphi,\psi]]=0$$。

泊松定理：若 $$\varphi$$ 和 $$\psi$$ 都是运动积分，将它们和 $$H$$ 代入雅可比恒等式，得到 $$[\varphi,\psi]$$ 也是运动积分。

> 刘维尔定理：对于有 $$s$$ 个自由度的力学系统，如果可以找到 $$s$$ 个相互独立的运动积分 $$\phi_1,\phi_2,...,\phi_s$$，且满足 $$[\phi_\alpha,\phi_\beta]=0(\alpha,\beta=1,2,...,s)$$，这样的系统称为**可积系统**，此时称 $$\phi_1,\phi_2,...,\phi_s$$ 是相互**对合**的。
>
> 系统可积时，其哈密顿函数属于运动积分之一或者可以用它们表示出来，而系统的运动方程可以通过积分的方法求解。

具体证明书上没写我也没自己推导，相关词条：[Integrable system](https://en.wikipedia.org/wiki/Integrable_system)、[Liouville–Arnold theorem](https://en.wikipedia.org/wiki/Liouville%E2%80%93Arnold_theorem)。

可积系统举例：对称重刚体的定点运动、各向同性有心力作用下的质点、保守完整的小振动系统......

不可积系统举例：绝大多数多体问题，e.g., 著名的三体问题。

> 可积系统的运动是确定论性的，即给定初始条件就可以知道系统过去和未来的运动情况；同时，如果初始条件有微笑得到变化，则系统的运动情况在变化前后的差别也是微小的，也就是运动轨道是稳定的；可积系统的运动限制在相空间的 $$s$$ 维环面上做规则运动。——10.5

#### 量子力学  量子泊松括号（对易子）

正则量子化 $$[X,Y]\rightarrow\frac{1}{i\hbar}[\hat X,\hat Y]=\frac{1}{i\hbar}(\hat X\hat Y-\hat Y\hat X)$$。

[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/)中的两个力学量 $$\hat X$$ 和 $$\hat Y$$ 是否可以同时具有确定的值就看它们的量子泊松括号 $$\frac{1}{i\hbar}(\hat X\hat Y-\hat Y\hat X)$$ 是否为零。

## 力学变分原理

Significance: 见梁老师本章引言。

### 变分法初步

一般地说，一个变量 $$J$$，如果其取值取决于函数关系 $$y=y(x)$$，就叫做函数 $$y(x)$$ 的**泛函**，记作 $$J[y(x)]$$。求泛函的极值问题就叫做**变分**问题。把变分问题转化为求解微分方程——**欧拉方程**。欧拉方程是变分问题所必须满足的**必要条件**。需要满足约束条件时，用拉格朗日乘子法处理欧拉方程。

一个简单的例子：$$J[y(x)]=\displaystyle\int_a^bF(x,y,y^\prime)dx$$，假设边界不变 $$\delta y\vert_a^b=0$$，则 $$J[y(x)]$$ 取极值（$$\delta J[y]=\displaystyle\int_a^b[\frac{\partial F}{\partial y}-\frac{d}{dx}(\frac{\partial F}{\partial y^\prime})]\delta ydx=0$$）的必要条件是 $$\frac{\partial F}{\partial y}-\frac{d}{dx}(\frac{\partial F}{\partial y^\prime})=0$$，或 $$\frac{\partial F}{dx}+\frac{d}{dx}(y^\prime\frac{\partial F}{\partial y^\prime}-F)=0$$。详情请见[力学变分原理](https://shi200005.github.io/download_file/ACM_Functional.pdf)。多变量推广、高阶导推广、有约束推广......

### 哈密顿原理

哈密顿原理：力学系统的动力学归结为一个变分原理：力学系统从时刻 $$t_1$$ 到时刻 $$t_2$$ 的一切可能运动之中，使**哈密顿作用量** $$S=\displaystyle\int_{t_1}^{t_2}L(t,q,\dot q)dt$$ 取极值的运动才是实际发生的运动。

- 位形空间的哈密顿原理：$$\delta \displaystyle\int_{t_1}^{t_2}L(q,\dot q,t)dt=0$$ <-> $$\displaystyle\int_{t_1}^{t_2}\displaystyle\sum_{\alpha=1}^s(\frac{d}{dt}\frac{\partial L}{\partial\dot q_\alpha}-\frac{\partial L}{\partial q_\alpha})\delta q_\alpha=0$$（拉格朗日方程）.

- 相空间的哈密顿原理：$$\delta \displaystyle\int_{t_1}^{t_2}[\displaystyle\sum_{\alpha=1}^s p_\alpha\dot q_\alpha-H(p,q,t)]dt=0$$ <-> $$\displaystyle\int_{t_1}^{t_2}\displaystyle\sum_{\alpha=1}^s [(\dot q_\alpha-\frac{\partial H}{\partial p_\alpha})\delta p_\alpha-(\dot p_\alpha-\frac{\partial H}{\partial q_\alpha})\delta q_\alpha]dt=0$$（哈密顿正则方程）.

- 位形世界的哈密顿原理

  将时间 $$t$$ 看作和广义坐标 $$q$$ 地位平等的变量，$$t$$ 相当于第 $$s+1$$ 个广义坐标，这 $$s+1$$ 个广义坐标构成了推广的**位形世界**。......**参数** $$\tau$$，$$\dot q_\alpha=\frac{q_\alpha^\prime}{t^\prime}$$......

  修改的拉格朗日函数 $$\Lambda=L(q,t,\frac{q^\prime}{t^\prime})t=\Lambda(q,t,q^\prime,t^\prime)$$，于是哈密顿原理成为 $$\delta\int\Lambda d\tau=0$$。

### 最小作用量原理

> 实际上，还有其他形式的最小作用量原理和哈密顿原理相似，最小作用量的名称并不意味着真是运动的作用量永远是最小，而只说明，真实运动的作用量稳定值。只有当积分长度是一个相当小的有限量时，真实运动的作用量才取极小值。

如果拉格朗日函数 $$L$$ 不显含时间（保守系统），修改后的拉格朗日函数 $$\Lambda$$ 中 $$t$$ 是可遗坐标......-> $$\Delta\int\displaystyle\sum_{\alpha=1}^sp_\alpha\dot q_\alpha dt=0$$ **雅可比最小作用量原理**

> 在 $$\Delta$$ 的变分中，考虑的时哈密顿函数 $$H$$ 守恒的一切可能的运动（但它们的 $$H$$ 各不相同）。这样，$$t$$ 不再可以任意给定，时间 $$t$$ 的变分 $$\Delta t$$ 不为零，特别是在两端点。

对于一般的力学系统 $$\Delta\int vds=\Delta\int\sqrt{2(E-V)}ds=0$$。

力学以外的变分原理：[几何光学](https://shi200005.github.io/2022/02/25/Optics/)中也有条变分原理，即费马原理 $$\delta\int\frac{1}{u}ds=\frac{1}{c}\delta\int nds=0$$。几何光学是波动光学的短波长极限，这就启发我们也可以把经典力学当作某种波动力学的短波长极限。

## 正则变换 哈密顿-雅可比方程

**揭示了向量子力学的过渡......**

### 正则变换

哈密顿原理 $$\delta \displaystyle\int_{t_1}^{t_2}L(q,\dot q,t)dt=0$$（位形空间中）或者 $$\delta \displaystyle\int_{t_1}^{t_2}[\displaystyle\sum_{\alpha=1}^s p_\alpha\dot q_\alpha-H(p,q,t)]dt=0$$（相空间中），被积函数如果加上初末值给定的一个时间全微分 $$U$$，则变分为 $$\delta\displaystyle\int_{t_1}^{t_2}\frac{dU}{dt}dt=0$$，并不改变动力学方程。

我们希望对哈密顿函数里的广义坐标和广义动量做变换，


$$
\begin{cases}
P_\alpha=P_\alpha(p,q,t)\\
Q_\alpha=Q_\alpha(p,q,t)\quad(\alpha=1,2,...,s).
\end{cases}
$$


得到一个与之等价的函数 $$K(P,Q,t)$$，变换后满足的变分原理与原来等价，


$$
\begin{cases}
\delta \displaystyle\int_{t_1}^{t_2}[\displaystyle\sum_{\alpha=1}^s p_\alpha\dot q_\alpha-H(p,q,t)]dt=0\\
\delta \displaystyle\int_{t_1}^{t_2}[\displaystyle\sum_{\alpha=1}^s P_\alpha\dot Q_\alpha-K(P,Q,t)]dt=0.
\end{cases}
$$


如何实现？按照上面的说法，$$(\displaystyle\sum_{\alpha=1}^s p_\alpha\dot q_\alpha-H)-(\displaystyle\sum_{\alpha=1}^s P_\alpha\dot Q_\alpha-K)=\frac{dU}{dt}$$，即 $$\displaystyle\sum_{\alpha=1}^s p_\alpha dq_\alpha-\displaystyle\sum_{\alpha=1}^s P_\alpha dQ_\alpha+(K-H)=dU$$ 即可，这就是**正则变换**。<span style="color: red;">我们希望经过这个变换，能变换出来尽可能多的可遗坐标和相应守恒的“广义动量”。</span>

怎么变？书上例子已经很清楚了。应用[勒让德变换](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0%E5%BE%AE%E5%88%86%E5%AD%A6)把宗量给变了。概念：母函数。

**泊松括号不变性**：在正则变换下，$$[\varphi,\psi]_{pq}=[\varphi,\psi]_{PQ}$$。

**无限小正则变换**我还没想好怎么概括比较好，先把梁老师的黑体结论扔上来。

1. 力学系统的正则变量在时刻 $$t$$ 的值，可由其初始值（常数）通过正则变换得出，这正则变换是时间 $$t$$ 的函数。
2. $$dH=\epsilon[H,G]$$. 检查哈密顿函数在哪些变换下不变，就能确定力学系统的所有运动积分！
3. 例子：有心力作用下的哈密顿量 $$H$$ 取绕某轴转动的角动量为母函数 $$G$$，算得 $$[H,G]=0$$。

### 哈密顿-雅可比方程

如何找到上文中能把正则变量都变成常数（初始值）的正则变换？我们希望 $$K(P,Q,t)=0$$，正则方程就保证了正则变量是常数作为变换后的“动量”。在哈密顿函数代入 $$K=0$$ 的条件，把原来的一阶 linear system of ODEs 变换为一阶 a nonlinear PDE，这就是**哈密顿-雅可比方程**，方程的解叫做**哈密顿主函数** $$S$$，其实就是拉格朗日函数 $$S=\displaystyle\int_{t_1}^{t_2}Ldt$$。

当 $$H$$ 不显含时间，可以把哈密顿-雅可比方程的控件变量与 $$t$$ 分离，令 $$S(q,P,t)=W(q,P)+f(t)$$，得到 $$H(q,\frac{\partial W}{\partial t})=-f^\prime(t)=E$$。也称前面这个方程为**哈密顿-雅可比方程**，$$W(q,P)$$ 为**哈密顿特征函数**。

一种特殊的可积系统（见[泊松定理](https://shi200005.github.io/2022/03/30/Advanced-Classical-Mechanics/#%E6%B3%8A%E6%9D%BE%E5%AE%9A%E7%90%86)）：完全可分离的系统，哈密顿函数是 $$s$$ 个独立部分的和， $$H(q_1,...,q_s,p_1,...,p_s)=\displaystyle\sum_{\alpha=1}^s H_\alpha(q_\alpha,p_\alpha)$$。

书中给出了一些用哈密顿-雅可比方程对力学系统进行正则变换求解然后再变回去的例子。其中谐振子的问题很有意思。早在高中学量子力学初步时，我们记忆了“速度和动量不可同时测准，能量和时间不可同时测准”，到[近代物理](https://shi200005.github.io/2022/07/15/Modern-Physics/)，谈论到为什么能量和时间也是一对共轭变量时，用的是光衍射条纹说明。这个打发高中生可以，打发本科生就不太行了。在这个例子里我们发现，能量和时间其实就是对系统做正则变换后的一对共轭变量，其实就是变换后的哈密顿函数的一对“动量”和“坐标”。也就给了我们一点点 taste。

在平方反比有心吸引力的例子里，提到哈密顿-雅可比方法总是直接给出轨道。

### 作用量变量与角变量

物理学中的**周期性运动**中，我们关注其**频率**。分为**天平动**和**转动**（回忆单摆相图）。现只讨论哈密顿特征函数 $$W$$ 可分离为 $$\displaystyle\sum_{\alpha=1}^s W_\alpha(q_\alpha;E,C_2,...,C_s)$$ 的情况。变换后的“动量”常数取为**作用量** $$J_\alpha=\oint p_\alpha dq_\alpha$$（对一个周期积分），$$J_\alpha$$ 只是积分常数 $$E,C_2,...,C_s$$ 的函数，于是 $$\displaystyle\sum_{\alpha=1}^s W_\alpha(q_\alpha;J_1,J_2,...,J_s)$$。把 $$J_\alpha$$ 的共轭变量 $$\omega_\alpha$$ 叫做**角变量**满足 $$\dot\omega_\alpha=\frac{\partial E}{\partial J_\alpha}$$，是 $$q_\alpha$$ 周期运动的频率。

例：一维谐振子。$$E=(\frac{1}{2\pi}\sqrt{\frac{k}{m}})J$$。**量子力学过渡**：量子化作用量 $$J=nh(n=0,1,2,...)$$，则 $$E=n\frac{h}{2\pi}\omega$$。

例：平方反比有心力吸引下的质点周期运动频率。延申：各个坐标周期运动如果有不同的运动频率......

### 正则微扰理论

> 在力学中，有许许多多的问题是无法精确求解的。但是经常遇见这样的情况，这些无法精确求解的问题与能够严格求解的问题之间，仅有微笑的差别，因而可以在后者严格解的基础上近似求解前者，这就是**微扰理论**。建立在正则变换基础上的正则微扰理论就是微扰理论的一种。

$$H=H_0+\epsilon H^\prime$$。蒙上眼睛不看微扰，解 $$H_0$$ 假定可以按哈密顿-雅可比方程求解出主函数 $$S(q_1,q_2,...,q_s;\frac{\partial S}{\partial q_1},\frac{\partial S}{\partial q_2},\frac{\partial S}{\partial q_s};t)$$，解出 $$S(q_1,q_2,...,q_s;\alpha_1,\alpha_2,...,\alpha_s;t)=0$$ 一堆积分常数 $$\alpha_\alpha,\beta_\alpha$$ 满足 $$\frac{\partial S}{\partial \alpha_\alpha}=\beta_\alpha$$。现在考虑微扰，这些常数就不在是常数，但是以 $$S$$ 为母函数，正则变换的关系不变，原来求出来的常量是正则变量，满足正则方程 


$$
\begin{cases}
\dot\alpha_\alpha=-\frac{\partial(\epsilon H^\prime)}{\partial\beta_\alpha},\\
\dot\beta_\alpha=-\frac{\partial(\epsilon H^\prime)}{\partial\alpha_\alpha}.
\end{cases}
$$


满足以微扰函数 $$\epsilon H^\prime$$ 为哈密顿函数的正则方程。这个方程一般称为**微扰方程**。

### 从“几何力学”到“波动力学”

先自己看看吧，我有的东西需要再看看再写。


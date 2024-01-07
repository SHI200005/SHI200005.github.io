---
layout: post
title: 电磁学 1.0
categories: BS-NJU-Course-Review-Physics
description: 电动力学前先来点
keywords: Electromagnetism
mathjax: true
---

The author wrote an physics article that pointed out a mathematical flaw of "Answers to 1000 Electromagnetic Problems (电磁学千题解) 2.1.45", the most authorized problem set on electromagnetism in China. The article won the first prize (~7%) of the 24th Basic Subject Forum (第24届基础学科论坛) on Sept 3, 2021. [Here is the link of the announcement](https://mp.weixin.qq.com/s/jYr5Fe89pT9xQCqE7lS8qw). This is such a accomplishment that I have to pin it in English on my website!

| 课程名称                | 电磁学                                                    |
| 学习时间                | 大二上                                                     |
| 周课时                    | 3                                                              |
| 本人成绩                | 93                                                            |
| 课程教材                | 徐游《电磁学》科学出版社                  |
| 个人建议参考教材 | 张之翔《电磁学千题解》科学出版社  |
| 先修课程                | 微积分 线性代数                                    |

版本 2021.11.20 Ver0.1, 2022.07.27 Ver0.1.1, 2024.01.05 Ver1.0

学过[数学物理方程](https://shi200005.github.io/2022/03/28/Partial-Differential-Equations/)之后再看看狂刷《千题解》的历程，感觉其中很多 cumbersome 的逻辑论述 formalize 在球坐标和柱坐标的 PDE 求解中（因为静电场方程就是泊松方程），所以自作主张略去这些 cumbersome 的逻辑论述，全部用 PDE 求解。

刘老师在课件中加入了过多之后课程的拓展，尤其是可怕的 PDE 相关，这一点只是让我们很 overwhelmed。整体来说，这门课很有挑战性，我很喜欢上。学习电磁学使我快乐。

## 矢量运算预备知识

矢量的标积（做功）、矢积（平行四边形有向面积）、混合积（平行六面体体积）

轴矢量与极矢量
 - 极矢量：镜面垂直量反向  e.g., 空间位矢、电场、电偶极矩等
 - 轴矢量：镜面平行量反向  e.g., 磁矩、磁感应强度等
 - 极矢量 $$\times$$ 极矢量 $$=$$ 轴矢量

立体角

- $$dΩ=\frac{dScosθ}{r^2}$$  

  如同平面角转完整个平面是 $$2\pi$$，不难从定义中看出，立体角转完整个空间是 $$4\pi$$。

正交曲线坐标系（直角坐标系、球坐标系、柱坐标系）与场论  见[微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E9%AB%98%E6%96%AF%E5%85%AC%E5%BC%8F%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F%E6%96%AF%E6%89%98%E5%85%8B%E6%96%AF%E5%85%AC%E5%BC%8F)

## 真空中固定点电荷的电场

### 电荷守恒

### 库仑定律

$$\vec F_{21}=\frac{1}{4\pi\epsilon_0}\frac{q_1q_2}{r_{21}^3}\vec r_{21}$$ 中学的时候学的系数是 $$k$$，现在为啥变成 $$\frac{1}{4\pi\epsilon_0}$$？方便后面高斯定理积分。

满足叠加原理

适用条件

- 真空、点电荷、静止

- 点电荷相对静止，且相对观察者也静止

- 可以拓宽到静源 & 动电荷，不能延拓到动源 & 静电荷

- 作为动源，有推迟效，与牛顿第三定律矛盾？这啥玩意来着？见 Ver 0.2 补充吧。或者说见电动力学，笔者将阅读朗道《场论》。（没毕业的我在说什么？毕业的时候还没看，书早送人了。。。）

  看作一个电荷泡在另一个电荷的场里。如果场源电荷在动，则要考虑场动量。

  pending！！！！！！

 - 例：均匀带电圆环/圆面等轴方向电场 -> 无限大均匀带电圆面产生匀强电场 $$E=\frac{\sigma}{2\epsilon_0}$$，其中 $$\sigma$$ 是带正电圆面的面电荷密度 -> 利用叠加原理，无限大**平行板电容器**板间电场 $$E=\frac{\sigma}{\epsilon_0}$$，其余电场是 0，只要够大，中间就可以看成匀强电场

- 例：均匀带电球面

  结论：球内电场为 0，球外电场如同点电荷在球心（开头笨人获奖论文的建模依据）。

 - 19 - 20 秋 期中试题：推导旋度为 0 与有心力场的等价性。
 - 1.2.29 电荷以 $$cosθ$$ 的电荷密度分布于球面，则球内部为匀强电场。这个场景在[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E8%BD%B4%E5%AF%B9%E7%A7%B0%E7%90%83%E5%87%BD%E6%95%B0---%E5%8B%92%E8%AE%A9%E5%BE%B7%E5%87%BD%E6%95%B0)中会再次出现 -> 勒让德多项式。

#### 电偶极子

等量异号点电荷对 $$q$$，负电荷指向正电荷适量 $$\vec l$$，电偶极矩为 $$\vec p=q\vec l$$。

推导中，所求点与两电荷距离远大于两电荷间距离，因此我们可以使用一些**泰勒展开**的近似处理库仑定律的分母项~ 结论：电偶极子产生的电势是 $$\Phi(\vec{r})=\frac{1}{4\pi\epsilon_0}\frac{\vec{p}·\vec{r}}{r^3}$$. 梯度是电场 $$\vec E=\frac{1}{4\pi\epsilon_0}(-\frac{\vec p}{r^3}+\frac{3(\vec p\cdot\vec r)\vec r}{r^5})$$.

极坐标求解：见课件 01-P147 附近。或数学物理方法教材。

- 补充：对于电荷面密度为 $$\sigma_e$$ 的电偶极层，电偶极子微元 $$dS$$ 施加给空间 $$P$$ 点的电势为 $$U(P)\vert_{dS}=-\displaystyle\frac{\sigma_el}{4\pi\epsilon_0}d\Omega$$  -> $$\vec E\vert_{dS}=\displaystyle\frac{\sigma_el}{4\pi\epsilon_0}\nabla\Omega$$。与后面安培环路定理的推导类似。后续将作为建立等效磁荷理论的基础。

### 高斯定理、环路定理

高斯定理 $$\oint_S\vec{E}·d\vec{S}=\frac{1}{\epsilon_0}\displaystyle\sum_{S内}Q$$ (discrete version) $$=\frac{1}{\epsilon_0}\displaystyle\int_{S内}\rho d\tau$$ (continuous version) 

 - 库仑定律 + 叠加原理 <--> 高斯定理 + 环路定理  其中**环路定理等价于库仑力是有心力** 证明见课件 01-10

## 导体周围的静电场、静电能量

### 导体静电平衡条件

均匀导体**内部场强处处为零**、每个均匀导体都是**等势体**（定性分析 -> **尖端效应**）、电荷静止不动（宏观）、导体**外侧**电场强度**垂直**于导体表面。（满足 高斯定理 + 环路定理） 导体电平衡弛豫时间极短

 - 利用高斯定理导出导体表面电场与电荷分布。重要习题：千题解 [2.1.37] $$E=\frac{σ}{ε_0}$$，千题解 [2.1.38] 导体单位面积所受的力 $$f=\frac{σ^2}{2ε_0}$$。

   confusion：为啥导体表面电场强度是 $$E=\frac{σ}{ε_0}$$，前文用库仑定律推无限大带电圆面在空间中电场强度 $$E=\frac{σ}{2ε_0}$$？请想，无限大带电圆面两侧电场强度都是 $$E=\frac{σ}{2ε_0}$$，但是导体电荷都在表面，外侧有垂直于表面的电场，内侧电场强度是 0。也就是说，可以把无限大带电导体圆面看成两侧表面面电荷密度都是 $$\frac{\sigma}{2}$$，就没问题了。

 - 徐游 P77 平行板电容器。P.S. 当两个极板所带电量的绝对值不等时，公式中的 $$Q$$ 应为用导线将两极板相连时自正极板流向负极板的电荷。

 - 应用：[范德格拉夫起电机](https://en.wikipedia.org/wiki/Van_de_Graaff_generator#Description)。注意，这是范德格拉夫，不是热力学里的范德瓦尔斯，更不是范德格瓦斯。

### 静电边值问题唯一性定理

边界条件可将静电场的空间分布唯一地确定下来。即给定边界条件后，不可能存在不同的静电场分布。19 - 20 秋 期中试题。静电学泊松方程唯一性定理可以看南大现工院李涛老师[课件](https://dsl.nju.edu.cn/litao/electrodynamics/Ch2-b.pdf)，李涛老师也是学物理出身的。

电像法。Justified by 静电边值问题唯一性定理

 - 例：无限大接地导体板对点电荷产生感应电荷的面电荷分布和空间电场分布。千题解 2.1.45 的答案错误，笨人已用论文严谨论述。

### 真空静止电荷系能量

$$W=\frac{1}{2}\displaystyle\int_V\rho Ud\tau+\frac{1}{2}\displaystyle\int_S\sigma UdS$$，从移动电荷静电力做功的功能转化角度，$$\frac{1}{2}$$ 来自静电力做功对称性。

平行板电容器能量  $$W=\frac{1}{2}CU^2$$  ->  真空电场能量密度：$$w=\frac{1}{2}\epsilon_0E^2$$，严格证明见**电动力学**（还没写）。

## 电介质

![Electromagnetism_Dielectric](\images\blog\Electromagnetism_Dielectric.JPG)

19 - 20 秋期中 试题：平行板电容器对电介质是吸引还是排斥？吸引。可以从电介质插入电容器时受力方向和静电能变化（电极电荷不变时静电能下降）两个角度论述。

### 电介质的行为

如果物体内部电子不能像导体里面那样自由移动，而是**束缚**在一定范围内，会怎么样？产生**极化电荷**。

 - 极性分子：分子正负电荷中心不重合。
 - 产生机制：电子位移极化（所有）、分子取向极化（极性分子）、离子位移极化（极性分子） 。后两者效果更明显。
 - 效果：产生**退极化场**，从原来处处电中性变成出现了宏观的极化电荷。
 - 均匀介质：极化电荷出现在介质表面。非均匀介质：可能出现内部体分布。

![Electromagnetism_Dielectric_Ball](\images\blog\Electromagnetism_Dielectric_Ball.JPG)

 - 电介质内与外场相反 电场 = 外电场 + 退极化场（矢量运算）

### 极化强度与极化电荷密度

**极化强度** $$\vec P$$  单位体积电偶极矩 $$\vec p$$ 代数和

- 取一个闭合面 $$\vec S$$，经计算有穿出面元 $$d\vec S$$ 的极化电荷 $$dQ'_{out}=\vec P\cdot d\vec S$$，$$Q'_{out}=\displaystyle\oint_S\vec P\cdot d\vec S$$，则留在闭合面内的极化电荷量是 $$Q'=-\displaystyle\oint_S\vec P\cdot d\vec S$$，$$\rho'=-\nabla\cdot\vec P$$（均匀介质内部 $$\rho'=0$$，只有表面有极化电荷）。
- 那表面极化电荷如何表示？**极化电荷面密度** $$\sigma'=\vec P\cdot \mathbf{\hat n}$$。
- 极化电流密度 pending！！！

### 电感应强度 $$\vec D$$（辅助物理量）

- 把体系中的自由电荷 $$Q_0$$ 也考虑进来，则宏观场满足 $$\displaystyle\oint_l\vec E\cdot d\vec l=0$$, $$\displaystyle\oint_S\vec E\cdot d\vec S=\frac{1}{\epsilon_0}\displaystyle\int_V(\rho_0+\rho')d\tau$$ (continuous); $$=\frac{1}{\epsilon_0}\displaystyle\sum_S(Q_0+Q')$$ (discrete); 微分形式 $$\nabla\times \vec E=0$$, $$\nabla\cdot\vec E=\frac{1}{\epsilon_0}{\rho_0+\rho'}$$.
- 由于我们一般能动地给系统加上 $$Q_0$$，然后通过物理学规律求解极化情况，所以构造关于 $$Q_0$$ 的辅助物理量 $$\vec D=\epsilon_0\vec E+\vec P$$，于是 $$\displaystyle\oint_S\vec D\cdot d\vec S=\displaystyle\sum_{S内}Q_0=...$$, $$\nabla\cdot\vec D=\rho_0$$（高斯定理），**没有环路定理**。

**电极化率**与**介电常数**

 - 本课程范围内我们只关注**各向同性线性介质**，关系：$$\vec P=\epsilon_0\chi\vec E$$，于是**电容率** $$\epsilon$$ 有 $$\vec D=\epsilon\vec E=\epsilon_0\epsilon_r\vec E=\epsilon_0(1+\chi)\vec E$$。平行板电容器里插入电介质，电容变成 $$C=\epsilon C_0$$。
 - 例：**电介质分界面**问题：$$\vec E$$ 有**环路定理**，界面两侧**切向**分量相等，可导出 $$\vec D$$ 界面两侧切向分量的关系；若界面无自由电荷，$$\vec D$$ 用**高斯定理**，界面两侧**法向**分量相等，可导出 $$\vec E$$ 界面两侧法向分量的关系。
 - 例：[均匀介质球](https://shi200005.github.io/download_file/PDE_Electric.pdf)。重要结论：**介质球内部的极化场是均匀的**。数学工具见[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E8%BD%B4%E5%AF%B9%E7%A7%B0%E7%90%83%E5%87%BD%E6%95%B0---%E5%8B%92%E8%AE%A9%E5%BE%B7%E5%87%BD%E6%95%B0)。

### 电介质的电场能
$$w=\frac{1}{2}\epsilon E^2$$

 - 例（书P118）：保持平行板电容器电压，将平行板电容器插入液体电介质中，液面会在电容器中上升（原因：电容器边缘效应）。比较液体重力势能增加和电场能增量。

## 稳恒电流场

上面我们考虑电荷不动的情况，下面我们考虑电荷移动的情况。

<img src="\images\blog\Electromagnetism_Current.JPG" alt="Electromagnetism_Current" width="300px;" />

### 连续性方程

电流 $$I=\frac{\Delta q}{\Delta t}=\displaystyle\int_S\vec j\cdot d\vec S$$，其中 $$\vec j$$ 是电流密度矢量  ->  电荷守恒 连续性方程 $$\nabla\cdot\vec j=-\frac{\partial\rho}{\partial t}$$

特殊情况：稳恒电流场 $$\nabla\cdot\vec j=-\frac{\partial\rho}{\partial t}=0$$。

- 由不随时间改变的电荷**分布**而产生，因此仍然可以看成是稳态的、准静态的，电势分布也不随时间改变。高斯定理和环路定理仍然成立。
- 对于稳恒电路，有**基尔霍夫第一定律** $$\sum I_i=0$$。辅以环路定理，构成解决**电工学**（我学过，学得极烂）问题的物理基础。

### 欧姆定律

$$U=IR$$，给出**电阻率**和**电导率**的关系 $$\sigma=\frac{1}{\rho}$$。微分形式：$$\vec E=\rho\vec j$$, $$\vec j=\sigma \vec E$$。经典模型：Drude 模型。

- 千题解链接 [4.2.41] 漏电电容器

## 真空中稳恒电流的磁场

前三章讨论静电场，不关磁场的事。而第四章讨论稳恒电流，电终于动了，磁也就有了。从本章到磁介质，我们关心静磁场。静磁场由稳恒电流产生。

**奥斯特**实验：长直载流导线与之平行放置的磁针受力偏转——**电流的磁效应** one .of the significances: 突破了非接触物体之间只存在有心力的观念。

安培的**分子电流图像**：分子被旋转的电子环绕，是个小磁体。分子电流整齐排列产生宏观磁化。

那么这个磁场是如何定量地被电荷地运动决定？

### 安培力

磁场对电流源施加的安培力：$$d\vec F=Id\vec l\times\vec B$$，广延形式 $$\vec F=(\vec j\times\vec B)d\tau$$。

- 推论：环线电流线在**均匀磁场**中所受力之和为 0；定义**磁矩** $$\vec m=\frac{1}{2}(\displaystyle\oint_C\vec r\times d\vec l)$$, $$d\vec m=\frac{1}{2}\vec r\times \vec JdV$$，所受力矩为 $$\vec\tau=\vec m\times\vec B$$。
  - 若规定 $$\vec m$$ 与 $$\vec B$$ 相互垂直时**磁势能** $$U_m$$ 为 0 ，则 $$U_m=-\vec m·\vec B$$。(2022.8.2更新：啊，突然发现刘老师课件上力矩用的字母是 $$L$$，一般物理上不是约定俗成 $$τ$$ 是力矩 $$L$$ 是角动量吗？是不是需要勘误一下呢？)
- 在不均匀磁场中，磁场总是将稳态平衡的 $$\vec m$$ 从磁场小处移向大处，同时力矩将磁矩转向与磁场平行方向。受力 $$F=-\nabla U_m$$。

### 毕奥-萨筏尔定律

电流源产生的磁场 $$\vec B$$：$$d\vec B=\frac{\mu_0}{4\pi}\frac{Id\vec l\times\vec r}{r^3}$$，广延形式 $$\vec B=\displaystyle\frac{\mu_0}{4\pi}\displaystyle\int\frac{\vec j\times\vec r}{r^3}d\tau$$。

- Laplace 由 毕奥和萨阀尔总结出的实验规律，通过微分分析得到（别告诉我只记得 Laplace 继续卖萌）。
- 推论：无限长载流导线磁场 $$B=\displaystyle\frac{\mu_0I}{2\pi r}$$。
- 推论：载流螺线管中的磁场 $$B=\mu_0nI$$  ->  两平行同向电流环（**Helmholtz 线圈**），半径与轴心距离相等时，轴线中心点磁场最均匀。在大学物理实验中应用。
- **磁场性质**：定义**磁通量** $$\Phi_B=\displaystyle\int_S\vec B\cdot d\vec S$$，推论**磁高斯定理** $$\displaystyle\oint_S\vec B\cdot d\vec S=0$$, $$\nabla\cdot B=0$$ ->  **无源场**（磁场线闭合、无自由磁荷）；
- 前面已经提到过环线电流线磁矩 $$\vec m$$，其在在很远处激发的磁场满足 $$\vec B=\frac{\mu_0}{4\pi}(-\frac{\vec m}{r^3}+\frac{3(\vec m\cdot\vec r)\vec r}{r^5})$$，是不是和电偶极子情况很像？

#### 安培环路定理

- 推论 课件 05-10 $$\vec B(\vec r)=\displaystyle\frac{\mu_0I}{4\pi}\nabla\Omega$$  ->  **安培环路定理**$$\displaystyle\oint_l\vec B\cdot d\vec l=\mu_0\displaystyle\sum_{l内}I$$, $$\nabla\times\vec B=\mu_0\vec j$$ （严格证明在徐游老师书上） ->  **有旋场**（非保守场、无势场）。

### 安培定律

电流元对电流元施加的作用力：$$\vec F_{12}=\displaystyle\frac{\mu_0}{4\pi}\displaystyle\frac{I_1I_2d\vec l_2\times(d\vec l_1\times\vec r_{12})}{r_{12}^3}$$。原始形式不好用。

电流单位“安培”的定义：放在真空中的两条无限长平行导线，通有相等的稳恒电流，若两导线相距 $$1m$$，而每一导线每米长度上所受另一导线对它的作用力为 $$2\times10^{-7}N$$，则导线上的电流定义为 $$1A$$。


## 电磁场与电荷运动

### 洛伦兹力

运动电荷在磁场中受洛伦兹力 $$\vec F=q\vec v\times\vec B$$

上文提到磁场对电流源施加的力是安培力。电流元中有运动电荷，在磁场中受洛伦兹力。洛伦兹力与安培力的关系：导线中安培力是晶格所带电荷受力的总和，是电子所受洛伦兹力的宏观表现。

于是，带电粒子在电磁场中运动受洛伦兹力与电场力，$$\vec F=q\vec v\times\vec B+q\vec E$$。不幸的是，电场和磁场是耦合的，实际处理极为复杂，但是我们只考虑一些简单情况，可以把各种复杂效应忽略。

应用：磁聚焦、磁约束、荷质比测定、回旋加速器、霍尔效应。

## 磁介质

在电介质部分，我们了解到将内部电子不能自由移动的物质放在电场里，物质内部也会对电场产生响应。在各向同性线性介质中，幸运地，这种响应和外场呈现线性关系，也就有了很多可以难为大二本科生的习题，虽然这是物理上最简单的情况了。那么，材料对磁场的响应情况如何？

### 磁介质的行为

 - 抗磁介质（所有物质都具有）

    经典解释：核外层固定轨道上电子成对占据，产生电子轨道磁矩
    抱歉，2022.7.27我又在思考一个问题，本课程在经典框架下讨论，此处运用的事实是，轨道上成对的“电子相向运动”，这实属一个很经典的描述，玻尔理论中引入电子轨道运动时，只是为了解释氢原子光谱现象，而轨道上成对电子是不是能用相向运动描述，大概是无法观测的，似乎也没听说过除抗磁性以外的其他物理现象印证这个说法......陷入浅思......所以大概用泡利不相容原理，这一对电子的自旋相反，然后总磁矩为零似乎更合理一些？2024.01.05 量子解释pending！！！

    超导体的 Meissner 效应：样品内部磁感应强度为 0。

 - 顺磁介质（多数过渡金属离子具有净磁矩）

    来源；在外磁场作用下，原子/离子磁矩取向与外磁场平行（磁化产生的磁矩大于电子附加磁矩）；无外场时，热涨落与外磁场效应对抗，无法形成有序磁矩

 - 铁磁介质（由永久磁铁的分子电流激发，磁滞曲线） （PS. 刘俊明老师，英文名 Ising，英文读爱辛，但德文读伊辛）

 - 其实还有反铁磁、亚铁磁等，但本课程范围不涉及

### 磁化强度与磁化电流密度

我们之前学了分子磁矩可以看作唤醒电流磁矩 $$\vec m$$，**磁化强度** $$\vec M$$ 是单位体积内分子磁矩代数和。

- 一磁介质体积元的磁化电流，等价于这个体积元的表面净电流。取包围介质元的曲面 $$\vec S$$，其具有边界 $$\vec l$$。在面上穿出来又回去的电流抵消，我们只需考虑其在 $$\vec S$$ 穿过结果没从边界回去/出来的那些表面电流...... $$dI'=\vec M\cdot d\vec l$$，$$I'=\displaystyle\oint_l\vec M\cdot d\vec l$$。穿过 $$\vec S$$ 的净电流又有 $$I'=\displaystyle\int_S\vec j'\cdot d\vec S$$，则 $$\displaystyle\int_S\vec j'\cdot d\vec S=\displaystyle\oint_l\vec M\cdot d\vec l$$，$$\vec j'=\nabla\times\vec M$$（均匀介质内部 $$I'=0$$ 取任意内部边界有去必有回，只有边界处有磁化电流）。
- 那边界磁化电流如何表示？**磁化电流面密度** $$i'=\vec M\times \mathbf{\hat n}$$。

### 磁场强度 $$\vec H$$（辅助物理量）

- 把体系中的自由电流密度 $$\vec j_0$$ 也考虑进来，则宏观场满足 $$\displaystyle\oint_S\vec B\cdot d\vec S=0$$, $$\displaystyle\oint_l\vec B\cdot d\vec l=\mu_0\displaystyle\int_S(\vec j_0+\vec j')\cdot d\vec S$$ (continuous); $$=\mu_0\displaystyle\sum_L(I_0+I')$$ (discrete); 微分形式 $$\nabla\times \vec B=\mu_0(\vec j_0+\vec j')$$, $$\nabla\cdot\vec B=0$$.
- 由于我们一般能动地给系统加上 $$j_0$$，然后通过物理学规律求解磁化情况，所以构造关于 $$j_0$$ 的辅助物理量 $$\vec H=\frac{\vec B}{\mu_0}-\vec M$$，于是 $$\displaystyle\oint_l\vec H\cdot d\vec l=\displaystyle\sum_{S内}I_0=\displaystyle\int_S\vec j_0\cdot d\vec S$$, $$\nabla\times\vec H=\vec j_0$$（环路定理），**没有高斯定理**（见下面永久磁铁的 $$\vec H$$ 图）。$$\vec j_0=0$$ 不等于 $$\vec H=0$$。

**磁导率**与**磁化率**

 - 本课程范围内我们首先关注顺磁与抗磁在外场不是很大时的**线性**响应，关系：$$\vec M=\chi_m\vec H$$，于是**磁导率** $$\mu$$ 有 $$\vec B=\mu\vec H=\mu_0\mu_r\vec H=\mu_0(1+\chi_m)\vec H$$。

 - 对于铁磁体，磁导率 $$\mu$$ 不是常量，还决定于铁磁质磁化历史。磁滞回线。

 - 永久磁铁的磁场纯系由永久磁铁的分子电流激发。例：沿轴均匀磁化圆柱形永久磁铁外部 $$\vec M=0$$，表面 $$\vec i'=\vec M$$......

   <img src="\images\blog\Electromagnetism_Permanent.JPG" alt="Electromagnetism_Permanent" width="300px;" />

 - 例：**磁介质分界面**问题：$$\vec H$$ 有**环路定理**，界面两侧**切向**分量相等，可导出 $$\vec B$$ 界面两侧切向分量的关系；假定界面无自由电流，$$\vec B$$ 用**高斯定理**，界面两侧**法向**分量相等，可导出 $$\vec B$$ 界面两侧法向分量的关系。

### 等效磁荷理论

本来想写，后来不想写了，算了吧。对我一点用都没有。


## 电磁感应

动电能生磁，有啥能生电流吗？**法拉第**电磁感应实验真把电流生出来了。

### 法拉第电磁感应定律

前文说过，电流会产生磁场。这个由给定回路磁通变化产生的磁场有什么特点？**楞次定律**：当回路磁通变化时，感应电流所产生的感应磁通总是力图阻止原磁通的变化（能量守恒的必然结果）。

**感应电动势**：$$\Sigma=-\displaystyle\frac{d\Phi_B}{dt}=-\displaystyle\int_S(\displaystyle\frac{\partial\vec B}{\partial t})\cdot d\vec S+\displaystyle\oint_l(\vec v\times\vec B)\cdot d\vec l$$，感生电动势 + 动生电动势。注意，这里**感应电场不再是保守场了**。考虑感生场，微分形式为 $$\nabla\times\vec E=-\displaystyle\frac{\partial \vec B}{\partial t}$$。动生电动势和感生电动势对于参考系是不对称的，我们需要狭义相对论消除。

做功问题和前文洛伦兹力和安培力的关系那里讨论差不多。洛伦兹力不做功，只有安培力做功。

### 自感与互感

**自感**：用于线圈时，回路可能有外来电流、或回路形状及周围磁介质发生变化，此时穿过回路自身的磁通量随之改变，从而在回路中激发感应电动势。$$\Sigma=-L\frac{dI}{dt}$$ 自感电动势将反抗回路中电流的改变。

**互感**：一对相互靠近的感应线圈，因一个或两个载流线圈的电流变化而在对方线圈中激起感应电动势。$$M_{12}=\frac{\Phi_{12}}{I_2}$$，$$M_{21}=\frac{\Phi_{21}}{I_1}$$，若互感问题不涉及铁磁质，从做功角度切入，可以证明 $$M_{21}=M_{12}=M$$。

### 磁场能量

无铁磁质感应电路能量 $$L=\frac{1}{2}LI_0^2$$

$$w_m=\frac{1}{2}\mu H^2=\frac{1}{2}BH$$

### 位移电流

经典电磁学框架下，静磁场安培环路定理 $$\displaystyle\oint_l\vec H\cdot d\vec l=\displaystyle\int_S\vec j_0\cdot d\vec S$$ 推广到动态变量，存在矛盾，例如

- 电容器充放电的非稳恒电流问题

  <img src="\images\blog\Electromagnetism_Displacement_Current.JPG" alt="Electromagnetism_Displacement_Current" width="450px;" />

  引入**电荷守恒**和**高斯定理**，构造位移电流 $$\vec j_D(t)=\displaystyle\frac{\partial\vec D}{\partial\vec t}$$，随即 $$\displaystyle\oint_l\vec H\cdot d\vec l=\displaystyle\int_S(\vec j_0+\displaystyle\frac{\partial\vec D}{\partial\vec t})\cdot d\vec S$$  形式上得到满足。
  
- [电动力学](???)给出，如果对 $$\nabla\times\vec B(\vec x)=\mu_0\vec J(\vec x)$$ 两边同时取 $$\nabla\cdot$$，则得 $$\nabla\cdot\vec J(\vec x)=0$$，显然不总成立。

但磁场高斯定理（无源）推广到动态变量仍成立，因为决定磁场的毕-萨定律仍成立。

## 麦克斯韦方程组与电磁波

当年把我骗到物理学院的方程组。

### 麦克斯韦方程组

总结上文，我们有

![Electromagnetism_Maxwell](\images\blog\Electromagnetism_Maxwell.JPG)

![Electromagnetism_Maxwell_BC](\images\blog\Electromagnetism_Maxwell_BC.JPG)
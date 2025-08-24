---
layout: post
title: 力学 1.0
categories: BS-NJU-Course-Review-Physics
description: 对于矢量力学的回顾
keywords: classical mechanics
mathjax: true
---

牛顿力学又称矢量力学，以牛顿三个运动定律为基础，运用分离物体、几何关系、矢量等方法。具体介绍可以参考梁昆淼老师《力学（下册）——理论力学》的开头部分（对比了牛顿力学和分析力学）。

牛顿力学与高中物理中的力学部分一脉相承，分析的思路是完全一样的，只不过加入一些新的规律（e.g. 力矩和角动量）、一些高等数学（e.g. 微积分和极少量线性代数）一些新的对象（e.g., 质点系和刚体）。有3点要特别注意：

1. 加入了高等数学，说白了就是熟练在解题中应用**链式法则** $$\displaystyle \frac{dx}{dt} = \frac{dx}{du}\frac{du}{dt}$$ .
2. 用泰勒展开进行必要的近似和化简。

| 课程名                       | 力学                                                                           |
| 学习时间                   | 大一上                                                                       |
| 周课时                       | 3                                                                                 |
| 本人成绩                   | 80                                                                               |
| 课程教材                   | 梁昆淼等 《力学（上册）》高等教育出版社         |
| 个人建议参考教材    | D. Morin Introduction to Classical Mechanics   |
| 先修课程                   | 微积分                                                                        |

PS. 此处先修课程《微积分》应包括常微分方程求解部分内容，因为牛顿第二定律的本质是一个常微分方程，坐标变换等关系也是由微分式描述，最终问题的求解大多归结于常微分方程的两边积分。

教材评论：（注意：此处主要评价教材印刷质量，而非梁老师的编写质量）梁昆淼老师的《力学（上下册）》在全国范围内享有美誉，体现了老先生在中国物理学教育上倾注的心血。尤其是作为南京大学物理学院的学生，都对梁老师有十分的敬仰之情。然而，当笔者，一个没有在高中阶段接受过正式物理竞赛训练的人，初来南大，希望通过熟读教材与物拔的同学齐头并进，便开始钻研这本书时，屡屡遭受挫败。

我于 2018 年秋季购买了第四版教材。首先，在我的印象中，高中的教材很少出现印刷错误，而我拿到的教材上充满了印刷错误，例如力学量的脚标从右下角写到右上角变成幂次、脚标丢失、标量矢量写法混淆、标错绕某点旋转的点等。其次，在一维运动学、动力学方程中，写错代数式中物理量正负号，不是按照约定俗成的格式写造成混乱和误会。面对没有学过的新知识，总是想要视教材为指导，发现教材和自己分析的有时大相径庭；有时解题没有思路看教材给出的参考答案，对照每一项的意义，发现都有点莫名其妙，不知道怎么来的。

我的高中物理老师向来对于物理学代数式的书写要求严苛，我认为这对于建立清晰的知识体系是很重要的。在与身边同学交流的过程中，发现相当部分同学对于“按照物理规律列代数式”毫无清晰认识，做题无非是乱凑凑答案，凑出来也不知道为什么是这样，为什么不是那样。

P.S. 复习过程中，我找到了几年来以为已经丢失的勘误表，因为以为丢失所以没有顺利交给老师。现在教材我已经处理掉了，也不知道教材有没有重印和校对。但是感兴趣的可以要来看看这张勘误表。

哈佛大学 **David Morin**'s *Introduction to Classical Mechanics* 数学形式和推导思路清晰，**几乎可以让我学会**。1-4，6-9章节对应《力学》课纲的全部要求。第5章为分析力学入门，10-12章页属于相对论入门性质，可不作为参考。此外，作为英语不太好的人，读这本教材毫无压力。

## 质点运动学

具体数学推导请见梁昆淼《力学》第12-14节。个人感觉这部分虽然很少 explicitly 去说但很重要。

### 直角坐标系

直角坐标系是“最简单”的坐标系：在于基矢 $$\vec e_i, \vec e_j, \vec e_k$$ 对时间求导为零，因此用这些基矢表示的矢量对时间的导数形式简单；而在实际问题分析中，选择合适的坐标系是最简单的，而不是选择直角坐标系是最简单的。

速度和加速度在各个基矢上的分量：

- $$x=x(t), y=y(t), z=z(t)$$.

- $$v_x(t)=\dot{x}, v_y(t)=\dot{y}, v_z(t)=\dot{z}$$.
- $$a_x(t)=\ddot{x}, a_y(t)=\ddot{y}, a_z(t)=\ddot{z}$$.

### 极坐标系

**平面**问题中很常用的坐标系(空间是三维的，“平面”是否不够好用？参见下文 质点动力学)，但是感觉用的比较多的还是《数学物理方程》中，运动学什么的 explicitly 用的真的不太多。**径向**单位向量表示为 $$\vec e_i$$ 方向向外，**横向**单位向量表示为 $$\vec e_j$$ 方向逆时针。

- $$\rho=\rho(t), \varphi=\varphi(t)$$.

- $$v_\rho(t)=\dot{\rho}, v_\varphi(t)=\rho\dot{\varphi}$$.
- $$a_\rho(t)=\ddot{\rho}-\rho\dot{\varphi}^2, a_\varphi(t)=\rho\ddot{\varphi}+2\dot{\rho}\dot{\varphi}$$.

### 自然“坐标系”

**已知指点相对于参考系统的轨道时**，质点的位置用从某点算起的曲线距离表明，速度矢量就用速率表明，加速度就用**切向加速度**和**法向加速度**表明。似乎是中学阶段从来没有 explicitly 提出过的的坐标系，但是我们却很常用。例如，求解轨道最高点的向心力和对轨道的压力时，我们就是在运用自然坐标系。**切向**单位向量表示为 $$\vec{e_t}$$ 方向沿着速度方向，**法向**单位向量表示为 $$\vec e_n$$ 方向向着曲率半径圆心。

- $$v_t(t)=\dot{s}, v_n(t)=0$$.
- $$\displaystyle a_t(t)=\ddot{s}, a_n=\frac{\dot{s}^2}{R} \text{ or } v\dot{\theta}$$.

## 质点动力学

动力学中，我们引入了**力**这个概念。列力学与运动学关系式时，请先检查参考系是否为惯性系。

应试：动力学与运动学的结合技巧：质点动力学问题的求解总是与微分方程的求解有关。以牛顿第二定律 $$\vec{F} = m\vec{a}$$ 的一维情况为例， $$a$$ 为 $$x$$ 对 $$t$$ 的二阶导， 也是 $$v$$ 对 $$t$$ 的一阶导，我们常常需要寻找 $$F$$ 与 $$v$$ 和 $$x$$ 的关系，再由分离变量法导出两边分别关于 $$x$$ 和 $$v$$ 的微分方程，然后做积分求解。在这个过程中，一个十分重要的代换是 $$\displaystyle \frac{dv}{dt} = v \frac{dv}{dx}$$ 。

### 牛顿运动定律

> First Law: One thing this law does is give a definition of zero force. Another thing it does is give a definition of an *inertial frame*, which is defined simply as a reference frame in which the first law holds.
>
> Second Law: One thing this law does is give a definition of nonzero force. (And it is consistent with the first law).
>
> Third Law: This law essentially postulates that momentum is conserved (that is, not dependent on time).
>
> --D.Morin Introduction to Classical Mechanics 2.1 Newton's Laws 

### 惯性参考系

>如何选择参考系是的力学规律在形式上最简单...似乎总是存在某种参考系，空间相对它使均匀的各向同性的，时间相对它是均匀的。这样的参考系称为惯性参考系。特别是，在这样的惯性参考系中，在某个时刻静止的自由物体将永远保持静止。——朗道《力学》

>通常教材中将不受到其他力作用的自由质点相对于其作匀速直线运动的参考系定义为惯性参考系，即据自由运动的特征定义惯性参考系。或者按另外一种说法是牛顿第一定律成立的参考系称为惯性参考系。按时空性质和按自由运动的特征这两种方式定义惯性参考系在一定程度上使等价的，在力学范围内它们能导出完全相同的结论。但是，前一种定义更反映物理本质。——鞠国兴《朗道<力学>解读》

#### 伽利略变换

> An "event" is something that take place at a specific location $$(x,y,z)$$, at a precise time $$(t)$$​. 
>
> ...If we "start the clock" ($$t=0$$) at the moment the origins coincide, then at time $$t$$....---Griffiths 12.1.3




$$
x'=x-vt\\
y'=y\\
z'=z\\
t'=t\\
$$



> 伽利略变换是描述经典力学中一个事件在两个不同的惯性参考系之间的变换，其中时间是绝对的，即两个参考系测量的时间完全相同。根据伽利略变换，可证明满足速度相加原理。事实上，理论和实验都证明任一物体所遵循的牛顿力学方程在不同的惯性系中的形式是相同的，即牛顿力学方程在伽利略变换下保持不变，这就是**经典力学的相对性原理**。——电动力学课件 6.1

## 非惯性参考系

参见 D. Morin Introduction to Classical Mechanics Chapter 9 Accelerated Frames of Reference。设 $$\displaystyle\frac{d}{dt}$$ 是 $$\vec A$$ 在一个坐标系中的变化率，$$\displaystyle\frac{\partial}{\partial t}$$ 是 $$\vec A$$ 在另一个与前面坐标系有相对运动的坐标系。

$$\displaystyle\frac{d\vec A}{dt}=\frac{\partial\vec A}{\partial t}+\vec\omega\times\vec A$$, therefore, $$\displaystyle\frac{d^2\vec A}{dt^2}=\frac{\partial^2\vec A}{\partial t^2}+\vec\omega\times(\vec\omega\times\vec A)+2\vec\omega\times\frac{\partial\vec A}{\partial t}+\frac{d\vec\omega}{dt}\times\vec A$$

非惯性参考系 -> $$\vec R$$ 是两个坐标系的相对位移，惯性力：

- translation $$\displaystyle-m\frac{\partial^2\vec R}{\partial t^2}$$ 
- 离心力 centrifugal $$-m\vec\omega\times(\vec\omega\times\vec R)$$ 
- 科里奥利力 Coriolis $$\displaystyle-2m\vec\omega\times\frac{\partial\vec R}{\partial t}$$ 
  - 地理：河流为什么蜿蜒？大气为什么环流？地转偏向力是一种科里奥利力，使北半球运动（非惯性系中 $$v=\displaystyle\frac{\partial\vec R}{\partial t}$$）的物体右偏，南半球运动的物体左偏。提示：非赤道某点 $$\omega$$ 与地轴平行，不与地平面平行，北半球有向上分量，南半球有向下分量。
- azimuthal $$\displaystyle-m\frac{d\vec\omega}{dt}\times\vec R$$

## 质点动力学的运动定理

一般在处理动力学问题时，考虑这样几个方面：1. 动量 $$\vec{p}$$。2. 动量矩 $$\vec{L}$$。3. 能量 $$E$$。4. 运动学约束。

### 动量矩（角动量）定理

$$\displaystyle \vec{L}=\vec{r}×\vec{p}$$, $$\displaystyle\vec{M}=\vec{r}×\vec{F}$$, $$\displaystyle\vec{M}=\frac{d\vec{L}}{dt}$$. 跟动量定理类比就行。

#### 拉莫尔进动

这玩意两门力学课从始至终没提过，因为刚体力学课上讲得不多，高年级天天拉莫尔进动。其实这玩意根本用不着刚体，我们并不考虑电子的自转动力学，只是考虑其磁矩在匀强磁场中的转动。在均匀磁场中力矩垂直于角动量，不改变角动量的大小，只改变角动量的方向，造成角动量 $$\vec{L}$$ 和轨道磁矩 $$\vec{μ_l}$$ 绕磁场 $$\vec{B}$$ 以恒定的角频率 $$ω$$ 做**拉莫尔进动**。

参见梁老师理论力学 6.6，首先根据[磁矩的定义](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E5%88%86%E5%AD%90%E7%8E%AF%E5%BD%A2%E7%94%B5%E6%B5%81%E6%A8%A1%E5%9E%8B)导出匀速圆周运动带电粒子磁矩 $$\vec\mu=g\vec L$$, 其中$$g=q/2m$$ 为旋磁比。[匀强磁场中](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E5%B0%8F%E5%8C%BA%E5%9F%9F%E7%94%B5%E6%B5%81%E5%9C%A8%E5%A4%96%E7%A3%81%E5%9C%BA)力矩 $$\vec M=\vec\mu\times\vec B$$，于是 $$\displaystyle\frac{d\vec L}{dt}=-g\vec B\times\vec L$$。进动频率为 $$\omega=gB$$。

<img src="\images\blog\Classical_Mechanics_Larmor.jpg" alt="Classical_Mechanics_Larmor" width="400px;" />

### 有心力

有心力的形式：$$\displaystyle \vec{F}(\vec{r})=-\nabla{V(r)}=-\frac{dV}{dr}\vec e_r$$. 举例：电场力、万有引力（**开普勒**三大定律）。参考阅读：D. Morin Introduction to Classical Mechanics Chapter 6 Central Force

- 定理1：**角动量守恒定理**： If $$V(\vec{r})=V(r)$$, then $$\displaystyle \frac{d\vec{L}}{dt}=0$$.
- 定理2： If a particle is subject to a central force only, then its motion takes place in a plane.

关于能量与运动，第34节“有心力”参见梁昆淼《力学（下册）——理论力学》中“有心力”一章。

 - 有趣习题：D. Morin Introduction to Classical Mechanics 6.7.4 Solutions: $$r^k$$ potential

小振动——在平衡位置附近对势能进行泰勒展开。

## 质点系动力学的运动定理

P.S. 一点关于质点/质点系动力学的助教 note： 1. 弹性碰撞前后物体速度。2. 物体撞墙前后动量是否守恒？[力学 - PHY180TA - Kinetics](https://shi200005.github.io/download_file/Classical_Mechanics_Kinetics.pdf)

目标（描述上）：质点系运动 = 质心运动 + 相对运动。 方法：使用质心参考系！

### 质心参考系

质心参考系是相对于惯性参考系**平动**的参考系。质心的位置：$$\displaystyle \vec{R_{CM}}=\frac{\sum{m_i\vec{r_i}}}{M}$$.

> 质心参考系的特殊性：——鞠国兴《朗道<力学>解读》
>
> 1. 描述系统力学性质的一些物理量（**角动量**、**动能**等）均可以**分解**为与质心有关的部分和相对于质心参考系的部分，即与质心有关的部分可以与其他部分完全分离。
> 2. 因为质心相对于惯性参考系可以有加速度，质心参考系一般而言并不是惯性参考系。相对于质心系，角动量定理和功能原理等具有与惯性参考系中完全相同的形式，其中不出现与惯性力有关的部分。
> 3. 相对于质心参考系系统的总动量总等于零。

对于 1. 的解释：角动量：**平行轴定理**；动能：**柯尼希定理**（都见本节下文）。参考阅读：D. Morin Introduction to Classical Mechanics 4.6 The CM Frame

对于 2. 的解释：参见梁昆淼《力学》5.41 动量矩定理。事实上，凡是选取**平动**参考系统时，物体所受惯性力系得合力总是作用于质心。

对于 3. 的解释：参见 柯尼希定理 部分的附件。

### 柯尼希定理

注意：质点系中的内力做功可以改变质点系的动能！例如：非弹性碰撞-动能减少；爆炸：动能增加。

新定理：柯尼希定理：质点系的动能 = 质心的动能 + 质点系相对于质心的相对运动动能 （可分离性）

Morin 书上相关内容整理成的教学材料[力学 - 质心参考系 - 柯尼希定理 - 约化质量](https://shi200005.github.io/download_file/Classical_Mechanics_CM_Frame.pdf)。

- 德语小知识：柯尼希，德语写作 König ，是一个德语姓氏（汉语意译为”王“，可以称为王老师）。其中词尾 "ig" 的发音是“一希”，不是“一克”或者“一个“，德国作曲家贝多芬的 first name Ludwig ”路德维希“同理。但是问题在于，柯尼希是荷兰人，不是德国人，我对荷兰语一窍不通，但猜测和德语差不多。

### 变质量质点动力学

经典情境是喷射着的火箭。无非是列出正确的微分方程然后求解，略。

## 刚体力学

刚体是一种特殊的质点系（质点间没有相对位置的变化），有六个自由度（三个质心自由度和三个旋转自由度）。可以证明**刚体内力所做的功为零**。

知识掌握自测：关于滚动的自行车或汽车轮胎受地面摩擦力的方向。

施于刚体的力可以沿着其作用线滑移，其所引起的力学作用完全不因此而改变。选取某一个参考点，计算主矢 $$\displaystyle \vec{S}=\sum_i{\vec{F_i}}$$ 决定刚体质心的运动，$$m\ddot{\vec{r}}_0=\vec F$$；主矩$$\displaystyle\vec{M}=\sum_i{\vec{M_i}}$$ 决定刚体相对于参考点的运动，$$\dot{\vec L}=\vec M$$。若主矢和对任意一点的主矩都为零，则刚体处于**动平衡**。

为确定刚体在空间中的位置，只要指出刚体中任选的一点（**基点**）的位置以及刚体对于该点的取向就可以了。刚体的任意运动可以归结为基点的平移和刚体绕基点做定点运动（下文解释定点运动是一种定点转动）。参见梁老师 6.1.4，任选基点定点转动角速度 $$\omega$$ 相同。既然基点的选取任意，则不妨选择**质心**。

### 刚体的定轴转动

有一个自由度。绕 $$z$$ 轴的转动：$$L_z=I_zw$$，其中$$\displaystyle I_z=\sum_i{m_ir_i^2}$$ 称为**转动惯量**，转动动能 $$\displaystyle T=\frac{I_z\omega^2}{2}$$.

知识点：不同几何物体关于不同轴转动的转动惯量。参考阅读：D. Morin Introduction to Classical Mechanics Chapter 7 Angular Momentum, Part I

拓展：参考阅读：D. Morin Introduction to Classical Mechanics 7.9.5 Slick calculations of I 分形几何体的转动惯量（利用自相似性）

### 刚体的平面平行运动

 有三个自由度。将运动分解为该对象**质心**的运动和绕过质心 $$z$$ 轴的定轴转动。

$$\vec{L}=M\vec{R}×\vec{V}+(I_z^{CM}\omega\prime)\vec e_z$$, $$\displaystyle T=\frac{1}{2}MV^2+\frac{1}{2}I_z^{CM}\omega\prime^2$$.

由此得出  $$L_z=(MR^2+I_z^{CM})\omega$$, $$\displaystyle T=\frac{1}{2}(MR^2+I_z^{CM})\omega^2$$.

- **平行轴定理**：不妨记 $$I_z=MR^2+I_z^{CM}$$. 质点系的动量矩 = 质心的动量矩 + 质点系相对于质心的相对运动动量矩。

### 刚体的定点运动

之前讨论动量矩 $$\vec{L}$$ 的方向都保持不变，接下来讨论更一般的情况，动量矩的方向可以改变。

#### 欧拉定理和欧拉角

**欧拉定理**（见梁老师理论力学 6.1.2）：定点运动刚体的任何一个位置移动都可以通过绕着此顶点的某一轴旋转一个角度达到。和定轴转动不同的是，这个轴会变化。

由此我们可以看到，经典力学中“轨道”和“自旋”之间的分别其实是很模糊的，但是到了量子力学，虽然我们用经典力学中的“自旋”类比，但是粒子的自旋是内禀性质，是不可以和“轨道”相互转化的。

见梁老师理论力学 6.1.7 图6.8 ：空间坐标系、本体坐标系。**欧拉角**：进动角 $$\varphi$$（空间坐标系 $$xOy$$ 平面上转的）、章动角 $$\theta$$（$$z$$ 轴转的）、自转角 $$\psi$$（本体坐标系 $$x'Oy'$$ 平面上转的）。

三个欧拉角和基点的坐标可以视为刚体的**六个自由度**。欧拉角和刚体定点转动角速度 $$\omega$$ 的关系为**欧拉运动学方程**。

#### 惯量张量与惯量主轴

惯量张量（取定点运动的点为原点建立直角坐标系） 

$$\mathbf {I}=\pmatrix{\int(y^2+z^2) dm & -\int (xy) dm &-\int (zx) dm \\ -\int (xy) dm & \int(z^2+x^2) dm & -\int (yz) dm \\ -\int (xz) dm & -\int (yz) dm & \int(x^2+y^2) dm}$$,

$$\vec{L}=\mathbf{I}\vec{\omega}$$ ，而 $$T=\frac{1}{2}\vec{\omega}\cdot\vec{L}$$。好的，我看到了一个实对称矩阵，在[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/#%E5%AE%9E%E5%AF%B9%E7%A7%B0%E7%9F%A9%E9%98%B5)里提到过，实对称矩阵是一定可以合同对角化且特征向量互相**正交**（**拥有一切实对称矩阵该有的美好品德**）！如果我们把惯量张量对角化，就可以得到惯量主轴。

惯量主轴：对角化惯量张量得到 $$\mathbf {I}=\pmatrix{I_1&0&0\\0& I_2&0\\0&0&I_3}$$ 。选取本体坐标系，以惯量主轴为基时，$$\vec{L}=(I_1\omega_1,I_2\omega_2,I_3\omega_3)$$。当刚体绕某一惯量主轴匀速转动时，处于**动平衡**。

#### 惯量主轴坐标系下欧拉动力学方程

在惯性坐标系下刚体动力学公式之一是 $$\dot{\vec L}=\vec M$$。但是我们希望研究坐标系原点在刚体质心，以惯量主轴为坐标轴的本体坐标系（可能是非惯性系）。参见**运动定律与非惯性参考系**，动力学方程应改为 $$\dot{\vec L}=\vec M+\vec L\times\vec\omega$$。


$$
\begin{cases}
I_1\dot\omega_1=M_1+(I_2-I_3)\omega_2\omega_3\\
I_2\dot\omega_1=M_2+(I_3-I_1)\omega_3\omega_1\\
I_3\dot\omega_1=M_3+(I_1-I_2)\omega_1\omega_2
\end{cases}
$$


利用惯量主轴不难求解的两类刚体力学问题

> - Strike a rigid object with an impulsive (that is, quick) blow. What is the motion of the object immediately after the blow?
> - An object rotates around a fixed axis. A given torque is applied. What is the frequency of the rotation? (Or conversely, given the frequency, what is the required torque?)

## 振动和波

机械波三要素：形变、恢复力、介质中的传播。谐振动的合成：1.方向相同，频率相同（简单）。 2. 方向相同，频率不同（拍频）。 3. 方向垂直，频率相同。 4. 方向垂直，频率不同（李萨如图形）。波分为横波（有偏振现象）和纵波，让我们以绳上一维横波的传播为例导出波动方程。

当你站在湖边看湖面飘着的一片树叶，你会发现树叶并没有随着水波扩散。波把扰动在空间上传播开来，但对扰动响应的物质并不随着波传播。关于波的科普网站——[Acoustics and Vibration Animations](https://www.acs.psu.edu/drussell/demos.html)。

此课程中我们研究一个自由度的振动，对于两个自由度的振动，详见[理论力学](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E5%B0%8F%E6%8C%AF%E5%8A%A8)中“小振动”部分。

对于 homogeneous linear differential equations 的求解，我们可以利用猜解法：$$\ddot{x}=ax$$，猜 $$x=Ae^{\alpha t}$$，然后带入方程求解 $$\alpha$$，例如这里我们求出 $$\alpha=±\sqrt{a}$$。此方法求解阻尼振动也很有用！

- 谐振动（简谐振动）

 - 阻尼振动：欠阻尼、过阻尼、临界阻尼
   推荐阅读：D. Morin Introduction to Classical Mechanics 3.3 Damped harmonic motion
   
   临界阻尼可以让系统最快地找到新稳态。
   
 - 受迫振动 -> 共振（共振频率、共振振幅）
   推荐阅读；梁昆淼《力学》 48.3节 或 D. Morin Introduction to Classical Mechanics 3.4 Driven (and damped) harmonic motion
   
   The damped harmonic oscillation $$\ddot x+2\gamma x+\omega_0^2x=f(x)$$ as a [(En) Linear Response](https://shi200005.github.io/2024/11/28/Linear-Response/) system. 

### 波动方程

绳子拉紧，放 $$x$$ 轴上，拉紧。某一段产生了形变（但绳子本身不沿自身方向移动）。通过列解绳子横向位移恢复原状的**经典力学牛顿方程**，做小量近似，绳上微扰传播的波动方程：$$\displaystyle\frac{\partial^2\psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial ^2 \psi}{\partial t^2}$$，其中 $$v=\sqrt{\displaystyle\frac{T}{\mu}}$$，其中 $$T$$ 是绳中张力（小振动条件下处处相等），$$\mu$$ 是绳子线密度。讲解的文本很多，例如梁昆淼老师的数学物理方法和 Griffiths 电动力学第九章。描述一个以一定速度传播，波形不变的行波，此处 $$v$$ 就是行波的波速。[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/)的重点之一就是求解这种线性偏微分方程。

注意：在液体和气体里不可能传播横波。

考虑以一定速度 $$v$$ 传播，传播时波形不变的一维绳上波，$$\psi(x,t)\vert_{t=0}=f(x)$$，其中 $$f(x)$$ 是 $$t=0$$ 时的波形，$$\psi(x,t)$$ 是绳上各点在某时某地的振动情况，显然 $$\psi(x,t)=f(x-vt)$$。参照 Hecht 2.1.1，$$\psi(x,t)=f(x-vt)$$ 对应的偏微分波动方程为 $$\displaystyle\frac{\partial^2\psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial ^2\psi}{\partial t^2}$$。 $$\psi(x,t)=f(x+vt)$$ 也是波动方程的解，对应以 $$-v$$​ 传播的波形。波动方程是**线性** PDE，我们可以把几个波线性**叠加**起来。

**阻抗**定义为 $$Z=T/v$$，则决定式为 $$Z=\sqrt{T\mu}$$。

### 简谐波（单色波）的复数表示

此部分主要来自 Hecht Optics 第二章。

研究 $$\psi(x,t)\vert_{t=0}=f(x)=A\sin{kx}$$，其中 $$k=\displaystyle\frac{2\pi}{\lambda}$$ 是波数，周期满足 $$\vert kx\tau\vert=2\pi$$ -> $$\psi(x,t)=A\sin{(kx-\omega t+\mathscr E)}$$。

定义**相** $$\varphi(x,t)=\sin{(kx-\omega t+\mathscr E)}$$，则**相速度** $$\left(\displaystyle\frac{\partial x}{\partial t}\right)\vert_{\varphi}=±\displaystyle\frac{\omega}{k}=±v$$。

上面说了，我们可以把波叠加。让叠加在数学运算上变得简单的操作，就是用**欧拉公式**用复数表示波函数。$$\varphi(x,t)=\text{Re}[Ae^{i(\omega t-kx+\mathscr E)}]=A\cos{(kx-\omega t+\mathscr E)}$$，因为物理学家太懒，简记为 $$\varphi(x,t)=Ae^{i(\omega t-kx+\mathscr E)}=Ae^{i\varphi}$$​。

> ...after expressing a wave as a complex function and then performing operations with/on that function, the real part can be recovered only if those operations are restricted to addition, subtraction, multiplication and/or integration with respect to a real variable. --Hecht 2.5

### 反射与透射

阅读材料：梁昆淼《力学》 52.2 反射波 或 **Griffiths 9.1.3**，对于一个沿 $$z$$ 轴正方向传播的一维机械波，（驻波：反射波和入射波叠加）

$$\tilde f(z,t)=\begin{cases}{\tilde A_Ie^{i(k_1z-\omega t)}+\tilde A_Re^{i(-k_1z-\omega t)}, \quad\text{for } z<0}\\ \tilde A_Te^{i(k_2z-\omega t)}\quad\text{for }z>0.\end{cases}$$

若绳子两介质**结点不受净力（质量为零）**，则**边界条件**为 

- 绳子连续：$$\tilde f(0^-,t)=\tilde f(0^+,t)$$, 
- 张力一致，即绳子切线方向连续：$$\displaystyle\frac{\partial\tilde f}{\partial z}\vert_{0^-}=\frac{\partial\tilde f}{\partial z}\vert_{0^+}$$.

推出复振幅之比 $$\displaystyle\tilde A_R=(\frac{k_1-k_2}{k_1+k_2})\tilde A_I$$, $$\displaystyle\tilde A_T=(\frac{2k_1}{k_1+k_2})\tilde A_I$$. 振幅 $$\displaystyle A_Re^{i\delta_R}=(\frac{k_1-k_2}{k_1+k_2}) A_Ie^{i\delta_I}$$, $$\displaystyle A_Te^{i\delta_T}=(\frac{2k_1}{k_1+k_2}) A_Ie^{i\delta_I}$$. 

- 若 $$\mu_2<\mu_1$$，即 $$v_2>v_1$$，则 $$\delta_R=\delta_T=\delta_I$$，$$\displaystyle A_R=(\frac{k_1-k_2}{k_1+k_2}) A_I$$, $$\displaystyle A_T=(\frac{2k_1}{k_1+k_2}) A_I$$。
- 若 $$\mu_2>\mu_1$$，即 $$v_2<v_1$$，则 $$\delta_R+\pi=\delta_T=\delta_I$$，$$\displaystyle A_R=(\frac{k_2-k_1}{k_1+k_2}) A_I$$, $$\displaystyle A_T=(\frac{2k_1}{k_1+k_2}) A_I$$ —— **半波损失**。

考虑反射和透射的振幅与入射波之比，两段 $$T$$ 应相等，$$Z=T/v$$，所以 反射系数 $$\displaystyle R=\frac{Z_1-Z_2}{Z_1+Z_2}$$，透射系数 $$\displaystyle T=\frac{2Z_1}{Z_1+Z_2}$$。

### 色散

例：考虑两列振幅相等、振动方向相同，频率相差很小，均沿 $$z$$ 轴传播的单色平面波叠加。


$$
\begin{cases}
E_1=A\cos(\omega_1t-k_1z) \\
E_2=A\cos(\omega_2t-k_2z) \\
\end{cases}
$$


令 $$\omega_1>\omega_2$$, $$\omega_1=\omega+d\omega$$,  $$\omega_2=\omega-d\omega$$, $$k_1=k+dk$$,  $$k_2=k-dk$$, 则 $$E=E_1+E_2=2A\cos[(d\omega)t-(dk)z]\cos[\omega t-kz]$$。

波包：$$\cos[(d\omega)t-(dk)z]$$，等振幅条件 $$(d\omega)t-(dk)z=\text{const}$$，微分得群速 $$\displaystyle v_g=\frac{dz}{dt}=\frac{d\omega}{dk}$$。

相速与群速的关系——瑞利群速公式：$$\displaystyle v_g=v_p-\lambda\frac{dv_p}{\lambda}$$，推导见于老师光学课件。

### 多普勒效应

$$\displaystyle f_o=\frac{v+v_o}{v+v_s}f_s$$


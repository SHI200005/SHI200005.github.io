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

哈佛大学 **David Morin**'s *Introduction to Classical Mechanics*。此教材数学形式和推导思路清晰，**几乎可以让我学会**。1-4，6-9章节对应《力学》课纲的全部要求。第5章为分析力学入门，10-12章页属于相对论入门性质，可不作为参考。此外，作为英语不太好的人，读这本教材毫无压力。

## 质点运动学

具体数学推导请见梁昆淼《力学》第12-14节。个人感觉这部分虽然很少 explicitly 去说但很重要。

### 直角坐标系

直角坐标系是“最简单”的坐标系：在于基矢 $$\hat{i}, \hat{j}, \hat{k}$$ 对时间求导为零，因此用这些基矢表示的矢量对时间的导数形式简单；而在实际问题分析中，选择合适的坐标系是最简单的，而不是选择直角坐标系是最简单的。

速度和加速度在各个基矢上的分量：

- $$x=x(t), y=y(t), z=z(t)$$.

- $$v_x(t)=\dot{x}, v_y(t)=\dot{y}, v_z(t)=\dot{z}$$.
- $$a_x(t)=\ddot{x}, a_y(t)=\ddot{y}, a_z(t)=\ddot{z}$$.

### 极坐标系

**平面**问题中很常用的坐标系(空间是三维的，“平面”是否不够好用？参见下文 质点动力学)，但是感觉用的比较多的还是《数学物理方程》中，运动学什么的 explicitly 用的真的不太多。**径向**单位向量表示为 $$\hat{i}$$ 方向向外，**横向**单位向量表示为 $$\hat{j}$$ 方向逆时针。

- $$\rho=\rho(t), \varphi=\varphi(t)$$.

- $$v_\rho(t)=\dot{\rho}, v_\varphi(t)=\rho\dot{\varphi}$$.
- $$a_\rho(t)=\ddot{\rho}-\rho\dot{\varphi}^2, a_\varphi(t)=\rho\ddot{\varphi}+2\dot{\rho}\dot{\varphi}$$.

### 自然“坐标系”

**已知指点相对于参考系统的轨道时**，质点的位置用从某点算起的曲线距离表明，速度矢量就用速率表明，加速度就用**切向加速度**和**法向加速度**表明。似乎是中学阶段从来没有 explicitly 提出过的的坐标系，但是我们却很常用。例如，求解轨道最高点的向心力和对轨道的压力时，我们就是在运用自然坐标系。**切向**单位向量表示为 $$\hat{t}$$ 方向沿着速度方向，**法向**单位向量表示为 $$\hat{n}$$ 方向向着曲率半径圆心。

- $$v_t(t)=\dot{s}, v_n(t)=0$$.
- $$\displaystyle a_t(t)=\ddot{s}, a_n=\frac{\dot{s}^2}{R} \text{ or } v\dot{\theta}$$.

## 质点动力学

动力学中，我们引入了**力(Force)**这个概念。列力学与运动学关系式时，请先检查参考系是否为惯性系。

应试：动力学与运动学的结合技巧：质点动力学问题的求解总是与微分方程的求解有关。以牛顿第二定律 $$\vec{F} = m\vec{a}$$ 为例， $$a$$ 为 $$x$$ 对 $$t$$ 的二阶导， 也是 $$v$$ 对 $$t$$ 的一阶导，我们常常需要寻找 $$F$$ 与 $$v$$ 和 $$x$$ 的关系，再由分离变量法导出两边分别关于 $$x$$ 和 $$v$$ 的微分方程，然后做积分求解。在这个过程中，一个十分重要的代换是 $$\displaystyle \frac{dv}{dt} = v \frac{dv}{dx}$$ 。

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

## 运动定律与非惯性参考系

非惯性参考系 -> 惯性力：1. translation 2. centrifugal 3. Coriolis 4. azimuthal

参见 D. Morin Introduction to Classical Mechanics Chapter 9 Accelerated Frames of Reference

前面”质点动力学“那部分矢量微分运算搞清楚了，这部分不是问题。

## 质点动力学的运动定理

一般在处理动力学问题时，考虑这样几个方面：1. 动量 $$\vec{p}$$。2. 动量矩 $$\vec{L}$$。3. 能量 $$E$$。4. 运动学约束。

### 动量矩（角动量）定理

$$\displaystyle \vec{L}=\vec{r}×\vec{p}, \vec{\tau}=\vec{r}×\vec{F}, \vec{\tau}=\frac{d\vec{L}}{dt}$$. 跟动量定理类比就行。

### 有心力

这部分内容在[电磁学](https://shi200005.github.io/2021/11/20/Electromagnetism/)保守场部分还将继续讨论。有心力的形式：$$\displaystyle \vec{F}(\vec{r})=-\nabla{V(r)}=-\frac{dV}{dr}\hat{r}$$. 举例：电场力、万有引力（**开普勒**三大定律）。参考阅读：D. Morin Introduction to Classical Mechanics Chapter 6 Central Force

- 定理1：**角动量守恒定理**： If $$V(\vec{r})=V(r)$$, then $$\displaystyle \frac{d\vec{L}}{dt}=0$$.
- 定理2： If a particle is subject to a central force only, then its motion takes place in a plane.

关于能量与运动，第34节“有心力”参见梁昆淼《力学（下册）——理论力学》中“有心力”一章。

 - 有趣习题：D. Morin Introduction to Classical Mechanics 6.7.4 Solutions: $$r^k$$ potential

小振动——在平衡位置附近对势能进行泰勒展开。

## 质点系动力学的运动定理

P.S. 一点关于质点/质点系动力学的助教 note： 1. 弹性碰撞前后物体速度。2. 物体撞墙前后动量是否守恒？[力学-PHY180TA-Kinetics](https://shi200005.github.io/download_file/Classical_Mechanics_Kinetics.pdf)

目标（描述上）：质点系运动 = 质心运动 + 相对运动。 方法：使用质心参考系！

### 质心参考系

质心参考系是相对于惯性参考系**平动**的参考系。质心的位置：$$\displaystyle \vec{R_{CM}}=\frac{\sum{m_i\vec{r_i}}}{M}$$.

> 质心参考系的特殊性：——鞠国兴《朗道<力学>解读》
>
> 1. 描述系统力学性质的一些物理量（**角动量**、**动能**等）均可以**分解**为与质心有关的部分和相对于质心参考系的部分，即与质心有关的部分可以与其他部分完全分离。
> 2. 因为质心相对于惯性参考系可以有加速度，质心参考系一般而言并不是惯性参考系。相对于质心系，角动量定理和功能原理等具有与惯性参考系中完全相同的形式，其中不出现与惯性力有关的部分。
> 3. 相对于质心参考系系统的总动量总等于零。

对于 1. 的解释：角动量：**平行轴定理**（见下一节 刚体力学-刚体的平面平行运动）；动能：**柯尼希定理**（见本节下文）。参考阅读：D. Morin Introduction to Classical Mechanics 4.6 The CM Frame

对于 2. 的解释：参见梁昆淼《力学》5.41 动量矩定理。事实上，凡是选取**平动**参考系统时，物体所受惯性力系得合力总是作用于质心。

对于 3. 的解释：参见 柯尼希定理 部分的附件。

### 柯尼希定理

注意：质点系中的内力做功可以改变质点系的动能！例如：非弹性碰撞-动能减少；爆炸：动能增加。

新定理：柯尼希定理：质点系的动能 = 质心的动能 + 质点系相对于质心的相对运动动能 （可分离性）

Morin 书上相关内容整理成的教学材料[力学-质心参考系-柯尼希定理-约化质量](https://shi200005.github.io/download_file/Classical_Mechanics_CM_Frame.pdf)。

- 德语小知识：柯尼希，德语写作 König ，是一个德语姓氏（汉语意译为”王“，可以称为王老师）。其中词尾 "ig" 的发音是“一希”，不是“一克”或者“一个“，德国作曲家贝多芬的 first name Ludwig ”路德维希“同理。但是问题在于，柯尼希是荷兰人，不是德国人，我对荷兰语一窍不通，但猜测和德语差不多。

### 变质量质点动力学

经典情境是喷射着的火箭。无非是列出正确的微分方程然后求解，略。

## 刚体力学

刚体是一种特殊的质点系（质点间没有相对位置的变化），有六个自由度（三个质心自由度和三个旋转自由度）。可以证明**刚体内力所做的功为零**。

知识掌握自测：关于滚动的自行车或汽车轮胎受地面摩擦力的方向。

### 施于刚体的力系的简化

施于刚体的力可以沿着其作用线滑移，其所引起的力学作用完全不因此而改变。

选取某一个参考点 $$O$$，计算$$\displaystyle \vec{S}=\sum_i{\vec{F_i}},\vec{M}=\sum_i{\vec{M_i}}$$. 前者决定刚体质心的运动，后者决定刚体相对于 $$O$$ 点的运动。

### 刚体的定轴转动

绕 $$z$$ 轴的转动：$$L_z=I_zw$$，其中$$\displaystyle I_z=\sum_i{m_ir_i^2}$$ 称为**转动惯量**，转动动能 $$\displaystyle T=\frac{I_z\omega^2}{2}$$.

知识点：不同几何物体关于不同轴转动的转动惯量。参考阅读：D. Morin Introduction to Classical Mechanics Chapter 7 Angular Momentum, Part I

拓展：参考阅读：D. Morin Introduction to Classical Mechanics 7.9.5 Slick calculations of I 分形几何体的转动惯量（利用自相似性）

### 刚体的平面平行运动

求解刚体动力学的一般步骤：1. 找到”作为一个整体研究的对象“。2. 将运动分解为该对象**质心**的运动和绕质心的旋转。3. 考虑我在”质点动力学的运动定理“中提到过的那4个方面。

对于第 2. 点：$$\vec{L}=M\vec{R}×\vec{V}+(I_z^{CM}\omega\prime)\hat{z}, T=\frac{1}{2}MV^2+\frac{1}{2}I_z^{CM}\omega\prime^2$$.

由此得出  $$L_z=(MR^2+I_z^{CM})\omega, T=\frac{1}{2}(MR^2+I_z^{CM})\omega^2$$.

- **平行轴定理**：不妨记 $$I_z=MR^2+I_z^{CM}$$. 质点系的动量矩 = 质心的动量矩 + 质点系相对于质心的相对运动动量矩。

### 刚体的定点运动

之前讨论动量矩 $$\vec{L}$$ 的方向都保持不变，接下来讨论更一般的情况，动量矩的方向可以改变。

> Consider a rigid body undergoing arbitrary motion. Pick any point $$P$$ in the body. Then at any instant, the motion of the body may be written as the sum of the translational motion of $$P$$, plus a rotation around some axis, $$\omega$$, through $$P$$ (the axis $$\omega$$ may change with time).

由此我们可以看到，经典力学中“轨道”和“自旋”之间的分别其实是很模糊的，但是到了量子力学，虽然我们用经典力学中的“自旋”类比，但是粒子的自旋是内禀性质，是不可以和“轨道”相互转化的。

1. 惯量张量

   考虑刚体绕轴旋转，其中**旋转轴过参考系原点**的情况。惯量张量 

   $$\hat {I}=\pmatrix{\int(y^2+z^2)&-\int xy&-\int zx\\-\int xy& \int(z^2+x^2)&-\int yz\\-\int xz&-\int yz&\int(x^2+y^2)}$$,

   $$\vec{L}=\hat{I}\vec{\omega}$$ ，而 $$T=\frac{1}{2}\vec{\omega}\cdot\vec{L}$$。好的，我看到了一个实对称矩阵，在[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)里提到过，实对称矩阵是一定可以合同对角化且特征向量互相**正交**（**拥有一切实对称矩阵该有的美好品德**）！如果我们把惯量张量对角化，就可以得到惯量主轴。

2. 惯量主轴

   对角化惯量张量得到 $$\hat {I}=\pmatrix{I_1&0&0\\0& I_2&0\\0&0&I_3}$$ ，在以惯量主轴为基的坐标系中，$$\vec{L}=(I_1\omega_1,I_2\omega_2,I_3\omega_3)$$。

   在力学上又有什么妙处呢？The principle axes are the axes around which the object can rotate with constant speed, without the need for any torque. (So in some sense, the object is "happy" to spin around a principle axis.)

3. 利用惯量主轴不难求解的两类刚体力学问题

   不要忘了灵活使用在“质点系”部分详细讨论过的质心系性质并运用在题目中！

   > - Strike a rigid object with an impulsive (that is, quick) blow. What is the motion of the object immediately after the blow?
   > - An object rotates around a fixed axis. A given torque is applied. What is the frequency of the rotation? (Or conversely, given the frequency, what is the required torque?)

   具体解题过程不赘述。

4. 欧拉公式

   如何在惯量主轴的基下表示动量矩定理？Projecting $$d\vec{L}/{dt}$$ onto the instantaneous principle axes, we have $$\tau_1=I_1\dot{\omega_1}+(I_3-I_2)\omega_2\omega_3$$ and two more.

5. 欧拉公式的应用：进动

   > **进动**（precession）是[自转](https://zh.wikipedia.org/wiki/自轉)物体之自转轴又绕着另一轴旋转的现象，又可称作**旋进**。在[天文学](https://zh.wikipedia.org/wiki/天文學)上，又称为“[岁差](https://zh.wikipedia.org/wiki/歲差)现象”。
   >
   > 常见的例子为[陀螺](https://zh.wikipedia.org/wiki/陀螺)。当其自转轴的轴线不再呈[铅直](https://zh.wikipedia.org/wiki/鉛直)时，即自转轴与对称轴不重合不平行时，会发现自转轴会沿着铅直线作旋转，此即“旋进”现象。另外的例子是[地球](https://zh.wikipedia.org/wiki/地球)的自转。
   >
   > 自旋的进动现象主要出现在[核磁共振](https://zh.wikipedia.org/wiki/核磁共振)与[磁振造影](https://zh.wikipedia.org/wiki/磁振造影)上。其中的例子包括了[稳定态自由旋进（进动）造影](https://zh.wikipedia.org/wiki/穩定態自由旋進造影)。
   >
   > **进动**是转动中的物体自转轴的指向变化。在物理学中，有两种类型的进动，自由力矩和诱导力矩，此处对后者的讨论会比较详细。在某些文章中，“进动”可能会提到地球经验的岁差，这是进动在天文观测上造成的效应，或是物体在轨道上的进动。 --Wiki_zh

## 振动和波

学不好这章，电动力学和量子力学都会死亡。

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
   
   Revisit the damped harmonic oscillation $$\ddot x+2\gamma x+\omega_0^2x=f(x)$$ after learning complex functions ([复变函数](https://shi200005.github.io/2022/03/28/Complex-Functions/)). This is a [(En) Linear Response](https://shi200005.github.io/2024/11/28/Linear-Response/) system. 

### 波动方程

绳子拉紧，放 $$x$$ 轴上，拉紧。某一段产生了形变（但绳子本身不沿自身方向移动）。通过列解绳子横向位移恢复原状的**经典力学牛顿方程**，做小量近似，绳上微扰传播的波动方程：$$\displaystyle\frac{\partial^2\psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial ^2 \psi}{\partial t^2}$$，其中 $$v=\sqrt{\displaystyle\frac{T}{\mu}}$$，其中 $$T$$ 是绳中张力，$$\mu$$ 是绳子线密度。讲解的文本很多，例如梁昆淼老师的数学物理方法和 Griffiths 电动力学第九章。参照[光学 - 一维波](https://shi200005.github.io/2022/02/25/Optics/#%E4%B8%80%E7%BB%B4%E6%B3%A2)，如果描述一个以一定速度传播，波形不变的行波。此处 $$v$$ 就是行波的波速。[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/)的重点之一就是求解这种线性偏微分方程。

考虑以一定速度 $$v$$ 传播，传播时波形不变的一维绳上波，$$\psi(x,t)\vert_{t=0}=f(x)$$，其中 $$f(x)$$ 是 $$t=0$$ 时的波形，$$\psi(x,t)$$ 是绳上各点在某时某地的振动情况，显然 $$\psi(x,t)=f(x-vt)$$。参照 Hecht 2.1.1，$$\psi(x,t)=f(x-vt)$$ 对应的偏微分波动方程为 $$\displaystyle\frac{\partial^2\psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial ^2\psi}{\partial t^2}$$。 $$\psi(x,t)=f(x+vt)$$ 也是波动方程的解，对应以 $$-v$$​ 传播的波形。波动方程是**线性** PDE，我们可以把几个波线性**叠加**起来。

### 简谐波（单色波）的复数表示

此部分主要来自 Hecht Optics 第二章。

研究 $$\psi(x,t)\vert_{t=0}=f(x)=A\sin{kx}$$，其中 $$k=\displaystyle\frac{2\pi}{\lambda}$$ 是波数，周期满足 $$\vert kx\tau\vert=2\pi$$ -> $$\psi(x,t)=A\sin{(kx-\omega t+\mathscr E)}$$。

定义**相** $$\varphi(x,t)=\sin{(kx-\omega t+\mathscr E)}$$，则**相速度** $$\left(\displaystyle\frac{\partial x}{\partial t}\right)\vert_{\varphi}=±\displaystyle\frac{\omega}{k}=±v$$。

上面说了，我们可以把波叠加。让叠加在数学运算上变得简单的操作，就是用**欧拉公式**用复数表示波函数。$$\varphi(x,t)=\text{Re}[Ae^{i(\omega t-kx+\mathscr E)}]=A\cos{(kx-\omega t+\mathscr E)}$$，因为物理学家太懒，简记为 $$\varphi(x,t)=Ae^{i(\omega t-kx+\mathscr E)}=Ae^{i\varphi}$$​。

> ...after expressing a wave as a complex function and then performing operations with/on that function, the real part can be recovered only if those operations are restricted to addition, subtraction, multiplication and/or integration with respect to a real variable. --Hecht 2.5

### 反射与透射

阅读材料：梁昆淼《力学》 52.2 反射波 或 **Griffiths 9.1.3**

$$\tilde f(z,t)=\begin{cases}{\tilde A_Ie^{i(k_1z-\omega t)}+\tilde A_Re^{i(-k_1z-\omega t)}, \quad\text{for } z<0}\\ \tilde A_Te^{i(k_2z-\omega t)}\quad\text{for }z>0.\end{cases}$$

若绳子两介质结点不受净力（质量为零），则**边界条件**为 $$\tilde f(0^-,t)=\tilde f(0^+,t)$$, $$\displaystyle\frac{\partial\tilde f}{\partial z}\vert_{0^-}=\frac{\partial\tilde f}{\partial z}\vert_{0^+}$$.

推出振幅之比 $$A_R=(\displaystyle\frac{k_1-k_2}{k_1+k_2})A_I$$, $$A_T=(\displaystyle\frac{2k_1}{k_1+k_2})A_I$$.

驻波：反射波和入射波叠加。

### 多普勒效应

$$\displaystyle f_o=\frac{v+v_o}{v+v_s}f_s$$


---
layout: post
title: 电动力学
categories: BS-NJU-Course-Review-Physics
description: 
keywords: Electrodynamics
mathjax: true
---

现在可以研究传播着的电磁波了。

| 课程名称                | 电动力学                                                 |
| 学习时间                | 大三上                                                     |
| 周课时                    | 3                                                              |
| 本人成绩                | 91                                                            |
| 课程教材                | 郭硕鸿《电动力学》高等教育出版社   |
| 个人建议参考教材 | 那还用问 当然是詹老师的课件             |
| 先修课程                | 微积分 电磁学 力学                                |

版本 2024.01.05 Ver0.1 

本文主要参考詹老师的课件，markdown 引用体内为直接引用原文。

## 电磁波的传播

### 真空自由空间


$$
\nabla\times\vec E(\vec x,t)=-\frac{\partial\vec B(\vec x,t)}{\partial t}\\
\nabla\times\vec B(\vec x,t)=\mu_0\epsilon_0\frac{\partial}{\partial t}\vec E(\vec x,t)\\
\nabla\cdot\vec E=0\\
\nabla\cdot\vec B=0
$$


计算 $$\nabla\times(\nabla\times\vec E)$$  -> $$\nabla^2\vec E(\vec x,t)-\mu_0\epsilon_0\displaystyle\frac{\partial^2}{\partial t^2}\vec E(\vec x,t)$$，同理 $$\nabla^2\vec B(\vec x,t)-\mu_0\epsilon_0\displaystyle\frac{\partial^2}{\partial t^2}\vec B(\vec x,t)$$。这就是波动方程，波速为 $$c=\displaystyle\frac{1}{\sqrt{\mu_0\epsilon_0}}$$，即为真空中光速。于是，波动方程写为......

#### 时谐电磁波（单色波）

$$\vec E(\vec x,t)=\vec E(\vec x)e^{-i\omega t}$$，$$\vec B$$ 同样。P.S. 在计算如能量密度、能流密度等实际测量的物理量时，对电场或磁场的表达式只取其**实数**部分代入计算。

电场和磁场满足关系 $$\vec B(\vec x)=-\displaystyle\frac{i}{\omega}\nabla\times\vec E(\vec x)$$，$$\vec E(\vec x)$$ 类似......

##### 时谐平面波

$$\vec E(\vec x)=\vec E_0e^{i\vec k\cdot\vec x}$$, $$\vec E(\vec x,t)=\vec E_0e^{i(\vec k\cdot\vec x-\omega t+\varphi_0)}$$ 等相面为平面，波矢 $$\vec k$$ 与等相面垂直，是电磁波在**无界空间**传播时的平面电磁波模式。

时谐平面波代入 $$\nabla\cdot\vec E=0$$  ->  $$\vec k\cdot\vec E=0$$  ->  **横波**。

考虑与磁场的关系，得到 $$\vec E=c\vec B\times\vec e_k$$，电场、磁场和传播方向右手互相垂直（TEM 波）。

<img src="\images\blog\Electrodynamics_Plain.JPG" alt="Electrodynamics_Plain" width="150px;" />

（图来自刘老师电磁学课件）

### 绝缘介质中

$$
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\\
\nabla\times\vec H=\vec \alpha_f+\frac{\partial\vec D}{\partial t}\\
\nabla\cdot\vec D=\rho_f\\
\nabla\cdot\vec B=0
$$



各向同性线性绝缘介质 $$\vec D=\epsilon\vec E$$, $$\vec B=\mu\vec H$$，波动方程里的波速变为 $$v_p=v_g=\displaystyle\frac{c}{n}$$，其中 $$n=\sqrt{\mu_r\epsilon_r}$$。

##### 时谐平面波

定义**阻抗** $$Z=\displaystyle\frac{E_0}{H_0}=\displaystyle\sqrt{\frac{\mu}{\epsilon}}$$  还记得[力学](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E4%B8%80%E7%BB%B4%E6%B3%A2)中的阻抗在一维波传播中的物理意义吗？这里阻抗之后菲涅耳定律用。

能量密度 $$\langle w\rangle=\displaystyle\frac{1}{2}\epsilon E_0^2=\displaystyle\frac{1}{2\mu}B_0^2$$，能流密度 $$\langle\vec S\rangle=\displaystyle\frac{1}{2}\sqrt{\displaystyle\frac{\epsilon}{\mu}} E_0^2\vec e_k$$。

### 反射定律和折射定律

研究**各向同性均匀线性介质**，**时谐平面波**的规律。对于**绝缘介质**，**分界面上没有自由电荷和传导电流面分布**时，代入电磁场边值关系，则得到中学时很熟悉的**反射定律**（$$\vec k'$$）和**折射定律**（$$\vec k''$$）。和光学中光程费马定理得到的结论一致（[理论力学 - 最小作用量原理](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E6%9C%80%E5%B0%8F%E4%BD%9C%E7%94%A8%E9%87%8F%E5%8E%9F%E7%90%86)）。

在光学波段，材料一般 $$\mu_1=\mu_2=\mu_0$$，此时折射定律叫**菲涅尔公式**。

#### 菲涅尔定律

根据波动方程和边值条件，我们求出反射波和折射波的方向和入射波的关系。那么它们的**振幅**和入射波本身有没有定量关系？

将入射波 $$\vec E_0$$, $$\vec B_0$$ 分解为偏振方向垂直于入射面（s 偏振）和偏振方向平行于入射面（p 偏振），分别代入边界条件，得到定量的**菲涅尔定律**。令人惊讶的是，当 $$\theta+\theta''=90\degree$$ 的时候，p 偏振的反射波电场强度解为 0，消失。这个 $$\theta$$ 就是 **布儒斯特角**

研究反射和折射能流密度振幅：反射系数 $$R$$ 和折射系数 $$T$$。

#### 全反射

在高中时，我们说光又光密介质（如玻璃）入射到光疏介质（如空气），当入射角大于临界角时，折射波消失，发生全反射。但是，虽然折射波没了几何意义，我们这里仍然在**复数域**考虑入射角大于临界角时的 $$\sin\theta''>1$$ 的解  ->  折射波为沿 $$x$$ 方向传播、振幅沿 $$z$$ 轴衰减的时谐波，沿分界面存在平均能流密度分量，沿面法线方向的平均能流密度为零。

### 电磁波在导电介质中的传播

材料介电常数事实上和电磁波频率相关，电磁波传播时会发生色散。

#### Lorenz 模型

描述无极分子构成的介质的介电常数的电子极化而引起的色散模型（回忆[电磁学 - 电介质的行为](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E7%94%B5%E4%BB%8B%E8%B4%A8%E7%9A%84%E8%A1%8C%E4%B8%BA)）。有人要问，电子被束缚着，只能原地挣扎，电磁波怎么传播？当然，电磁波的传播不是通过电子像信鸽一样送信传播出去的，传播的是一种运动的形式，电磁波强迫电子极化振荡，这种振荡就是电磁波的体现。

物理模型：用**阻尼谐振子**近似表征电子在振荡的电磁场中被束缚下的运动，电子振荡有个本征频率 $$\omega_0$$。求解[力学 - 受迫振动](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E4%B8%80%E4%B8%AA%E8%87%AA%E7%94%B1%E5%BA%A6%E7%9A%84%E6%8C%AF%E5%8A%A8)方程，得到相对介电常数的解为 $$\epsilon_r(\omega)=1+\chi=1+\displaystyle\frac{\omega_p^2}{\omega_0^2-\omega^2-i\gamma\omega}$$，其中 $$\gamma$$ 为受迫振动方程里的“阻尼系数”，$$\omega_p^2=\displaystyle\frac{Ne^2}{m\epsilon_0}$$ 为介质的等离子体频率。

介电常数的解为复数，其实，我们对它的分析完全可以参照受迫振动的振幅分析，对实部和虚部的物理意义分析可以参见 [David Tong: Lectures on Kinetic Theory - Linear Response](http://www.damtp.cam.ac.uk/user/tong/kintheory/four.pdf)。

如果频率接近共振频率，介电常数存在一个比较大的虚部（dissipative part），介质存在显著的吸收损耗，此区域随着频率增加，折射率反而减小，称为**反常色散**。如果频率远离共振区域，只需要去介电常数的实部，忽略虚部，电磁波传播时的损耗可以忽略。

#### Drude 模型

描述自由电子占主导的导体（如贵金属）的介电常数。

这时含有电子振荡本征频率的谐振项在受迫振动方程中消失。相对介电常数的复数解为 $$\epsilon_r(\omega)=1-\displaystyle\frac{\omega_p^2}{\omega^2+i\gamma\omega}$$，其中 $$\omega_p^2=\displaystyle\frac{Ne^2}{m\epsilon_0}=\displaystyle\frac{\sigma_c\gamma}{\epsilon_0}$$，其中 $$\sigma_c=\displaystyle\frac{Ne^2}{\gamma m}$$ 为金属电导率。

- 在低频和微波波段（$$\omega\ll\omega_p$$），相对介电常数实部是一个与频率无关的**负数**（$$10^4$$ 量级 电磁波不允许在媒质中传播），虚部有极大的值。电磁波入射到导体表面**穿透深度几乎为 0**，因此都可以看成**理想导体**。

- 在近红外 / 可见光区波段，相对介电常数是一个绝对值不是特别大的负数......电磁波不允许在金属体内传播，一旦入射到金属导体表面，则在金属表面下急剧衰减。

- 等离子体色散特性 - 等离子体频率（不懂）。

导电介质：把两个模型结合起来，在低频情况下，Lorenz 模型保留实部 $$\epsilon_c(\omega)>0$$，导电性的贡献用 $$i\displaystyle\frac{\sigma_c}{\omega}$$ 表示。电磁波入射到导电介质表面，可以在内部传播，随着深度的增加振幅呈现指数衰减。

### 理想导体矩形波导及谐振腔

通过上面对电磁波在材料中传播的介电常数的物理源头讨论，结合实验事实，

> 低频的电磁波（如微波）入射到如金属表面时，其穿透深度非常小（在纳米尺度），而反射率几乎接近 100%。故当微波在金属波导中传播时，物理上把金属看成理想导体。对于理想导体，进入导体的穿透深度 $$\delta\rightarrow0$$，导体内部的电磁场可以近似认为为零。此时，电流被限制在贴近表面厚度趋于 0 的薄层，刑场无损耗的面电流 $$\vec\alpha_f$$ 分布和面电荷 $$\sigma_f$$ 分布。——课件 4.6

注意，自由空间中的时谐平面波解是 TEM 波，来源于全空间都有 $$\nabla\cdot\vec E=0$$，但在波导管中，由于金属表面出现面电荷和面电流分布，这个微分关系在边界失效，我们求得的满足波动方程的解便不再是 TEM 波。

当**矩形波导管内部为真空**时，波动方程 $$\nabla^2\vec E(\vec x)+k_0^2\vec E(\vec x)=0$$, $$\vec B(\vec x)$$ 同......，其中 $$k_0=\omega/c$$。设电磁波沿波导轴线 $$z$$ 方向传播，


$$
\vec E(\vec x,t)=\vec E(x,y)e^{i(k_zz-\omega t)}\\
\vec H(\vec x,t)=\vec H(x,y)e^{i(k_zz-\omega t)}\\
$$


解得 $$E,H_{x,y}$$ 与 $$E,H_z$$ 的关系。此时我们发现 $$E_z$$ 和 $$H_z$$ 不能同时为零，因此波导中不存在 TEM 波。

#### 简并模

- TE 模（横电模）$$E_z=0$$

  结论：解得 $$H_z(x,y)=H_0\cos(k_xx)\cos(k_yy)$$ 以及 $$E,H_{x,y}$$。在横向 $$x,y$$ 方向，电磁波振幅分布为驻波，记为模式为 $$TE_{mn}$$。基模 $$TE_{01},TE_{10}$$，实际应用中，我们抑制高阶模。

- TM 模（横磁模）$$H_z=0$$

  结论：解得 $$E_z(x,y)=E_0\sin(k_xx)\sin(k_yy)$$ 以及 $$E,H_{x,y}$$。在横向 $$x,y$$ 方向，电磁波振幅分布为驻波，记为模式为 $$TM_{mn}$$。基模 $$TM_{11}$$，不能有 0。

上述 $$k_x=\displaystyle\frac{m\pi}{a}$$, $$k_y=\displaystyle\frac{n\pi}{b}$$，波传播的波矢 $$k_z=\sqrt{k_0^2-(k_x^2+k_y^2)}$$ 必须为**实数**，才能以行波方式传播  ->  截止频率 $$\omega_c=\pi c\sqrt{(m/a)^2+(n/b)^2}$$ 和相应截止波数 $$k_c=\omega_c/c$$，是针对具体模式谈论的。

我们发现，$$TM_{mn}$$ 和 $$TE_{mn}$$ 有相同的色散关系，为简并模。我们不希望它们同时在波导传播。幸运的是，$$TE_{01}$$$$, $$$$TE_{10}$$ 没有其相应的 $$TM$$ 简并模，对应波段是 single mode band。

#### 群速度和相速度

相速度 $$v_p=\displaystyle\frac{dz}{dt}$$，群速度 $$v_g=\displaystyle\frac{d\omega}{dk_z}$$。结论：波在波导管中传播时，$$v_p=\displaystyle\frac{c}{\sqrt{1-(\omega_c/\omega)^2}}$$, $$v_pv_c=c^2$$。

### 理想导体矩形谐振腔

利用金属谐振腔激发微波波段的电磁波。利用分离变量法求解电磁场方程，得到谐振腔的本征圆频率 $$\omega_{mnl}$$ 与谐振腔几何线度的关系。

## 电磁波的辐射

>辐射是指能量以电磁波的形式从场源向远场发射的现象，而电磁波就是由随时间交变运动的电荷系统辐射出来的。
>
>本章的讨论仅限于如何从给定的电流分布计算出辐射的电磁波。——电动力学课件 5.1

真空麦克斯韦方程组


$$
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\\
\nabla\times\vec B=\mu_0\vec J+\mu_0\epsilon_0\frac{\partial}{\partial t}\vec E\\
\nabla\cdot\vec E=\frac{\rho}{\epsilon_0}\\
\nabla\cdot\vec B=0\\
$$


磁场无源，引入磁矢势 $$\vec A$$，代入 $$\nabla\times\vec E$$  ->  $$\nabla\times(\vec E(\vec x,t)+\displaystyle\frac{\partial\vec A(\vec x,t)}{\partial t})=0$$ 无旋，引入标势满足 $$\vec E+\displaystyle\frac{\partial\vec A}{\partial t}=-\nabla\varphi(\vec x,t)$$  -> $$\vec E(\vec x,t)=-\nabla\varphi(\vec x,t)-\displaystyle\frac{\partial\vec A(\vec x,t)}{\partial t}$$ .

### 规范变换与规范不变性

矢势 $$\vec A$$ 和标势 $$\varphi$$ 是我们构造出来的，具有一定的任意性。要求选取不同的电磁势，电场和磁场不发生改变。如果 $$\vec A$$ 和 $$\varphi$$ 是一对满足条件得到电磁势，我们已经讨论过 $$\vec A'=\vec A+\nabla\psi$$ 不改变 $$\vec B$$，若要 $$\vec E$$ 也不变，相应应有 $$\varphi'=\varphi-\displaystyle\frac{\partial\psi}{\partial t}$$。变换前后对应电磁场相同，成为**规范变换不变性**（简称**规范不变性**）。

#### 达朗贝尔方程

麦克斯韦方程组四个微分方程中，为了构造电磁势，我们已经用了 $$\nabla\cdot\vec E$$ 和 $$\nabla\times\vec B$$，把电磁势代入剩下的两个 $$\nabla\times\vec E$$ 和 $$\nabla\cdot\vec B$$ 中，得到，


$$
\nabla^2\vec A-\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}-\nabla(\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial\varphi}{\partial t})=-\mu_0\vec J \\
\nabla^2\varphi+\frac{\partial}{\partial t}\nabla\cdot\vec A=-\frac{\rho}{\epsilon_0}\\
$$


为了方便，我们加某种限制条件，称之为**规范辅助条件**（简称**规范条件**），我们已经讨论过，在电磁波问题中，我们一般采用**洛伦兹规范** $$\nabla\cdot\vec A+\displaystyle\frac{1}{c^2}\frac{\partial\varphi}{\partial t}=0$$。然后，上述方程组将简化为漂亮的


$$
\begin{bmatrix}
		\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}
	\end{bmatrix}
	\begin{bmatrix}
		A_1 \\ A_2 \\ A_3 \\ \varphi  
	\end{bmatrix}
	=
	\begin{bmatrix}
		\mu_0J_1  \\ \mu_0J_2 \\ \mu_0J_3 \\ \rho/\epsilon_0  
	\end{bmatrix}
$$


这就是**达朗贝尔方程**（洛伦兹规范下的电磁势微分方程）。

- 例：用达朗贝尔方程求解自由空间中的平面电磁波，和我们之前直接用麦克斯韦方程组解出来的一致。
- 例：用库伦规范求解自由空间中的平面电磁波，和用洛伦兹规范求得的电场和磁场一致。

### 推迟势

考虑含时电荷源产生的标势，代入**达朗贝尔方程**，......


$$
\varphi(\vec x,t)=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho(\vec x',t-\frac{r}{c})}{r}dV'\\
\vec A(\vec x,t)=\frac{\mu_0}{4\pi}\int_{V'}\frac{\vec J(\vec x',t-\frac{r}{c})}{r}dV'\\
$$


> 电荷 / 电流所产生的物理作用不能够立刻传至场点，而是需要在较晚的时刻到达场点，这个推迟的时间 $$r/c$$ 为电磁作用春波所需要的时间，我们将上面两个电磁势的表达式成为**推迟势**。——电动力学课件 5.2

可以证明推迟势满足**洛伦兹规范**。

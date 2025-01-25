---
layout: post
title: 电动力学 1.0
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

本文主要参考詹老师的课件，markdown 引用体内为直接引用原文。

## 电磁波的传播

### 真空自由空间


$$
\nabla\times\vec E(\vec x,t)=-\frac{\partial\vec B(\vec x,t)}{\partial t}\\
\nabla\times\vec B(\vec x,t)=\mu_0\epsilon_0\frac{\partial}{\partial t}\vec E(\vec x,t)\\
\nabla\cdot\vec E=0\\
\nabla\cdot\vec B=0
$$


计算 $$\nabla\times(\nabla\times\vec E)$$  -> $$\nabla^2\vec E(\vec x,t)-\mu_0\epsilon_0\displaystyle\frac{\partial^2}{\partial t^2}\vec E(\vec x,t)$$，同理 $$\nabla^2\vec B(\vec x,t)-\mu_0\epsilon_0\displaystyle\frac{\partial^2}{\partial t^2}\vec B(\vec x,t)$$。这就是[波动方程](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E6%B3%A2%E5%8A%A8%E6%96%B9%E7%A8%8B)，波速为 $$c=\displaystyle\frac{1}{\sqrt{\mu_0\epsilon_0}}$$，即为真空中光速。

#### 时谐电磁波（单色波）

$$\vec E(\vec x,t)=\vec E(\vec x)e^{-i\omega t}$$，$$\vec B$$ 同样。P.S. 在计算如能量密度、能流密度等实际测量的物理量时，对电场或磁场的表达式只取其**实数**部分代入计算。

电场和磁场满足关系 $$\vec B(\vec x)=-\displaystyle\frac{i}{\omega}\nabla\times\vec E(\vec x)$$，$$\vec E(\vec x)$$ 类似......

##### 时谐平面波

$$\vec E(\vec x)=\vec E_0e^{i\vec k\cdot\vec x}$$, $$\vec E(\vec x,t)=\vec E_0e^{i(\vec k\cdot\vec x-\omega t+\varphi_0)}$$ 等相面为平面，波矢 $$\vec k$$ 与等相面垂直，是电磁波在**无界空间**传播时的平面电磁波模式。

时谐平面波代入 $$\nabla\cdot\vec E=0$$  ->  $$\vec k\cdot\vec E=0$$  ->  **横波**。

考虑与磁场的关系，得到 $$\vec E=c\vec B\times\vec e_k$$，电场、磁场和传播方向右手互相垂直（TEM 波）。

<img src="\images\blog\Electrodynamics_Plain.JPG" alt="Electrodynamics_Plain" width="300px;" />

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

定义**阻抗** $$\displaystyle Z=\frac{E_0}{H_0}=\sqrt{\frac{\mu}{\epsilon}}$$  还记得力学中的[阻抗](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E6%B3%A2%E5%8A%A8%E6%96%B9%E7%A8%8B)在一维波传播中的物理意义吗？这里阻抗之后菲涅耳定律用。

能量密度 $$\displaystyle\langle w\rangle=\frac{1}{2}\epsilon E_0^2=\frac{1}{2\mu}B_0^2$$，能流密度 $$\langle\vec S\rangle=\displaystyle\frac{1}{2}\sqrt{\displaystyle\frac{\epsilon}{\mu}} E_0^2\vec e_k$$。

### 反射定律和折射定律

研究**各向同性均匀线性介质**，**时谐平面波**的规律。对于**绝缘介质**，**分界面上没有自由电荷和传导电流面分布**时，代入电磁场边值关系，则得到中学时很熟悉的**反射定律**（$$\vec k'$$）和**折射定律**（$$\vec k''$$，斯涅尔定律）。和光学中光程费马定理得到的结论一致（[理论力学 - 最小作用量原理](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E6%9C%80%E5%B0%8F%E4%BD%9C%E7%94%A8%E9%87%8F%E5%8E%9F%E7%90%86)）。

#### 菲涅尔定律

根据波动方程和边值条件，我们求出反射波和折射波的方向和入射波的关系。那么它们的**振幅**和入射波本身有没有定量关系？[力学机械波对应](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#波动方程

将入射波 $$\vec E_0$$, $$\vec B_0$$ 分解为偏振方向垂直于入射面（[s 偏振](https://shi200005.github.io/2023/11/02/Language/#physics-1)）和偏振方向平行于入射面（p 偏振），分别代入边界条件，得到定量的**菲涅尔定律**。定义介质阻抗 $$\displaystyle Z=\sqrt{\frac{\mu}{\epsilon}}$$，
$$
\text{s 偏振}:
\begin{cases}
\displaystyle \frac{E_0'}{E_0}=\frac{Z_2\cos\theta-Z_1\cos\theta''}{Z_2\cos\theta+Z_1\cos\theta''}\\
\displaystyle \frac{E_0''}{E_0}=\frac{2Z_2\cos\theta}{Z_2\cos\theta+Z_1\cos\theta''}\\
\end{cases}  \\
\text{p 偏振}:
\begin{cases}
\displaystyle \frac{H_0'}{H_0}=\frac{Z_1\cos\theta-Z_2\cos\theta''}{Z_1\cos\theta+Z_2\cos\theta''}\\
\displaystyle \frac{H_0''}{H_0}=\frac{2Z_1\cos\theta}{Z_2\cos\theta+Z_1\cos\theta''}\\
\end{cases}
$$


研究反射和折射能流密度振幅：反射系数 $$\displaystyle R=\frac{E_0'^2}{E_0^2}$$ 和折射系数 $$\displaystyle T=\frac{Z_2^{-1}E_0''^2\cos\theta''}{Z_1^{-1}E_0^2\cos\theta''}$$。不是直接对入（反、透）射波的能流操作，而是将其投影到界面的法向方向。

### 电磁波在导电介质中的传播

材料介电常数事实上和电磁波频率相关，电磁波传播时会发生**色散**。

#### 绝缘体 - Lorenz 模型

描述无极分子构成的介质的介电常数的电子极化而引起的色散模型（回忆[电磁学 - 电介质的行为](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E7%94%B5%E4%BB%8B%E8%B4%A8%E7%9A%84%E8%A1%8C%E4%B8%BA)）。有人要问，电子被束缚着，只能原地挣扎，电磁波怎么传播？当然，电磁波的传播不是通过电子像信鸽一样送信传播出去的，传播的是一种运动的形式，电磁波强迫电子极化振荡，这种振荡就是电磁波的体现。

物理模型：忽略电子之间的相互作用力，用**阻尼谐振子**近似表征电子在振荡的电磁场中被束缚下的运动，电子振荡有个本征频率 $$\omega_0$$。求解受迫振动方程 $$\displaystyle\ddot x+\gamma\dot x+eE_0\cos(\omega t)/m=0$$，得到相对介电常数的解为 $$\epsilon_r(\omega)=1+\chi=1+\displaystyle\frac{\omega_p^2}{\omega_0^2-\omega^2-i\gamma\omega}$$，其中 $$\gamma$$ 为受迫振动方程里的“阻尼系数”，$$\omega_p^2=\displaystyle\frac{Ne^2}{m\epsilon_0}$$ 为介质的等离子体频率。介电常数的解为复数，参见 [(En) Linear Response](https://shi200005.github.io/2024/11/28/Linear-Response/)。

折射率随波长增大而减小的色散称为**正常色散**，正常色散区  $$v_g<v_p$$。如果频率接近共振频率，介电常数存在一个比较大的虚部（dissipative part），介质存在显著的吸收损耗，此区域随着频率增加，折射率反而减小，称为**反常色散**，反常色散区 $$v_g>v_p$$。如果频率远离共振区域，只需要去介电常数的实部，忽略虚部，电磁波传播时的损耗可以忽略。关于此模型中电磁波转播时振幅的衰减、损耗和反常色散区光速超过 $$c$$ 的现象，详见 Griffiths 9.4.3。

- 在光学中，柯西公式：在正常色散区内折射率随波长变化的经验公式 $$\displaystyle n=A+\frac{B}{\lambda^2}+\frac{C}{\lambda^4}$$。

#### 导体

##### Drude 模型

描述自由电子占主导的导体（如贵金属）的介电常数。这时含有电子振荡本征频率的谐振项在受迫振动方程中消失（电子自由了，不被“弹簧”牵着了）。相对介电常数的复数解为 $$\epsilon_r(\omega)=1-\displaystyle\frac{\omega_p^2}{\omega^2+i\gamma\omega}$$，其中 $$\omega_p^2=\displaystyle\frac{Ne^2}{m\epsilon_0}=\displaystyle\frac{\sigma_c\gamma}{\epsilon_0}$$，其中 $$\sigma_c=\displaystyle\frac{Ne^2}{\gamma m}$$ 为金属电导率。

- 在低频和微波波段（$$\omega\ll\omega_p$$），相对介电常数实部是一个与频率无关的**负数**（$$10^4$$ 量级，电磁波不允许在媒质中传播），虚部有极大的值。电磁波入射到导体表面**穿透深度几乎为 0**，因此都可以看成**理想导体**。

- 在近红外 / 可见光区波段，相对介电常数是一个绝对值不是特别大的负数......电磁波不允许在金属体内传播，一旦入射到金属导体表面，则在金属表面下急剧衰减。

- 等离子体色散特性 - 等离子体频率（不懂）。

##### 电磁场方程 - 导体内部衰减波

补充：参见 Griffiths 9.4.1。这时，导体内部允许有自由电流存在，根据欧姆定律 $$\vec J_f=\sigma\vec E$$，代入麦克斯韦方程组求解。

- 结论：向导体内注入自由电荷，自由电荷会流到导体边界，最终内部自由电荷为零，符合我们对导体静电平衡态的认知；

- 等一段时间，导体内自由电荷变为零后，麦克斯韦方程组变为

- 
  $$
  \nabla^2\vec E=\mu\epsilon\frac{\partial^2\vec E}{\partial t^2}+\mu\sigma\frac{\partial\vec E}{\partial t},\\
  \nabla^2\vec B=\mu\epsilon\frac{\partial^2\vec B}{\partial t^2}+\mu\sigma\frac{\partial\vec B}{\partial t}.
  $$
  

  这不就是[阻尼振动](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E6%8C%AF%E5%8A%A8%E5%92%8C%E6%B3%A2)方程，解得 $$\tilde{\vec E}(z,t)=\tilde{\vec E}_0e^{-\kappa z}e^{i(kz-\omega z)}$$，磁场长得一样。于是我们看到电磁场在导体内部传播时是怎么随着穿透深度指数衰减的。穿透深度 $$d=1/\kappa$$。对于理想导体，$$\sigma→\infty$$，$$\kappa→0$$。

- 进一步，导体内部的衰减波是横波，见 Griffiths。

最后，对于导电介质：把两个模型结合起来，在低频情况下，Lorenz 模型保留实部 $$\epsilon_c(\omega)>0$$，导电性的贡献用 $$i\displaystyle\frac{\sigma_c}{\omega}$$ 表示。电磁波入射到导电介质表面，可以在内部传播，随着深度的增加振幅呈现指数衰减。

### 理想导体矩形波导及谐振腔

> 低频的电磁波（如微波）入射到如金属表面时，其穿透深度非常小（在纳米尺度），而反射率几乎接近 100%。故当微波在金属波导中传播时，物理上把金属看成理想导体。对于理想导体，进入导体的穿透深度 $$\delta\rightarrow0$$，导体内部的电磁场可以近似认为为零。此时，电流被限制在贴近表面厚度趋于 0 的薄层，形成无损耗的面电流 $$\vec\alpha_f$$ 分布和面电荷 $$\sigma_f$$ 分布。——课件 4.6

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

**群速度和相速度**：波在波导管中传播时，$$v_p=\displaystyle\frac{c}{\sqrt{1-(\omega_c/\omega)^2}}$$, $$v_pv_c=c^2$$。

**理想导体矩形谐振腔**：利用金属谐振腔激发微波波段的电磁波。利用分离变量法求解电磁场方程，得到谐振腔的本征圆频率 $$\omega_{mnl}$$ 与谐振腔几何线度的关系。

## 运动电荷产生的电磁势和电磁场

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


为了方便，我们加某种限制条件，称之为**规范辅助条件**（简称**规范条件**），我们已经讨论过，在电磁波问题中，我们一般采用**洛伦兹规范** $$\nabla\cdot\vec A+\displaystyle\frac{1}{c^2}\frac{\partial\varphi}{\partial t}=0$$（在静磁场中使用的[**库伦规范**](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E7%A3%81%E7%9F%A2%E5%8A%BF)）。然后，上述方程组将简化为漂亮的


$$
\begin{bmatrix}
	\displaystyle\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}
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

洛伦兹规范下的拉格朗日力学见[理论力学 - 拉格朗日力学的推广](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E5%8A%9B%E5%AD%A6%E7%9A%84%E6%8E%A8%E5%B9%BF)。

### 推迟势

I can know the news only AFTER things happened....

考虑含时电荷源产生的标势 $$\rho(\vec x,t)=Q(t)\delta(\vec x)$$，代入**达朗贝尔方程**，-> $$\varphi(r,t)=\displaystyle\frac{1}{4\pi\epsilon_0r}Q(t-\frac{r}{c})$$......

$$
\varphi(\vec x,t)=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho(\vec x',t-\frac{r}{c})}{r}dV'\\
\vec A(\vec x,t)=\frac{\mu_0}{4\pi}\int_{V'}\frac{\vec J(\vec x',t-\frac{r}{c})}{r}dV'\\
$$


> 电荷 / 电流所产生的物理作用不能够立刻传至场点，而是需要在较晚的时刻到达场点，这个推迟的时间 $$r/c$$ 为电磁作用春波所需要的时间，我们将上面两个电磁势的表达式成为**推迟势**。——电动力学课件 5.2

可以证明推迟势满足**洛伦兹规范**。

- 有了推迟势，可以推出相应的场 $$\vec E(\vec r,t),\vec B(\vec r,t)$$​（Jefimenko's Equations），详见 Griffiths 10.2.2。
- 运动的点电荷产生的电磁势（Liénard-Wiechert potentials），详见 Griffiths 10.3.1。注意，对于有时间推迟效应的源积分，则相应积分体积将发生变化（类似于多普勒效应，**不是狭义相对论效应**）。产生的电磁场 $$\vec B(\vec x,t)=\displaystyle\frac{1}{c}\vec r\times\vec E(\vec x,t)$$.
  - 匀速直线运动情况产生的电磁场：见 Griffiths 10.3.2，$$\vec B=\displaystyle\frac{1}{c^2}(\vec v\times\vec E)$$​。
- 上面两个推论都用到了 $$t_r=t-\displaystyle\frac{r}{c}$$ 是空间场点 $$\vec x$$ 的隐函数。

## 电磁波的辐射

>辐射是指能量以电磁波的形式从场源向远场发射的现象，而电磁波就是由随时间交变运动的电荷系统辐射出来的......本章的讨论仅限于如何从给定的电流分布计算出辐射的电磁波。——电动力学课件 5.1
>
>When charges *accelerate*, their fields can transport energy irreversibly out to infinity - a process we call **radiation**. ---Griffiths 11.1.1

辐射部分关注的核心物理量：坡印廷矢量。

### 电磁多极辐射

采用势的多级展开，讨论单频做简谐振荡的小区域电荷和电流系统在远场所产生的辐射问题（远场满足 $$l\ll\lambda\ll r$$​，也称辐射区场）。

辐射场和静电磁场的对比——场矢量大小与辐射源距离的衰减关系。见 Griffiths 11.1.1.

简谐振荡的小区域电荷 $$\vec J(\vec x',t)=\vec J(\vec x')e^{-i\omega t}$$  <->  $$\rho(\vec x',t)=\rho(\vec x')e^{-i\omega t}$$。记体系含时电偶极矩 $$\vec p(t)=\vec pe^{-i\omega t}$$，其中 $$\vec p=\displaystyle\int_{V'}\rho(\vec x')\vec x'dV'$$。

该 $$\vec J(\vec x',t)$$ 产生 $$\vec A(\vec x,t)=\vec A(\vec x)e^{-i\omega t}$$，其中 $$\vec A(\vec x)=\displaystyle\frac{\mu_0}{4\pi}\displaystyle\int_{V'}\frac{\vec J(\vec x')}{r}e^{ikr}dV'$$，其中 $$e^{ikr}$$ 时推迟作用因子。

将电荷（源）存在的小区域放置到坐标原点，记 $$R=\vert\vec x\vert$$，$$\vec n=\vec x/R$$。我们通过对 $$r\approx R-\vec n\cdot \vec x'$$ 的近似展开 $$\vec A$$，注意，坟墓中的距离可以扔掉后面的相位项，但分子中关于相位的振荡项不能扔掉相位项。进一步展开结果中的指数因子 $$e^{-ik\vec n\cdot\vec x'}=1-ik\vec n\cdot\vec x'+...$$，得 $$\vec A(\vec x)=\vec A^{(0)}(\vec x)+\vec A^{(1)}(\vec x)+...$$，其中 $$\displaystyle\vec A^{(0)}(\vec x)=\frac{\mu_0}{4\pi}\frac{e^{ikR}}{R}\int_{V'}\vec J(\vec x')dV'$$ 称为电偶极辐射，后一项 $$\displaystyle\vec A^{(1)}(\vec x)=-ik\frac{\mu_0}{4\pi}\frac{e^{ikR}}{R}\int_{V'}\vec J(\vec x')\vec n\cdot\vec x'dV'$$ 又可以分解为磁偶极辐射和电四极辐射 $$\vec A^{(1)}(\vec x)=\vec A_m^{(1)}(\vec x)+\vec A_D^{(1)}(\vec x)$$。磁偶极辐射和电四极辐射得功率要远小于电偶极辐射。

#### 电偶极辐射

$$\displaystyle\vec A^{(0)}(\vec x)=\frac{\mu_0}{4\pi}\frac{e^{ikR}}{R}\int_{V'}\vec J(\vec x')dV'$$ , $$\displaystyle\langle S_p\rangle=\frac{1}{32\pi^2\epsilon_0c^3}\frac{\omega^4 p^2}{R^2}\sin^2\theta\vec n$$. 

可以传播很远并伴随有能量的传输；短波长的辐射功率药远于长波长辐射。

#### 有加速度的点电荷的辐射

详见 Griffiths 11.2。

大二下学近代物理的时候我就特别蒙蔽，玻尔原子模型的问题在于如果电子围绕原子核运动就会不断向外辐射能量。我咋就不知道会向外辐射能量呢？

我们在推迟势部分已经导出运动电荷产生的电磁势和电磁场，现在我们可以进一步导出坡印廷矢量。注意，当考虑向外辐射的能量时，我们只考虑坡印廷矢量与距离成平方反比的项。经过冗长推导，得到辐射功率的 Larmor formula：$$\displaystyle P=\frac{\mu_0q^2a^2}{6\pi c}$$，其中 $$a$$​ 是电荷运动的加速度。

由于此时点电荷会向外辐射能量，根据能量守恒，如果给一个力让中性粒子和带电粒子加速运动，带电粒子会以更小的加速度作为代价。详见 Griffiths。

## 狭义相对论

局限于惯性参考系的理论，解决物理规律在**惯性参考系**之间的物理量转换问题。

牛顿力学方程在[伽利略变换](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E6%83%AF%E6%80%A7%E5%8F%82%E8%80%83%E7%B3%BB)下保持不变，不幸的是，电磁学基本定律不能保持不变。麦克斯韦方程组提出的光速 $$c$$ 是关于什么参考系的速度？Michelson-Morley 试图测量光速沿不同方向的差异，结果发现没有差异。

狭义相对论

- 两条基本假设：相对性原理、光速不变原理（两个事件间隔 $$s^2=c^2(\Delta t)^2-(\Delta x)^2-(\Delta y)^2-(\Delta z)^2$$ 参考系变换下不变）
- 三个重要推论：同时的相对性（一个光源向两个方向射光，从两个有相对运动的参考系看，什么时候到达两个目标点）、运动时钟延缓（$$\Delta t=\displaystyle\frac{\Delta\tau}{\sqrt{1-(v/c)^2}}$$，$$\Delta\tau$$ 为在该物体的静止坐标系中测到的时间）、运动尺度缩短（$$l=l_0{\sqrt{1-(v/c)^2}}$$，$$l_0$$ 为在该物体的静止坐标系中测到的长度）。

### 洛伦兹变换

两个惯性系，$$\Sigma'$$ 相对于 $$\Sigma$$ 以 $$v$$ 沿 $$x$$ 轴匀速运动。代入两个事件的间隔在两个参考系中相等的条件，得到洛伦兹变换（两个惯性系时空坐标原点事件：两个空间原点重合时开始掐表），


$$
x'=\gamma(x-\beta c)\\
y'=y\\
z'=z\\
t'=\gamma(t-\frac{\beta}{c}x)\\
$$


where $$\beta=v/c$$, $$\gamma=1/\sqrt{1-\beta^2}$$. 由此可见，在 $$\beta\approx0$$ 的极限下，洛伦兹变换还原为[伽利略变换](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E4%BC%BD%E5%88%A9%E7%95%A5%E5%8F%98%E6%8D%A2)。伽利略相对性是狭义相对论在低速度下的近似。


$$
x'=x-vt\\
y'=y\\
z'=z\\
t'=t\\
$$


把形式凑对称点，把间隔里的 $$c^2\Delta t^2$$ 项改写成 $$-(ic\Delta t)^2$$。定义坐标 $$x_4=ict$$，洛伦兹变换也可改写成矩阵形式


$$
\begin{bmatrix}
	x_1' \\ x_2' \\ x_3' \\ x_4' \\
\end{bmatrix}

=

\begin{bmatrix}
	\gamma & 0 & 0 & i\beta\gamma \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    -i\beta\gamma & 0 & 0 & \gamma \\ 
\end{bmatrix}

\begin{bmatrix}
	x_1 \\ x_2 \\ x_3 \\ x_4  
\end{bmatrix}
$$


记为 $$\vec x'=\hat a\vec x$$。不难发现，其**逆变换矩阵**应该是转置矩阵 $$\hat{\tilde a}$$（从物理意义上）。变换，然后逆变换的操作为 $$\hat a\hat{\tilde a}=I$$，毕竟，如果 $$\Sigma'$$ 相对于 $$\Sigma$$ 沿 $$x$$ 轴以 $$v$$ 运动，如果 $$\Sigma''$$ 相对于 $$\Sigma'$$ 沿 $$x'$$ 轴以 $$-v$$ 运动，则 $$\Sigma''$$ 应当与 $$\Sigma$$ 相对静止，否则洛伦兹将感到深深的恐惧。

这里注意，我们把实对称矩阵推广到复数域定义了厄米矩阵，在量子力学中关注厄米共轭，满足 $$\hat U^H=\hat U$$。这里洛伦兹变换矩阵也是复矩阵，但这里满足的 $$\hat a\hat{\tilde a}=I$$ 只是取转置，没有取厄米共轭。因为我们想讨论与物理直觉对应的坐标系转换，逆变换就是转置矩阵，不是厄米共轭矩阵，所以这里考虑转置矩阵，就不足为奇了。

狭义相对论局限性举例：双生子佯谬。狭义相对论不能解决，必须用广义相对论解决。

**洛伦兹变换下的不变量**：e.g., 两个事件的间隔、电荷的电量、波的位相 $$\varphi$$。

### 4-Vector

在三维空间直角坐标系里，我们可以定义两个向量的内积。如果我们对空间坐标系做[正交变换](https://shi200005.github.io/2021/09/30/Linear-Algebra/#%E6%AD%A3%E4%BA%A4%E5%8F%98%E6%8D%A2)，则可以保证内积不变。那么，在四维时空里，如何定义两个时空向量的“内积“，使得在惯性系的洛伦兹变换下，该”内积“不发生改变？前面已经说了，变换惯性参考系时，两个事件的**间隔**不变。

定义四维时空向量 $$x^\mu=(x^0,x^1,x^2,x^3)^T$$，其中 $$x^0=ct$$，其余为空间坐标。更一般地，$$a^\mu=(a^0,a^1,a^2,a^3)^T$$, $$a_\mu=(a_0,a_1,a_2,a_3)^T=(-a^0,a^1,a^2,a^3)^T$$，则内积可表示为 $$a_\mu b^\mu=a^\mu b_\mu$$。Griffiths 定义间隔 $$I=(\Delta x)^\mu(\Delta x)_\mu=-c^2(\Delta t)^2+(\Delta d)^2$$。

- 闵可夫斯基图与因果论。

### 多普勒效应和光行差现象

> 多普勒效应指的是在不同的参考系中观察到的频率存在差异。光行差现象指的是光源运动时，光的传播方向亦发生变化。——电动力学课件 6.4

求解：根据波的位相是洛伦兹变换下的不变量。-> 红移与宇宙膨胀。

- 例：速度变换公式：见 Griffiths Eq. (12.45) 或电动力学课件 6.3.4.

  如果研究的对象是真空中的电磁波，若 $$u_x=c,u_y=u_z=0$$，则 $$u_x'=c,u_y'=u_z'=0$$；若 $$u_x=0,u_y=c,u_z=0$$，则 $$u_x'=v,u_y'=\sqrt{c^2-v^2},u_z'=0$$, $$u'=c$$。第二种情况就是光的传播方向发生变化的例子。

### 相对论力学

This part comes from Griffiths chap 12.2.

绝对时空观下，动量是质量乘以速度。在相对论时空观下，我相对于一个参考系 $$S$$ 以 $$\vec u=d\vec l/dt$$ 运动，一段时间内，该参考系观察到我有一个位移。但是，这段运动在该参考系中的时间间隔是 $$dt$$，我自己参考系里的时间间隔是 $$d\tau$$，已经在钟慢效应 $$d\tau=\sqrt{1-u^2/c^2}dt$$ 里讨论过了。

为了保证在相对运动的惯性系中，在一个惯性系中动量守恒过程在另一个惯性系中也动量守恒。在相对论力学中，我在 $$S$$ 中的动量，速度 $$\vec\eta=d\vec l/d\tau$$ 应该用我自己参考系中的时间间隔，$$\vec p=m\vec\eta=\displaystyle\frac{m\vec\mu}{\sqrt{1-u^2/c^2}}$$；同时，能量守恒给出相对论**能量**形式应为 $$E=\displaystyle\frac{mc^2}{\sqrt{1-u^2/c^2}}$$。这个相对论能量形式给出静止物体的总能量为 $$E=mc^2$$。非静止情况下，以 $$u$$ 展开的二次项就是绝对时空观里的动能。重要结论：$$E^2-p^2c^2=m^2c^4$$。

- 相对论时空观下，闭合体系的动量和能量守恒。不幸的是，质量不守恒。
- 如果零质量粒子以光速运动，则 $$\vec p,E$$ 成为不定形，可以非 0，满足 $$E=p^2c^2$$。就是光子。不同的光子怎么区分，相对论力学给不了我们，但是普朗克告诉我们 $$E=h\nu$$。

#### 牛顿运动定律

第一定律规定惯性系，仍成立。

第二定律 $$\vec F=\displaystyle\frac{d\vec p}{dt}$$​ 仍成立，但注意动量是相对论下的。

- 恒定力作用下粒子加速，速度将趋近于光速但不能超过。见 Griffiths Example 12.10。

第三定律不成立。

### 相对论电磁学

未完待续

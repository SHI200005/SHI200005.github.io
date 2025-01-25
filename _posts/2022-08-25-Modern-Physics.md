---
layout: post
title: 近代物理
categories: BS-NJU-Course-Review-Physics
description: 有点像高年级课程之前的预科班
keywords: modern physics
mathjax: true
---

任课老师是好老师，但不妨碍课是门烂课，学了不如不学，不如自学。所以我们接着自学 **Griffiths**（引用体内为 Griffiths）。

| 学习时间                 | 大二下                                                                                |
| 周课时                     | 4                                                                                         |
| 本人成绩                 | 98                                                                                       |
| 课程教材                 | 徐克尊 《近代物理学（第4版）》中科大出版社 2019 |
| 个人建议参考教材 | 无                                                                                        |
| 先修课程                 | 理论力学 量子力学 电动力学 数学物理方法                   |

那时候氢原子电子自旋轨道相互作用，教材上赫然写着轨道角动量和自旋角动量不再分别守恒，而总角动量守恒，轨道角动量和自旋角动量分别绕着总角动量做拉莫尔进动。首先，我根本不知道什么是拉莫尔进动；其次，看着哈密顿的两个角动量点乘，我看不出怎么这俩不守恒，而总角动量又守恒，更别提谁绕着谁做拉莫尔进动了。

## 不含时微扰理论

设 $$\hat H^0\psi_n^0=E_n^0$$，加上微扰 $$\hat H=\hat H^0+\lambda\hat H'$$，按 $$\lambda$$ 的不同阶展开。[笔记](https://shi200005.github.io/download_file/Quantum_Mechanics_Time_Independent.pdf)

如果基态能量非简并，

- 一阶微扰的能量修正

  $$\hat H^0\psi_n^1+\hat H'\psi_n^0=E_n^0\psi_n^1+E_n^1\psi_n^0$$，用 $$\langle\psi_n^0\vert$$ 作用一下得 $$E_n^1=\langle\psi_n^0\vert\hat H'\vert\psi_n^0\rangle$$。

  > ... the first-order correction to the energy is the *expectation value* of the perturbation in the *unperturbed* state. 

  [经典对应](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#正则微扰理论)：理论力学里的正则微扰一阶近似的例子里，也有能量修正是非微扰解在一阶微扰下的期望，可见量子和经典有很好的对应。

- 一阶微扰波函数和二阶微扰能量修正

  把 $$\psi_n^1$$ 用 $$\psi^0_m$$ 为基展开（除去 $$m=n$$），带入得 $$\displaystyle\psi_n^1=\sum_{m\ne n}\frac{\langle\psi_m^0\vert\hat H'\vert\psi_n^0\rangle}{E_n^0-E_m^0}\psi_m^0$$ 。

  $$\hat H^0\psi_n^2+\hat H'\psi_n^1=E_n^0\psi_n^2+E_n^1\psi_n^1+E_n^2\psi_n^0$$，最后得 $$\displaystyle E_n^2=\sum_{m\ne n}\frac{\vert\langle\psi_m^0\vert \hat H'\vert\psi_n^0\rangle\vert^2}{E_n^0-E_m^0}$$。

如果基态能量简并，

$$\psi^0=\alpha\psi_a^0+\beta\psi_b^0$$ , $$\langle\psi_a^0\vert\psi_b^0\rangle=0$$，则微扰造成的能级修正将造成能级分裂。

- 二重简并的一阶微扰的能量修正

  设  $$\hat W_{ij}=\langle\psi_i^0\vert\hat H'\vert \psi_j^0\rangle$$，则 $$E_{\pm}^1=\ldots\pm\ldots$$ 见 Griffiths Eq.[6.26]。一般也不用算这么麻烦的。显然 $$\psi^0$$ 是 $$\hat H$$ 的本征函数，线性组合系数是什么？我们需要找到一个与 $$\hat H'$$ 对易的算符 $$\hat A$$（对应的物理量守恒），使 $$\psi^0$$ 同时是两个算符的本征函数，这时有结论 $$W_{ab}=0$$，这样分裂的两个能级分别是 $$W_{aa}$$ 和 $$W_{bb}$$，计算方法和非简并情况一样。这种情况下，$$\hat A'$$ 的本征值可以用来标记量子态，这个本征值就被称为**好量子数**，例如不考虑微扰的氢原子电子波函数中的 $$n,l,m$$ 都是好量子数。

- 多重简并的一阶微扰能量修正

  见书上 6.2.2 例子。

### 氢原子能级的精细结构

能量修正值与能量值的数量级之比是 $$\alpha^2$$ 量级（就解释了这玩意为啥叫精细结构常数），看下面结论就明白了。如果是非氢原子，精细结构的能量修正与 $$Z$$ 的四次方成正比，所以重元素的相对论效应更明显。

#### 相对论动能修正

在原子中相对论效应通常很小，可以在非相对论的薛定谔方程的基础上，作相对论效应修正而得到精细结构。在[相对论力学](https://shi200005.github.io/2022/04/10/Electrodynamics/#相对论力学)中，相对论动能为 $$\displaystyle T=\frac{mc^2}{\sqrt{1-(v/c)^2}}-mc^2$$，展开得 $$\displaystyle\frac{p^2}{2m}-\frac{p^4}{8m^3c^2}+\ldots$$。于是微扰哈密顿 $$\displaystyle\hat H_r'=-\frac{\hat p^4}{8m^3c^2}$$......

微扰是球对称的，则可以用非简并微扰处理（pending！！）最终 $$\displaystyle E_r^1=-\frac{E_n^2}{2mc^2}(\frac{4n}{l+1/2}-3)=E_n\alpha^2\frac{1}{4n^2}(\frac{4n}{l+1/2}-3)$$。

#### 自旋 - 轨道相互作用修正

[力学 - 拉莫尔进动](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#拉莫尔进动)里已经导出匀速圆周运动带电粒子的磁矩 $$\displaystyle\vec\mu=\frac{q}{2m}\vec L$$，于是电子的磁矩为 $$\displaystyle\vec\mu_e=-\frac{e}{2m_e}\vec L_e$$。然而这是经典的结论，考虑电子的**自旋磁矩** $$\vec S$$，量子电动力学（我不会）给出的结论是 $$\displaystyle\vec\mu_e=-g_s\frac{e}{2m_e}\vec S$$，其中 $$g_s\approx 2$$，也就是 $$\displaystyle\vec\mu_e=-\frac{e}{m_e}\vec S$$。

如果把电子视为静止，原子核围绕其做轨道旋转，根据[毕奥 - 萨阀尔定律](https://shi200005.github.io/2022/03/29/Electromagnetism/#毕奥-萨筏尔定律)计算原子核在电子处产生磁场 $$\vec B$$。如果把原子核视为静止，电子围绕其做轨道旋转有**轨道角动量** $$\vec L$$。原子核在电子处产生的磁场和电子轨道角动量之间的关系是 $$\displaystyle\vec B=\frac{1}{4\pi\epsilon_0}\frac{e}{mc^2r^3}\vec L$$。

电子**自旋**磁矩放在原子核绕电子**轨道**旋转形成的磁场里有[能量](https://shi200005.github.io/2022/03/29/Electromagnetism/#安培力) $$H=-\vec{\mu}·\vec{B}$$。带入上面的结论，转换为原子核静止的实验室坐标系（见 Griffiths 6.3.2，我现在还不会），得自旋 - 轨道相互作用附加能量算符 $$\hat H'_{so}=\xi(r)\hat S\cdot\hat L$$，其中 $$\displaystyle \xi(r)=\frac{e^2}{8\pi\epsilon_0}\frac{1}{mc^2r^3}$$。

分析这个附加哈密顿，考虑 $$[\hat S_i,\hat L_j]=0$$，可以算出 $$[\hat H'_{so},\hat L]=i\hbar\xi(r)\hat S\times\hat L$$，$$[\hat H'_{so},\hat S]=i\hbar\xi(r)\hat L\times\hat S$$，$$[\hat H'_{so},\hat S^2]=0$$，$$[\hat H'_{so},\hat L^2]=0$$。可以看出，这个附加能量使自旋和轨道角动量不再分别守恒，但总角动量 $$\vec J=\vec L+\vec S$$ 守恒。回忆不显含时间物理量的海森堡方程 $$\displaystyle\frac{d}{dt} \langle Q\rangle=\frac{i}{\hbar}[\hat H,\hat Q]$$，不难推出 $$\displaystyle\frac{d}{dt}\vec L=\frac{i}{\hbar}\vec J\times\vec L$$, $$\displaystyle\frac{d}{dt}\vec S=\frac{i}{\hbar}\vec J\times\vec S$$。经典图像：$$\vec{L}$$ 和 $$\vec{S}$$ 以相同的角速度围绕 $$\vec{J}$$ 做[拉莫尔进动](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#拉莫尔进动)，大小不变，方向改变。$$m_l$$ 和 $$m_s$$ 就不再是好量子数，描述电子状态的好量子数为 $$n,l,j,m_j$$。$$j=l+s,l-s$$，其中电子自旋量子数 $$s=1/2$$。

再根据 $$J^2=L^2+S^2+2\vec L\cdot\vec S$$ 算出 $$\hat H\cdot\hat S$$ 的本征值，得 $$\displaystyle E_{fs}^1=E_n\alpha^2\frac{1}{n^2}(\frac{n}{j+1/2}-\frac{3}{4})$$。考虑了自旋 - 轨道耦合后，能级将按照 $$j$$ 的不同取值（$$\vec{S}$$ 和 $$\vec{L}$$ 的平行或反平行取向）而分裂。

### 塞曼效应

现象：把光源放在磁场中，光源发出的每一条谱线都会分裂成几条偏振的谱线。

磁矩放在磁场里有[能量](https://shi200005.github.io/2022/03/29/Electromagnetism/#安培力) $$H=-\vec{\mu}·\vec{B}$$。讨论原子磁矩时，由于原子核磁矩比电子磁矩小 2~3 个数量级，所以忽略原子核磁矩。对于外磁场中的单电子，塞曼效应微扰为 $$\displaystyle H_Z'=-(\vec\mu_l+\vec\mu_s)\cdot\vec B_{\text{ext}}=\frac{e}{2m}(\vec L+2\vec S)\cdot\vec B_{\text{ext}}$$。

原子内部磁场造成自旋 - 轨道耦合微扰，外磁场造成塞曼效应微扰，最终效果要看内外磁场的相对大小。内磁场远小于外磁场时，塞曼效应微扰占主导；外磁场远小于内磁场时，自旋 - 轨道耦合微扰占主导；内外磁场可以相比拟时，有点难搞，我不搞。在这里我只提及弱外磁场的情况，因为与**电子顺磁共振**相关。

#### 弱外磁场塞曼效应

可以首先忽略原子与外磁场的相互作用，在此基础上考虑原子与外磁场的作用。上面已经说过，考虑自旋 - 轨道耦合，好量子数为 $$n,l,j,m_j$$，一阶微扰能量修正为 $$\displaystyle E_Z^1=\langle n l j m_j\vert\hat H_Z'\vert nljm_j\rangle=\frac{e}{2m}\vec B_{\text{ext}}\cdot\langle\vec L+2\vec S\rangle$$。前面已经说过，$$\vec J$$, $$\vec S$$ 都绕着 $$\vec J$$ 进动，一顿操作猛如虎，参见 Griffiths 6.4.1，得 $$\langle\vec L+2\vec S\rangle=g_J\langle\vec J\rangle$$，其中 $$\displaystyle g_J=1+\frac{j(j+1)-l(l+1)+3/4}{2j(j+1)}$$ 为**朗德因子**。于是 $$E_Z^1=\mu_Bg_JB_{\text{ext}}m_j$$，其中 $$\displaystyle\mu_B=\frac{e\hbar}{2m}$$ 是**玻尔磁子**（轨道磁矩的最小单元）。

弱磁场下这种能级分裂在普通光学波段上太小。将总磁矩分解为平行于 $$J$$ 的分量和垂直于 $$J$$ 的分量。可以证明垂直分量的平均值为 $$0$$，平行分量（也称有效磁矩）是守恒量。有效磁矩在外磁场有取向势，按照 $$m_j$$ 的取值分裂。能级间隔为 $$ΔE=g_jμ_BB$$。在垂直于外磁场的方向上加频率满足频率为上述 $$ΔE/h$$ 时，相邻能级之间会有很大的概率发生跃迁，电磁波于磁能级间隔对应的固有频率发生共振而被强烈地吸收，就是磁共振现象。前提是原子的磁矩不是 $$0$$，这种固体样品中磁矩不为零的原子会顺着外磁场排列...(参见《电磁学 - 磁介质》)，这种磁共振又叫**电子顺磁共振**。

### 氢原子能级的超精细结构

略。

## 变分原理

原理：$$E_g\le\langle\psi\vert\hat H\vert\psi\rangle=\langle\hat H\rangle$$。应用：化学中寻找复杂分子的基态能量，反正不知道波函数具体是啥，用一堆可调参数瞎写波函数疯狂算能量，算出来最小的那个能量一般很接近分子的基态能量。

### 氦原子基态能量

实验值为 $$E_g=-78.975eV$$，哈密顿 $$\hat H\psi_0=(8E_1+V_{ee})\psi_0$$。

- 若直接忽略两电子之间的库伦势 $$v_{ee}$$，波函数为 $$\displaystyle\psi_{0}(\vec r_1,\vec r_2)=\psi_{100}({\vec r_1})\psi_{100}({\vec r_2})=\frac{8}{\pi a^3}e^{-2(r_1+r_2)/a}$$，能量为基态氢原子能量的 $$8$$ 倍（玻尔公式中），即 $$109eV$$。这个能量比实验值低，因为哈密顿不对。
- 不忽略库伦势，但带入波函数为氢原子基态波函数的乘积，一顿操作猛如虎，得到基态能量约 $$-75eV$$。这个能量比实验值略高，但很接近了。这里波函数是错的，但八九不离十，而哈密顿是对的。
- 考虑两电子相互作用对波函数的影响，对每个电子来说原子核电荷被另一个电子部分屏蔽为 $$Z<2$$，再带着参数 $$Z$$ 将解出的假基态能量对 $$Z$$ 求的极小值，得到基态能量约 $$-77.5eV$$，比之前的解还接近实验值。

## WKB 近似

> The **WKB** (Wentzel, Kramers, Brillouin) method is a technique for obtaining approximate solutions to the **time-independent** Schrödinger equation in **one dimension** (the same basic idea can be applied to many other differenctial equations, and to the **radical part** of the Schrödinger equation in three dimensions). It is particularly useful in calculating **bound-state energies** and **tunneling rates** through pentential barriers.

在[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/#定态薛定谔方程)中已经讨论过方势下波函数的解。现在假设 $$V(x)$$ 不是常数，但相对于 $$1/k$$ 或 $$1/\kappa$$ 变化缓慢。

### $$E>V$$

薛定谔方程写作 $$\displaystyle\frac{\partial^2\psi}{\partial x^2}=-\frac{p^2}{\hbar^2}\psi$$, where $$p(x)=\sqrt{2m[E-V(x)]}$$ is real. 设 $$\psi(x)=A(x)e^{i\phi(x)}$$。近似：$$A''/A\ll(\phi')^2 \text{ and }p^2/\hbar^2$$ 一顿操作猛如虎，$$\displaystyle\psi(x)\approx\frac{C}{\sqrt{p(x)}}e^{\pm\frac{i}{\hbar}\int p(x)dx}$$。

### 隧穿

考虑方势垒散射态，一顿操作猛如虎，得隧穿率 $$T\approx e^{-2\gamma}$$ 其中 $$\displaystyle\gamma=\frac{1}{\hbar}\int_0^a\vert p(x)\vert dx$$。

#### $$\alpha$$ 衰变源的寿命

放射性衰变的种类

- $$α$$ 衰变：原子核吐一个 $$α$$ 粒子（氦核）

- $$β$$ 衰变：核里面质子/中子的转换过程中，可能涉及电子等粒子的释放（14N 的衰变就是一种β衰变，衰变为 14C，14C 测年法的原理......）
- $$γ$$ 跃迁：原子核经历 $$α$$ 衰变或 $$β$$ 衰变以后往往处于激发态，原子核从激发态到较低能态或基态的退激发跃迁......

$$\alpha$$ 衰变模型：喷出的 $$\alpha$$ 粒子具有一个正能量，离核近的时候有吸引负势，出了这个范围被带正电的母核库伦排斥，有衰减的正排斥势。见 Griffiths Figure 8.5，中间形成非方势垒，可以算 $$\alpha$$ 粒子逃出去的概率。结论：$$\displaystyle\gamma=K_1\frac{Z}{\sqrt{E}}-K_2\sqrt{Zr_1}$$，母核寿命 $$\displaystyle\tau=\frac{2r_1}{v}e^{2\gamma}$$，对于不同母核，指数项为主要特征，近似有 $$\log\tau\propto1/\sqrt{E}$$。

### The Connection Formulas

$$E>V$$ or $$E<V$$ 的 WKB 近似在 $$E\to V$$ 时 $$p(x)$$ 发散。那怎么办？见 Griffiths 8.3。[贝塞尔函数](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#贝塞尔函数)、Airy's function。

## 含时微扰理论

之前说过，以上都是定态薛定谔方程。现在我们研究**跃迁**过程。如果哈密顿中的含时部分远小于定态部分，含时部分可以看做一个微扰。[笔记](https://shi200005.github.io/download_file/Quantum_Mechanics_Time_Dependent.pdf)

### 二能级系统

设系统在非微扰下有两个本征态，分别为 $$\hat H_0\psi_a=E_a\psi_a$$, $$\hat H_0\psi_b=E_b\psi_b$$，其中 $$E_b> E_a$$。考虑微扰，波函数仍以本征态为基展开，$$\Psi(t)=c_a(t)\psi_ae^{-iE_at/\hbar}+c_b(t)\psi_be^{-iE_bt/\hbar}$$。系统随时间的演化就是考察 $$c_a(t)$$, $$c_b(t)$$。

设 $$\hat H=\hat H_0+\hat H'(t)$$。带入薛定谔方程 $$\hat H\Psi=i\hbar\Psi$$。设 $$H_{ij}'=\langle\psi_i\vert\hat H'\vert\psi_j\rangle$$，一般来说矩阵对角元都是零，即 $$H_{ii}'=\langle\psi_i\vert\hat H'\vert\psi_i\rangle=0$$，因为我们考虑微扰使系统在两个能级之间跃迁，而不改变本征态对应的本征能量。一顿操作猛如虎，得方程组


$$
\begin{cases}
\displaystyle\dot c_a=-\frac{i}{\hbar}H_{ab}'e^{-i\omega_0t}c_b \\
\displaystyle\dot c_b=-\frac{i}{\hbar}H_{ba}'e^{i\omega_0t}c_a.
\end{cases}
$$


其中 $$\omega_0=(E_b-E_a)/\hbar$$。

#### 一阶含时微扰理论

设 $$c_a(0)=1$$, $$c_b(0)=0$$，带入微分方程组一次，得


$$
\begin{cases}
\displaystyle c_a^{(1)}(t)=1 \\
\displaystyle c_b^{(1)}(t)=-\frac{i}{\hbar}\int_0^tH_{ba}'(t')e^{i\omega_0t'}dt'.
\end{cases}
$$

##### 多能级推广

如果系统初态在 $$\psi_N$$，


$$
c_N(t)\approx1-\frac{i}{\hbar}\int_0^tH'_{NN}(t')dt'\\
c_m(t)\approx\frac{i}{\hbar}\int_0^tH'_{mN}(t')e^{i(E_m-E_n)t'/\hbar}dt'
$$


##### 正弦微扰

若 $$\hat H'(\vec r,t)=V(\vec r)\cos(\omega t)$$，$$V_{ij}=\langle\psi_i\vert V\vert\psi_j\rangle$$。在 $$\omega\approx\omega_0$$ 下近似，一顿操作猛如虎，得 $$\displaystyle P_{a\to b}(t)=\vert c_b(t)\vert^2\approx\frac{\vert V_{ba}\vert^2}{\hbar}\frac{\sin^2[(\omega_0-\omega) t/2]}{(\omega_0-\omega)^2}$$。

### 原子与电磁波相互作用

原子与电场相互作用。设原子尺度远小于电磁波尺度。设电磁波为单色偏振波，则可以视为原子泡在 $$\vec E=E_0\cos(\omega t)\vec e_k$$。则 $$\hat H'_{ba}=-\mathscr{P}E_0\cos(\omega t)$$，其中 $$\mathscr{P}=q\langle\psi_b\vert z\vert\psi_a\rangle$$，使我们想起来经典电磁学里的**电偶极矩** $$q\vec r$$。泡在这样的电场里，就是把上面正弦微扰情况里的 $$V_{ba}$$ 换成 $$-\mathscr PE_0$$。

如果原子本来在低能态，吸收能量 $$E_b-E_a=\hbar\omega_0$$ 跃迁到高能态，可算出 $$\displaystyle P_{a\to b}(t)\approx(\frac{\vert \mathscr P\vert E_0} {\hbar})^2\frac{\sin^2[(\omega_0-\omega) t/2]}{(\omega_0-\omega)^2}$$。

如果原子本来在高能态，吸收能量 $$E_b-E_a=\hbar\omega_0$$ 跃迁到低能态，可算出 $$\displaystyle P_{b\to a}(t)\approx(\frac{\vert \mathscr P\vert E_0} {\hbar})^2\frac{\sin^2[(\omega_0-\omega) t/2]}{(\omega_0-\omega)^2}$$。同时释放两个光子，这就是**激光**的原理。

- laser: light amplification by stimulated emission of radiation.

### 自发辐射

略。

### 氢原子跃迁的选择定则

辐射率的计算归结于计算 $$\langle\psi_i\vert\hat{\vec r}\vert\psi_j\rangle$$。详见笔记，得到跃迁要满足选择定则：$$Δl=±1$$, $$Δm=0,±1$$。

<img src="\images\blog\Modern_Physics.jpg" alt="modern-physics-1" width="400px;" />

## 浸渐近似

前面一部分含时微扰考虑系统在两个不同状态间跃迁，不同量子态的本征值不变，那个矩阵对角元都为零。现在研究在外界变化比系统内部变化慢很多的情况下，本征态变化的情况，用 **adiabatic approximation**。在这里，我们不需要哈密顿的含时部分很小，只需要它很慢。在分子物理学中，从假设原子核静止开始分析电子波函数的近似方法是 **Born-Oppenheimer approximation**。

### 浸渐理论

> ...if the particle was initially in the *n*th eigenstate of $$\hat H^i$$, it will be carried (under the Schrödinger equation) into the *n*th eigenstate of $$\hat H^f$$...

证明过程略。先假设系统收到又小又慢的微扰 $$\hat H'=Vf(t)$$，因为小，可以用一阶微扰理论。结合一阶含时和不含时微扰理论，如果系统初态为 $$\Psi(0)=\psi_n^i$$，则系统末态量子态变化 $$\psi_n\to\psi_m,m\neq n$$ 的概率为 $$\displaystyle\langle\psi(T)\vert\psi_m^f\rangle =[\frac{iAV_{nn}V_{nm}}{\hbar(E_m-E_n)}+$$ $$\sum_{n\neq k\neq m}$$ $$\frac{V_{{nk}}V_{kn}}{(E_n-E_k)(E_m-E_n)}$$ $$]e^{iE_nT/\hbar}$$，是一个**二阶小量**。现在假设扰动是又慢又大的，则可以切成很多又慢又小的微扰，而量子态转换的概率是二阶小量，会随着切割份数无穷而趋于零。（[经典对应](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#浸渐不变量与哈内角)）与经典力学中**哈内角**相对应的量子力学概念是**贝瑞相**和**阿哈罗诺夫 - 玻姆效应**，之后没用过，本科也没学，我就先不写。test

## 散射

前面贝瑞相我应该不写了，但这部分我之后会回来写。但现在不写。等我写完这部分就1.0了。


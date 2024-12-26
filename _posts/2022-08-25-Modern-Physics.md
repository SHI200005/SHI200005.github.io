---
layout: post
title: 近代物理
categories: BS-NJU-Course-Review-Physics
description: 有点像高年级课程之前的预科班
keywords: modern physics
mathjax: true
---

| 学习时间                 | 大二下                                                                                |
| 周课时                     | 4                                                                                         |
| 本人成绩                 | 98                                                                                       |
| 课程教材                 | 徐克尊 《近代物理学（第4版）》中科大出版社 2019 |
| 个人建议参考教材 | 无                                                                                        |
| 先修课程                 | 理论力学 量子力学 电动力学                                           |

任课老师是好老师，课是门烂课，学了不如不学，不如自学。如同氢原子能级的精细结构，真不知道没学量子力学和电动力学咋学。所以我们接着自学 Griffiths。

## 不含时微扰理论

设 $$\hat H^0\psi_n^0=E_n^0$$，加上微扰 $$\hat H=\hat H^0+\lambda\hat H'$$，按 $$\lambda$$ 的不同阶展开。

如果基态能量非简并，

- 一阶微扰的能量修正

  $$\hat H^0\psi_n^1+\hat H'\psi_n^0=E_n^0\psi_n^1+E_n^1\psi_n^0$$，用 $$\langle\psi_n^0\vert$$ 作用一下得 $$E_n^1=\langle\psi_n^0\vert\hat H'\vert\psi_n^0\rangle$$。

  > ... the first-order correction to the energy is the *expectation value* of the perturbation in the *unperturbed* state. 

  [经典对应](https://shi200005.github.io/2022/04/30/Advanced-Classical-Mechanics/#正则微扰理论)：理论力学里的正则微扰一阶近似的例子里，我们看到非线性谐振子的振幅修正为零，频率修正为 $$\displaystyle\omega_0(1+\frac{3b}{8k}A^2)$$。由于谐振子能量为 $$\displaystyle\frac{1}{2}m\omega^2A^2$$，不难看出能量修正为 $$\displaystyle\frac{3}{8}A^4b+o(b)$$。而非微扰解 $$x=A\sin(\omega_0(t+\beta))$$ 在微扰 $$bx^4$$ 下的期望 $$bA^4\langle\sin^4(\omega_0(t+\beta))\rangle$$ 就是 $$\displaystyle\frac{3}{8}A^4b$$。可见量子和经典有很好的对应。

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

弱磁场下这种能级分裂在普通光学波段上太小。在垂直于外磁场的方向上加频率满足频率为上述 $$ΔE/h$$ 时，相邻能级之间会有很大的概率发生跃迁，电磁波于磁能级间隔对应的固有频率发生共振而被强烈地吸收，就是磁共振现象。前提是原子的磁矩不是 $$0$$，这种固体样品中磁矩不为零的原子会顺着外磁场排列...(参见《电磁学 - 磁介质》)，这种磁共振又叫电子顺磁共振。

#### 氢原子能级的超精细结构

略。

## 变分原理



## WKB 近似



## 含时微扰理论



## 绝热近似



## 散射





麦克斯韦分布的来源（[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)）：麦克斯韦分布是气体分子质心运动的速度分布，它满足非简并条件（$$e^\alpha\gg1$$）的理想气体所遵从的麦克斯韦-玻尔兹曼分布的一种特殊情形。

玻尔兹曼分布。能量均分定理 -> 不同种类分子的自由度 -> 理想气体热容。 不如直接去看[统计物理](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/)。固体热容不如直接去看**固体物理**但我还没打算写。



## 量子力学初步

### 波粒二象性

光子的粒子特性：普朗克的辐射不连续量子假说（[统计物理 - 玻尔兹曼统计的应用](https://shi200005.github.io/2022/09/10/Statistical-Mechanics/#%E7%8E%BB%E5%B0%94%E5%85%B9%E6%9B%BC%E7%BB%9F%E8%AE%A1%E7%9A%84%E5%BA%94%E7%94%A8)、光电效应实验、康普顿实验。光子的波动性：干涉、衍射。

电子的波动性：德布罗意波、电子的晶体衍射实验、电子双棱镜干涉实验。应用：低能单子衍射仪（LEED），电子显微镜，e.g., 透射电镜（TEM）、反射电竞（REM）、扫描电镜（SEM）。

## 电子自旋和原子能级的精细结构

### 电子自旋和自旋-轨道相互作用

能级的精细结构分裂导致相应光谱的精细结构分裂。原子吸收和辐射电磁波可以近似看作是一种电偶极振荡，对于这种电偶极辐射，原子对应的跃迁要满足选择定则：$$Δl=±1$$, $$Δj=0,±1$$. 这个到了量子力学我详细写。
![](/images/blog/modern-physics-1.jpg)

### 外场中的原子

将总磁矩分解为平行于J的分量和垂直于 $$J$$ 的分量。可以证明垂直分量的平均值为 $$0$$，平行分量（也称有效磁矩）时守恒量。有效磁矩在外磁场有取向势，按照 $$m_j$$ 的取值分裂。能级间隔为 $$ΔE=g_jμ_BB$$。

## 核衰变和核反应

### 放射性衰变

α衰变：原子核吐一个α粒子

- β衰变：核里面质子/中子的转换过程中，可能涉及电子等粒子的释放。(14N的衰变就是一种β衰变，衰变为14C，14C测年法的原理是......)
- γ跃迁：原子核经历α衰变或β衰变以后往往处于激发态，原子核从激发态到较低能态或基态的退激发跃迁......

---
layout: post
title: 电磁学 1.0
categories: BS-NJU-Course-Review-Physics
description: 电动力学前先来点
keywords: Electromagnetism
mathjax: true
---

The author wrote an physics article that pointed out a mathematical flaw of "Answers to 1000 Electromagnetic Problems (电磁学千题解) 2.1.45", the most authorized problem set on electromagnetism in China. The article won the first prize (~7%) of the 24th Basic Subject Forum (第24届基础学科论坛) on Sept 3, 2021. [Here is the link of the announcement](https://mp.weixin.qq.com/s/jYr5Fe89pT9xQCqE7lS8qw). This is such a accomplishment that I have to pin it in English on my website!

| 课程名称                | 电磁学                                                                                            |
| 学习时间                | 大二上                                                                                            |
| 周课时                    | 3                                                                                                      |
| 本人成绩                | 93                                                                                                    |
| 课程教材                | 徐游《电磁学》科学出版社                                                          |
| 个人建议参考教材 | 张之翔《电磁学千题解》科学出版社  詹鹏老师电动力学课件  |
| 先修课程                | 微积分 线性代数  复变函数                                                          |

第一部分：建立麦克斯韦方程组


$$
\text{微分方程}\\
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\\
\nabla\times\vec H=\vec J_f+\frac{\partial\vec D}{\partial t}\\
\nabla\cdot\vec D=\rho_f\\
\nabla\cdot\vec B=0\\
\text{边值关系}\\
\mathbf{\hat{n}}_{21}\times(\vec E_2-\vec E_1)=0\\
\mathbf{\hat{n}}_{21}\times(\vec H_2-\vec H_1)=\alpha_f\\
\mathbf{\hat{n}}_{21}\cdot(\vec D_2-\vec D_1)=\sigma_f\\
\mathbf{\hat{n}}_{21}\cdot(\vec B_2-\vec B_1)=0\\
\text{本构关系}\\
\vec D=\vec D(\vec E,\vec B)\\
\vec H=\vec H(\vec E,\vec B)\\
$$



## 真空中点电荷产生的电场

### 固定点电荷——库仑定律

$$\displaystyle \vec F_{12}=\frac{1}{4\pi\epsilon_0}\frac{Q_1Q_2}{r_{21}^3}\vec r_{12}$$ 中学的时候学的系数是 $$k$$，现在为啥变成 $$\displaystyle \frac{1}{4\pi\epsilon_0}$$？方便后面高斯定理积分。满足**叠加原理**。

空间中的电荷源产生电场，试探电荷 $$q$$ 泡在这种电场里，受到的力有一种之和电荷源有关的关系：电荷源在空间中产生了电场 $$\vec E=\displaystyle\frac{1}{4\pi\epsilon_0}\displaystyle\int_{V'}\displaystyle\frac{\vec r}{r^3}\rho(\vec x')dV'$$。对应标量势 $$\varphi(\vec x)=\displaystyle\frac{1}{4\pi\epsilon_0}\displaystyle\int_{V'}\displaystyle\frac{\rho(\vec x')}{r}dV'$$，$$\vec E(\vec x)=-\nabla\varphi(\vec x)$$，完全可以通过矢量分析联系起来。

适用条件
- 真空、点电荷、静止。点电荷相对静止，且相对观察者也静止。可以拓宽到静源 & 动电荷，不能延拓到动源 & 静电荷。
- 作为动源，[有推迟效](https://shi200005.github.io/2022/04/10/Electrodynamics/#%E6%8E%A8%E8%BF%9F%E5%8A%BF)。一动一不动的两个点电荷之间的相互作用力与牛顿第三定律矛盾。

**电偶极矩**：等量异号点电荷对 $$q$$，负电荷指向正电荷适量 $$\vec l$$，电偶极矩为 $$\vec p=q\vec l$$。后续我们研究电偶极子在空间产生的电场特点。

重要推论：无限大均匀带电金属板两侧为方向相反的匀强电场。匀强电场的产生 -> 无限大平行板电容器，内部为匀强电场，外部电场为 0。后续结合高斯定理理解。

### 高斯定理、环路定理

高斯定理积分形式：电通量 $$\displaystyle\oint_S\vec{E}·d\vec{S}=\frac{1}{\epsilon_0}\sum_{S内}Q$$ (discrete version) $$\displaystyle=\frac{1}{\epsilon_0}\int_{S内}\rho d\tau$$ (continuous version) ；微分形式：$$\displaystyle\nabla\cdot\vec E(\vec x)=\frac{1}{\epsilon_0}{\rho(\vec x)}$$。**有源场**。

- 微分形式联想记忆：$$\nabla^2\displaystyle\frac{1}{r}=-4\pi\delta(\vec r)$$。
- 可以推广到非稳态的动态场，$$\displaystyle\nabla\cdot\vec E(\vec x,t)=\frac{1}{\epsilon_0}{\rho(\vec x,t)}$$。

环路定理积分形式：$$\displaystyle\oint_l\vec E\cdot d\vec l=0$$；微分形式：$$\nabla\times \vec E=0$$。**无旋场**（保守场、有心力场）。

- 只适用于**静电场**，不可以推广到非稳态的动态场。

- 库仑定律 + 叠加原理 <--> 高斯定理 + 环路定理  其中**环路定理等价于库仑力是有心力** 证明见电磁学课件 01-10。19 - 20 秋 期中试题：推导**旋度**为 0 与**有心力场**的等价性。

> 在不同介质的交界面上，由于越过分界面两侧介质的介电特性和界磁特性会发生跳变性（非连续性）的差异，因此在一般情况下，电磁场也会发生突变。换句话说，在这个界面上麦克斯韦方程组的**微分形式将失效**（即麦克斯韦方程组中出现的空间导数失去意义）。但是，麦克斯韦方程组的**积分形式仍然成立**。
>
> Maxwell 方程组在其微分形式和积分形式之间等效转换的前提是电磁场在解域内处处连续可微。——电动力学课件 1.5

### 电流场

#### 电荷守恒、连续性方程

电流 $$\displaystyle I=\frac{\Delta Q}{\Delta t}=\int_S\vec J\cdot d\vec S$$，其中 $$\vec J$$ 是电流密度矢量  -- **电荷守恒**  -->  电荷-电流连续性方程 $$\displaystyle\nabla\cdot\vec J=-\frac{\partial\rho}{\partial t}$$

#### 欧姆定律

$$U=IR$$，给出**电阻率**和**电导率**的关系 $$\displaystyle\sigma=\frac{1}{\rho}$$。微分形式：$$\vec E=\rho\vec j$$, $$\vec j=\sigma \vec E$$。经典模型：Drude 模型。

- 千题解链接 [4.2.41] 漏电电容器。

## 真空中运动带电粒子产生的磁场

**奥斯特**实验：长直载流导线与之平行放置的磁针受力偏转——**电流的磁效应** one of the significances: 突破了非接触物体之间只存在有心力的观念。

### 安培定律

电流元对电流元施加的作用力：$$\displaystyle\vec F_{12}=\frac{\mu_0}{4\pi}\frac{I_1I_2d\vec l_2\times(d\vec l_1\times\vec r_{12})}{r_{12}^3}=\frac{\mu_0}{4\pi}\frac{\vec J_1dV_1\times(\vec J_2dV_2\times\vec r_{12})}{r_{12}^3}$$。原始形式不好用。

- 电流单位“安培”的定义：放在真空中的两条无限长平行导线，通有相等的稳恒电流，若两导线相距 $$1m$$，而每一导线每米长度上所受另一导线对它的作用力为 $$2\times10^{-7}N$$，则导线上的电流定义为 $$1A$$。
- 除非是闭合回路，否则不服从作用力与反作用力定律。

### 毕奥-萨筏尔定律

问：参照电场概念的建立，安培定律能否写成 $$\vec F_{12}=\vec J_1dV_1\times\vec B$$？答：电流源产生的磁场**磁感应强度** $$\vec B$$：$$\displaystyle d\vec B(\vec x)=\frac{\mu_0}{4\pi}\frac{Id\vec l\times\vec r}{r^3}=\frac{\mu_0}{4\pi}\frac{\vec J(\vec x')\times\vec r}{r^3}$$，广延形式 $$\displaystyle\vec B(\vec x)=\frac{\mu_0}{4\pi}\int\frac{\vec J(\vec x')\times\vec r}{r^3}dV'$$。

重要推论：[无限长均匀密绕通电螺线管轴向磁感应强度](http://www.phycai.sjtu.edu.cn/pub/webphy/content/ch08/sec0803.htm)。匀强磁场的产生 -> 无限长通电螺线管，内部为匀强磁场，外部磁场为 0。后续结合环路定理理解。

### 高斯定理、环路定理/安培定理

高斯定理积分形式：$$\displaystyle\oint_S\vec B\cdot d\vec S=0$$，微分形式：$$\nabla\cdot \vec B(\vec x)=0$$ 。**无源场**（磁场线闭合、无自由磁荷）。

- 可以推广到非稳态的动态场，$$\nabla\cdot\vec B(\vec x,t)=0$$。

环路定理积分形式：$$\displaystyle\oint_l\vec B(\vec x)\cdot d\vec l=\mu_0\displaystyle\int_S\vec J\cdot d\vec S$$, $$\nabla\times\vec B(\vec x)=\mu_0\vec J(\vec x)$$。**有旋场**（非保守场、无势场）。

- 不可以推广到非稳态的动态场。

## 电磁感应

动电能生磁，有啥能生电流吗？**法拉第**电磁感应实验真把电流生出来了。

### 法拉第电磁感应定律

前文说过，电流会产生磁场。这个由给定回路磁通变化产生的磁场有什么特点？**楞次定律**：当回路磁通变化时，感应电流所产生的感应磁通总是力图阻止原磁通的变化（能量守恒的必然结果）。

定义**磁通量** $$\displaystyle\Phi_B=\int_S\vec B\cdot d\vec S$$。**感应电动势**：$$\displaystyle\varepsilon=-\frac{d\Phi_B}{dt}=-\int_S(\frac{\partial\vec B}{\partial t})\cdot d\vec S+\oint_l(\vec v\times\vec B)\cdot d\vec l$$，感生电动势 + 动生电动势。注意，这里**感应电场不再是保守场了**。**变化的磁场激发电场**。动生电动势和感生电动势对于参考系是不对称的，我们需要狭义相对论消除（pending！！！）。

考虑感生场，积分形式为 $$\displaystyle\varepsilon=\oint_l\vec E\cdot d\vec l=-\int_S\frac{\partial\vec B}{\partial t}\cdot d\vec S$$  微分形式为 $$\displaystyle\nabla\times\vec E=-\frac{\partial \vec B}{\partial t}$$。

### 位移电流

我们已经指出了不能推广到动态情况的电场旋度如何推广到动态状态，那么磁场旋度呢？如果对 $$\nabla\times\vec B(\vec x)=\mu_0\vec J(\vec x)$$ 两边同时取 $$\nabla\cdot$$，则得 $$\nabla\cdot\vec J(\vec x)=0$$，显然不总成立。引入**电荷守恒**和电场**高斯定理**微分形式，构造位移电流 $$\vec J_D(t)=\epsilon_0\displaystyle\frac{\partial}{\partial t}\vec E$$，随即 $$\nabla\times\vec B(\vec x)=\mu_0(\vec J+\vec J_D)$$ 形式上得到满足。

### 自感与互感

**自感**：用于线圈时，回路可能有外来电流、或回路形状及周围磁介质发生变化，此时穿过回路自身的磁通量随之改变，从而在回路中激发感应电动势。$$\displaystyle\Sigma=-L\frac{dI}{dt}$$ 自感电动势将反抗回路中电流的改变。

**互感**：一对相互靠近的感应线圈，因一个或两个载流线圈的电流变化而在对方线圈中激起感应电动势。$$\displaystyle M_{12}=\frac{\Phi_{12}}{I_2}$$，$$\displaystyle M_{21}=\frac{\Phi_{21}}{I_1}$$，若互感问题不涉及铁磁质，从做功角度切入，可以证明 $$M_{21}=M_{12}=M$$。

无铁磁质感应电路能量 $$\displaystyle L=\frac{1}{2}LI_0^2$$。

## 电介质

介质的存在会使内部电荷分布对外界产生响应，在考虑麦克斯韦方程组时，电荷和电流密度不仅仅只有施加的自由电荷和电流，还有因为介质响应所产生的极化电荷和磁化电流。麦克斯韦方程组中的电荷 $$\rho_0$$ 和电流 $$\vec J_0$$ 将改为 $$\rho=\rho_f+\rho_p$$, $$\vec J=\vec J_f+\vec J_P+\vec J_M$$，其中 f 角标为自由电荷和电流。

### 电介质的行为

如果物体内部电子不能像导体里面那样自由移动，而是**束缚**在一定范围内，会怎么样？

 - 极性分子：分子正负电荷中心不重合。产生机制：电子位移极化（所有）、分子取向极化（极性分子）、离子位移极化（极性分子） ，相当于产生了电偶极矩。后两者效果更明显。

 - 效果：产生**退极化场**，从原来处处电中性变成出现了宏观的极化电荷。

 - 均匀介质：极化电荷出现在介质表面。非均匀介质：可能出现内部体分布。

 - 铁电体可以产生自发极化。

 - 19 - 20 秋期中 试题：平行板电容器对电介质是吸引还是排斥？吸引。可以从电介质插入电容器时受力方向和静电能变化（电极电荷不变时静电能下降）两个角度论述。

 - 电介质内与外场相反 电场 = 外电场 + 退极化场（矢量运算）

   ![Electromagnetism_Dielectric](\images\blog\Electromagnetism_Dielectric.JPG)

   ![Electromagnetism_Dielectric_Ball](\images\blog\Electromagnetism_Dielectric_Ball.JPG)

### 极化强度、极化电荷、电位移矢量和极化电流

**极化强度** $$\vec P$$ （单位体积电偶极矩 $$\vec p$$ 代数和）和**极化电荷** $$\rho_P$$.

- 考虑因为极化而从封闭曲面跑出去的电荷和留在曲面内的 $$\rho_P$$......，得到积分形式 $$\displaystyle\int_V\rho_Pd=-\oint_S\vec P\cdot d\vec S$$；微分形式 $$\rho_P=-\nabla\cdot\vec P$$。均匀介质被均匀极化，内部 $$\rho_P=0$$，只有表面有极化电荷。
- 两种介质分界面，微分形式失效，**通过积分形式推出**分界面极化电荷分布 $$\sigma_P=-(\vec P_2-\vec P_1)\cdot\mathbf{\hat{n}}_{21}$$。

**电位移矢量**（**电感应强度**） $$\vec D$$（辅助物理量）

- 由于我们一般能动地给系统加上自由电荷，然后通过物理学规律求解极化情况，所以构造关于自由电荷的辅助物理量 $$\vec D=\epsilon_0\vec E+\vec P$$，于是 $$\nabla\cdot\vec D=\rho_f$$（高斯定理），**没有环路定理**。

<span style="color: red;">于是，我们得到介质中的麦克斯韦方程组之一</span>：$$\nabla\cdot\vec D=\rho_f$$。两种介质分界面，微分形式失效。通过**积分形式**，高斯定理给出分界面极化电荷分布 $$\mathbf{\hat{n}}_{21}\cdot(\vec D_2-\vec D_1)=\sigma_f$$，若分界面没有自由电荷则界面两侧**法向**分量相等；环路定理给出 $$\mathbf{\hat{n}}_{21}\times(\vec E_2-\vec E_1)=0$$，两侧**切向**分量相等。

- **本构关系** $$\vec D=\vec D(\vec E,\vec B)$$​，对于绝大部分材料，在弱场作用下为线性依赖关系。

  **电极化率** $$\chi$$ 与**介电常数**（**电容率** $$\epsilon$$）

   - 本课程范围内我们只关注**各向同性线性介质**，关系：$$\vec P=\epsilon_0\chi\vec E$$，于是**电容率** $$\epsilon$$ 有 $$\vec D=\epsilon\vec E=\epsilon_0\epsilon_r\vec E=\epsilon_0(1+\chi)\vec E$$。平行板电容器里插入电介质，电容变成 $$C=\epsilon C_0$$。

**极化电流** $$\vec J_P$$ 

- 当 $$\displaystyle\frac{\partial\rho_p}{\partial t}\neq 0$$ 时，根据**连续性方程**，得到**极化电流** $$\vec J_P$$ 满足 $$\vec J_P=\displaystyle\frac{\partial\vec P}{\partial t}$$。

## 磁介质

### 分子环形电流模型

环形电流产生**磁矩** $$\displaystyle\vec m=i\vec S=\frac{1}{2}I(\oint_C\vec r\times d\vec l)=\frac{1}{2}\oint_C\vec r\times\vec jd\tau$$。

安培的**分子电流图像**：分子被旋转的电子环绕，是个小磁体。分子电流整齐排列产生宏观磁化。形成磁矩 $$\vec m=i\vec S=\pi ia^2\vec n$$。也叫**磁偶极矩**，因为其在在很远处激发的磁场满足 $$\displaystyle\vec B=\frac{\mu_0}{4\pi}(-\frac{\vec m}{r^3}+\frac{3(\vec m\cdot\vec r)\vec r}{r^5})$$，和电偶极矩形式一样。

### 磁介质的行为

 - 抗磁介质（所有物质都具有）

   经典解释：核外层固定轨道上电子成对占据，产生电子轨道磁矩
   抱歉，2022.7.27我又在思考一个问题，本课程在经典框架下讨论，此处运用的事实是，轨道上成对的“电子相向运动”，这实属一个很经典的描述，玻尔理论中引入电子轨道运动时，只是为了解释氢原子光谱现象，而轨道上成对电子是不是能用相向运动描述，大概是无法观测的，似乎也没听说过除抗磁性以外的其他物理现象印证这个说法......陷入浅思......所以大概用泡利不相容原理，这一对电子的自旋相反，然后总磁矩为零似乎更合理一些？2024.01.05 量子解释pending！！！

   **超导体**的 Meissner 效应：样品内部磁感应强度为 0。

 - 顺磁介质（多数过渡金属离子具有净磁矩）

   来源；在外磁场作用下，原子/离子磁矩取向与外磁场平行（磁化产生的磁矩大于电子附加磁矩）；无外场时，热涨落与外磁场效应对抗，无法形成有序磁矩

 - 铁磁介质（由永久磁铁的分子电流激发，磁滞曲线） 

 - 其实还有反铁磁、亚铁磁等，但本课程范围不涉及

### 磁化强度与磁化电流密度

我们之前学了分子磁矩可以看作环形电流磁矩 $$\vec m$$，**磁化强度** $$\vec M$$ 是单位体积内分子磁矩代数和。

- 一磁介质体积元的磁化电流，等价于这个体积元的表面净电流。取包围介质元的曲面 $$\vec S$$，其具有边界 $$\vec l$$。在面上穿出来又回去的电流抵消，我们只需考虑其在 $$\vec S$$ 穿过结果没从边界回去/出来的那些表面电流...... $$I_M=\displaystyle\oint_l\vec M\cdot d\vec l$$ ，微分形式  $$\vec J_M=\nabla\times\vec M$$（均匀介质内部 $$I'=0$$ 取任意内部边界有去必有回，只有边界处有磁化电流；**超导**球体内无磁化电流，电流只出现在超导球体的表面层）
- 取散度得 $$\nabla\cdot\vec J_M=0$$，无源，不引起电荷积累，介质磁化电流没有对电荷分布产生贡献，没有磁化电荷（前面极化电荷有相应极化电流）。

这时，我们得到 $$\nabla\times\vec B=\mu_0(\vec J_f+\vec J_M+\vec J_P)+\mu_0\epsilon_0\displaystyle\frac{\partial}{\partial t}\vec E$$。

**磁场强度** $$\vec H$$ （辅助物理量）

- 由于我们一般能动地给系统加上 $$\vec J_f$$，然后通过物理学规律求解磁化情况，所以构造关于 $$\vec J_f$$ 的辅助物理量 $$\displaystyle\vec H=\frac{\vec B}{\mu_0}-\vec M$$，于是 $$\nabla\times\vec H=\vec J_f+\displaystyle\frac{\partial\vec D}{\partial t}$$（环路定理），**没有高斯定理**（见下面永久磁铁的 $$\vec H$$ 图）。$$\vec J_f=0$$ 不等于 $$\vec H=0$$。

<span style="color: red;">于是，我们得到介质中的麦克斯韦方程组之一</span>：$$\nabla\times\vec H=\vec J_f+\displaystyle\frac{\partial\vec D}{\partial t}$$。两种介质分界面，微分形式失效。通过**积分形式**，环路定理给出分界面极化电荷分布 $$\mathbf{\hat{n}}_{21}\times(\vec H_2-\vec H_1)=\alpha_f$$，若分界面没有自由电荷则界面两侧**切向**分量相等；高斯定理给出 $$\mathbf{\hat{n}}_{21}\cdot(\vec B_2-\vec B_1)=0$$，两侧**法向**分量相等。

- **本构关系** $$\vec H=\vec H(\vec E,\vec B)$$，对于绝大部分材料，在弱场作用下为线性依赖关系。

  **磁导率**与**磁化率**

  - 本课程范围内我们首先关注顺磁与抗磁在外场不是很大时的**线性**响应，关系：$$\vec M=\chi_m\vec H$$，于是**磁导率** $$\mu$$ 有 $$\vec B=\mu\vec H=\mu_0\mu_r\vec H=\mu_0(1+\chi_m)\vec H$$。

  - 对于铁磁体，磁导率 $$\mu$$ 不是常量，还决定于铁磁质磁化历史。磁滞回线。

  - 永久磁铁的磁场纯系由永久磁铁的分子电流激发。例：沿轴均匀磁化圆柱形永久磁铁外部 $$\vec M=0$$，表面 $$\vec i'=\vec M$$......

    <img src="\images\blog\Electromagnetism_Permanent.JPG" alt="Electromagnetism_Permanent" width="400px;" />

  - 例：**磁介质分界面**问题：$$\vec H$$ 有**环路定理**，界面两侧**切向**分量相等，可导出 $$\vec B$$ 界面两侧切向分量的关系；假定界面无自由电流，$$\vec B$$ 用**高斯定理**，界面两侧**法向**分量相等，可导出 $$\vec B$$ 界面两侧法向分量的关系。

## 电磁场的能量

### 洛伦兹力

运动电荷在磁场中受洛伦兹力 $$\vec F=q\vec v\times\vec B$$。

上文提到磁场对电流源施加的力是安培力。电流元中有运动电荷，在磁场中受洛伦兹力。洛伦兹力与安培力的关系：导线中安培力是晶格所带电荷受力的总和，是电子所受洛伦兹力的宏观表现。洛伦兹力不做功，只有安培力做功。

于是，带电粒子在电磁场中运动受洛伦兹力与电场力，$$\vec F=q\vec v\times\vec B+q\vec E$$。不幸的是，电场和磁场是耦合的，实际处理极为复杂，但是我们只考虑一些简单情况，可以把各种复杂效应忽略。

应用：磁聚焦、磁约束、荷质比测定、回旋加速器、霍尔效应。

洛伦兹力不做功，那能干啥？例：Griffiths 8.3 磁悬浮列车。

### 电磁场的能量密度和能流密度矢量

> 电磁场对带电体系统作用遵守洛伦兹力，这种作用力使得带点系统的机械能发生变化，......，带点系统的机械能增加量应该等于电磁场能量的减少量。......描述电磁场的能量：电磁场的能量密度 $$w$$ 和电磁场能流密度矢量（**坡印亭矢量**） $$\vec s$$。

孤立体系中的电磁场能量和机械能相互转化 $$\displaystyle\int_{\infty}\vec f\cdot\vec vdV=-\frac{d}{dt}\int_{\infty}wdV$$，$$\nabla\cdot\vec s+\displaystyle\frac{\partial w}{\partial t}+\vec f\cdot\vec v=0$$。由于洛伦兹力不做功，$$\vec f\cdot\vec v=\vec J_f\cdot\vec E$$，...，凑出 $$\vec s=\vec E\times\vec H$$, $$\displaystyle\frac{\partial w}{\partial t}=\vec E\cdot\frac{\partial\vec D}{\partial t}+\vec H\cdot\frac{\partial\vec B}{\partial t}$$。

经观察，容易发现对于各向同性线性介质 $$w=\displaystyle\frac{1}{2}\epsilon E^2+\displaystyle\frac{1}{2}\mu H^2$$​。电场能 + 磁场能。

## Conservation Laws

**This part mainly comes from Griffiths 8.2.**

Analyzing the fields of a moving point charge in Griffiths 10.3.2. Fact: the net electromagnetic force on a pair of moving charges can be in violation of Newton's third law.

###  Momentum

Consider the total electromagnetic force on the charges in volume $$\mathscr V$$  ->  the force per unit $$\vec f=\rho\vec E+\vec J\times\vec B$$. Now transform $$\rho$$, $$\vec J$$ into $$\vec E$$, $$\vec B$$. 

Introduce the **Maxwell stress tensor** $$\displaystyle T_{ij}=\epsilon(E_iE_j-\frac{1}{2}\delta_{ij}E^2)+\frac{1}{\mu_0}(B_iB_j-\frac{1}{2}\delta_{ij}B^2)$$.

> Physically, $$\overleftrightarrow T$$ is the force per unit area (or **stress** acting on the surface). More precisely, $$T_{ij}$$ is the force (per unit area) in the $$i$$th direction acting on an element of surface oriented in the $$j$$th direction--"diagonal" elements ($$T_{xx},T_{yy},T_{zz}$$) represents *pressures*, and "off-diagonal" elements ($$T_{xy},T_{xz}$$,etc.) are *shears*.

Now $$\vec f=\nabla\cdot\overleftrightarrow T-\epsilon_0\mu_0\displaystyle\frac{\partial\vec S}{\partial t}$$, where $$\vec S$$ is the [Poynting vector](https://shi200005.github.io/2022/03/29/Electromagnetism/#%E7%94%B5%E7%A3%81%E5%9C%BA%E7%9A%84%E8%83%BD%E9%87%8F%E5%AF%86%E5%BA%A6%E5%92%8C%E8%83%BD%E6%B5%81%E5%AF%86%E5%BA%A6%E7%9F%A2%E9%87%8F).

The total electromagnetic force on the charges in volume $$\mathscr V$$: $$\vec F=\displaystyle\oint_S\overleftrightarrow T\cdot d\vec a-\epsilon_0\mu_0\frac{d}{dt}\int_\mathscr V \vec Sd\tau$$. Consider the third law, $$\vec F=\displaystyle\frac{d\vec p_{\text{mech}}}{dt}$$, where $$\vec p_{\text{mech}}$$ is the (mechanical) momentum of the particles in volume $$\mathscr V$$. Therefore, $$\displaystyle\oint_S\overleftrightarrow T\cdot d\vec a=\frac{d\vec p_{\text{mech}}}{dt}+\epsilon_0\mu_0\frac{d}{dt}\int_\mathscr V \vec Sd\tau$$. *Momentum stored in the fields*: $$\vec p=\epsilon_0\mu_0\displaystyle\int_\mathscr V \vec Sd\tau$$. *Momentum per unit time flowing in through the surface*: $$\displaystyle\oint_S\overleftrightarrow T\cdot d\vec a$$.

**The momentum density in the fields** is $$\vec g=\epsilon_0\mu_0\vec S=\displaystyle\frac{1}{c^2}\vec S=\epsilon_0(\vec E\times\vec B)$$. 

> when there *are* charges around the field momentum by itself, and the mechanical momentum by itself, are not conserved--charges and fields exchange momentum, and only the *total* is conserved.--Griffiths 8.2

### Angular Momentum

**The angular momentum density in the fields** is $$\vec l=\vec r\times\vec g=\epsilon_0[\vec r(\vec E\times\vec B)]$$.

---

第二部分：静电场与静磁场问题

## 静电场问题

电场与磁场脱耦，问题简化为



$$
\text{微分方程}\\
\nabla\times\vec E=0\\
\nabla\cdot\vec D=\rho_f\\
\text{边界条件}\\
\mathbf{\hat{n}}_{21}\times(\vec E_2-\vec E_1)=0\\
\mathbf{\hat{n}}_{21}\cdot(\vec D_2-\vec D_1)=\sigma_f\\
\text{本构方程}\\
\vec D=\vec D(\vec E)
$$



均匀、各向同性、线性介质有**静电势微分方程** $$\nabla^2\varphi(\vec x)=-\displaystyle\frac{\rho_f}{\epsilon}$$（一个泊松方程）。从静电势函数考虑，边界条件成为


$$
\varphi_2=\varphi_1\\
\epsilon_2\frac{\partial \phi_2}{\partial n_{21}}-\epsilon_1\frac{\partial \phi_1}{\partial n_{12}}=-\sigma_f
$$



以上便是 PDE 的定解问题，学过数学物理方法，很自然知道求解套路：

- 1.2.29 电荷以 $$\cosθ$$ 的电荷密度分布于球面，则球内部为匀强电场。这个场景在[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E8%BD%B4%E5%AF%B9%E7%A7%B0%E7%90%83%E5%87%BD%E6%95%B0---%E5%8B%92%E8%AE%A9%E5%BE%B7%E5%87%BD%E6%95%B0)中会再次出现 -> 勒让德多项式。

 - 例：[均匀介质球](https://shi200005.github.io/download_file/PDE_Electric.pdf)。重要结论：**介质球内部的极化场是均匀的**。数学工具见[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E8%BD%B4%E5%AF%B9%E7%A7%B0%E7%90%83%E5%87%BD%E6%95%B0---%E5%8B%92%E8%AE%A9%E5%BE%B7%E5%87%BD%E6%95%B0)。

### 静电边值问题唯一性定理

边界条件可将静电场的空间分布唯一地确定下来。即给定边界条件后，不可能存在不同的静电场分布。19 - 20 秋 期中试题。静电学泊松方程唯一性定理可以看南大现工院李涛老师[课件](https://dsl.nju.edu.cn/litao/electrodynamics/Ch2-b.pdf)。

**电像法**/**镜像法**（Justified by 静电边值问题唯一性定理）

- 经常边界条件没有直接给定，让人头疼。但某些很幸运的情况下，空间电场等效于边界上的电荷被像电荷替代。要求像电荷出于所求解区域之外。
 - 例：无限大接地导体板对点电荷产生感应电荷的面电荷分布和空间电场分布。千题解 2.1.45 的答案错误，笨人已用论文严谨论述。
   - 该论文的一个推论：均匀带电球面：球内电场为 0，球外电场如同点电荷在球心（可直接用库仑定律求解）。
 - 例：在点电荷的电场中放置接地导体球，**就导体球外的静电场而论**，好像不存在导体球，而存在一个特定位置特定电量的点电荷。详见梁老师 10.1 (七) 母函数 例6。

### 静电场能量

$$\displaystyle W=\frac{1}{2}\int_{\infty}\vec E\cdot\vec DdV=\frac{1}{2}\int_{\infty}\varphi\rho_fdV-\frac{1}{2}\oint_{S}\varphi\vec D\cdot d\vec S$$ 对孤立体系后一项趋向于零。

- 真空中 $$\displaystyle W=\frac{1}{2}\int_V\rho Ud\tau+\frac{1}{2}\int_S\sigma UdS$$，从移动电荷静电力做功的功能转化角度，$$\displaystyle \frac{1}{2}$$ 来自静电力做功对称性。 

- 例：**平行板电容器**能量  $$\displaystyle W=\frac{1}{2}CU^2$$。

  例（徐游老师书P118）：保持平行板电容器电压，将平行板电容器插入液体电介质中，液面会在电容器中上升（原因：电容器边缘效应）。比较液体重力势能增加和电场能增量。

### 导体静电平衡

均匀导体**内部场强处处为零**、每个均匀导体都是**等势体**（定性分析 -> **尖端效应**）、电荷静止不动（宏观）、导体**外侧**电场强度**垂直**于导体表面。（满足 高斯定理 + 环路定理） 导体电平衡弛豫时间极短

于是，边界条件


$$
\mathbf{\hat{n}}\times\vec E=0\\
\mathbf{\hat{n}}\cdot\vec D=\sigma_f
$$


从静电势函数考虑，边界条件成为


$$
\varphi\vert_{\text{边界}}=\text{常数}\\
\epsilon_2\frac{\partial\varphi_2}{\partial n}=-\sigma_f
$$


 - 利用高斯定理导出导体表面电场与电荷分布。重要习题：千题解 [2.1.37] $$\displaystyle E=\frac{σ}{ε_0}$$，千题解 [2.1.38] 导体单位面积所受的力 $$\displaystyle\vec f=\frac{σ^2}{2ε_0}\mathbf{\hat{n}}$$。静电场所施加在导体上的压力始终是负压力，驱使导体被拉向电场存在的区域。

 - 例：**平行板电容器**

   可直接用库仑定律求解。均匀带电圆环/圆面等轴方向电场 -> 无限大均匀带电圆面产生匀强电场 $$\displaystyle E=\frac{\sigma}{2\epsilon_0}$$，其中 $$\sigma$$ 是带正电圆面的面电荷密度 -> 利用叠加原理，无限大**平行板电容器**板间电场 $$\displaystyle E=\frac{\sigma}{\epsilon_0}$$，其余电场是 0，只要够大，中间就可以看成匀强电场。

   confusion：为啥导体表面电场强度是 $$\displaystyle E=\frac{σ}{ε_0}$$，前文用库仑定律推无限大带电圆面在空间中电场强度 $$\displaystyle E=\frac{σ}{2ε_0}$$？请想，无限大带电圆面两侧电场强度都是 $$\displaystyle E=\frac{σ}{2ε_0}$$，但是导体电荷都在表面，外侧有垂直于表面的电场，内侧电场强度是 0。也就是说，可以把无限大带电导体圆面看成两侧表面面电荷密度都是 $$\displaystyle\frac{\sigma}{2}$$，就没问题了。

   徐游 P77  P.S. 当两个极板所带电量的绝对值不等时，公式中的 $$Q$$ 应为用导线将两极板相连时自正极板流向负极板的电荷。

 - 应用：[范德格拉夫起电机](https://en.wikipedia.org/wiki/Van_de_Graaff_generator#Description)。

### 格林函数

见[数学物理方程 - 格林函数](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E6%A0%BC%E6%9E%97%E5%87%BD%E6%95%B0%E6%B3%95-1)，例题见电动力学课件。

### 电多极矩

#### 电偶极子

推导中，所求点与两电荷距离远大于两电荷间距离，因此我们可以使用一些**泰勒展开**的近似处理库仑定律的分母项~ 结论：电偶极子产生的电势是 $$\displaystyle\Phi(\vec{r})=\frac{1}{4\pi\epsilon_0}\frac{\vec{p}·\vec{r}}{r^3}$$. 梯度是电场 $$\displaystyle\vec E=\frac{1}{4\pi\epsilon_0}(-\frac{\vec p}{r^3}+\frac{3(\vec p\cdot\vec r)\vec r}{r^5})$$.

极坐标求解：见课件 01-P147 附近。或数学物理方法教材。

研究一个小区域内分布的电荷体系，在空间很远处产生的电场。对电荷体系产生电场势函数在三维空间进行[高阶泰勒展开](https://shi200005.github.io/2021/09/30/Calculus/#%E5%B9%B6%E7%9F%A2%E4%B8%8E%E5%BC%A0%E9%87%8F)。零级——电荷集中于一点产生的电势 $$\displaystyle\propto\frac{1}{R}$$，一级——系统电偶极矩 $$\displaystyle\propto\frac{1}{R^2}$$、二级——系统电四极矩 $$\displaystyle\propto\frac{1}{R^3}$$、三级——系统电八极矩 $$\displaystyle\propto\frac{1}{R^4}$$......

> 电偶极矩考量的是体系是否具有镜面对称性破缺；电四极矩则考量体系是否有球对称破缺。——电动力学讲义

## 静磁场问题

特殊情况：对于稳恒电流所激发的稳恒电场，本质上是静电场，满足无旋性，因此同样可以引入电势进行描述。注：仅仅靠静电场是无法维持恒定电流的，必须有非静电力的存在。**稳恒电流场** $$\displaystyle\nabla\cdot\vec J(\vec x)=-\frac{\partial\rho}{\partial t}=0$$。注意到此时**没有位移电流**。对于均匀线性各向同性磁性介质，$$\nabla\times\vec B(\vec x)=\nabla\times(\mu\vec H)=\mu\vec J$$。




$$
\text{微分方程}\\
\nabla\times\vec E=0\\
\nabla\times\vec H=\vec J_f\\
\nabla\cdot\vec D=\rho_f\\
\nabla\cdot\vec B=0\\
\nabla\cdot\vec J=0\\
\vec J=\sigma\vec E\\
\text{边值关系}\\
\mathbf{\hat{n}}_{21}\times(\vec E_2-\vec E_1)=0\\
\mathbf{\hat{n}}_{21}\cdot(\vec J_2-\vec J_1)=0\\
\text{本构关系}\\
\vec D=\vec D(\vec E)\\
$$



从静电势函数考虑，$$\nabla\cdot\vec J=\sigma\nabla\cdot\vec E=-\sigma\nabla^2\varphi=0$$，满足拉普拉斯方程 $$\nabla^2\varphi=0$$。

一些杂七杂八结论

- 对于稳恒电路，有**基尔霍夫第一定律** $$\sum I_i=0$$。辅以环路定理，构成解决**电工学**（我学过，学得极烂）问题的物理基础。

- 推论：无限长载流导线磁场 $$B=\displaystyle\frac{\mu_0I}{2\pi r}$$。
- 推论：载流螺线管中的磁场 $$B=\mu_0nI$$  ->  两平行同向电流环（**Helmholtz 线圈**），半径与轴心距离相等时，轴线中心点磁场最均匀。在大学物理实验中应用。

### 磁矢势

回想[微积分 - 斯托克斯定理](https://shi200005.github.io/2021/09/30/Calculus/#%E9%AB%98%E6%96%AF%E5%85%AC%E5%BC%8F%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F%E6%96%AF%E6%89%98%E5%85%8B%E6%96%AF%E5%85%AC%E5%BC%8F) $$\displaystyle\oint_{l}\vec A\cdot d\vec l=\int_{S}(\nabla\times\vec A)\cdot d\vec S=\int_{S}\vec B\cdot d\vec S$$，不难猜到 $$\vec B=\nabla\times\vec A$$ 即为所求。但是，这样，$$\vec B$$ 对应的 $$\vec A$$ 不唯一，加上任何一个标量势的梯度仍满足 $$\vec B=\nabla\times(\vec A+\nabla\phi)$$（根据[矢量分析](https://shi200005.github.io/2021/09/30/Calculus/#%E9%AB%98%E6%96%AF%E5%85%AC%E5%BC%8F%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F%E6%96%AF%E6%89%98%E5%85%8B%E6%96%AF%E5%85%AC%E5%BC%8F)，任何标量场的梯度场都是无旋场）。

在静磁学中，我们一般取**库伦规范**势，满足 $$\nabla\cdot\vec A=0$$。P.S. 在随时间变化的磁场中，我们一般取**洛伦兹规范**势，见[电动力学](https://shi200005.github.io/2022/04/10/Electrodynamics/#%E8%A7%84%E8%8C%83%E5%8F%98%E6%8D%A2%E4%B8%8E%E8%A7%84%E8%8C%83%E4%B8%8D%E5%8F%98%E6%80%A7)。

这样的磁矢势怎么找？见电动力学课件 1.2。利用 $$\displaystyle\nabla\frac{1}{r}=-\frac{\vec r}{r^3}$$，难运算，我们最终得到符合条件的 $$\displaystyle\vec A(\vec x)=\frac{\mu}{4\pi}\int\frac{\vec J(\vec x')}{r}dV'$$  ->  $$\nabla\cdot\vec B(\vec x)=\nabla\cdot(\nabla\times\vec A)=0$$  **无源场**。在稳恒电流场条件下，难证明上述磁矢势满足

- Eq (1.2.31-1.2.41) $$\nabla\cdot\vec A=0$$. 欢呼！
- Eq (1.2.30-1.2.46)$$\nabla\times\vec B(\vec x)=-\nabla^2\vec A(\vec x)=\mu_0\vec J(\vec x)$$  ->  **安培环路定理**（电磁学里给的几何方法也很难，当然这里也很难）这个解的形式 $$\nabla^2 A_i(\vec x)=-\mu J_i(\vec x)$$ 于静电势泊松方程颇为相似。

例：均匀磁场的矢势、均匀带电球壳匀速绕轴转动的矢势。

边值关系：对于线性均匀磁介质，切向分量连续。库伦规范给出法向分量连续。

电磁势在量子力学中具有可观测的物理学效应（AB 效应和 AC 效应），见[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/)。

### 静磁场的唯一性定理

见课件。

### 静磁场能量

$$\displaystyle W_M=\frac{1}{2}\int_{\infty}\vec B\cdot\vec HdV=\frac{1}{2}\int_{\infty}\nabla\cdot(\vec A\times\vec H)dV+\frac{1}{2}\int_{V}\vec A\cdot\vec J_fd\vec V$$  只需考虑后一项对有电流分布区域的积分。

- 某电流分布在给定外磁场中的相互作用能......

### 磁标势解法

> 若所讨论的空间为单连通区域切区域内无传导电流，则磁场可用磁标势描述；若全空间无传导电流，则在全空间都可以定义磁标势。
>
> 优点：一是可以借用静电学中的一些处理问题的方法；二是在处理永久磁铁（无自由电流）、超导体（超导电流看成是磁化电流）所激发的磁场时，采用这种方法非常方便。——电动力学课件

此时 $$\nabla\times\vec H=0$$，可以引入 $$\vec H=-\nabla\varphi_m$$。

- 例：证明均匀磁化永磁介质球壳空腔内磁场为 0。

### 磁多级矩

和电多极矩一样，可以把磁矢势在三维空间做泰勒展开。注意，零级展开项总是 0，因为目前还没有磁单极子存在的证据。对于一级展开项，我们有 $$\displaystyle\vec A^{(1)}=\frac{\mu_0}{4\pi}\frac{\vec m\times\vec R}{R^3}$$, $$\varphi_m^{(1)}=\displaystyle\frac{\vec m\cdot\vec R}{4\pi R^3}$$。

### 小区域电流在外磁场

可对外磁场小区域进行多级展开......

#### 安培力

磁场对电流源施加的安培力：$$d\vec F=Id\vec l\times\vec B$$，广延形式 $$\vec F=\displaystyle\int_V\vec J(\vec x')\times\vec B_edV'$$。

- 推论：环线电流线在**均匀磁场**中所受力之和为 0（$$\vec F=I\displaystyle(\oint_{l}d\vec l)\times\vec B$$）；所受力矩为 $$\vec\tau=\vec m\times\vec B$$。
  - 若规定 $$\vec m$$ 与 $$\vec B$$ 相互垂直时**磁势能** $$U_m$$ 为 0 ，则 $$U_m=-\vec m·\vec B$$。
- 在不均匀磁场中，磁场总是将稳态平衡的 $$\vec m$$ 从磁场小处移向大处，同时力矩将磁矩转向与磁场平行方向。受力 $$F=-\nabla U_m$$。


---
layout: post
title: 复变函数 1.0
categories: BS-NJU-Course-Review-Physics
description: 对于数学物理方法的回顾
keywords: mathematical physics
mathjax: true
---

> Complex analysis studies **analytic functions**; this is a major restriction on the type of functions studied, leading to the fact that analytic functions have many amazing and useful properties.  -- Garrity, All the math you need to know...

| 学习时间                  | 大二下                                                                                 |
| 周课时                      | 4                                                                                          |
| 本人成绩                  | 91                                                                                        |
| 课程教材                  | 梁昆淼 《数学物理方法（第四版）》科学出版社 2010 |
| 个人建议参考教材   | 同上                                                                                     |
| 先修课程                  | 微积分                                                                                  |

## 复变函数

详见[复变函数 - 引言](https://shi200005.github.io/download_file/Complex_Functions_Intro.pdf)。

### 复数与复数的运算

> 在一个扩充的数域种的运算，其逻辑和哲学基础本质上是形式主义的；这扩充的数域必须通过定义来创造，这些定义是随意的。但是如果不能在更大的范围内保持在运来范围内同行的规则和性质，它是毫无用处的。这些扩充又是可以和“实际”对象相联系，通过这种方式为新的应用提供工具，这是最重要的，但是这只能提供一种动力而不是扩充的合理性的逻辑证明。——科朗、罗宾《数学是什么》

### 复变函数
$$z=x+iy, f(z)=u(x,y)+iv(x,y)$$

### 导数

柯西-黎曼方程（条件/ C-R 条件）$$\displaystyle\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}, \frac{\partial v}{\partial x}=-\frac{\partial u}{\partial y}$$。复变函数可导要求沿复数平面上任一曲线逼近的结果相同。如果考虑沿实轴和虚轴两种方式逼近的结果相同，则为 C-R 条件，即复变函数可导的必要条件。

复变函数可导的**充分必要条件**：函数的4个偏导数存在且连续，并且满足 C-R 条件（函数的实部和虚部通过 C-R 条件联系）。

### 解析函数、调和函数
在某点及其邻域上可导的函数 $$f(z)$$ 在该点解析，处处解析的函数是解析函数。解析函数是物理学家喜欢的好函数。

若函数 $$f(z)=u+iv$$ 在区域上解析，则 $$u$$ 和 $$v$$ 是两组正交曲线族，且均为区域上的**调和函数**（满足拉普拉斯方程 $$\nabla^2u=0,\nabla^2v=0$$，由 C-R 条件再求导得到）、虚实可互求。

- 补充：数学上可以证明，如果调和函数在区域内不恒为常数，则函数在区域内没有极值。例：如果试探电荷放入纯净电力电场，则不可能稳定平衡，否则将违背高斯定律。
- 调和函数举例：电势。 [复变函数 - 平面标量场](https://shi200005.github.io/download_file/Complex_Functions_Field.pdf)。电场线与等势线可互求。

### 多值函数
没用（至少目前）。

## 复变函数的积分

### 柯西定理
解析函数。对于单连通区域，对环路积分的实部和虚部分别使用[格林公式](https://shi200005.github.io/2021/09/30/Calculus/#%E9%AB%98%E6%96%AF%E5%85%AC%E5%BC%8F%E6%A0%BC%E6%9E%97%E5%85%AC%E5%BC%8F%E6%96%AF%E6%89%98%E5%85%8B%E6%96%AF%E5%85%AC%E5%BC%8F)，将 C-R 条件分别带入，得到柯西定理：环路积分为零。

$$\oint f(z)dz=\oint udx-vdy+i\oint vdx+udy \\ =-\iint(\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y})dxdy+i\iint(\frac{\partial u}{\partial x}-\frac{\partial v}{\partial y})dxdy=0$$

对于复连通区域，抠掉奇点，割成单连通区域，带孔区域积分为零。于是沿内外边界线逆时针方向（denote as "ac"）积分相等。

$$\displaystyle\oint_{l,ac}f(z)dz=\displaystyle\sum_{i=1}^n\oint_{l_i,ac}f(z)dz$$

### 柯西公式
通过不定积分结论：$$\displaystyle\frac{1}{2\pi i}\oint_l\frac{dz}{z-\alpha}=0$$ （$$l$$ 不包围 $$\alpha$$）；$$\displaystyle\frac{1}{2\pi i}\oint_l\frac{dz}{z-\alpha}=1$$ （$$l$$ 包围 $$\alpha$$）；$$\displaystyle\frac{1}{2\pi i}\oint_l(z-\alpha)^ndz=0$$ （$$n\neq-1$$）.

导出柯西公式：$$\displaystyle f(\alpha)=\frac{1}{2\pi i}\oint_l\frac{f(z)}{z-\alpha}dz$$.

柯西公式将解析函数在任何一内点的值用沿边界线的回路积分表示了出来。这是因为解析函数在各点的值通过 C-R 条件相互联系着。从物理上说，解析函数紧密联系于平面标量场，而平面场的边界条件决定着区域内部的场。也可以推广到 $$l$$ 的外部包含无限远点的区域。

柯西公式的三个推论“解析函数可求导任意多次（下一章：幂级数在收敛圆内可以逐项求导任意多次）。模数定理、刘维尔定理。

## 幂级数展开

### 收敛圆与收敛半径
感觉和微积分里数项级数一样。幂级数在收敛圆内绝对收敛、一致收敛，在圆外发散。幂级数的和在收敛圆的内部是解析函数，**在收敛圆内不可能出现奇点**。幂级数在收敛圆内可以逐项求导任意多次。逐项积分或逐项求导不改变收敛半径。

### 泰勒级数展开
既然解析函数的任意阶导数都存在，自然可以期望把解析函数展为复变项的[泰勒级数](https://shi200005.github.io/2021/09/30/Calculus/#%E5%BE%AE%E5%88%86%E5%AD%A6)。

### 解析延拓
实变函数原来定义在实数域，但是在复平面上画个圈圈，复数域的圈圈上的弧满足积分值为零的话就可以算了。用在之后“应用留数定理计算实变函数定积分”。

### 洛朗级数展开
当所研究的区域上**存在函数的奇点**时，就需要考虑在去除奇点的**环域**上的展开。求洛朗展开系数有个公式，但一般不用那个公式，而是通过**拆拆凑凑**的方法。请注意在哪个环域上展开！

例题也放[复变函数 - 平面标量场](https://shi200005.github.io/download_file/Complex_Functions_Field.pdf)里了。得到[数学物理方程 - m 阶贝塞尔函数](https://shi200005.github.io/download_file/Mat_Phy_Bessel.pdf)的洛朗展开（[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E8%B4%9D%E5%A1%9E%E5%B0%94%E5%87%BD%E6%95%B0)）。

概念：**可去奇点**、**极点**和**本性奇点**。对于可去奇点，例如 $$f(z)=\sin(z)/z$$ 在 $$z=0$$，若补充定义 $$f(z)=1$$，则 $$f(z)$$ 在整个平面上又是解析函数了。

## 留数定理

### 留数定理
如果被积复变函数在回路所围闭区域上是解析的，则回路积分等于零。如果回路包围奇点，在鼓励几点附近展为**洛朗级数，-1 次幂的系数叫做留数**。设复变函数在回路多为区域上除了有限个孤立奇点外解析，在闭区域上除孤立奇点外连续，则$$\displaystyle \oint_lf(z)dz=2\pi i \sum_{j=1}^n \text{Res} f(b_j)$$. 求留数时，展成洛朗级数得到 -1 次幂项，或者善用**洛必达法则**。

### 应用留数定理计算实变函数定积分
有用，在 [(En)Advanced Statistical Mechanics](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/) 就用了。一般来说就是把实变函数延拓成一个单位圆（三角函数有理式，积分上下限0到$$2\pi$$，欧拉公式换元），或者一个无限大的半圆加上实轴上的横线。适用条件是可以证明解析延拓的复数圆弧积分为 0，也就把实变函数定积分归结为区域内留数问题。详见[复变函数 - 应用留数定理计算实变函数定积分](https://shi200005.github.io/download_file/Complex_Functions_Integral.pdf)。

---

关于傅里叶变换和拉普拉斯变换在求解微分方程中的应用，参见[积分变换法 - 数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E7%A7%AF%E5%88%86%E5%8F%98%E6%8D%A2%E6%B3%95)。

## 傅里叶变换

为什么要进行傅里叶变换？我们都有很直观的印象：发出一个元音，做频谱图，可以通过频谱特征分辨是哪个元音（**语音识别**的原理之一）。**量子力学**中的坐标表象和动量表象，**固体物理**中的倒格矢都是傅里叶变换......返朴转载的这篇讲得不错，[为什么要进行傅里叶变换？Bill's Blog](http://ibillxia.github.io/blog/2013/04/04/why-do-Fourier-transformation/)

### 傅里叶级数
将周期函数展开为傅里叶级数。周期函数要满足迪里希利条件：(1) 处处连续，或在每个周期中只有有限个第一类间断点；(2) 在每个周期中只有有限个极值点。则傅里叶级数收敛，为...不过，一顿积分猛如虎之前先看看 $$f(x)$$ 是不是奇函数或者偶函数。对于周期函数 $$f(x+2l)=f(x)$$，

- 实数形式

  展开为 $$\displaystyle f(x)=a_0+\sum_{k=1}^\infty(a_k\cos\frac{k\pi x}{l}+b_k\sin\frac{k\pi x}{l})$$，其中 $$\displaystyle a_k=\frac{1}{\delta_kl}\int_{-l}^lf(\xi)\cos\frac{k\pi\xi}{l}d\xi$$，$$\displaystyle b_k=\frac{1}{l}\int_{-l}^lf(\xi)\sin\frac{k\pi\xi}{l}d\xi$$。其中$$\delta_k=2(k=0) \text{ or } 1(l\neq0)$$。

- 复数形式

  $$\displaystyle f(x)=\sum_{n=-\infty}^\infty C_ne^{inx/l}$$，其中 $$\displaystyle C_n=\frac{1}{2l}\int_{-l}^lf(x)e^{inx/l}$$。

傅里叶级数展开收敛于 $$\displaystyle\frac{f(x^+)+f(x^-)}{2}$$.

### 希尔伯特空间

上面我们可以看成满足迪里希利条件的函数$$f(x)$$ 在不同频率三角函数的基上展开。这些基相互正交且有无穷多维。如果 $$f(x)$$ 这样展开前后是等效的，且展开系数是唯一的，那么这些基构成的空间就是完备的，是希尔伯特空间。在[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/)中，不同边界条件下用不同基展开，这些基也构成希尔伯特空间。

完备性关系：对于一组完备的标准正交基，有$$\displaystyle\sum_n\vert\phi_n\rangle\langle\phi_n\vert=\boldsymbol{1}$$。概念可参见 Griffiths Quantum Mechanics 3.2.3。应用可参见**一维伊辛模型严格解**（详见以后会有的**高等统计物理**），还是**矩阵 SVD 分解**（详见[机器学习](https://shi200005.github.io/2022/12/05/Machine-Learning/)）。

### 傅里叶积分

对于**非周期**且满足迪里希利条件的函数$$f(x)$$，可以将其视作**周期为无穷大**的周期函数，且在 $$-\infty<x<\infty$$ **绝对可积**，傅里叶级数也就转化成为傅里叶积分（如果不能满足，请见**拉普拉斯变换**）。

- 实数形式

  $$\displaystyle f(x)=\int_0^\infty A(\omega)\cos(\omega x)d\omega+B(\omega)\sin(\omega x)d\omega$$ -> $$\displaystyle A(\omega)=\frac{1}{\pi}\int_{-\infty}^{\infty}f(\xi)\cos(\omega \xi) d\xi, B(\omega)=\displaystyle \frac{1}{\pi}\int_{-\infty}^{\infty}f(\xi)\sin(\omega \xi) d\xi$$.

  在此节给出一些例子，如**矩形函数**和**有限正弦波列**的傅里叶变换结果。

- 复数形式的傅里叶积分，详见[复变函数 - 复数形式的傅里叶积分](https://shi200005.github.io/download_file/Complex_Functions_Fourier.pdf)。

- 矩形函数 <-> sinc 函数在数字信号处理的应用 rect <-> sinc in digital signal processing

  Introduced in [(En) Information Theory](https://shi200005.github.io/2023/10/03/Information-Theory/). A continuous band-limited time-series (to $$W$$ Hz) can be **perfectly** reconstructed, if uniformly (in time) sampled with a minimum frequency of $$2W$$. Related theorem: [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem). A method is using sinc function, related theorem: [Whittaker–Shannon interpolation formula](https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula). Math was elaborate in this online handout: [10.4: Perfect Reconstruction](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Signals_and_Systems_(Baraniuk_et_al.)/10%3A_Sampling_and_Reconstruction/10.04%3A_Perfect_Reconstruction), check the former section for unclear equations :-).

### 基本性质

傅里叶变换的基本性质：导数定理、积分定理、相似性定理、延迟定理、位移定理、卷积定理（[傅里叶变换的性质及基本应用](https://zhuanlan.zhihu.com/p/78775455)）。用于**微分方程求解**（详见[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2%E6%B3%95)）。傅里叶变换和微分方程的求解联系何在？在于**导数定理**——对于给定初始值的偏微分方程或常微分方程，可以转化为常微分方程或者普通的方程。傅里叶变换的基本性质中应用最多的便是**导数定理**和**卷积定理**。

### $$δ$$ 函数

$$δ$$ 函数即狄拉克函数，用于研究物理学中的质点、点电荷等抽象模型。据我的记忆，该函数由物理学家发明，最初被数学家不齿。$$δ$$ 函数是一种广义函数，可以看成某些通常函数序列的极限，这些极限通常在积分意义下理解，文中给出 **3 种函数序列极限导出的 $$\delta$$ 函数**，通过这些函数序列进行傅里叶变换再求极限，可以得到 **$$δ$$ 函数的广义傅里叶变换**：常数$$\displaystyle\frac{1}{2\pi}$$.

> Functions that are localized in the time domain have Fourier transforms  that are spread out across the frequency domain and vice versa, a  phenomenon known as the [uncertainty principle](https://en.wikipedia.org/wiki/Fourier_transform#Uncertainty_principle). --[Wikipedia](https://en.wikipedia.org/wiki/Fourier_transform)

## 拉普拉斯变换

前文说到，傅里叶变换一个很重要的应用就是求解微分方程。然而，并不是所有函数都可以做傅里叶变换（狄里希利、绝对可积），比如正弦函数就不可以。那么对于 driven force 是正弦形式的非齐次微分方程怎么处理？乘以一个指数型收敛因子再进行傅里叶变换，就是**拉普拉斯变换** $$\bar f(p)=\mathscr L[f(t)]=\displaystyle\int_0^\infty f(t)e^{-pt}dt$$，其中当 $$t>0$$ 时，$$f(t)=0$$。

条件：(1) 在$$0≤t<\infty$$ 的任一有限区间上，除了有限个第一类间断点外，函数 $$f(t)$$ 及其导数是处处连续的，(2) 存在常数 $$M>0$$ 和 $$\sigma>0$$，使对于任何 $$t$$ 值 ($$0≤t<\infty$$)，有 $$\vert f(t)\vert<Me^{\sigma t}$$。

详见[复变函数 - 拉普拉斯变换及其应用](https://shi200005.github.io/download_file/Complex_Functions_Laplace.pdf)。和傅里叶变换一样，傅里叶变换和微分方程的求解联系也在于**导数定理**——傅里叶变换的基本性质中应用最多的便是**导数定理**和**卷积定理**。

常用于求解非齐次偏微分方程，详见[数学物理方程](https://shi200005.github.io/2022/02/16/Partial-Differential-Equations/#%E6%A0%BC%E6%9E%97%E5%87%BD%E6%95%B0%E6%B3%95)。

把微分方程做拉普拉斯变换求解后怎么变回去？没傅里叶变换那么容易，一般运用各种定理，然后查表，我一般就直接问 ChatGPT 了。

### 控制理论

研究 linear time invariant (LTI) 系统的性质，利用拉普拉斯变换在频域研究，扔掉初始条件，考虑拉普拉斯变换后，频域输出与输入之比记为 $$G$$，the transfer function。

卷积定理在控制理论中的重要性：反馈回路中，输出被喂给输入，在反馈回路中为卷积关系。

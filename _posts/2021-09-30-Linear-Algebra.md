---
layout: post
title: 线性代数 1.0
categories: BS-NJU-Course-Review-Mathematics
description: 对于微积分与线性代数的回顾
keywords: linear algebra
mathjax: true
---

如无特殊说明，本篇在实数域讨论。作为时间顺序上的第一篇，我在此规定整个网站的符号规范：标量用 $$a$$，矢量用 $$\vec a$$（并且是物理学家喜欢的列矢量），矩阵用 $$\mathbf a$$，二阶张量用 $$\overleftrightarrow{a}$$。和量子力学中的算符无关！但是，如果只是出现了 $$a$$，可能是广义上的张量，不一定是标量。区分的原因：笨人太笨，经常连谈论的是几阶张量都想不清楚。

| 学习时间                 | 线性代数(第一层次)：大一上                                                                |
| 周课时                     | 4                                                                                                              |
| 本人成绩                 | 78                                                                                                            |
| 课程教材                 | 张运清等 《线性代数讲义》科学出版社 2013                                    |
| 个人建议参考教材  | 任广千等 《线性代数的几何意义》西安电子科技大学出版社 2015 |
| 先修课程                 | 无                                                                                                            |

参考阅读：

1. 任广千等 《线性代数的几何意义》西安电子科技大学出版社 2015
2. Garrity, T. A. (2021). *All the Math You Missed: But Need to Know for Graduate School*. Cambridge University Press. Chapter 1.
3. Horn, Roger A.; Johnson, Charles R. (2013). *Matrix Analysis, second edition*. Cambridge University Press.

## 线性空间与线性变换

线性 $$f$$：$$f(ax_1+bx_2)=af(x_1)+bf(x_2)$$。可叠加的。

概念的数学定义请参见任意一本相关教科书。**线性空间**。以一定的标准（一组**基**）描述某个范围（**线性空间**）内的事物（**向量**）。基的数量：线性空间的维数 $$\dim(V)$$。

核 kernel  $$T:V\to W$$, $$\ker(T)=\{v\in V:T(v)=0\}$$

像 image  $$T$$, $$\text{Im}(T)=\{w\in W:\text{there exists a }v\in V\text{with }T(v)=0\}$$.

### 直和、直积

给定两个向量空间 $$V$$ 和 $$W$$ 定义在同一个域 $$F$$ 上，$$V \oplus W$$ 是一个新的向量空间，其中元素是形式为有序对 $$(v,w)$$ 的元素，其中 $$v \in V$$ 和 $$w \in W$$，$$V \oplus W$$ 满足向量空间的性质。直和要求 $$V∩W=\{0\}$$，直积无需。

- 对于有限维线性空间，如果 $$V$$ 和 $$W$$ 不重合，则直积和直和概念相同。例： $$\mathbb{R}^3 = \mathbb{R}^2 \oplus \mathbb{R}$$。
- 对于无限维线性空间，直和允许有限多分量非零，直积允许无限多分量非零。

### 矩阵 - 线性变换

**矩阵**代表**线性变换** $$T:V\rightarrow W$$ 在给定基下的描述（在教学中竟然完全没有被强调）。

- 《线性代数的几何意义》任广千等 5.5 矩阵与线性变换关系的几何意义。

矩阵的**秩**与线性变换中变换前后图形**维度**的关系（退化变换：pia~拍到低维）。

 - 《线性代数的几何意义》任广千等 6.3 线性方程组的秩及解的关系的几何意义。

特殊的矩阵——**非退化的方阵**：联系的两个线性空间维数相同，可以看成在同一个线性空间下做**基变换**（相应有**坐标变换**关系）。

## 求解线性方程组

利用**高斯消元法**求解线性方程组 $$\mathbf A\vec x=\vec b$$。高斯消元法求解线性方程组在后续徒手解矩阵特征值对应的**特征向量**时是必要的。示例：[线性代数 - 求解线性方程组](https://shi200005.github.io/download_file/Linear_Algebra_Solve_Eqs.pdf)。方法：通过初等行变换将 $$\mathbf A$$ 相关增广矩阵变成行简化梯形矩阵。设 $$\mathbf A$$ 有 $$m$$ 行 $$n$$ 列。

- 解唯一
  - $$\mathbf A$$ 是满秩方阵，$$\vec b$$ 在 $$\mathbf A$$ 的列空间内。如果 $$\vec b=\vec 0$$ 齐次，则一定是零解。

- 解无穷多 
  - $$m\ge n$$（不胖），$$\mathbf A$$ 非满秩，$$\vec b$$ 在 $$\mathbf A$$ 的列空间内。
  - $$m<n$$（胖）。
  - **数值方法**：带有变体的最小二乘法。

- 无解
  - $$\vec b$$ 不在 $$\mathbf A$$ 的列空间内。齐次方程组一定有零解，不属于此类。
  - **数值方法**：最小二乘法及其变体。数值方法部分见[计算物理](https://shi200005.github.io/2025/02/02/Computational-Physics/)。

## 行列式

行列式几何意义的定义（来自Garrity）

> Definition 1.5.4 The *determinant* of the matrix $$A$$ is the signed volume of the image of the unit cube.

应用：[微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%AD%A6)中多元积分换元的**雅可比矩阵** -> 雅可比矩阵及其**行列式**的几何意义（不同坐标系下积分值应保持一致）

 - 《线性代数的几何意义》任广千等 5.11 雅可比矩阵及其行列式的几何意义。
 - 《数学分析新讲II》张筑生 第十三章 5.a 注记。

行列式的计算

- [Adjugate matrix](https://en.wikipedia.org/wiki/Adjugate_matrix). 用于一种定义方阵行列式的方式。$$\det(A)=\displaystyle\sum_{k=1}^n(-1)^{k+1}a_{1k}\det(A_{1k})$$（来自Garrity），对于物理空间的描述（例如变换），绝大部分都是三维方阵，考场手算方法：

  ![](/images/blog/Linear_Algebra_3D_Determinant.jpg)

- 对于计算物理中的数据处理，矩阵一般比较大，但是不可能让你算矩阵的行列式，因为它们大部分是 sparse matrices。

- 行列式的计算在后续徒手解矩阵**特征值**时是必要的。

## 特征值和特征向量

$$\mathbf A\vec v=\lambda\vec v$$  对 $$\vec v$$ 这种向量做线性变换 $$\mathbf A$$ 后，向量的方向居然没变，长度变为原来的特征值 $$\lambda$$ 倍。

示例：[线性代数 - 求解特征值和特征向量](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)。你需要在[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/)考场上**徒手**完成以上操作。在**非线性动力学**（链接在以后会写的**系统生物学**）中，特征值实部的正负决定了**不动点的稳定性**。

> 几何意义：如果矩阵对某一个向量或某些向量只发生伸缩变换，不对这些向量产生旋转效果，那么这些向量就称为这个矩阵的特征向量，伸缩的比例就是特征值。特征向量在一个矩阵的作用下作伸缩运动，伸缩的幅度由特征值确定。
>

复数特征值及特征向量的几何意义，我在**系统生物学**的 fixed point analysis 会 revisit，看

- 《线性代数的几何意义》任广千等 5.8.5 矩阵相似的几何意义。

### 相似矩阵

> 如果有可逆方阵 $$\mathbf P$$，使得方阵 $$\mathbf A$$ 和方阵 $$\mathbf B$$ 满足 $$\mathbf A=\mathbf P\mathbf B\mathbf{P}^{-1}$$，那么矩阵 $$\mathbf A$$ 和 $$\mathbf B$$ 被称为相似矩阵。
>
> 多么简洁、深刻的定义啊。深刻得让俺看了 $$n$$ 遍都不明白怎么俩矩阵就相似了？哪里相似了。

重要意义：相似矩阵 $$\mathbf A$$ 和 $$\mathbf B$$ 是**同一个线性变换**（在同一线性空间中）在**两个不同基**下的表示矩阵。而可逆矩阵 $$\mathbf P$$ 就是**基变换矩阵**。

- 《线性代数的几何意义》任广千等 4.2.4 基变换的几何意义。

说白了就比如，在基 1 下，变换矩阵 $$\mathbf A$$ 把向量 $$\vec x$$ 变成了 $$\vec x^\prime$$，也就是 $$\mathbf A\vec x=\vec x^\prime$$；在基 2 下，变换矩阵 $$\mathbf B$$ 把向量 $$\vec y$$ 变成了向量 $$\vec y^\prime$$，也就是 $$\mathbf B\vec y=\vec y^\prime$$。这两组基之间的变换关系是 $$\mathbf P\vec y=\vec x$$ 以及 $$\mathbf P\vec y^\prime=\vec x^\prime$$（向量在不同基之下都是用 $$\mathbf P$$ 变换，也就是 $$\mathbf A$$ 和 $$\mathbf B$$ 是同一个线性变换）。那么很显然，$$\mathbf B=\mathbf P^{-1}\mathbf A\mathbf P$$，相似！

这里 $$\vec x$$ 和 $$\vec y$$ 是不同坐标系下的同一个向量的坐标，基向量不同，坐标就不同。若该向量在基 1 下的坐标是 $$\vec x$$，在基 2 下的坐标就是 $$\vec y=\mathbf{P}^{-1}\vec{x}$$，反之 $$\mathbf{P}\vec y=\vec{x}$$。

![Linear_Algebra_Similar](\images\blog\Linear_Algebra_Similar.jpg)

[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/#%E5%BD%A2%E5%BC%8F%E7%90%86%E8%AE%BA)中对于力学量矩阵的**表象变换**就是这么个变换。

相似变换的理想目标：找到与 $$\mathbf A$$ 相似的**对角化**矩阵，实质是寻找一个适当的坐标系，使得该变换对这个新的坐标系上的单位向量（或基向量）只做伸缩变换，不做旋转变换。一般什么样的矩阵一定能对角化？见“实对称矩阵”。
 - 《线性代数的几何意义》任广千等 5.9 矩阵相似的几何意义。

### 相似对角化

$$n×n$$ 方阵可对角化的充要条件是有 $$n$$ 个线性无关的特征向量（满秩）。

如果需要在考场上徒手对角化矩阵，步骤和下面[线性代数 - 实对称矩阵对角化](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)是一样的，只不过基变换矩阵不一定是正交化矩阵罢了。

### 矩阵的迹

迹是特征值的和，行列式是特征值的积。因为相似变换是同一个变换在不同基下的表示，所以这个变换对于任何基下特征向量的变化都是一样的，所以相似变换不改变特征值，也就不改变迹和行列式。

### 约尔当标准型

不幸的是，有时候我们想变换的这个方阵还真不是满秩。为了方便地处理下文 Matrix Exponential 的问题，再不济也要化成[约尔当标准型](https://en.wikipedia.org/wiki/Jordan_normal_form)！怎么化呢？这个页面的 [Example](https://en.wikipedia.org/wiki/Jordan_normal_form#Example) 已经解释得跟清楚了。

#### Matrix Exponential

【GRAD-UPDATE】为啥要对角化？因为对角化后的矩阵可能很方便我们处理。闲话不多说，相似对角化的一个优秀品格就是 $$\mathbf A^n=\mathbf P\mathbf\Lambda^n\mathbf P^{-1}$$。这玩意学的时候不觉得有什么意思，性质穿脑过，佛祖心中留。直到需要解矩阵形式的微分方程组时，才知道这玩意在 [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential) 里是多么重要啊！参见 [Diagonalizable case](https://en.wikipedia.org/wiki/Matrix_exponential#Computing_the_matrix_exponential)。

遇到 $$\displaystyle\frac{\partial}{\partial t}\vec X=\mathbf A\vec X$$ 的问题，解的形式是 $$\vec X=e^{\mathbf At}\vec X_0$$. 哈哈，注意不是 $$\vec X=\vec X_0e^{\mathbf At}$$，因为矩阵相乘不 guarantee 交换律。对于满秩或非满秩的 $$\mathbf A$$，用相似变换变成约尔当标准型（要是对角就太好了），然后就可以参考 [Differential Equations - Systems of Equations](https://math24.net/method-matrix-exponential.html) 求解了。不知道谁写的，写得还挺好。

## 二次型

$$
f(\vec x)=ax_1^2+bx_2^2+2cx_1x_2\\

=
\begin{bmatrix}
	x_1 & x_2 \\
\end{bmatrix}

\begin{bmatrix}
	a & c \\
    c & b \\
\end{bmatrix}

\begin{bmatrix}
	x_1 \\ x_2 \\
\end{bmatrix}
\\
=\vec x^T\mathbf A\vec x
$$



定义了**内积**的线性空间叫**欧氏空间**，于是欧几里得可以度量几何对象。在教学中，**内积空间**相关部分被省去，我认为极不合理。我们要理解度量矩阵的作用是协调内积在不同基下算出的内积不同。

二次型可以看作是内积的推广。如果对二次型进行的是**合同变换**，$$\vec x=\mathbf P\vec y$$, $$f(\vec x)=\vec x^T\mathbf A\vec x=\vec y^T(\mathbf P^T\mathbf A\mathbf P)\vec y$$，目的便是在于使二次型的函数值保持不变！我们还发现了好东西：**实对称矩阵** $$\mathbf A$$。

重要概念：正定、半正定、惯性指数等。及其几何意义。

【GRAD-UPDATE】 $$\mathbf A^T\mathbf A$$ 是半正定矩阵，因为 $$\vec x^T(\mathbf A^T\mathbf A)\vec x=(\mathbf A\vec x)^T(\mathbf A\vec x)$$，应用：**最小二乘回归**是**凸优化**问题。或许[机器学习](https://shi200005.github.io/2022/12/05/Machine-Learning/)里写一下？

此部分内容详见
 - 《线性代数的几何意义》任广千等 7 二次型的几何意义

## 正交变换

正交变换：$$\mathbf P^T=\mathbf P^{-1}$$, $$\mathbf P^T\mathbf P=I$$.

$$\vec x^T\mathbf A\vec x=\vec y^T\mathbf P^T\mathbf A\mathbf P\vec y=\vec y^T\mathbf P^{-1}\mathbf A\mathbf P\vec y=\vec y^T\mathbf B\vec y$$, where $$\mathbf B=\mathbf P^{-1}\mathbf A\mathbf P$$. 咱这里 $$\mathbf P$$ 还是代表**基变换矩阵**。

既是相似变换，又是合同变换，便是**正交变换**。结合两个变换的几何意义可知，正交变换是一种**刚性变换**（不改变物体的尺寸和正交关系，e.g., 平移、旋转、镜像）。在理论力学、固体物理等课程中有涉及。

 - 《线性代数的几何意义》任广千等 5.13 矩阵的等价、相似与合同关系。
 - 应用：[固体物理](https://shi200005.github.io/2023/03/15/Solid-State-Physics/)晶体宏观对称性。

### 实对称矩阵

如果矩阵 $$\mathbf A $$ 是**实对称矩阵**，则其一定能**正交对角化**：$$\mathbf P^T\mathbf A\mathbf P=\mathbf\Lambda$$，对角矩阵对角元为 $$\mathbf A$$ 的特征值（能正交对角化是极端美好的品质，**不管是不是满秩的**）。示例：[线性代数 - 实对称矩阵对角化](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)。几何直观：想象 $$\displaystyle g(\vec x')=\frac{1}{4}x_1'^2-\frac{5}{4}x_2'^2+\frac{\sqrt{3}}{2}x_1'x_2'=\vec x'^T\mathbf A\vec x'$$，是一个定义在 $$xOy$$ 平面上的函数，其函数值可以用 $$xOy$$ 之上的**马鞍**表示（二次型 -> 马鞍面）。你总能移动一下这张坐标纸，让轴落在对称的位置，得到 $$f(\vec x)=x_1^2-2x_2^2=\vec x^T\Lambda\vec x$$。这里基变换矩阵是顺时针旋转 60° 的刚性变换矩阵！同时也请注意到特征值和矩阵的迹的关系！

实对称矩阵典型例子

- 惯量张量（[力学](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E5%88%9A%E4%BD%93%E7%9A%84%E5%AE%9A%E7%82%B9%E8%BF%90%E5%8A%A8)）。
- [证明：协方差矩阵是半正定矩阵](https://blog.csdn.net/qcyfred/article/details/71598815)（[概率论](https://shi200005.github.io/2022/02/17/Probability/#%E5%8D%8F%E6%96%B9%E5%B7%AE)，直观地想象，将高维变量空间做刚性变换，使互相垂直（独立）的新变量方差主元都落在变换后的坐标轴上，协方差为 0，新变量各个维度的方差就是矩阵的特征值们，都是非负的）。

在后续的[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/#%E5%8E%84%E7%B1%B3%E5%8F%98%E6%8D%A2%E5%92%8C%E5%8E%84%E7%B1%B3%E5%85%B1%E8%BD%AD)中，引入了**厄米矩阵**，其实**实对称矩阵**就是厄米矩阵元素都是实数的特殊形式。而正交矩阵就是**酉矩阵**元素都是实数的特殊形式。

## 矩阵求导

【GRAD-UPDATE】链接[微积分](https://shi200005.github.io/2021/09/30/Calculus/)。

系统性总结参见 [矩阵求导术（上）](https://zhuanlan.zhihu.com/p/24709748)& [矩阵求导术（下）](https://zhuanlan.zhihu.com/p/24709748)——知乎用户[长躯鬼侠](https://www.zhihu.com/people/chang-qu-gui-xia)的文章。写得挺循循善诱的，也有和机器学习（[(En) Machine Learning](https://shi200005.github.io/2022/12/05/Machine-Learning/)）中相关运算的结合。

其中行列式的微分详见[行列式微分形式的推导](https://zhuanlan.zhihu.com/p/144255438)——知乎用户 [genekiller](https://www.zhihu.com/people/jiahao-lee-73) 的文章，结论为：可逆情形下的行列式微分形式：$$d\vert\mathbf A\vert=\vert\mathbf A\vert tr(\mathbf{A^{-1}}d\mathbf A)$$。Jacobi's formula

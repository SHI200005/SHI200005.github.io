---
layout: post
title: 线性代数 1.0
categories: BS-NJU-Course-Review-Physics
description: 对于微积分与线性代数的回顾
keywords: linear algebra
mathjax: true
---

**矩阵是线性变换。**

更新记录 2021.09.30,Ver 0.1 2021.09.30,Ver 0.11 2023.01.01,Ver0.12 2023.01.07,Ver1.0 2023.09.18,Ver1.1 相似对角化 约尔当标准型 Matrix exponential  2023.12.24,Ver2.0 

| 学习时间                 | 线性代数(第一层次)：大一上                                                                |
| 周课时                     | 4                                                                                                              |
| 本人成绩                 | 78                                                                                                            |
| 课程教材                 | 张运清等 《线性代数讲义》科学出版社 2013                                    |
| 个人建议参考教材  | 任广千等 《线性代数的几何意义》西安电子科技大学出版社 2015 |
| 先修课程                 | 无                                                                                                            |

很多数理理解像我一样差的同学学完（虽然成绩可能比我高不少），仍不知道自己学了什么。

参考阅读：

1. 任广千等 《线性代数的几何意义》西安电子科技大学出版社 2015
2. Garrity, T. A. (2021). *All the Math You Missed: But Need to Know for Graduate School*. Cambridge University Press. Chapter 1.
3. Horn, Roger A.; Johnson, Charles R. (2013). *Matrix Analysis, second edition*. Cambridge University Press.

## 线性空间与线性变换

线性 $f$：$f(ax_1+bx_2)=af(x_1)+bf(x_2)$。可叠加的。

概念的数学定义请参见任意一本相关教科书。

以一定的标准（一组**基**）描述（**向量**）某个范围（**线性空间**）内的事物。

基的数量：线性空间的维数（$$\dim(V)$$）。核（kernel）、像（image，见行列式定义）。

## 矩阵 - 线性变换

**矩阵**代表**线性变换**（$$T:V\rightarrow W$$）在给定基下的描述。（在教学中竟然完全没有被强调）

- 《线性代数的几何意义》任广千等 5.5 矩阵与线性变换关系的几何意义

矩阵的**秩**与线性变换中变换前后图形**维度**的关系。

 - 《线性代数的几何意义》任广千等 6.3 线性方程组的秩及解的关系的几何意义

特殊的矩阵——**非退化的方阵**：联系的两个线性空间维数相同，可以看成在同一个线性空间下做**基变换**（相应有**坐标变换**关系）。

### 应用

应用：[固体物理](https://shi200005.github.io/2023/03/15/Solid-State-Physics/)晶体宏观对称性

应用：[微积分](https://shi200005.github.io/2021/09/30/Calculus/#%E5%A4%9A%E5%85%83%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%AD%A6)中多元积分换元的雅可比矩阵 -> 雅可比矩阵及其行列式的几何意义

 - 《线性代数的几何意义》任广千等 5.11 雅可比矩阵及其行列式的几何意义
 - 《数学分析新讲II》张筑生 第十三章 5.a 注记

应用：利用**高斯消元法**求解线性方程组 $$\hat A\vec x=\vec b$$

- 技能：行简化梯形矩阵、齐次以及非齐次方程组解的结构。示例：[线性代数-求解线性方程组](https://shi200005.github.io/download_file/Linear_Algebra_Solve_Eqs.pdf)。高斯消元法求解线性方程组在后续徒手解矩阵特征值对应的**特征向量**时是必要的。
- 知识链接：计算物理导论-最小二乘法，参见《线性代数的几何意义》任广千等 6.7 超定方程组的最小二乘解的几何意义

## 行列式

行列式几何意义的定义（来自Garrity）

> Definition 1.5.4 The *determinant* of the matrix $$A$$ is the signed volume of the image of the unit cube.

作为考察重点但实际上没用的：诡异行列式的计算。评价：行列式只要记住基本计算方法即可，任何复杂计算在以后的课程中不会用到，却占到期中考试巨大分值，实属不解。

就我目前遇到的情况而言，对于物理空间的描述（例如变换），绝大部分都是三维方阵，对于计算物理中的数据处理，矩阵一般比较大，但是不可能让你算矩阵的行列式，因为它们大部分是 sparse matrices。对于三维方阵对应的三阶行列式的计算，在不使用计算软件的情况下，下面的方法最高效（实际中会用到！）

![](/images/blog/Linear_Algebra_3D_Determinant.jpg)

行列式的计算在后续徒手解矩阵**特征值**时是必要的。

### 伴随矩阵

[Adjugate matrix](https://en.wikipedia.org/wiki/Adjugate_matrix). 用于一种定义方阵行列式的方式。$$\det(A)=\displaystyle\sum_{k=1}^n(-1)^{k+1}a_{1k}\det(A_{1k})$$（来自Garrity）。

## 特征值和特征向量

示例：[线性代数-求解特征值和特征向量](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)。你需要在[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/)考场上**徒手**完成以上操作。在**非线性动力学**（链接在以后会写的**系统生物学**）中，特征值实部的正负决定了**不动点的稳定性**。

> 几何意义：如果矩阵对某一个向量或某些向量只发生伸缩变换，不对这些向量产生旋转效果，那么这些向量就称为这个矩阵的特征向量，伸缩的比例就是特征值。特征向量在一个矩阵的作用下作伸缩运动，伸缩的幅度由特征值确定。
>

复数特征值及特征向量的几何意义，我在**系统生物学**的 fixed point analysis 会 revisit，看

- 《线性代数的几何意义》任广千等 5.8.5 矩阵相似的几何意义

### 矩阵的迹

迹是特征值的和，行列式是特征值的积。[Geometric interpretation of trace](https://mathoverflow.net/questions/13526/geometric-interpretation-of-trace) 先放着，以后revisit。

### 相似矩阵

> 如果有可逆方针 $$\mathbf P$$，使得方阵 $$\mathbf A$$ 和方阵 $$\mathbf B$$ 满足 $$\mathbf A=\mathbf{PBP^{-1}}$$，那么矩阵 $$\mathbf A$$ 和 $$\mathbf B$$ 被称为相似矩阵。
>
> 多么简洁、深刻的定义啊。深刻得让俺看了 $$n$$ 遍都不明白怎么俩矩阵就相似了？哪里相似了。

重要意义：相似矩阵 $$\mathbf A$$ 和 $$\mathbf B$$ 是**同一个线性变换**（在同一线性空间中）在**两个不同基**下的表示矩阵。而可逆矩阵 $$\mathbf P$$ 就是**基变换矩阵**。

说白了就比如，在基 1 下，变换矩阵 $$\mathbf A$$ 把向量 $$\mathbf x$$ 变成了矩阵 $$\mathbf x^\prime$$，也就是 $$\mathbf{Ax}=\mathbf x^\prime$$；在基 2 下，变换矩阵 $$\mathbf B$$ 把向量 $$\mathbf y$$ 变成了向量 $$\mathbf y^\prime$$，也就是 $$\mathbf{By}=\mathbf y^\prime$$。这两组基之间的变换关系是 $$\mathbf{Py}=\mathbf{x}$$ 以及 $$\mathbf{Py^\prime}=\mathbf{x^\prime}$$（向量在不同基之下都是用 $$\mathbf P$$ 变换，也就是 $$\mathbf A$$ 和 $$\mathbf B$$ 是同一个线性变换）。那么很显然，$$\mathbf{B}=\mathbf{P^{-1}AP}$$，相似！！！

这里 $$\mathbf x$$ 和 $$\mathbf y$$ 是不同坐标系下的同一个向量的坐标，基向量不同，坐标就不同。若该向量在基 1 下的坐标是 $$\mathbf x$$，在基 2 下的坐标就是 $$\mathbf y=\mathbf{P}^{-1}\mathbf{x}$$，反之 $$\mathbf{Py}=\mathbf{x}$$。

![Linear_Algebra_Similar](\images\blog\Linear_Algebra_Similar.jpg)

[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/#%E5%BD%A2%E5%BC%8F%E7%90%86%E8%AE%BA)中对于力学量矩阵的**表象变换**就是这么个变换。

相似变换的理想目标：找到与A相似的**对角化**矩阵，实质是寻找一个适当的坐标系，使得该变换对这个新的坐标系上的单位向量（或基向量）只做伸缩变换，不做旋转变换。一般什么样的矩阵一定能对角化？见“实对称矩阵”。
 - 《线性代数的几何意义》任广千等 5.9 矩阵相似的几何意义

### 相似对角化

n×n 方阵可对角化的充要条件是有 n 个线性无关的特征向量（满秩）。

如果需要在考场上徒手对角化矩阵，步骤和下面[线性代数-实对称矩阵对角化](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)是一样的，只不过基变换矩阵不一定是正交化矩阵罢了。

### 约尔当标准型

不幸的是，有时候我们想变换的这个方阵还真不是满秩。为了方便地处理下文 Matrix Exponential 的问题，再不济也要化成[约尔当标准型](https://en.wikipedia.org/wiki/Jordan_normal_form)！怎么化呢？这个页面的 [Example](https://en.wikipedia.org/wiki/Jordan_normal_form#Example) 已经解释得跟清楚了。

#### Matrix Exponential

【GRAD-UPDATE】为啥要对角化？因为对角化后的矩阵可能很方便我们处理。闲话不多说，相似对角化的一个优秀品格就是 $$\mathbf A^n=\mathbf{P\Lambda}^n\mathbf{P^{-1}}$$。这玩意学的时候不觉得有什么意思，性质穿脑过，佛祖心中留。直到需要解矩阵形式的微分方程组时，才知道这玩意在 [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential) 里是多么重要啊！参见 [Diagonalizable case](https://en.wikipedia.org/wiki/Matrix_exponential#Computing_the_matrix_exponential)。

遇到 $$\frac{\partial}{\partial t}\mathbf X=\mathbf{AX}$$ 的问题，解的形式是 $$\mathbf X=e^{\mathbf At}\mathbf X_0$$. 哈哈，注意不是 $$\mathbf X=\mathbf X_0e^{\mathbf At}$$，因为矩阵相乘不 guarantee 交换律。对于满秩或非满秩的 $$\mathbf A$$，用相似变换变成约尔当标准型（要是对角就太好了），然后就可以参考 [Differential Equations - Systems of Equations](https://math24.net/method-matrix-exponential.html) 求解了。不知道谁写的，写得还挺好。

## 二次型

相关概念：合同变换与合同矩阵。在教学中，内积空间相关部分被省去，我认为极不合理。我们要理解度量矩阵的作用是协调内积在不同基下算出的内积不同。对二次型进行的是**合同变换**（$$x=Cy, f(x)=x^TAx=y^T(C^TAC)y$$），目的便是在于使二次型的函数值保持不变！

重要概念：正定、半正定、惯性指数等。及其几何意义。

【GRAD-UPDATE】 $$A^TA$$ 是半正定矩阵，因为 $$x^T(A^TA)x=(Ax)^T(Ax)$$，应用：**最小二乘回归**是**凸优化**问题。或许[机器学习](https://shi200005.github.io/2022/12/05/Machine-Learning/)里写一下？

此部分内容详见
 - 《线性代数的几何意义》任广千等 7 二次型的几何意义

## 正交变换

既是相似变换，又是合同变换，便是正交变换。结合两个变换的几何意义可知，正交变换是一种**刚性变换**。在理论力学、固体物理等课程中有涉及。
 - 《线性代数的几何意义》任广千等 5.13 矩阵的等价、相似与合同关系

### 实对称矩阵

正交矩阵：$$P^TP=E$$。如果矩阵$$ A $$是**实对称矩阵**，则其一定能**合同对角化**：$$P^TAP=\Lambda$$（**!!ACHTUNG!!**能合同对角化是极端美好的品质，**不管是不是满秩的**）。示例：[线性代数-实对称矩阵对角化](https://shi200005.github.io/download_file/Linear_Algebra_Diagonal.pdf)。在后续的[量子力学](https://shi200005.github.io/2022/08/20/Quantum-Mechanics/)中，引入了**厄米矩阵**，其实**实对称矩阵**就是厄米矩阵元素都是实数的特殊形式。而正交矩阵就是**酉矩阵**元素都是实数的特殊形式。

实对称矩阵典型例子：惯量张量（[力学](https://shi200005.github.io/2022/02/23/Classical-Mechanics/#%E5%88%9A%E4%BD%93%E7%9A%84%E5%AE%9A%E7%82%B9%E8%BF%90%E5%8A%A8)）、[证明：协方差矩阵是半正定矩阵](https://blog.csdn.net/qcyfred/article/details/71598815)（[概率论](https://shi200005.github.io/2022/02/17/Probability/#%E5%8D%8F%E6%96%B9%E5%B7%AE)，直观地想象，将高维变量空间做刚性变换，使互相垂直（独立）的新变量方差主元都落在变换后的坐标轴上，协方差为 0，新变量各个维度的方差就是矩阵的特征值们，都是非负的）。

## 矩阵求导

【GRAD-UPDATE】链接[微积分](https://shi200005.github.io/2021/09/30/Calculus/)。

系统性总结参见 [矩阵求导术（上）](https://zhuanlan.zhihu.com/p/24709748)& [矩阵求导术（下）](https://zhuanlan.zhihu.com/p/24709748)——知乎用户[长躯鬼侠](https://www.zhihu.com/people/chang-qu-gui-xia)的文章。写得挺循循善诱的，也有和机器学习（[(En) Machine Learning](https://shi200005.github.io/2022/12/05/Machine-Learning/)）中相关运算的结合。

其中行列式的微分详见[行列式微分形式的推导](https://zhuanlan.zhihu.com/p/144255438)——知乎用户 [genekiller](https://www.zhihu.com/people/jiahao-lee-73) 的文章，结论为：可逆情形下的行列式微分形式：$$d\vert A\vert=\vert A\vert tr(A^{-1}dA)$$。


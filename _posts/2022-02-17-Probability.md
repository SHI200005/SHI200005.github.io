---
layout: post
title: 概率论 1.0
categories: BS-NJU-Course-Review-Mathematics
description: 概率论
keywords: probability
mathjax: true
---

用概率描述的目的来源于对事实的不确定性。理论上，可以根据我们对（并不完全的认识的）事实给出一件事发生的（可能并不准确的）概率，用于**权衡利弊**。这个概率的真实性需要通过这个事件实际发生的频率核实。当我们关于事实的知识改变时，可能这个理论上的概率值也将改变。在 [(En) Machine Learning](https://shi200005.github.io/2022/12/05/Machine-Learning/) 和之后的 [(En) Information Theory](https://shi200005.github.io/2023/10/03/Information-Theory/) 中，将会有更深的体会。

事实上，这门课可能是最为重要的一门课（尤其是日后转到其他定量科学领域）。作为9-11节的晚间专业选修课，这门课也是一门绝对的水课。如果我早点意识到这门课对我的重要性和修读课程的水性，早点开始自学，就不会走这么多弯路了。[TED演讲：先教统计学再教微积分!](https://www.bilibili.com/video/BV1W7411E7JF?p=2)

符号说明：$$X$$ —— 随机变量，$$x$$ —— 随机变量的取值；常把 $$X=x$$ 简写为 $$x$$。$$X_i$$ —— 随机变量的一个样本，$$x_i$$ —— 该样本取值。

| 学习时间                                   | 大二上                                   |
| 周学时                                       | 3                                             |
| 本人成绩                                   | 94                                           |
| 课程教材                                   | 名存实亡 已绝版...                |
| 个人建议参考教材                   | 本人这篇                                |
| 先修课程                                   | 微积分  线性代数  复变函数 |

## External References

1. Kardar, Mehran. *Statistical physics of particles*. Cambridge University Press, 2007.
3. Leonard Mlodinow. *The Drunkard's Walk*: How Randomness Rules Our Lives. Vintage Books, 2008.

## 概率论的基本概念

### 等可能概型（古典概型）

### 条件概率

$$\displaystyle P(A\vert B)=\frac{P(A,B)}{P(B)}$$, $$P(\text{老板不回你邮件}\vert\text{你被老板开除})$$ 接近于 $$1$$， $$P(\text{你被老板开除}\vert\text{老板不回你邮件})$$ 并不大。

### 全概率公式与Bayes 公式

1. $$\displaystyle P(B_i|A)=\frac{P(A|B_i)P(B_i)}{P(A)}=\frac{P(A|B_i)P(B_i)}{\displaystyle\sum_{j=1}^{n}P(A|B_j)P(B_j)}$$ 

      后验概率 $$P(B_i\vert A)$$ = (  似然性 $$P(A\vert B_i)$$ *  先验概率 $$P(B_i)$$) / 标准化常量 $$P(A)$$

2. 可用于求解**后验概率**（在得到信息之后再重新加以修正的概率），利用**条件概率**公式联系**后验概率**和**先验概率**

      【Intuition】先验概率：感染者的检测结果是阳性的概率（试剂盒靠谱不靠谱）；后验概率：测试结果为阳性的人是感染者的概率（看到自己阳了要不要信）。试剂盒还算靠谱，到底要不要信？请看 Ref 3 第六章的例子——[概率论 - 贝叶斯公式](https://shi200005.github.io/download_file/Probability_Bayes.pdf)。

      【刑事案件】**迈克·林奇**是为数不多的认真研究过英国数学家**托马斯.贝叶斯**在1750年左右创立的概率理论的人之一。这一研究是极为耗费精力的，但林奇在研究数学之余，还学会了经商和出去推销他的构想，这在英国的学术界还是件颇为不易的事。美东时间2024年8月19日，据媒体报道，迈克·林奇乘坐的英国豪华风帆游艇**“贝叶斯”号（Bayesian）**在意大利西西里岛外海沉没，林奇失踪；22日，据报道，林奇的遗体已被寻获，被发现卡在船舱内的床垫中； 24日，意大利检方表示沉船事件初步调查方向是有人涉嫌过失沉船罪和多项过失杀人罪。——[百度百科](https://baike.baidu.com/item/%E8%BF%88%E5%85%8B%C2%B7%E6%9E%97%E5%A5%87/1069455)

### 独立事件

若 $$A, B$$ 互为独立事件，则 $$P(A,B)=P(A)P(B)$$, $$P(A\vert B)=P(A)$$. 

## 随机变量及其分布

关于更多随机变量分布[概率分布](https://www.yuque.com/angsweet/machine-learning/shu-xue-ji-chu_shu-xue-ji-chu_gai-lv-tong-ji_gai-lv-fen-bu)。[一张图说明二项分布、泊松分布、指数分布、几何分布、负二项分布、伽玛分布的联系](https://zhuanlan.zhihu.com/p/32932782)。

### 离散型随机变量

#### 二项分布 

$$X\sim b(n,p)$$  $$n$$ 重伯努利试验 -> 二项分布 后面的泊松分布和几何分布都是描述伯努利实验的

[定量理解二项式分布的泊松和高斯近似](https://zhuanlan.zhihu.com/p/27604254)。二项分布表达式里的阶乘使计算很恼人，还好在一些情况下可以**近似**成更容易计算的分布（具体数学详见泊松分布和正态分布）：

- 近似为**泊松分布**：$$n$$ 很大而 $$p$$ 很小 -> $$X\sim b(n,p)$$-> $$X\sim π(λ)$$, $$λ=np$$。
- 近似为**正态分布**：$$n$$ 很大，$$p$$ 接近 $$1/2$$ -> $$X\sim b(n,p)$$ ->  $$X\sim N(μ,σ^2)$$。

#### 泊松分布 

$$X\sim π(λ)$$

泊松分布作为泊松过程的“某时段内发生事件数”的分布。泊松过程**无记忆性**，事件发生的等待时间间隔服从**指数分布**，参见[泊松分布与指数分布的联系](https://zhuanlan.zhihu.com/p/261961315)。从泊松过程推出泊松分布：[泊松分布与泊松过程](https://zhuanlan.zhihu.com/p/431389631)。

泊松分布作为**二项分布**的近似：$$n$$ 很大而 $$p$$ 很小 -> $$X\sim b(n,p)$$-> $$X\sim π(λ)$$, $$λ=np$$。证明详见[概率论 - 泊松分布作为二项分布的近似](https://shi200005.github.io/download_file/Probability_Binomial_Poisson.pdf)。【Intuition】用泊松过程推导泊松分布的时候，就是从一件事发生还是不发生出发，取时间间隔的极限小，也就是考虑极限情况下做伯努利试验成不成功，$$p$$ 很小则代表鲜有成功，则为**稀有事件**的描述，所以是二项分布的极限情况。

【GRAD-UPDATE】**Thinning property**: 从一个泊松过程中随机选取一些事件（选取的概率是常数 $$r$$），这些事件依然构成泊松过程。泊松过程的适用条件：试想一个任意的过程，从该过程中随机地选取极少的事件。事件之间的相关性随时间衰减，如果选的事件足够稀少（相关性小），那么选出的事件可以近似地用泊松过程描述。

【GRAD-UPDATE】本科阶段只讨论了事件发生概率是常数 $$r$$ 的情况，结论是一段时间 $$T$$ 内发生事件的计数 $$N$$ 满足 $$\langle N\rangle=rt$$，$$\langle N^2\rangle=\langle N\rangle$$. 考虑更一般的情况，事件发生概率 $$r(t)$$ 随时间变化，但是各个事件的发生没有关联，有结论 $$\displaystyle\langle N\rangle=\int_0^Tdt*r(t)$$，$$\langle N^2\rangle=\langle N\rangle$$。文章详见[泊松分布与泊松分布(II)](https://zhuanlan.zhihu.com/p/603123138)，推导过程详见[概率论 - 一般的泊松过程与泊松分布](https://shi200005.github.io/download_file/Probability_Poisson_Inhomo.pdf)。

【GRAD-UPDATE】**一维随机游走**（birth-and-death）过程中，细致平衡给出稳态时系统在稳态“格点”附近的分布也是泊松分布。

#### 几何分布

【GRAD-UPDATE】在伯努利实验中，得到一次成功所需要的试验次数分布。在生物物理实验数据中描述**多态动力学**的 **burst-size distribution**。

### 连续型随机变量 

分布函数 c.d.f.（数学家更喜欢，考虑到有离散情况的数学形式）、概率密度 p.d.f.（物理学家更喜欢，与统计系综的概念联系紧密，相信信息学家也更喜欢这个）。

#### 均匀分布 

$$X\sim U(a,b)$$

#### 指数分布

指数分布具有**无记忆性**。闲聊：知乎网友[指数分布的分布函数是怎么得到的？](https://www.zhihu.com/question/354825596/answer/893242882)。

泊松分布与指数分布的联系：**泊松过程**的两个事件发生时间间隔符合指数分布。

#### 正态分布（高斯分布）

$$X$$~$$N(μ,σ^2)$$

正态分布作为**二项分布**的近似：$$n$$ 很大，$$p$$ 接近 $$1/2$$ -> $$X\sim b(n,p)$$ ->  $$X\sim N(μ,σ^2)$$。【GRAD-UPDATE】求解方法（注意，两种方法近似出来的方差略有不同）：

- 例：biased random walk 求解 Fokker-Planck 近似下的小偏差（$$p$$ 接近于 $$1/2$$）的概率偏微分方程，详见[随机过程 - 随机游走与二项分布](https://shi200005.github.io/download_file/Probability_Binomial_Normal_Fourier.pdf)。
- 通过 [Stirling 近似](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula)再取连续极限，[概率论 - 二项分布近似为正态分布](https://shi200005.github.io/download_file/Probability_Binomial_Normal.pdf)。

#### Gamma 分布

以后再说  泊松过程第 $$n$$ 次事件出现的时间服从 Gamma 分布

### 随机变量和的分布

如果随机变量 $$X_1\sim P_1$$ 和 $$X_2\sim P_2$$ 相互**独立**，则 $$X=X_1+X_2$$ 的分布函数为 

连续：$$P(X=x)=\displaystyle\int_{\text{all}} P_1(X_1=u)P_2(X_2=X-u)du$$

离散：$$P(X=x)=\displaystyle\sum_{\text{all}} P_1(X_1=u)P_2(X_2=X-u)$$

我们在这里看到了**卷积**，于是想到了**傅里叶变换**的**卷积定理**（详见[复变函数](https://shi200005.github.io/2022/02/15/Complex-Functions/#%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2)）。

结论（独立）

- **Merging property**: 泊松 + 泊松还是泊松，参数为求和。

- 【GRAD-UPDATE】多个相同指数分布随机变量的和 Erlang Distribution: 产生于电话接线背景，可以用于描述生物信号转导中的 N-Step **Cascade**，每一步都是指数分布。

  Example in biophysics: analytical continuous model solution of protein distribution when produced in bursts, and the burst size obeys the exponential distribution. Reference: Friedman, N., Cai, L., & Xie, X. S. (2006). Linking stochastic dynamics to population distribution: an analytical framework of gene expression. *Physical review letters*, *97*(16), 168302. Note that Laplace transform (see [复变函数](https://shi200005.github.io/2022/02/15/Complex-Functions/#%E6%8B%89%E6%99%AE%E6%8B%89%E6%96%AF%E5%8F%98%E6%8D%A2)) was applied to solve it. [online](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.168302)

  The [exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution), [Erlang distribution](https://en.wikipedia.org/wiki/Erlang_distribution), and [chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution) ([数理统计](https://shi200005.github.io/2022/02/18/Statistics/#%E5%B8%B8%E7%94%A8%E6%8A%BD%E6%A0%B7%E5%88%86%E5%B8%83)) are special cases of the [gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution).

- 已知一个随机变量为指数分布，与另一个随机变量的和为指数分布，另一个随机变量是指数分布吗？**不是**。见 Thomas & Cover Elements of Information Theory 习题 9.3。

- 正态 + 正态还是正态，期望为期望和，方差为方差和，证明：[Sum of normally distributed random variables](https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables)。

如果两个**正态分布**的随机变量有**相关性**，则它们的和还是高斯分布，期望为相加，方差并非简单相加。推导见上面 [Sum of normally distributed random variables](https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables)。

## 多维随机变量及其分布

### 联合分布

以二维随机变量为例 $$F(x,y)=P\{(X≤x)∩(Y≤y)\}=P\{X≤x, Y≤y\}$$
 - 连续型随机变量联合概率密度 $$\displaystyle F(x,y)=\int_{-∞}^y{f(u,v)dudv}$$, $$\displaystyle\frac{\partial^2{F(x,y)}}{\partial x\partial y}=f(x,y)$$​.

#### Multivariate Gaussian Distribution

$$G(\vec {x})=\displaystyle (2\pi )^{-k/2}\det({\boldsymbol {\Sigma }})^{-1/2}\exp \left(-{\frac {1}{2}}(\vec {x} -{\vec {\mu }})^T{\boldsymbol {\Sigma }}^{-1}(\vec {x} -{\vec {\mu }})\right)$$

其中 $$\vec {x}$$ 是 $$k$$ 维随机变量摞成的一个列向量。问题：为什么指数部分取协方差矩阵的逆？其实不用太繁琐的数学推导——Hint: 协方差矩阵是**实对称矩阵**，能够合同对角化（[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/#%E5%AE%9E%E5%AF%B9%E7%A7%B0%E7%9F%A9%E9%98%B5)），然后请自行对随机变量进行基变换，你会明白。

### 边缘分布

以二维随机变量为例 $$(X,Y)$$ 关于 $$X$$ 的边缘分布函数：$$P\{X≤x\}=P\{X≤x,y<∞\}=F(x,∞)=F_X(x)$$.

- 连续型随机变量边缘概率密度：$$\displaystyle f_X(x)=\int_{-∞}^{∞}{f(x,y)dy}$$.

已知联合分布可导出随机变量各自的条件分布，已知各自的条件分布不能导出它们的联合分布。

### 条件分布

$$P(y\vert x)=\displaystyle\frac{P(x,y)}{P(x)}$$.

### 相互独立与两两独立

三个随机变量**相互独立**能推出三对随机变量**两两独立**，反之推不出。示例见下图，$$Z=X\oplus Y$$，即布尔代数里的 XOR 运算。

![Probability_Pairwise](\images\blog\Probability_Pairwise.jpg)

通信加密和解码应用例：[One-time pad](https://en.wikipedia.org/wiki/One-time_pad) (thanks Prof Kschischang and TA Amir Tasbihi @ ECE1520 UofT)。

### 复合形式

$$P((z\vert y)\vert x)$$ 其实就是 $$P(z\vert(x,y))$$.

$$P(x_1,x_2,x_3)=p(x_2,x_3\vert x_1)=P((x_3\vert x_2)\vert x_1)P(x_2\vert x_1)P(x_1)=p(x_3\vert x_1,x_2)P(x_2\vert x_1)P(x_1)$$. Just imagine finding a probability grid in a 3-D sample space. Find the grid axis after axis.

## 随机变量的数字特征

### 期望

$$E(X+Y)=E(X)+E(Y)$$ 总成立；$$E(XY)=E(X)E(Y)$$ 在 $$X,Y$$ 相互独立时成立。

### 方差

$$D(X)=\text{Var}(X)=E\{[(X)-E(X)]^2\}$$. 

$$D(aX)=a^2D(X)$$, $$D(X+Y)=D(X)+D(Y)+2\text{Cov}(X,Y)$$.

- P.S. 并不是所有概率分布都存在有限的方差！例如 $$\displaystyle P(x)=\frac{1}{\pi}\frac{\gamma}{(x-a^2)+\gamma^2}(-\infty<x<\infty)$$，也称为 Lorentz-Cauchy distribution 就没有。

### Law of total expectation & variance 

(using conditional probability of different cases)

[$$E(X)=E(E(X\vert Y))$$](https://en.wikipedia.org/wiki/Law_of_total_expectation) i.e. lives of light bulbs from different factories

[$$\text{Var}(X)=E[\text{Var}(X\vert Y)]+\text{Var}(E[X\vert Y])$$](https://en.wikipedia.org/wiki/Law_of_total_variance)

Related work in systems biology

- Huh, D., & Paulsson, J. (2011). Random partitioning of molecules at cell division. *Proceedings of the National Academy of Sciences*, *108*(36), 15004-15009. [online](https://www.pnas.org/doi/full/10.1073/pnas.1013171108)
- Hilfinger, A., & Paulsson, J. (2011). Separating intrinsic from extrinsic fluctuations in dynamic biological systems. *Proceedings of the National Academy of Sciences*, *108*(29), 12167-12172. [online](https://www.pnas.org/doi/10.1073/pnas.1018832108)

### 常见分布の期望 & 方差表

| 种类 | 分布                                                                                      | 数学期望 | 方差           |
| 离散 | 二项分布 $$P(X=m)=\binom{N}{m}p^m(1-p)^{N-m}$$, $$X\in \mathbb{N_0}$$ | $$np$$           | $$np(1-p)$$ |
| 离散 | 泊松分布 $$P(X=m)=\frac{x^m e^{-\lambda}}{m!}$$ , $$X\in \mathbb{N_0}$$                       | $$λ$$              | $$λ$$                |
| 离散 | 几何分布 $$P(X=m)=(1-p)^{k-1}p$$, $$X\in \mathbb{N_0}$$             | $$\frac{1}{p}$$             | $$\frac{1-p}{p^2}$$           |
| 连续 | 均匀分布 $$f(X=x)=\frac{1}{b-a}$$, $$X\in[a,b]$$                          | $$\frac{a+b}{2}$$         |$$\frac{(b-a)^2}{12}$$         |
| 连续 | 指数分布  $$f(X=x)=\lambda e^{-\lambda x}$$ ,$$X\in[0,\infty)$$                  | $$\frac{1}{θ}$$              | $$\frac{1}{θ^2}$$              |
| 连续 | 正态分布 $$f(X=x)=\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{-(x-\mu)^2}{2\sigma^2}}$$, $$X\in(-\infty,\infty)$$  | $$μ$$              | $$σ^2$$              |

- Poisson 在法语里是🐟的意思。
- 【GRAD-UPDATE】离散随机变量分布中的二项分布、泊松分布和几何分布的均值和方差计算：见 [Generating Functions](https://shi200005.github.io/download_file/Probability_Generating_Functions.pdf)。

### 矩 moment

$$\displaystyle \mu _{n}=\sum \limits _{i=1}^{\infty }(x_{i}-c)^{n}P(x_{i})$$, $$\displaystyle \mu _{n}=\int _{-\infty }^{\infty }(x-c)^{n}\,f(x)\,dx$$.

### The characteristic function

对概率分布做**傅里叶变换**（参见[复变函数](https://shi200005.github.io/2022/02/15/Complex-Functions/#%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2)）得到 *the characteristic function* $$\displaystyle\tilde p(k)=\langle e^{-ikx}\rangle=\int dxp(x)e^{-ikx}$$，then moments of the PDF around any point $$x_0$$ can be generated by expanding $$e^{ikx_0}\tilde p(k)=\displaystyle\sum_{n=0}^\infty\frac{(-ik)^n}{n!}\langle(x-x_0)^n\rangle$$。

### The cumulant generating function

$$\ln\tilde p(k)$$，我们称把这个东西对 $$k$$ 的展开项是 *cumulants*，Kardar 在书中 2.2 节用 $$\langle x^n\rangle_c$$ 表示，van Kampen 在书中用 $$\langle\langle x^n\rangle\rangle$$ 表示，维基百科中表示为 $$\kappa_n(x)$$。Why do we care about cumulants? 对于图形法背后的数学，在书中图形法的后一页解释得很清楚了，不再赘述。

> An important theorem allows easy computation of moments in terms of the cumulants: represent the $$n$$th cumulant graphically as a *connected cluster* of $$n$$ points. The $$m$$th moment is then obtained by summing all possible subdivisions of $$m$$ points into groupings of smaller (connected or disconnected clusters).
>
> ![Probability_Cumulant](\images\blog\Probability_Cumulant.JPG)

高斯分布 $$\displaystyle p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp[-\frac{(x-\lambda)^2}{2\sigma^2}]$$ 的优良品质是 $$\langle x\rangle_c=\lambda$$, $$\langle x^2\rangle_c=\sigma^2$$, $$\langle x^3\rangle_c=\langle x^4\rangle_c=...=0$$​，也就是任何阶中心矩都可以用均值和方差两个参数表示。

得名：如果随机变量 $$x_i$$ 相互**独立**，则 $$\displaystyle\kappa_n(\sum x_i)=\sum\kappa_n(x_i)$$。

上面这些单变量统计分布可以解决（更高级的去看[(En) Advanced Statistical Mechanics](https://shi200005.github.io/2023/05/07/Advanced-Statistical-Mechanics/)），下面是多变量分布的简单性质。

### 协方差

定义：$$\text{Cov}(X,Y)=E\{[(X)-E(X)][(Y)-E(Y)]\}=E(XY)-E(X)E(Y)$$.

$$D(X+Y)=D(X)+D(Y)+2E\{[(X)-E(X)][(Y)-E(Y)]\}$$.

相关系数：$$\displaystyle ρ_{XY}=\frac{\text{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}$$. (Term: [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).)

性质：[协方差矩阵是半正定矩阵](https://blog.csdn.net/qcyfred/article/details/71598815)，参见[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/#%E5%AE%9E%E5%AF%B9%E7%A7%B0%E7%9F%A9%E9%98%B5)。

### 相关系数

相关系数描述的是**线性**相关程度。性质是$$\vertρ_{XY}\vert≤1$$，当且仅当 $$Y=a+bX$$ 时取等号。若$$X,Y$$ 独立，则相关系数一定为零；若相关系数为零，不一定独立。感觉这个名字有点误导性。

随机变量独立意味着 $$P(x,y)=P(x)P(y)$$。描述两个随机变量是否独立：**互信息**，详见 [(En) Information Theory](https://shi200005.github.io/2023/10/03/Information-Theory/)。

## 大数定理

*Markov's inequality*: $$X$$ non-negative, for every $$a>0$$, $$\displaystyle P[X\geq a]\leq\frac{E[X]}{a}$$. （其实很弱）

*Chebyshev's inequality*: Using *Markov's*, $$X$$ -> $$(X-\mu)^2$$, then $$\displaystyle P\{\vert X-μ\vert\geq a\}\leq\frac{\sigma^2}{a^2}$$. 

**The weak law of large numbers**: for i.i.d. samples $$X_i$$, $$\displaystyle\bar X=\frac{1}{n}\sum_{k=1}^{n}{X_k}$$, $$\displaystyle D[\bar X]=\frac{σ^2}{n}$$. Using *Chebyshev's*, $$X$$ -> $$\bar X$$, $$a$$ -> $$\epsilon$$, then $$\displaystyle P\{\vert\bar X-μ\vert\geq \epsilon\}\leq\frac{1}{n}\frac{\sigma^2}{\epsilon^2}$$ goes to zero when $$n$$ goes to infinity.

辛钦定理：$$\displaystyle\lim_{n\to\infty} P\{\vert\bar X-μ\vert< ε\}=1$$ 均值收敛于期望，不需要方差存在。具体证明没涉及到，好像需要 Kolmogorov 收敛定理，先不管它。

## 中心极限定理

### De Moivre-Laplace 定理 

前面正态分布部分讲过，$$n$$ 很大，$$p$$ 接近 $$1/2$$ 时，**二项分布**近似为**正态分布**。

### Lyapunov 定理

无论各个随机变量服从什么分布，只要满足定理的条件（the cumulants of the individual random variables are finite），那么 **i.i.d.** 样本之**和**当样本数很大时，就近似地服从**正态分布**。为什么呢？其实 Kardar 那本书的第二章讲得很清楚了。

Sum $$X=\displaystyle\sum_{i=1}^{N}x_i$$, $$x_i$$ are i.i.d. from a distribution. We have $$\langle X^n\rangle_c=N\langle x^n\rangle_c$$. Construct $$\displaystyle y=\frac{X-N\langle x\rangle_c}{\sqrt N}$$, so $$\langle y^n\rangle_c\propto N^{1-n/2}$$. As $$N\rightarrow\infty$$, **only the second cumulant survives**, and the PDF for $$y$$ converges to the **normal distribution**, $$\displaystyle\lim_{N→\infty}p(y=\frac{\displaystyle\sum_{i=1}^N x_i-N\langle x \rangle_c}{\sqrt N})=\frac{1}{\sqrt{2\pi\langle x^2\rangle_c}}\exp(-\frac{y^2}{2\langle x^2\rangle_c})$$. 

- 特例（学 Lyapunov 之前用这个引出）：伯努利试验次数很多时，成功次数总和 $$S_n$$ 的分布符合正态分布，归一化变量 $$\displaystyle S_n=\frac{S_n-E(S_n)}{\sqrt{\text{Var}(S_n)}}$$~$$N(0,1)$$。证明详见 Garrity, All the math you need to know... chapter 18.5，因为试验次数多，处理大阶乘时用到了 [Stirling's Approximation](https://shi200005.github.io/2021/09/30/Calculus/#stirlings-formula).

## 后记

> 社会和个人法则是一个概率和机遇的问题。就统计学而论，这些法则还是不可抵挡的；它们甚至可以自我调节。人们如果符合这些法则的中心倾向，那就是正常的，而那些处于极端的人则是病态的，所以“我们大多数人”试图使自己变得正常，这实际上反过来影响了关于正常的概念。原子没有这种倾向。人类科学表现出物理学中所没有的反馈效应。——Ian Hacking

概率 *probabilis* —— Marcus Tullius Cicero (106 BC - 43 BC)  罗马共和国。量化对事实的不确定性最初被用于古罗马法庭判决。

样本空间 —— Gerolamo Cardano (1501-1576)

频率依概率 —— Galileo Galilei (1564 - 1642)

数学期望 —— Blaise Pascal (1623 - 1662)

二项分布 —— Jacob Bernoulli (1654-1705) 伯努利关心如果不事先知道概率分布，从频率推测概率有多大的把握。后来发展为伯努利大数定理。

De Moivre-Laplace 定理 —— Abraham de Moivre (1667-1754) 把 Pascal 三角一直往下算，发现下面近似为正态分布。

贝叶斯公式 —— Thomas Bayes (1701 - 1761) 如何联系后验概率和先验概率，即你看到的结果和事物本身性质之间的概率联系。

相关系数 —— Francis Galton (1822 - 1911) 研究孩子从父母遗传性状的规律。

---
layout: post
title: 数理统计 1.0
categories: BS-NJU-Course-Review-Mathematics
description: 对于概率论与数理统计的回顾
keywords: data statistics and analysis
mathjax: true
---

> ... the fundamental difference between probability and statistics: the former concerns predictions based on fixed probabilities; the latter concerns the inference of those probabilities based on observed data. --The drunkard's walk, Leonard Mlodinow

符号说明：$$\mu$$ —— 统计量（以均值为例），$$\hat\mu$$ —— 统计量的估计值（仅此篇）。

| 学习时间                                   | 大二上                                |
| 周学时                                       | 3                                         |
| 本人成绩                                   | 94                                       |
| 课程教材                                   | 名存实亡（因为已绝版） |
| 个人建议参考教材                   | 无                                        |
| 先修课程                                   | 微积分 线性代数 概率论   |

## External References

1. Leonard Mlodinow. *The Drunkard's Walk*: How Randomness Rules Our Lives. Vintage Books, 2008.

## 样本及抽样分布

总体：$$X$$，样本：$$(X_1,X_2,...,X_n)$$。我们关注样本，因为我们能得到的是样本，然后用统计学知识推测总体的性质。
- 下面我们用的样本都是**简单随机样本(independent and identically distributed, i.i.d.)**：若样本中的每个个体与总体有相同的分布，样本个体相互独立，总体中的个体总数与样本容量满足$$\displaystyle\frac{N}{n}≥10$$，则这些样本可以看作是**不放回抽样**得到的。
- 若总体 $$X$$ 的分布为 $$F(x)$$，则简单随机样本 $$(X_1,X_2,...,X_n)$$ 的联合分布为 $$\displaystyle\prod_{i=1}^{n}{F(x_i)}$$。 后面最大似然法要用。

### 样本的常用统计量

设总体均值为 $$μ$$，方差为 $$σ$$，则对于 $$n$$ 个简单随机样本：

- 样本均值 $$\displaystyle\bar{X}=\frac{1}{n}\sum_{i=1}^{n}{X_i}$$, $$E(\bar X)=\mu$$, $$\displaystyle E[D(\bar X)]=\frac{\sigma^2}{n}$$.

- 样本方差 $$\displaystyle S^2=\frac{1}{n-1}\sum_{i=1}^{n}{(X_i-\bar{X})^2}$$，是总体方差的**无偏估计**，概念见下文参数估计。

  问：样本的二阶中心矩是 $$\displaystyle S_n^2=\frac{1}{n}\sum_{i=1}^{n}{(X_i-\bar{X})^2}$$，为什么样本方差除以样本容量减去 $$1$$？答：可以证明样本二阶中心矩的期望是 $$\displaystyle E(S_n^2)=\frac{n-1}{n}σ^2$$，并不是 $$σ^2$$（[计算过程](https://www.zhihu.com/question/20099757/answer/13971886)），而 $$E(S^2)=\sigma^2$$。这是因为从总体抽样得到样本，我们在样本方差中采用的是样本均值，样本均值是总体均值的无偏估计，但是采用样本均值会使对总体方差的估计产生偏差，所以要采用无偏修正值（[直观解释](https://www.zhihu.com/question/20099757/answer/26586088)）。

- 样本各阶矩的期望 $$E[M_k]=E[X^k]$$；协方差/方差 $$\displaystyle\text{Cov}(M_k,M_j)=\frac{1}{n}(E[X^{k+j}]-E[X^k]E[X^j])$$。[推导](https://shi200005.github.io/download_file/Statistics_Cov.pdf)

### 常用抽样分布

因为**正态分布**是**最常见**的总体分布，于是我们讨论正态分布总体的常用抽样分布。标准正态分布的 $$α$$ 分位数是很简单很直观的东西。在下文的区间估计里，对于已知一个正态总体，分为均值和方差是否已知的情况，不同情况下要确定置信区间和置信度，则要用到这些奇奇怪怪的抽样分布。

- 卡方分布 $$\chi^2(n)$$：若 $$X$$~$$N(0,1)$$，则 $$\displaystyle\sum_{i=1}^{n}{X_i^2}$$~$$\chi^2(n)$$。 有表可查。是一种 **Gamma 分布**。e.g., $$\displaystyle\frac{(n-1)S^2}{\sigma^2}$$~$$\chi^2(n)$$.
- $$t$$ 分布：若 $$X \sim N(0,1)$$，$$Y\sim \chi^2(n)$$，$$X,Y$$ 相互独立，$$\displaystyle T=\frac{X}{\sqrt{Y/n}}$$。e.g., $$\displaystyle\frac{\bar  X-\mu}{S/\sqrt{n}}$$~$$T(n-1)$$，对比 $$\displaystyle\frac{\bar  X-\mu}{\sigma/\sqrt{n}}$$~$$N(0,1)$$.
- $$F$$ 分布：若 $$X\sim \chi^2(n)$$，$$Y\sim \chi^2(m)$$，$$X,Y$$ 相互独立，$$\displaystyle F=\frac{X/n}{Y/m}$$。e.g., 对于两个正态总体，$$\displaystyle\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$$~$$F(n-1,m-1)$$.

## 参数估计

总体分布的某个参数未知，通过抽取出的样本去估计这个未知的参数。**估计方法**有点估计法、频率替换法、极大似然估计法等；**估计量的评选标准**有无偏性、有效性、一致性等。

### 点估计

设总体 $$X$$ 的**分布函数的形式已知**，但它的一个或多个参数未知，借助于总体 $$X$$ 的一个样本来估计总体未知参数的值的问题。利用不同方法，得到的估计量可能不同。

#### 频率替换法

频率作为概率。

#### 矩估计法

用样本 $$k$$ 阶矩作为总体 $$k$$ 阶矩的估计量, 建立含有待估参数的方程, 从而解出待估参数。举例：总体期望的估计就是样本 $$1$$ 阶原点矩，总体方差的估计就是样本 $$2$$ 阶中心矩。（无偏、一致）

#### 极大似然估计法 MLE

（Maximum Likelihood Estimate，在机器学习里非常重要）对于总体的分布没有完整的认知（比如说知道服从某种分布，但分布的具体参数未知），从测量中得到一些样本。写出得到样本的概率表达式，式中含有未知参数。求使实验中得到样本的概率取最大值的参数值。极大估计值可能不存在也可能不唯一。方法是粗略的，要知道估计值的准确性还要做区间估计。

利用[贝叶斯公式](https://shi200005.github.io/2022/02/17/Probability/#全概率公式与bayes-公式)，求使实验中得到样本的概率取最大值的参数值，等同于给定试验结果时参数为某值的概率。实操中就是取极值，即概率对参数偏导为 $$0$$。$$\displaystyle P(\theta\vert x)=\frac{P(x\vert \theta)P(\theta)}{P(x)}$$，假定没有对参数的先验知识，$$P(\theta)=\text{const}$$。$$P(x)$$ 是标准化常量，与参数 $$a$$ 无关，$$P(x)=\int d\theta P(x\vert \theta)$$。因此，求 $$P(\theta\vert x)$$ 的极大值归结为求 $$P(x\vert \theta)$$ 的极大值。

- 为什么 MLE 要使用 $$\log$$ 概率？我觉得有两点原因，首先 $$\log$$ 是单调函数，但这很 trivial，因为单调函数太多了。根本还是来源于我们的样本是“简单随机抽样”，相互独立，抽到这组样本的概率便是把抽到各个样本的概率相乘，而 $$\log$$ 可以把连乘转化为求和。
- 例：对于一个正态总体，均值的极大似然估计值为样本均值，方差的极大似然估计值为样本 $$2$$ 阶中心矩。
- 如果对于被估计的参数有先验的偏好，$$P(A)$$ 可以并不是常数，详见[(En) Machine Learning]()。

##### Fisher 信息量

我们能从观察值里获得多少关于参数的信息，即观察值相对于参数的变化是否敏感。设 $$\mathscr l(\theta\vert x)=\log P(x\vert\theta)$$，则 Fischer 信息量则为 $$\displaystyle\mathcal I(\theta)=\text{Var}(\frac{\partial\mathscr l}{\partial\theta})$$。

#### 无偏性

虽然得到的估计值与真实值不同，但**估计值的期望**与真实值一样。反复将这一估计量使用多次，就“平均”来说其偏差为零 -> 无系统误差。e.g., $$E[M_k]=E[X^k]$$ 样本 $$k$$ 阶**原点矩**是对总体 $$k$$ 阶原点矩的**无偏估计**；样本**二阶中心矩**就是对总体均值的**有偏估计**。

#### 有效性

如果在样本容量 $$n$$ 相同的情况下，某一**无偏**估计量的方差更小，就更有效。e.g., 算术均值比加权均值有效（证明过程中用了**方幂不等式**，不难证明）。**罗 - 克拉美不等式**——达到方差下界的无偏估计量，没用过，课件里有例子，以后用到再说。

#### 一致性 / 相合性

随着样本容量的增大，一个估计量的值稳定于待估参数的真值。e.g., 一般矩法得到的估计量是一致估计量。e.g., 一般极大似然估计具有一致性（这句话没搞懂）。

### 区间估计

用点估计估计出一个值，这个值估计得有多靠谱呢？例如，我们可以确定真值就在估计值上下一个范围内的概率是多少。一般来说我们如果需要真值在范围内的把握比较大，这个范围会相对大些；我们想要一个小范围得到好的精度，我们就不那么确定真值真的在这个范围里......

正态总体的区间估计方法：根据对总体均值和方差的已知知识，构造一个样本函数——**枢轴量**，使其分布满足之前讨论过的**抽样分布**，例如 $$N(0,1)$$, $$t$$ 分布、$$F$$ 分布（细节省略），然后查表截参数取值即可。

非正态总体的区间估计方法：抽很多样，根据[中心极限定理](https://shi200005.github.io/2022/02/17/Probability/#lyapunov-%E5%AE%9A%E7%90%86)，把样本均值构造成正态分布即可。

## 假设检验

若对参数一无所知，用**参数估计**的方法处理。若对参数有所了解，但是怀疑猜测需要证实的时候，用**假设检验**的方法来处理，决定接受或拒绝假设。

假设我认为总体分布有某种特征（果蝇大部分是白眼）。从总体中抽取一些样本，抽取出的样本是这种结果居然是一间概率非常小的事（$$100$$ 只果蝇里抽出来的 $$5$$ 只全都是红眼）！于是我深刻怀疑之前对于总体分布特征的认知是错误的（大概果蝇大部分还是红眼）。“小概率原理”、**概率意义下的反证法**

依赖于样本值的判断是可能出错的。**弃真错误/第一类错误**概率一般取为 $$α$$，**取伪错误/第二类错误**概率一般取为 $$β$$。假设检验的指导思想是控制 $$α$$，然后若有必要，则通过**增大样本容量**的办法控制 $$β$$。通常把有把握的、有经验的结论作为原假设，或者尽可能使后果严重的错误成为第一类错误。可以证明，当样本容量确定后，犯两类错误的概率不可能同时减小（证明从略）。

方法：与区间估计方法类似。

## 方差分析

只讲了**单因素试验**的方差分析。

研究燃料种类 $$A_j,(j=1,2,...,s)$$ 对于火箭射程 $$X$$ 的影响是否显著。每种燃料 $$A_j$$ 做实验，分别得到一些样本 $$X_j$$，每组 $$n_j$$ 个样本，所有组共 $$n$$ 个样本。认为 $$X_j$$~$$(N,σ^2)$$（我们假定方差相同），检验每种燃料的均值 $$μ_j$$ 是否相同（假设$$H_0$$：相同）。

构造
 - 总离差平方和$$S_T$$：反映了全部实验数据的波动大小。
 - 误差平方和$$S_E$$：主要反映了由于随机误差而引起的数据波动大小。无论假设是否成立，$$\displaystyle\frac{S_E}{\sigma^2}$$ ~ $$\chi^2(n-s)$$
 - 效应平方和$$S_A$$：主要反映了的不同水平而引起的数据波动大小。只有假设成立时，才有$$\displaystyle\frac{S_E}{\sigma^2}$$ ~ $$\chi^2(s-1)$$
 - $$S_T=S_E+S_A$$.

对于给定的显著性水平，拒绝域是 $$\displaystyle\frac{S_A/(s-1)}{S_E/(n-s)}>F_\alpha(s-1,n-s)$$。

## 后记

chi-square test -- Karl Pearson (1875-1936) to determine whether a set of data actually conforms to the distribution you believe it conforms to.

significance testing -- Ronald Fisher (1890 - 1902) a formal procedure for calculating the probability of our having observed what we observed *if* the hypothesis we are testing is true.

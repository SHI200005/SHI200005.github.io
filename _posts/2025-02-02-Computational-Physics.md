---
layout: post
title: 计算物理 1.0
categories: BS-NJU-Course-Review-Other
description: 特别重要
keywords: computational physics
mathjax: true
---

<img src="https://raw.githubusercontent.com/SHI200005/Examples/refs/heads/main/fractal/Ukiyo_e.png" alt="Computing_Make" style="zoom:80%;" />

https://github.com/SHI200005/Examples/tree/main/fractal

## References

[1] [Mehta P et. al., Phys Rep. 2019 May 30;810:1-124.](https://www.sciencedirect.com/science/article/pii/S0370157319300766)

## 微分

用插值函数 $$y(x)$$ 代替原始函数的微分 $$f'(x)$$。步长 $$h$$。

- 一阶数值微分：线性插值 -> 两点微分。向前差分、向后差分、**中心差分** $$\displaystyle f'(x_n)=\frac{y_{n+1}-y_{n-1}}{2h}$$。
- 二阶数值微分：二次插值 -> 三点公式 -> 再求微商 -> 二阶数值微分 $$\displaystyle f''(x_n)=\frac{y_{n-1}-2y_n+y_{n+1}}{h^2}$$。

## 积分

用插值函数的积分代替原函数的积分。步长 $$\Delta x$$。

- 线性插值函数 -> 梯形公式。截断误差 $$\displaystyle R=-\frac{(\Delta x)^3}{12}f''(\eta)$$  ($$x_i<\eta<x_{i+1}$$)。
- 二次插值函数 -> 抛物线积分 / 辛普生积分。$$\displaystyle R=-\frac{(\Delta x)^5}{90}f^{(4)}(\eta)$$  ($$x_i<\eta<x_{i+1}$$)。

## 常微分方程

$$\displaystyle \frac{dy}{dt}=f(y,t)$$, $$y(0)=y_0$$.

- 欧拉法（折线法）Forward Euler：向前差分代替微分，$$f(y,t)$$ 用前端点 $$f(y_n,t_n)$$ 代替。局部截断误差 $$\propto\Delta t^2$$，总体截断误差 $$\propto\Delta t$$。

- 改进的欧拉法 implicit mid-point Euler：向前差分代替微分，$$f(y,t)$$ 用前后端点平均值 $$\displaystyle\frac{1}{2}(f(y_n,t_n)+f(y_{n+1},t_{n+1}))$$ 代替。总体截断误差 $$\propto\Delta t^2$$。

  例：用上述两种方法分别求解一维谐振子，前者雅可比矩阵特征值的模严格大于一，解不稳定；后者等于一。详见 PHY1610 lecture 11.

- Runge - Kutta 法：迂回复盘。

  - 二阶 Runge - Kutta 法：用欧拉法预测中间点 $$f(y_{n+1/2},t_{n+1/2})$$，向前差分代替微分，$$f(y,t)$$ 用中间点代替。总体截断误差 $$\propto\Delta t^2$$。
  - **四阶 Runge - Kutta 法（RK4）**：[Derivation of the Runge–Kutta fourth-order method](https://en.wikipedia.org/wiki/Runge–Kutta_methods#Derivation_of_the_Runge–Kutta_fourth-order_method)。总体截断误差 $$\propto\Delta t^4$$。

- 积分运动方程：Verlet、Leapfrog 等方法。例：[GROMACS Tutorials](http://www.mdtutorials.com/gmx/)。

## 偏微分方程

思路：用差分或其他常微分求解方法代替微分，下一个时间点的某个空间点的函数值由上一个时间点的该点和相邻的点确定。边界的点只有半边相邻的点，还要考虑边界条件。

- Explicit methods: e.g., $$\displaystyle\frac{T_{s+1}-T_s}{\Delta t}=FT_s$$

- Implicit methods: e.g., $$\displaystyle\frac{T_{s+1}-T_s}{\Delta t}=FT_{s+1}$$

  跟上面的各有优缺点，反正我应该就用上面的。

- 稳定性条件（必要条件）

  - 周期性边界条件：[Von Neumann stability analysis](https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis)

    >  The analysis is based on the [Fourier decomposition](https://en.wikipedia.org/wiki/Fourier_decomposition) of [numerical error](https://en.wikipedia.org/wiki/Numerical_error)...
    >
    >  A finite difference scheme is stable if the errors made at one time step of the calculation do not cause the errors to be magnified as the computations are continued.

  - [Courant–Friedrichs–Lewy condition](https://en.wikipedia.org/wiki/Courant–Friedrichs–Lewy_condition)

    > The principle behind the condition is that, for example, if a wave is moving across a discrete spatial grid and we want to compute its amplitude at discrete time steps of equal duration, then this duration must be less than the time for the wave to travel to adjacent grid points.

- 求本征值：打靶法：瞎猜本征值，然后带回微分方程看满不满足边界条件，反正就是瞎蒙。

## 线性代数

求解线性方程组，大一课上手算用高斯消元法，霸凌 python 则使用

- 求解线性方程组 -> **LU 分解法**：例：$$\mathbf A$$ 是 $$n$$ 阶**方阵**，则线性方程组 $$\mathbf A\vec x=\vec b$$ 有可能有唯一确定的解（也有可能无解或有无穷多解）

  ，将 $$\mathbf A$$ 一步一步转化为上三角方阵，转化矩阵有固定的生成套路，转化为 $$\displaystyle\prod_{i=1}^{n}\mathbf M_{i}\mathbf A\vec x=\prod_{i=1}^{n}\mathbf M_{i}\vec b$$。包： scipy: linalg.solve()。

  - 矩阵求逆：$$\mathbf A\vec x_i=\vec b_i$$，设 $$\vec b_i$$ 除了第 $$i$$ 列是 $$1$$，其他都是 $$0$$。然后排成 $$\mathbf A\mathbf X=\mathbf I$$。用 LU 分解法算出每个 $$x_i$$ 排成 $$\mathbf X=\mathbf A^{-1}$$。包： scipy: linalg.inv()：

- 求矩阵特征值与特征向量

  Givens 旋转变换：$$Q_{pq}=\sin\theta$$, $$Q_{qp}=-\sin\theta$$, $$Q_{pp}=Q_{qq}=\cos\theta$$. $$\mathbf{Q^T AQ}$$ 是正交变换。
  $$
  \mathbf Q(p,q,\theta)=
  \begin{bmatrix}
  1 & \quad & \quad & \quad & \quad \\
  \quad & \ddots & \quad & \quad & \quad \\
  \quad & \cos\theta & \quad & \sin\theta & \quad \\
  \quad & \quad & \ddots & \quad & \quad \\
  \quad & -\sin\theta & \quad & \cos\theta & \quad \\
  \quad & \quad & \quad & \ddots & \quad \\
  \quad & \quad & \quad & \quad & 1\\
  \end{bmatrix}
  $$


  - 对称矩阵：Jacobi 方法：使用正交矩阵 $$\mathbf Q$$ 对 $$\mathbf A$$ 做 Givens 旋转变换，使对角元比重逐步增加（每一步选择绝对值最大的非对角元位置作为 $$p,q$$），使非对角元逐步变小，当非对角元太小，就近似认为完成。
  - QR 方法：利用 [QR decomposition](https://en.wikipedia.org/wiki/QR_decomposition#Relation_to_RQ_decomposition)（例如 Givens 旋转）将矩阵分解为正交矩阵 $$\mathbf Q$$ 和上三角矩阵 $$\mathbf R$$ 的乘积，然后通过 [QR Algorithm](https://en.wikipedia.org/wiki/QR_algorithm) 逐步迭代，实现矩阵对角化。

## 非线性方程求根

- 搜索法：迈步走，变号回头，步长减半接着走。
- 二分法：砍一半看变不变号。
- Newton - Raphson：用直线代替原函数，直线的零点代替方程的根。
- 割弦法：上面的微分用差分代替。

前两者收敛慢，但后两者如遇到拐点或多根可能不收敛，因此先用前两者确定根的范围，再用后两者求精确值。

## 随机数

随机数的产生：线性同余法产生均匀分布的伪随机数：$$x_{n+1}=(a_n+b)\mod(m)$$，其中 $$x_0$$ 叫种子。实际模拟中我们需要随机数看似独立，所以不能瞎选参数。具体怎么选我没细研究。一般我们调包获得质量有保障的伪随机数：$$U(0,1)$$ from i.i.d，然后根据需要产生符合某种分布的随机数。

### 符合某种分布的随机数

已有 $$U(0,1)$$ 的 i.i.d. 样本，得到**服从某种概率分布**的随机数。

- 连续型：若概率密度函数有显式反函数 -> 反函数法；

- 连续型：若概率密度函数有显式反函数 -> 舍选抽样法。

- 离散型：连续型聚聚。

- Metropolis 方法：设概率密度函数是 $$f(x)$$，细致平衡跃迁几率满足 $$f(x)T_{x\to x'}=f(x')T_{x'\to x}$$。满足这种条件的跃迁几率不唯一，Metropolis 方法选择 $$\displaystyle T_{x\to x'}=\min(1,\frac{f(x')}{f(x)})$$。

  步骤：当前状态为 $$x$$，以等概率原则随机产生新状态 $$x'$$；若 $$\displaystyle\frac{f(x')}{f(x)}\geq1$$，接受新状态，否则产生随机数 $$\xi\sim U(0,1)$$，若 $$\displaystyle\xi<\frac{f(x')}{f(x)}$$ 则接受新状态。反之舍弃新状态。

## 快速傅立叶变换

把信号被离散化为采样点 $$\displaystyle\hat f_q=\sum_{j=0}^{n-1} f_je^{\pm2\pi ijq/n}$$. 用 $$n\times n$$ 矩阵 $$\mathbf F(n)_{jq}=e^{2\pi ijq/n}$$（其中$$j,q$$ 从 0 数起），实现 $$f$$ 到 $$\hat f$$ 的转化，


$$
\mathbf F(n)
\begin{bmatrix}
f_0 \\ f_1 \\ \vdots \\ f_{n-1}
\end{bmatrix}
=
\begin{bmatrix}
\hat f_0 \\ \hat f_1 \\ \vdots \\ \hat f_{n-1}
\end{bmatrix}
$$




计算成本为 $$\mathcal O(n^2)$$。不如想点办法转化。

设 $$\omega_n=e^{2\pi i/n}$$，则 $$\omega_n^2=\omega_{n/2}$$。于是 $$\displaystyle\hat f_q=\sum_{j=0}^{n-1}\omega_n^{qj} f_j$$。假设 $$n=2^{m}$$，$$\displaystyle\hat f_q=\sum_{j=0}^{n/2-1}\omega_{n/2}^{qj} f_{2j} + \omega_{n}^{q}\sum_{j=0}^{n/2-1}\omega_{n/2}^{qj} f_{2j+1}$$，如此操作，直到全拆开。计算成本为 $$\mathcal O(n\log n)$$。变换之后数据长度与原始采样信号是一样的。矩阵表示为


$$
\mathbf F(n)=

\begin{bmatrix}
\mathbf I(n/2) & \mathbf\Lambda(n/2) \\
\mathbf I(n/2) & -\mathbf\Lambda(n/2) \\
\end{bmatrix}

\begin{bmatrix}
\mathbf F(n/2) & \mathbf 0(n/2) \\
\mathbf 0(n/2) & \mathbf F(n/2) \\
\end{bmatrix}

\mathbf P(n)
$$



其中 $$\mathbf P(n)$$ 是 [Bit-reversal permutation](https://en.wikipedia.org/wiki/Bit-reversal_permutation) 矩阵。对角矩阵 $$\mathbf\Lambda(n/2)_{jj}=e^{2\pi ij/n}$$。

### 采样定律

那么采多少样够用？A continuous band-limited time-series (to *W* Hz) can be **perfectly** reconstructed, if uniformly (in time) sampled with a minimum frequency of 2*W*. Related theorem: [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem). A method is using sinc function, related theorem: [Whittaker–Shannon interpolation formula](https://en.wikipedia.org/wiki/Whittaker–Shannon_interpolation_formula). Math was elaborate in this online handout: [10.4: Perfect Reconstruction](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Signals_and_Systems_(Baraniuk_et_al.)/10%3A_Sampling_and_Reconstruction/10.04%3A_Perfect_Reconstruction), check the former section for unclear equations :-).

(Related to [复变函数](https://shi200005.github.io/2022/02/15/Complex-Functions/#%E5%82%85%E9%87%8C%E5%8F%B6%E7%A7%AF%E5%88%86), since the Fourier transform of the rect is sinc.)

### 滤波

将原信号进行傅立叶变换，将得到的数据去掉需要滤波的频率，进行傅立叶逆变换拿回信号。

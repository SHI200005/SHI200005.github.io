---
layout: post
title: (En) Machine Learning
categories: PhD-UT-Course-Review
description: 特别重要
keywords: Machine Learning
mathjax: true
---

If you have no idea of Machine Learning, then you are out of date. This post is built on Prof Anton Zilman's lectures and materials. 

## References

[1] [Mehta P et. al., Phys Rep. 2019 May 30;810:1-124.](https://www.sciencedirect.com/science/article/pii/S0370157319300766)

[2] [CS231n: Deep Learning for Computer Vision](https://cs231n.github.io)

## Concepts of statistical learning

### Bias-variance tradeoff

Ref 1 fig 4 & 5

<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>两张图片一行</title>
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 列布局 */
            gap: 10px; /* 图片之间的间距 */
            justify-items: center;
        }
        .grid-container img {
            width: 100%; /* 让图片填充单元格 */
        }
    </style>
</head>
<body>
    <div class="grid-container">
        <img src="https://ars.els-cdn.com/content/image/1-s2.0-S0370157319300766-gr4.jpg" alt="图片1">
        <img src="https://ars.els-cdn.com/content/image/1-s2.0-S0370157319300766-gr5.jpg" alt="图片2">
    </div>
</body>
</html>
### Gradient Descent


To minimize the function $$F(\vec x)=F(x_1,x_2,\ldots,x_n)$$:

- **Steepest Descent Method**: Moves in the direction of $$-\nabla F$$ with a variable step size to find a smaller function value.
  *Drawback:* Prone to severe oscillations.

- **Conjugate Gradient Method**: Integrates the current gradient with the previous search direction and gradient to determine the search direction.

- **Stochastic gradient descent (SGD)**

  To be completed.

## Supervised Learning

Given data set and the label of each data point, if I get a new data point, what label should it have?

### Linear clustering

#### Continues label - linear regression

As introduced in [计算物理](https://shi200005.github.io/2025/02/02/Computational-Physics/#最小二乘拟合).

#### Distcrete labels - logistic regression

To classify data points $$x_i$$ into **two categories** $$y_i=\{0,1\}$$. Draw a **straight** line $$\vec 0={\vec x_i}^T\vec w+\vec b_0=\vec{\mathbf x_i}^T\vec{\mathbf w}$$, where $$\vec{\mathbf x_i}=(1,\vec x_i)$$, $$\vec{\mathbf w}=(\vec b_0,\vec w)$$ which means it doesn't have to cross the origin. 

- Hard classifier: for a data point $$x_i$$, $$s_i=\vec{\mathbf x_i}^T\vec{\mathbf w}$$. Different signs of $$s_i$$ indicate on different sides of the line -> two categories.

- Soft classifier: give the probability that the data points belong to each side. $$\displaystyle P(y_i=1\vert\vec x_i,\mathbf{\vec w})=\frac{1}{1+e^{-\mathbf{\vec x_i}^T\mathbf{\vec w}}}$$. Denote $$\displaystyle\sigma(s)=\frac{1}{1+e^{-s}}$$ as the **logistic** (or **sigmoid**) function.

  The error function = the negative log-likelihood = the *cross entropy* -> no close form solution for minimial cross entropy -> e.g., [gradient descent](https://shi200005.github.io/2025/02/02/Computational-Physics/#优化问题). 

  - Given two **Gaussian distribution** $$\displaystyle P(\vec x\vert y=i)=\frac{1}{\sqrt{2\pi\det(\hat A)}}\exp\left(-\frac{1}{2}(\vec x-\vec\mu_i)^T\hat\Sigma^{-1}(\vec x-\vec\mu_i)\right)$$ with the same covarince matrix $$\hat\Sigma$$ and means $$\vec\mu_0$$ and $$\vec\mu_1$$. Then $$\displaystyle\frac{P(y=1\vert\vec x)}{P(y=0\vert\vec x)}=\exp(\vec x^T\vec w+\vec\theta)$$, where $$\displaystyle\vec\theta=-\frac{1}{2}(\vec\mu_1 - \vec\mu_0)^T\hat\Sigma^{-1}(\vec\mu_1 - \vec\mu_0)+\ln(\frac{P(s=1)}{P(s=0)})$$  and $$\vec w=\hat\Sigma^{-1}(\vec\mu_1 - \vec\mu_0)$$, which are independent on data points.
  - [Linear regression and quadratic regression examples](https://github.com/SHI200005/Examples/blob/main/machine_learning/regression.ipynb).

To classify data points into more categories, use **SoftMax**. $$\vec y_i\in\mathbb Z_2^M$$, e.g., $$\vec y=(1,0,\ldots,0)$$ meas $$\vec x_i$$ belongs to class 1. The SoftMax function: the probability of $$\vec x_i$$ being in class $$m'$$: $$\displaystyle P(y_{im'}=1\vert\vec x_i,\{\vec w_k\}_{k=0}^{M-1})=\frac{e^{-\vec x_i^T\vec w_{m'}}}{\sum_{m=0}^{M-1}e^{-\vec x_i^T\vec w_{m}}}$$...

### Nonlinear clustering - neural networks

A course from SciNet: [DAT112 Neural Network Programming (Apr 2024)](https://education.scinet.utoronto.ca/course/view.php?id=1327).

input layer (input features $$\vec x={x_1,x_2,\ldots,x_d}$$) -> hidden layers -> output layer (output scaler $$a_i(\vec x)$$, a simple classifier), trianed by [gradient descent](https://shi200005.github.io/2025/02/02/Computational-Physics/#优化问题)

<img src="https://ars.els-cdn.com/content/image/1-s2.0-S0370157319300766-gr35.jpg" alt="图片1">

Ref 1 fig 35

> The universal approximation theorem: a neural network with a single hidden layer can approximate any continous, multi-input/multi-output function with arbitrary accuracy.

**Calculating the gradient - the backpropagation algorithm**

> is a clever procedure that exploits the layered structure of neural networks to more efficiently compute gradients.
>
> is simply the ordinary chaim rule for partial differential...

**Convolutional Neural Networks (CNNs)**

> a translationally invariant neural network that respects locolity of the input data.

<img src="https://ars.els-cdn.com/content/image/1-s2.0-S0370157319300766-gr42.jpg" alt="图片1">

Ref 1 fig 42.

Pending!!! Does "convolution" here related to the convolution thereom in Fourier transform???

## Unsupervised learning

Given a bunch of data, are there any structures?

### Linear dimensionality reduction

#### Principle component analysis (PCA)

Brief idea: high dimension data -> covariance matrix -> high variance - feature; low variance - noise -> throw away the low-variance dimension by an **orthogonal transformation** (linear!) -> a lower dimensional space, the *latent space*. Two examples with explanations in "[my biophysics reading course](https://drive.google.com/drive/folders/1AM40tWbmIJNYv9EMDSzS00GHat5agrKi)": [MachineLearning1.ipynb](https://github.com/SHI200005/Examples/blob/main/BiophysicsReading/MachineLearning1.ipynb), [MachineLearning2.ipynb](https://github.com/SHI200005/Examples/blob/main/BiophysicsReading/MachineLearning2(1).ipynb).

### Nonlinear dimensionality reduction

#### *t*-stochastic neighbor embedding (t-SNE)

> Attempting to represent data in a space of dimensionality lower than its intrinsic dimensionality can lead to a “crowding” problem.
>
> When used appropriately, t-SNE is a powerful technique for unraveling the hidden structure of high-dimensional datasets while at the same time preserving locality.

In the high dimensional space: $$\displaystyle p_{ij}=\frac{1}{2N}(p_{i\vert j}+p_{j\vert i})$$, where $$\displaystyle p_{i\vert j}=\frac{\exp(-\Vert x_i-x_j\Vert^2/2\sigma_i^2)}{\sum_{k\neq i}\exp(-\Vert x_i-x_k\Vert^2/2\sigma_i^2)}$$ (Gaussian, the likelihood that $$x_j$$ is $$x_i$$'s neighbour), where $$\sigma_i^2$$ is decided by making the *perplexity* the same $$\Sigma=2^{H(p_i)}$$ across all data points, where $$H(p_i)=-\sum_jp_{j\vert i}\log_2p{j\vert i}$$ is the local entropy.

In the low dimensional space: $$\displaystyle q_{ij}=\frac{(1+\Vert y_i-y_j\Vert^2)^{-1}}{\sum_{k\neq j}(1+\Vert y_i-y_k\Vert^2)^{-1}}$$ (long tailed, the likelihood that $$y_j$$ is $$y_i$$'s neighbour).

Then minimize the Kullback-Leibler divergence between $$q_{ij}$$ and $$p_{ij}$$ by gradient descent (stochasticity here!).

Usually the data points are described in high dimensions. How do we visualize them on a 2D printable plot? One example in "[my biophysics reading course](https://drive.google.com/drive/folders/1AM40tWbmIJNYv9EMDSzS00GHat5agrKi)": [MachineLearning2.ipynb](https://github.com/SHI200005/Examples/blob/main/BiophysicsReading/MachineLearning2(1).ipynb).

#### Diffusion Map

### Clustering

Why clustering is important? See [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox). Two piles of data points can be positively correlated within each group, but negatively correlated overall.

#### K-means

If the points stay close, then they are in a same cluster. Cluster the given points with a given number of cluster. Two examples with explanations in "[my biophysics reading course](https://drive.google.com/drive/folders/1AM40tWbmIJNYv9EMDSzS00GHat5agrKi)": [MachineLearning1.ipynb](https://github.com/SHI200005/Examples/blob/main/BiophysicsReading/MachineLearning1.ipynb), [MachineLearning2.ipynb](https://github.com/SHI200005/Examples/blob/main/BiophysicsReading/MachineLearning2(1).ipynb).

#### Gaussian mixture model

## Generative models

> A model that can lern to represent and sample from a probability distribution is called generative.
>
> at their most basic level are complex parametrizations of the probability distribution the data is drawn from.

### Energy-based models

#### Maximum entropy (MaxEnt)

The simplest energy-based generative models. 

As I have said in Probability ([概率论](https://shi200005.github.io/2021/10/02/Probability/)), we use probability to describe something because we lack information of the whole thing. Entropy quantifies the uncertainty of a distribution. When we don't know something, we cannot "bias" to pretend we know. Thus, given some information of a distribution, we plug in the information (usually use **Lagrange multipliers**, see Calculus([微积分](https://shi200005.github.io/2021/09/30/Calculus/)) and **maximize the entropy** of the distribution for estimation. 

If the mean of a continuous distribution is specified, the maximum entropy distribution is **Boltzmann** (exponential); if the mean and the standard deviation of a continuous distribution are specified, the maximum entropy distribution is **Gaussian** (normal).

**Simulating Brownian motions**

Given potential $$E(x)$$, then we know the corresponding stationary distribution $$\displaystyle p(x)=\frac{1}{Z}e^{-\beta E(x)}$$. However, the known $$E_0(x)$$ is not the actual potential and the distribution from experiment doesn't obey $$p(x)$$. How can we get a more realistic choice for $$p(x)$$ consistent with the experimental data?

From experiment we observe $$\langle A_i(x)\rangle_\text{exp}=\langle A_i(x)\rangle_p$$. Construct  and minimizing $$\displaystyle\mathcal L=-\int p(x)\ln(p)dx-\alpha(\int p(x)dx-1)-\sum_i\lambda_i(\langle A_i(x)\rangle_p-\langle A_i(x)\rangle_\text{exp})$$, then $$\displaystyle p(x)=\frac{1}{Z}e^{-\beta E_0(x)+\sum_i\lambda_iA_i(x)}$$.

Regression algorithm: from $$E_0(x)$$ get $$p_0(x)$$, calculate $$\delta A_i^0=\langle A_i\rangle_\text{exp}-\langle A_i\rangle_0$$ and set $$\lambda_i^{(0)}=-\eta\delta A_i^0$$, where $$\eta$$ is learning rate. Calculate $$E_n(x)$$ and get $$p_n(x)$$, then $$\lambda_i^{(n+1)}=\lambda_i^{(n)}-\eta\delta A_i^n$$, until good enough.

#### Boltzmann Machines

To be completed.

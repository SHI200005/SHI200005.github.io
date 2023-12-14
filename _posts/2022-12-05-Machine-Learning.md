---
layout: post
title: (En) Machine Learning
categories: PhD-UT-Course-Review
description: 
keywords: Machine Learning
mathjax: true
---

我可算懂了，本学期前半段的《随机过程》是进阶版《概率论》，后半段的《机器学习》是进阶版《数理统计》。谢谢多伦多大学研一秋，让我体验进阶版南京大学大二上。

版本 2022.12.05,Ver0.0

参考文献：[Mehta P et. al., Phys Rep. 2019 May 30;810:1-124.](https://www.sciencedirect.com/science/article/pii/S0370157319300766)

## 概率与统计基础补充

### Multivariate Gaussian Distribution

$$G(\mathbf {x})=\displaystyle (2\pi )^{-k/2}\det({\boldsymbol {\Sigma }})^{-1/2}\,\exp \left(-{\frac {1}{2}}(\mathbf {x} -{\boldsymbol {\mu }})^{\!{\mathsf {T}}}{\boldsymbol {\Sigma }}^{-1}(\mathbf {x} -{\boldsymbol {\mu }})\right)$$

其中 $$\mathbf {x}$$ 是 $$k$$ 维随机变量摞成的一个列向量。问题：为什么指数部分取协方差矩阵的逆？其实不用太繁琐的数学推导——Hint: 协方差矩阵是实对称矩阵，能够合同对角化（[线性代数](https://shi200005.github.io/2021/09/30/Linear-Algebra/)），然后请自行对随机变量进行基变换，你会明白。

## 有监督的 (Supervised)

给定数据集，以及每个数据点的标签。如果拿到一个新的数据点，它的标签将是什么？

1. 如果标签是连续取值——线性回归(Linear Regression)

   最小二乘回归

   统计解释： maximum likelihood estimation of a vector $$x$$, given linear measurements corrupted by Gaussian measurement errors.

2. 如果标签是离散类别——逻辑回归(Logistic Regression)

   - 缺点：逻辑回归是一种线性归类，难以精确分类。对策：使用多层神经网络，实现非线性归类。

     

## 无监督的(Unsupervised)

给定一坨数据，它们有怎样的结构？

### 降维

- 主元分析 (PCA)
  - SVD 分解
- t-SNE 
- Diffusion Map

### 聚类

- K-means
- Gaussian Mixture Model
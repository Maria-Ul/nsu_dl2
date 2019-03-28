# Seminar 5

How to apply discussed techniques in PyTorch. Dive deeper into previous Pytorch demos.

## Plan

The idea of the seminar is following. We will talk about of some problem, the possible solutions of it and the pros and cons of these solutions. As the solutions would be imperfect, we will talk about the solutions of such non-perfect solutions and so on going sequentially through each item.

1. Optimization methods
   - [x] vanilla gradient descent
   - [x] mini-batch or stochastic GD 
   - [x] shuffle the data
   - [x] monitor train/val loss and metrics
   - [x] choose appropriate learning rate on small dataset
   - [x] Scheduled learning rate: learning rate decay, decay on plateau
   - [x] averaged SGD
2. Weights initialization
   - [ ] constant, zero, random
   - [ ] Saturation gradient (initialization with big numbers)
   - [ ] Vanishing gradients (initialization with small numbers)
   - [ ] unsupervised (auto-encoders)
   - [ ] Glorot for symmetric activation functions (sigmoid), Xe for not (relu)
   - [ ] batch-normalization (internal covariance shift)

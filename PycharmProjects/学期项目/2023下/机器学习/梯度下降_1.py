import numpy as np

X = [2,6,9]
n_samples = len(X)
print(n_samples)





class BatchGradientDescent:
    def __init__(self, eta=0.01, n_iter=1000, tolerance=0.001):
        self.eta = eta  # 学习率
        self.n_iter = n_iter    # 迭代次数
        self.tolerance = tolerance  # 两次训练损失差最小值

    # X 样本集合，y 预测值（假设
    def fit(self, X, y):
        n_samples = len(X)  # 样本数量
        X = np.c_[np.ones(n_samples), X]  # 增加截距项
        n_features = X.shape[-1]

        self.theta = np.ones(n_features)
        self.loss_ = [0]

        self.i = 0
        while self.i < self.n_iter:
            self.i += 1
            errors = X.dot(self.theta) - y
            loss = 1 / (2 * n_samples) * errors.dot(errors)
            delta_loss = loss - self.loss_[-1]
            self.loss_.append(loss)
            if np.abs(delta_loss) < self.tolerance:
                break
            else:
                gradient = 1 / n_samples * X.T.dot(errors)
                self.theta -= self.eta * gradient

        return self
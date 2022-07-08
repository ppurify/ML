import numpy as np

class LinearRegression(object):
    def __init__(self, fit_intercept=True, copy_X=True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X

        self._coef = None
        self._intercept = None
        self._new_X = None
        
        self._theta_pred = None

    def fit(self, X, y):

        self._new_X = X

        if self.fit_intercept == True:
            one_vector = np.ones((len(self._new_X), 1))
            self._new_X = np.concatenate( (one_vector, self._new_X), axis =1 )

        XTX = np.dot(self._new_X.T, self._new_X)
        XTX_inv = np.linalg.inv(XTX)
        theta_pred = np.dot(np.dot(XTX_inv, self._new_X.T), y)

        self._theta_pred = theta_pred
        self._intercept = self._theta_pred[0]
        self._coef = self._theta_pred[1:]
        
        return self

    def predict(self, X):
        if self.fit_intercept == True:
            one_vector = np.ones((len(X), 1))
            new_X = np.concatenate((one_vector, X), axis = 1)
        else:
            pass

        return np.dot(new_X, self._theta_pred)

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept

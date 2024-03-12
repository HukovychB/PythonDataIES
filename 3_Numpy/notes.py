import numpy as np #ALWAYS DO THIS AS IN R
a = np.array([[[1,3], [2,4]], [[3,5], [4,6]]])
a
a.ndim
a.shape

b = np.arange(27)
b
rb = b.reshape((3,3,-1)) #-1 to correctly specify the 3rd dimension
rb.shape

rb.mean()
a.mean()
a.min()
a.max() # max value
a.argmax() #index of the max value
a.cumsum()
a.cumprod()
a.T
a.dot(a)
a.T.dot(a)

#sequence generation
x=0
y=100
n_point=1000
c = np.linspace(x,y,n_point)
c

np.random.seed(12345)
r = np.random.randn(4)
n = np.random.normal(loc = 0, scale = 1, size = 4)
r
n


pip install matplotlib

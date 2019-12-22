import numpy 
import pickle

# print(np.random.randn(10))

x = numpy.arange(10)
print(x)
f = open('x.pkl','wb')
pickle.dump(x,f)

f = open('x.pkl','rb')
print(pickle.load(f))
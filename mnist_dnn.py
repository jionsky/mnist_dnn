import numpy as np
from scipy import misc


batch_size = 128
epochs = 20

'''
use numpy load mnist data from mnist.npz
'''
def load_data(path='mnist.npz'):
    f = np.load(path)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test) 

'''
input initial w1 w2 w3 ...., output w1 grad,w2 grad w3 grad ....
w.share = (10,28*28)
x.share = (28*28,)
return grad_w.share = (10,28*28)
'''
def grad(w,x):
    grad_w[:] = w[:]
    exp_value = []
    sum_exp =0
    for i in range(w.share[0]):
        exp_value.append(exp_fun(w[i],x))
        sum_exp+=exp_fun[i]
    for i in range(w.share[0]):
        grad_w[i] =(sum_exp -exp_fun[i])/sum_exp * x
    return grad_w
    
''' 
calculate two vector inner product 
'''
def exp_fun(w,x):
    value = np.exp(np.dot(w,x))
    return value

'''
calculate Multi-class Classification Cross Entropy
'''
def loss_fun(w,x,label):
    exp_value = []
    sum_exp =0
    for i in range(w.share[0]):
        exp_value.append(exp_fun(w[i],x))
        sum_exp+=exp_fun[i]
    loss_value = np.log(exp_value[label]/sum_exp)
    return loss_value
'''
training function input x data 
'''
def training_fun(data,label,w,w_new):
    for i in range(epochs):
        grad_w = grad(w,x)
        w_new = w - rate * grad_w
        loss_value = loss_fun(w_new,data,label)
        print(loss_value)
     
    

(x_train, y_train), (x_test, y_test) = load_data()
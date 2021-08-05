import numpy as np
import matplotlib.pyplot as plt 


def displacement(s0, a, t):
    s = s0 + np.multiply(v0,t) + 1/2*np.multiply(a,pow(t,2))
    return s

def plot_displacement(s0, a, t):
    s = displacement(s0, a, t)
    plt.plot(t, s)
    plt.title('Displacement vs Time plot')
    plt.ylabel("displacement")
    plt.xlabel("time")
    plt.show()
    return 

if __name__ == '__main__':
    t = np.linspace(0, 2 , num=20)
    #s = np.linspace(0, 0 , num=200)
    s0 = 0
    v0 = 0
    a = -10

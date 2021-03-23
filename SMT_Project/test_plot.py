import matplotlib.pyplot as plt
import numpy as np

# t = np.arange(0.0, 2.0, 0.01)
# print(t)
# s = 1 + np.sin(2*np.pi*t)
#print(s)
t=[1,2,3,4,5,6,7,8,9]
s=[10,100,10,110,120,130,140,150,170]
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
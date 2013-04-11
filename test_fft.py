#the purpose of this test is to read in a list of values from the physioData
#and then do something with it


import numpy as np
import matplotlib.pyplot as plt


#read in the data file (4 signals(t) with 60000 data points)
fi_1 = open('./set-a-text/a03.csv', 'r')
fi_2 = open('./set-a-text/a03.fqrs.txt', 'r')

#TODO: maybe use csv module... 

ti=[]   #time
sig1=[] #signal 1
sig2=[]
sig3=[]
sig4=[]

bfqrs=[]


#signal data
head_1=fi_1.readline()
head_2=fi_1.readline()

for line in fi_1:
	myline = [y.strip() for y in line.split(',')]
	ti.append(myline[0])
	sig1.append(myline[1])
	sig2.append(myline[2])
	sig3.append(myline[3])
	sig4.append(myline[4])
#fqrs event times

for line in fi_2:
	bfqrs.append(line.strip())


# for x in xrange(100):
# 	print sig1[x], sig2[x], sig3[x], sig4[x]


#turn our lists into numpy arrays
bb=np.array(bfqrs, dtype=float)

t=np.array(ti,dtype=float)
s1=np.array(sig1,dtype=float)
s2=np.array(sig2, dtype=float)
s3=np.array(sig3,dtype=float)
s4=np.array(sig4,dtype=float)


x = []
y = []

for ms, v  in enumerate(s1):

	if  v> 40:
		#plt.scatter(ms,v)
		x.append(ms)
		y.append(v)

#plt.show()
plt.scatter(x,y)

print float(len(x))

# print "t", type(t), t.shape, t.dtype
# print "s1", type(s1), s1.shape, s1.dtype
# print "s2", type(s2), s2.shape, s2.dtype
# print "s3", type(s3), s3.shape, s3.dtype
# print "s4", type(s4), s4.shape, s4.dtype
# print "s5", type(bb), bb.shape, bb.dtype

#do something

#plot time and the bb events overlayed

# fig, axes = plt.subplots(nrows=3)

# colors = ('k', 'r', 'b')
# for ax, color in zip(axes, colors):
# 	data = np.random.random(1) * np.random.random(10)
# 	ax.plot(data, marker='o', linestyle='none', color=color)
x=xrange(0,60000)

def abs_sq(signal):
	fs=np.fft.fft(signal)
	temp=np.absolute(fs)
	return np.square(temp)

def plot_power_spec(signal1,signal2,signal3,signal4):
	s_w12=abs_sq(signal1)
	s_w22=abs_sq(signal2)
	s_w32=abs_sq(signal3)
	s_w42=abs_sq(signal4)

	#print x[0], signal[0]
	plt.xlim((0,1000))
	plt.plot(x, s_w12)
	plt.plot(x, s_w22)
	plt.plot(x, s_w32)
	plt.plot(x, s_w42)
	plt.show()

#plt.plot(t,s1)
plt.show()
#plot_power_spec(s1,s2,s3, s4)




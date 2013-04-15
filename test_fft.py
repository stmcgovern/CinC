#the purpose of this test is to read in a list of values from the physioData
#and then do something with it


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as ss
#from tempfile import TemporaryFile

#outfile=TemporaryFile()

#read in the data file (4 signals(t) with 60000 data points)
fi_1 = open('./set-a-text/a01.csv', 'r')
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

#have lists of each input stream
#scrub the lists(catch and replace "-")
#save lists to own object(avoid having to process csv file each time)

#1. turn lists into lists of *only* numbers
#for now assigns a "-" entry to +/- 1 of previous value
def just_numbers(sig):
	x=0.0
	for i,s in enumerate(sig):
		if s=='-':
			x=float(sig[i-1])
			if(x>0):
				sig[i]=x+1
			else:
				sig[i]=x-1

just_numbers(sig2)


#2. turn our lists into numpy arrays
bb=np.array(bfqrs, dtype=float)

t=np.array(ti,dtype=float)
s1=np.array(sig1,dtype=float)
s2=np.array(sig2, dtype=float)
s3=np.array(sig3,dtype=float)
s4=np.array(sig4,dtype=float)

#3. save our numpy arrays (not now)
#np.save(outfile, t)

#4. get dominant frequencies for a signal

def freq_dom_plot(sig):
	fs=np.fft.rfft(sig)
	x=fs.shape
	print "shape", fs.shape
	print "freq shape", fs.shape
	plt.scatter(xrange(x[0]), fs)
	plt.xlim((0,1000))
	plt.ylim((-10000,10000))
	plt.show()


#freq_dom_plot(sig2)

def abs_sq(sig):
	fs=np.fft.rfft(sig)
	temp=np.absolute(fs)
	return np.square(temp)

def freq_2_plot(sig):
	fs=abs_sq(sig)
	x=fs.shape
	print "shape", fs.shape
	print "freq shape", fs.shape
	plt.scatter(xrange(x[0]), fs)
	plt.xlim((0,1000))
	#plt.ylim((-10000,10000))
	plt.show()


#freq_2_plot(sig1)

#5. get a list of peak frequencies


power=abs_sq(sig1)

#arbitrarily cut it off at 400
power_slice=power[:400]
#print np.ptp(power)
#peaks= ss.find_peaks_cwt(power,np.arange(1,10))
#peaks=ss.argrelmax(power)
peaks=ss.argrelmax(power_slice)
x=peaks[0].shape
print peaks
for p in peaks:
	plt.scatter(p, power[p])


#plt.scatter(xrange(x[0]),peaks[0])
#plt.show()

#return a list of frequencies in descending order by amplitude(first 400)

def freq_rank(sig):
	power=abs_sq(sig)
	powers=power[:400]
	#peaks=ss.argrelmax(power_slice)
	
	max_freq=[]
	#max_freq.append(biggest_freq(power_slice))
	for x in xrange(100):
		max_peak=np.argmax(powers)
		powers[max_peak]=0
		max_freq.append(max_peak)
	


	# red_power_slice=power_slice.remove(max_peak)
	# for f in red_power_slice:
	# 	max_peak=np.argmax(red_power_slice)
	# 	max_freq.append(max_peak)
	# 	red_power_slice=power_slice.remove(max_peak)
	return max_freq


freqs_s1=freq_rank(sig1)
print freqs_s1

power=abs_sq(sig1)
plt.scatter(xrange(100),power[freqs_s1])
plt.show()




# for ms, v  in enumerate(s1):

# 	if  v> 40:
# 		#plt.scatter(ms,v)
# 		x.append(ms)
# 		y.append(v)

#plt.show()
#plt.scatter(x,y)

#print float(len(x))

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

#plt.plot(t,s2)
#plt.show()
#plot_power_spec(s1,s2,s3, s4)




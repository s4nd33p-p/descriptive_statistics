from matplotlib import pyplot as plt
import random,math,string
class stat(object):
	"""docstring for stat"""
	def __init__(self,l1,l2):
		super(stat, self).__init__()
		self.values = l1
		self.fre = l2
		self.sortfre=sorted(self.fre)
		self.relfreq=[self.fre[i]/sum(self.fre) for i in range(len(self.values))]
	def pieplot(self):
		data=self.fre
		label=self.values
		a=string.hexdigits
		colors=[]
		for i in range(len(data)):		#here i was generating some random hex values of colors 
			colors.append(("#"+"".join([random.choice(a) for i in range(6)])).upper())
		plt.pie(data,labels=label,colors=colors,shadow=True)
		plt.show()
	def bargraph(self):
		xvalues=self.values
		yvalues=self.fre
		fig=plt.figure()
		ax=fig.add_axes()
		plt.bar(xvalues,yvalues)
		plt.axis([0,6,0,6])
		plt.xlabel("values")
		plt.ylabel("frequency")
		plt.show()
	def call_mean(self):
			return sum(self.fre)/len(self.fre)
	def call_median(self):
		li=sorted(self.fre)
		if(len(self.fre)%2==0):
			mid=len(self.fre)//2
			return (li[mid]+li[mid+1])/2
		else:
			return li[len(self.fre)//2]
	def call_mode(self):
		return max(self.fre)
	def call_samplevariance(self,z):
		mean=self.call_mean()
		s=0
		for i in range(len(z)):
			s=s+math.pow((z[i]),2)
		return (s-(len(z)*(math.pow(mean,2))))/(len(z)-1)

	def call_samplevariance_on_values(self,z):
		mean=sum(self.values)/len(self.values)
		s=0
		for i in range(len(z)):
			s=s+math.pow((z[i]),2)
		return (s-(len(z)*(math.pow(mean,2))))/(len(z)-1)

	def to_stem_leaf(self):	#to convert the frequencies into stem leaf representation						
		data=self.fre        #result:[[stem1,[leaves-1]],[stem2,[leaves-2]]]
		leaves=[]
		test=[]
		result=[]
		for i in data:
			j=str(i)
			test.append([j[:-1],j[-1]])
			leaves.append(j[:-1])
		leaves=sorted(set(leaves))
		for j in leaves:
			tmp=[]
			for k in test:
					if(k[0]==j):
						tmp.append(int(k[1]))
			result.append([int(j),tmp])
		return sorted(result)

	@staticmethod
	def from_stemleaf_to_interval(a):		#this works on integer values only 
		vals=[]								#input:[[stem1,[leaves-1]],[stem2,[leaves-2]]]
		for i in a:
			for j in i[1]:
				vals.append(i[0]*10+j)
		return vals

	@staticmethod
	def from_sl_to_values(b):		#this works for float values
		vals=[]
		for i in a:
			c=str(i[0])
			for j in i[1]:
				j=str(j)
				re=c+j
				vals.append(float(re))
		return vals

	def call_standarddeviation(self):
		x=self.call_samplevariance(self.fre)
		return math.sqrt(x)

	def call_standarddeviation_on_values(self):
		y=self.call_samplevariance_on_values(self.values)
		return math.sqrt(y)

	def call_percentile(self,p):
		np=len(self.fre)*p
		print(len(self.fre))
		if(np%1==0.0):
			return [[np,np+1],(self.sortfre[int(np+1)]+self.sortfre[int(np+2)])/2]
		else:
			return [[math.ceil(np)],self.sortfre[math.ceil(np)]]

	def default_percentiles(self):
		first_percentile=self.call_percentile(0.25)
		second_percentile=self.call_percentile(0.50)
		third_percentile=self.call_percentile(0.75)
		return ([first_percentile,second_percentile,third_percentile])

	def chebyshevs_result(self):
		mean=self.call_mean()
		s=self.call_standarddeviation()
		k=3/2
		t=100*(1-(1/(k**2)))
		d1=mean-(k*s)
		d2=mean+(k*s)
		return [t,[d1,d2]]

	def scatter_plt(self):		#this plot will help in recognizing normal datasets
		color=(0,0,0)
		plt.scatter(self.values,self.relfreq,c=color,alpha=0.5)
		plt.show()

	def call_corelation_total(self):
		re=0
		x1=sum(self.values)/len(self.values)
		y1=self.call_mean()
		for i,j in zip(self.values,self.fre):
			re+=(i-x1)*(j-y1)
		s1=self.call_standarddeviation()
		s2=self.call_standarddeviation_on_values()
		return re/((len(self.fre))*s1*s2)
if __name__ == '__main__':
	freq=[9,8,5,5,6,7]								#input the frequencies here	
	values=[i for i in range(len(freq))]	# input the values here
	ob=stat(values,freq)
	print("mode is "+str(ob.call_mode()))
	print("----------------------------")
	print("mean is "+str(ob.call_mean()))
	print("----------------------------")
	print("median is "+str(ob.call_median()))
	if(ob.call_mean()==ob.call_median() or ((abs(ob.call_mean()-ob.call_median()))>0 and (abs(ob.call_mean()-ob.call_median()))<1)):
		print("----------------------------")
		print("the given data set is normal dataset check its barplot,scaterplot")
	print("----------------------------")
	print("sample variance of frequencies is "+str(ob.call_samplevariance(freq)))
	print("----------------------------")
	print("sample variance on values is "+str(ob.call_samplevariance_on_values(values)))
	print("----------------------------")
	print("deviation on frequencies is "+str(ob.call_standarddeviation()))
	print("----------------------------")
	print("deviation on values is "+str(ob.call_standarddeviation_on_values()))
	if(ob.call_corelation_total()<0):
		print("----------------------------")
		print("co-relation coefficient is"+str(ob.call_corelation_total()))
		print("the data is negatively co-related")
		print("i.e,small x values are associated with large y")
	else:
		print("----------------------------")
		print("the data is positively co-related")
		print("i.e,large x values are associtated with large y values,co-relation coefficient is"+str(ob.call_corelation_total()))
	print("----------------------------")
	print("chebyshevs result :")
	print(str(ob.chebyshevs_result()[0])+"  percentile of data is between intervals "+str(ob.chebyshevs_result()[1][0])+" and "+str(ob.chebyshevs_result()[1][1]))
	ob.pieplot()
	ob.bargraph()
	ob.scatter_plt()

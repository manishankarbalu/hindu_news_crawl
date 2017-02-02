def diff(f,s):
	cnt=0	
	d1=dict()
	d2=dict()
	for i in f:
		if(d1.has_key(i)):
			d1[i]=d1[i]+1
		else:
			d1[i]=1

	for i in s:
		if(d2.has_key(i)):
			d2[i]=d2[i]+1
		else:
			d2[i]=1
	print d1
	print d2
	for i in d1:
		if(d2.has_key(i)):
			d1[i]=abs(d1[i]-d2[i])
			d2[i]=0
	print d1
	cnt=0
	for i in d1:
		cnt=cnt+d1[i]
	for i in d2:
		cnt=cnt+d2[i]
	print d1
	print d2
	return cnt

name1=raw_input("enter first name")
name2=raw_input("enter second name")
count=diff(name1,name2)
#count=count-1
print count
seq="flames"
l=list(seq)
j=0
for i in range(1,6*count):
	#print i	
	if(len(l)!=1):
		if(j<len(l)):
			if(i%count==0 and i!=0 ):
			
				#print l[j]
				del l[j]
				j=j-1
		if(j+1==len(l)):
			j=0
		else:				
			j=j+1
	#print j,len(l)
				
print 'you are '
print l


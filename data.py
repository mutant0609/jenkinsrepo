#!/path/to/python/virtualenv
#!/usr/bin/env python3
#import numpy as np
import csv
import re
import sys
import os
import json
import pandas as pd
import pprint
import collections
import json
from collections import OrderedDict

payload = []
mylist = []
		



class Myobject:
	def __init__(self):
		self._v = 0
		self._id = ""
		
		self.submitted_at = ''
		self.soft_delete = ''
		self.status = ''
		self.approved = ''
		self.other_images = ''
		self.entered_by= {'id':"", 'login':""}
		self.response = []
		self.task={'id':"",'name':""}
	def add(self,question,answer):
		self.response.append({'question':question,'answer':answer})
	

	

#x = Myobject()
#print(x.entered_by['id'])
#os.getcwd()

surveys_df = pd.read_csv("data5.csv")
head=surveys_df.columns
length = head.__len__()
#print(length)
#print(surveys_df[0:1])
#print(surveys_df['What is the cost per product?'].dtype)
#print(surveys_df.dtypes)
for st in head:
	if (surveys_df[st].dtype=='float64' or surveys_df[st].dtype=='int64'):
		mylist.append(st)
		

#print(mylist)


workpath=os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(workpath,'data5.csv'), 'r') as data:
	incsv = csv.reader(data)
	next(incsv)
	for line in incsv:

		#print(line)
		y = Myobject()
		y.entered_by['login']=line[3]
		#y.task['name']=line[15]
		for n in range(4,length):
			if head[n] in mylist:
				f = line[n]
				if (line[n]==""):
					f=float('NaN')
				y.add(head[n],float(f))
			else:
				y.add(head[n],line[n])
		#print(y.__dict__)
		payload.append(y)

output = []


for l in payload:
	z=OrderedDict([('_id',l._id),('_v',l._v),('submitted_at',l.submitted_at),('soft_delete',l.soft_delete),('status',l.status),('approved',l.approved),('other_images',l.other_images),('entered_by',l.entered_by),('response',l.response),('task',l.task)])
	output.append(z)
	#print(json.dumps(z, ensure_ascii=False))


print(json.dumps(output,ensure_ascii=False))
#json.dumps(output,outfile.txt,ensure_ascii=False)





		




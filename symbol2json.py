import zipfile
import sys
import json
"""A script to convert from mse-set to json format"""

if len(sys.argv) < 2:
    print("usage: python3 mse2json.py set.mse-set [output_name]")

if len(sys.argv) >= 3:
    fname = sys.argv[2]
else:
    fname = 'jsonstring'

zipf = zipfile.ZipFile(sys.argv[1],'r')

setf = zipf.open('symbol5.mse-symbol') # To read the set symbol

content = [x.decode('utf-8') for x in setf]
zipf.close()

tabs = []
# test
for i,line in enumerate(content):
    ## count the number of tabs at the beginning of a string
    tabs.append(line.count('\t'))
    #print('%d - %s'%(tabs[i],line),end='')
tabs.append(-1)

f = open(fname+'.txt','w')
j = open(fname+'.json','w')

jsonstring=''
ccount = 1

first_point = False # Flag
last_point = False

for i,line in enumerate(content):
    line = line.strip()
    line = line.replace('"','') # remove double quotes
    key,val = line.split(':',maxsplit=1)
    if key == 'part':
        key = key+str(ccount)
        ccount +=1
    if key == 'point' and tabs[i] == tabs[i-1]:
        first_point = True
    if tabs[i] - tabs[i+1] >= 2:
        last_point = True
    if tabs[i] < tabs[i+1]:
        line = '"'+key.strip()+'":'
    else:
        line = '"'+key.strip()+'":"'+val.strip()+'"'

    if i == 0:
        line = '{'+line
    if tabs[i] == tabs[i+1]:
        line = '\t'*tabs[i]+line.strip()+','
    if tabs[i] < tabs[i+1]:
        line = '\t'*tabs[i]+line.strip()+'{'
        if 'point' in line and not first_point:
            line = '\t'*tabs[i]+'{'        
        if 'point' in line and first_point:
            line = line[:-1]+'[{'
            first_point = False
        
    if tabs[i] > tabs[i+1]:
        line = '\t'*tabs[i]+line.strip()+'}'*(tabs[i]-tabs[i+1])+','
        if last_point:
            line = line[:-(tabs[i]-tabs[i+1]+1)] + '}]},'
            last_point=False        
        if i == len(content)-1:
            line = line[:-1]+'}'
        
#    if i == len(content)-1:
#        line = '\t'*tabs[i]+line.strip()+'}'
#    print(line,end='\n')
    jsonstring = jsonstring+line
    f.write(line+'\n')
f.close()

jsonstring = jsonstring.replace('\t','')
todump = json.loads(jsonstring)
json.dump(todump,j,indent=4)
j.close()

import csv
data=[]
target=[]
symplist=[]
with open('Training.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for lines in csv_reader:
        if line_count>0:
            n = (len(lines))
            X=lines[:131]
            Y=lines[132]
            data.append(X)
            target.append(Y)
        else:
            Z=lines[:131]
            symplist=Z
        line_count += 1
#print(target)
#for row in data:
#    print (row)
testlist=['a','b','a','c','d','e']
testele='a'
#print (testlist.count('a'))
def distinct(a):
    b=[]
    for i in a:
        if(i not in b):
            b.append(i)
    return b
targetdis=distinct(target)
def probTarget(list,a):
    b=list.count(a)
    n=len(list)
    prob=(float(b)/n)
    return prob
#print (probTarget(testlist,testele))
targetProb=[]
def allProbTraget(list):
    for i in range (len(list)):
        targetProb.append(probTarget(list,list[i]))
#allProbTraget(testlist)
#print (targetProb)
#print (target)
#print (symplist)
#assuming input
user=['itching','shivering']
#print (testlist.index('d'))
def symPerProb(sym,dis,fact):
    sym_count=0
    trows=len(data)
    index_sym = symplist.index(sym)
    for i in range (len(data)):
        if (float(data[i][index_sym])==float(fact) and target[i]==dis):
            sym_count +=1
    prob = (float(sym_count)/(target.count(dis)))
    return prob
def symTotProb(user,targetlist,symptomlist):
    eachtargetprob=[]
    for i in range(len(targetlist)):
        for j in range(len(symptomlist)):
            tl=[]
            if (symptomlist[j] in user):
                tl.append(symPerProb(symptomlist[j],targetlist[i],1))
            else:
                tl.append(symPerProb(symptomlist[j], targetlist[i], 0))
        eachtargetprob.append(tl)
    return eachtargetprob
totProb=symTotProb(user,target,symplist)

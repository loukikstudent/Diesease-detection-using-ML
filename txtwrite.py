import csv
data=[]
col=[]
with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for lines in csv_reader:
        if line_count>0:
            n = (len(lines))
            X=lines[:10]
            data.append(X)
        else:
            Z=lines[:10]
            col=Z
        line_count += 1
print (col)
print (len(col))
print (data[0])
x=open('test.txt','a')
for i in range (len(data)):
    x.write('INSERT INTO registerations ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9}) VALUES ("{10}","{11}","{12}","{13}",{14},{15},"{16}","{17}","{18}","{19}");\n'.format(*col,*data[i]))

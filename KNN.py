import math
import operator

testdata=[]
realdata=[]

# k-nn with eucledian distance
def data_train(dataset,k):
    count=0
    temp = []
    tempkey={} 
    with open('src/ecoli_train.csv') as tr:
        for line in tr:
            datasum = 0
            count = count + 1
            # skip the first row
            if count == 1: 
                continue
            else:
                x = line.strip().split(',')
                for j in range(0,len(dataset)):
                    datasum += ((dataset[j] - float(x[j+1]))**2)
                datasum = math.sqrt(datasum)
                temp.append((datasum,x[0],x[len(x)-1]))
        # rank the result
        temp.sort()

        # list the k-nearest neighbour to the new data
        for x in range(0,k): 
            if x == 0:
                tempkey[temp[x][2]]=1
            else:
                if tempkey.has_key(temp[x][2]):
                    tempkey[temp[x][2]]=tempkey[temp[x][2]]+1 
                else:
                    tempkey[temp[x][2]]=1

        print ('key :'),tempkey 
        print ("")
        # choose the class with most value as a class for new data
        a = max(tempkey.iteritems(), key=operator.itemgetter(1))[0]     
        print a 
        return a

# get the test data and predict the class
def data_test():
    count=0
    with open('src/ecoli_test.csv') as ts:
        for line in ts:
            data = [] 
            count = count + 1
            if count == 1: 
                continue
            else:
                x = line.strip().split(',')
                for i in range(0,len(x)):
                    if i == 0 or i == (len(x)-1):
                        continue 
                    else:
                        data.append(float(x[i])) 
                testdata.append(data_train(data,K)) 
                realdata.append(x[len(x)-1])

# compare the real class and predicted class to find accuracy
def check(test,real):
    true = 0
    for i in range (0,len(test)):
        print "Prediction : " , testdata[i] , " Real : " , realdata[i]
        if test[i] == real[i]:
            true += 1
        print "True : ", true
    acc = float(true)/float(len(test))
    print ""
    print "Accuracy : ", acc

K = input("K: ")
data_test()

print testdata
print ""
print realdata
print ""

check(testdata,realdata)



    

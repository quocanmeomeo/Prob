import random
import matplotlib.pyplot as plt

def pack():
    lstOutcome = []
    for i in range (5):
        lstOutcome.append(i+1)
    return random.choice(lstOutcome)

def pack1():
    lstPack1 = []
    lstPack1.append(pack())
    return lstPack1

def pack5():
    lstPack5 = []
    for i in range (5):
        lstPack5.append(pack())
    return lstPack5

def pack3():
    lstPack3 = []
    for i in range (5):
        lstPack3.append(pack())
    return lstPack3

def openfull():
    lstCounter = [0,0,0,0,0]
    intPackCount = 0
    while 0 in lstCounter:
        intPackCount += 1
        a = pack1()[0]
        if (a>=1 and a<=5):
            lstCounter[a-1] += 1
    return intPackCount

def openfull3():
    lstCounter = [0,0,0,0,0]
    intPackCount = 0
    while 0 in lstCounter:
        intPackCount += 1
        a = pack3()
        for i in range(len(a)):
            if (a[i] >= 1 and a[i] <= 5):
                lstCounter[a[i] - 1] += 1
    return intPackCount

def openfull5():
    lstCounter = [0,0,0,0,0]
    intPackCount = 0
    while 0 in lstCounter:
        intPackCount += 1
        a = pack5()
        for i in range(len(a)):
            if (a[i] >= 1 and a[i] <= 5):
                lstCounter[a[i] - 1] += 1
    return intPackCount

def open1m1():
    lstPack = []
    lstPackCount = []
    for i in range (100):
        lstPackCount.append(0)
    for i in range (1000000):
        a = openfull()
        lstPackCount[a]+=1
        lstPack.append(a)
    for i in (range(len(lstPackCount))):
        lstPackCount[i] = (lstPackCount[i]/1000000)*100
    return lstPackCount

def plotbar(data):
    # Creating the bar graph
    plt.figure(figsize=(20, 6))
    plt.bar(range(len(data)), data, color='skyblue')

    # Adding title and labels
    plt.title('Bar Graph of List Data')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig('bar_graph.png')

def open1m3():
    lstPack = []
    lstPackCount = []
    b=0
    for i in range (20):
        lstPackCount.append(0)
    for i in range (1000000):
        a = openfull3()
        lstPackCount[a]+=1
        lstPack.append(a)
    for i in (range(len(lstPackCount))):
        b += (lstPackCount[i]/1000000) * i
        lstPackCount[i] = (lstPackCount[i]/1000000)
    print(b)
    return lstPackCount

def open1m5():
    lstPack = []
    lstPackCount = []
    b=0
    for i in range (20):
        lstPackCount.append(0)
    for i in range (1000000):
        a = openfull5()
        lstPackCount[a]+=1
        lstPack.append(a)
    for i in (range(len(lstPackCount))):
        b += (lstPackCount[i]/1000000) * i
        lstPackCount[i] = (lstPackCount[i]/1000000)
    print(b)
    return lstPackCount

print(open1m3())
print(open1m5())

plotbar(open1m3())




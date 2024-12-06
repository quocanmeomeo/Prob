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

def sta1():
    # 11P1
    a = []
    for i in range (11):
        a += pack1()
    return a

def sta2():
    # 1P3 9P1
    a = []
    for i in range (9):
        a += pack1()
    a += pack3()
    return a

def sta3():
    # 1P5 1P3 5P1
    a = []
    for i in range (5):
        a += pack1()
    a += pack3()
    a += pack5()
    return a

def sta4():
    # 1P5 7P1
    a = []
    for i in range (7):
        a += pack1()
    a += pack5()
    return a

def sta5():
    #2P3 6P1
    a = []
    for i in range (3):
        a += pack1()
    a += pack3()
    a += pack3()
    return a

def sta6():
    #1P5 2P3 2P1
    a = []
    for i in range (2):
        a += pack1()
    a += pack3()
    a += pack3()
    a += pack5()
    return a

def sta7():
    #2P5 3P1
    a = []
    for i in range(3):
        a += pack1()
    a += pack5()
    return a

def sta8():
    #2P5 1P3 1P1
    a = []
    a += pack1()
    a += pack3()
    a += pack5()
    a += pack5()
    return a

def sta9():
    #1P5 3P3
    a = []
    a += pack3()
    a += pack3()
    a += pack3()
    a += pack5()
    return a

def test_sta1():
    a = []
    for i in range (100000):
        b = sta1()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta2():
    a = []
    for i in range (100000):
        b = sta2()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta3():
    a = []
    for i in range (100000):
        b = sta3()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta4():
    a = []
    for i in range (100000):
        b = sta4()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta5():
    a = []
    for i in range (100000):
        b = sta5()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta6():
    a = []
    for i in range (100000):
        b = sta6()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta7():
    a = []
    for i in range (100000):
        b = sta7()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta8():
    a = []
    for i in range (100000):
        b = sta8()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta9():
    a = []
    for i in range (100000):
        b = sta9()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

print("strategy 1: 11 Pack 1                    -> " + str(round((test_sta1()*100),2))+"%")
print("strategy 2: 9 Pack 1, 1 Pack 3           -> " + str(round((test_sta2()*100),2))+"%")
print("strategy 3: 5 Pack 1, 1 Pack 3, 1 Pack 5 -> " + str(round((test_sta3()*100),2))+"%")
print("strategy 4: 7 Pack 1, 1 Pack 5           -> " + str(round((test_sta4()*100),2))+"%")
print("strategy 5: 6 Pack 1, 2 Pack 3,          -> " + str(round((test_sta5()*100),2))+"%")
print("strategy 6: 2 Pack 1, 2 Pack 3, 1 Pack 5 -> " + str(round((test_sta6()*100),2))+"%")
print("strategy 7: 3 Pack 1, 2 Pack 5           -> " + str(round((test_sta7()*100),2))+"%")
print("strategy 8: 1 Pack 1, 1 Pack 3, 2 Pack 5 -> " + str(round((test_sta8()*100),2))+"%")
print("strategy 9: 3 Pack 3, 1 Pack 5           -> " + str(round((test_sta9()*100),2))+"%")
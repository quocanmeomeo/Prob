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
    for i in range (3):
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
    print(sum(lstPack)/len(lstPack))
    for i in (range(len(lstPackCount))):
        lstPackCount[i] = (lstPackCount[i]/1000000)*100
    return lstPackCount

def plotbar(data):
    # Creating the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(data)), data, color='#44281d')

    # Adding title and labels
    plt.ylabel('Wining rate (%)', color='#44281d')

    # Setting x-axis range
    plt.xlim(0, 40)

    ax = plt.gca()
    # Changing background color and axis color
    ax.set_facecolor('#FFF5E7')  # Set background color
    ax.spines['bottom'].set_color('#44281d')  # X-axis color
    ax.spines['left'].set_color('#44281d')  # Y-axis color
    ax.spines['top'].set_color('#44281d')
    ax.spines['right'].set_color('#44281d')
    ax.xaxis.label.set_color('#44281d')  # X-axis label color
    ax.yaxis.label.set_color('#44281d')  # Y-axis label color
    ax.tick_params(axis='x', colors='#44281d')  # X-axis tick color
    ax.tick_params(axis='y', colors='#44281d')  # Y-axis tick color
    ax.title.set_color('#44281d')  # Title color

    # Adding a vertical line at the mean value (11.42)
    mean_value = 11.42
    plt.axvline(x=mean_value, color='#cc6600', linestyle='--', linewidth=3)

    # Adding text to show the mean value below the line
    plt.text(mean_value, plt.ylim()[0] - 0.1 * plt.ylim()[1], f'Mean = {mean_value}', color='#cc6600', ha='center')

    # Saving the figure
    plt.savefig('bar_graph_openpack.png')

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
    for i in range (6):
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
    a += pack5()
    a += pack3()
    a += pack3()
    a += pack3()
    return a

def sta10():
    #1P1 4P3
    a = []
    a += pack3()
    a += pack3()
    a += pack3()
    a += pack3()
    a += pack1()
    return a

def sta11():
    #4P1 3P3
    a = []
    a += pack3()
    a += pack3()
    a += pack3()
    a += pack1()
    a += pack1()
    a += pack1()
    a += pack1()
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

def test_sta10():
    a = []
    for i in range (100000):
        b = sta10()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def test_sta11():
    a = []
    for i in range (100000):
        b = sta11()
        if (1 in b) and (2 in b) and (3 in b)and (4 in b) and (5 in b):
            a.append(1)
        else:
            a.append(0)
    c = sum(a)/len(a)
    return c

def find_combinations_1():
    options = [10, 25, 40]
    lower_limit = 110
    upper_limit = 115
    strategy_counter = 1
    unique_strategies = set()

    def find_combinations_recursive(current_combination, current_sum):
        nonlocal strategy_counter

        if lower_limit <= current_sum <= upper_limit:
            num_pack_10 = current_combination.count(10)
            num_pack_25 = current_combination.count(25)
            num_pack_40 = current_combination.count(40)
            strategy = (num_pack_10, num_pack_25, num_pack_40)

            if strategy not in unique_strategies:
                unique_strategies.add(strategy)
                strategy_name = f"strategy{strategy_counter}: {num_pack_10} Pack 1, {num_pack_25} Pack 3, {num_pack_40} Pack 5"
                print(strategy_name)
                strategy_counter += 1

        if current_sum >= upper_limit:
            return

        for option in options:
            find_combinations_recursive(current_combination + [option], current_sum + option)

    find_combinations_recursive([], 0)

counter_t = 0
import concurrent.futures

# Define the strategies and their winning rates
strategies = [
    ([10] * 11, "Strategy 1: 11 Pack 1", 60.44),
    ([10] * 9 + [25], "Strategy 2: 9 Pack 1, 1 Pack 3", 67.90),
    ([10] * 5 + [25] + [40], "Strategy 3: 5 Pack 1, 1 Pack 3, 1 Pack 5", 73.97),
    ([10] * 7 + [40], "Strategy 4: 7 Pack 1, 1 Pack 5", 67.83),
    ([10] * 6 + [25] * 2, "Strategy 5: 6 Pack 1, 2 Pack 3", 67.7),
    ([10] * 2 + [25] * 2 + [40], "Strategy 6: 2 Pack 1, 2 Pack 3, 1 Pack 5", 73.92),
    ([10] * 3 + [40] * 2, "Strategy 7: 3 Pack 1, 2 Pack 5", 73.78),
    ([10] + [25] + [40] * 2, "Strategy 8: 1 Pack 1, 1 Pack 3, 2 Pack 5", 78.89),
    ([25] * 3 + [40], "Strategy 9: 3 Pack 3, 1 Pack 5", 78.72),
    ([25] * 4 + [10], "Strategy 10: 4 Pack 3, 1 Pack 1", 73.88),
    ([25] * 3 + [10]*4, "Strategy 11: 3 Pack 3, 4 Pack 1", 74.14)
]

def evaluate_combination(current_combination):
    global counter_t
    a = []
    for i in range(1000):
        counter = [0, 0, 0, 0, 0]
        b = 0
        for j in current_combination:
            if j == 10:
                counter[random.choice([0, 1, 2, 3, 4])] += 1
            elif j == 25:
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
            elif j == 40:
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
                counter[random.choice([0, 1, 2, 3, 4])] += 1
            b += j
            if not (0 in counter):
                a.append(b)
                break
    if a:
        expect = sum(a) / len(a)

        return current_combination, sum(current_combination), expect
    return None

def find_combinations():
    options = [10, 25, 40]
    lower_limit = 110
    upper_limit = 115
    combinations = []

    def find_combinations_recursive(current_combination, current_sum):
        if lower_limit <= current_sum <= upper_limit:
            combinations.append(current_combination)

        if current_sum >= upper_limit:
            return

        for option in options:
            find_combinations_recursive(current_combination + [option], current_sum + option)

    find_combinations_recursive([], 0)

    # Use ProcessPoolExecutor to parallelize the evaluation
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(evaluate_combination, combinations))

    # Filter out None results
    results = [result for result in results if result is not None]

    # Sort the combinations by their expected value
    results.sort(key=lambda x: x[2])

    # Print the sorted combinations with strategy names and winning rates
    for combination in results:
        strategy_name = "Unknown Strategy"
        winning_rate = "N/A"
        for strategy, name, rate in strategies:
            if sorted(combination[0]) == sorted(strategy):
                strategy_name = name
                winning_rate = rate
                break
        print(
            f"{combination[0]} = {combination[1]}, Expected {combination[2]}, {strategy_name}, Winning rate: {winning_rate}%")


### Simulation functions ###

#Run this function to simulate the number of single packs neeed
#plotbar(open1m1())


#Run these code to print strategies and their winning rate
# s1 = round((test_sta1()*100),2)
# s2 = round((test_sta2()*100),2)
# s3 = round((test_sta3()*100),2)
# s4 = round((test_sta4()*100),2)
# s5 = round((test_sta5()*100),2)
# s6 = round((test_sta6()*100),2)
# s7 = round((test_sta7()*100),2)
# s8 = round((test_sta8()*100),2)
# s9 = round((test_sta9()*100),2)
# s10 = round((test_sta10()*100),2)
# s11 = round((test_sta11()*100),2)
# print("strategy 1: 11 Pack 1                    -> " + str(s1)+"%" +" - "+ str (round((((1*11)+(3*0)+(5*0))),2)))
# print("strategy 2: 9 Pack 1, 1 Pack 3           -> " + str(s2)+"%" +" - "+ str (round((((1*9)+(3*1)+(5*0))),2)))
# print("strategy 3: 5 Pack 1, 1 Pack 3, 1 Pack 5 -> " + str(s3)+"%" +" - "+ str (round((((1*5)+(3*1)+(5*1))),2)))
# print("strategy 4: 7 Pack 1, 1 Pack 5           -> " + str(s4)+"%" +" - "+ str (round((((1*7)+(3*0)+(5*1))),2)))
# print("strategy 5: 6 Pack 1, 2 Pack 3,          -> " + str(s5)+"%" +" - "+ str (round((((1*6)+(3*2)+(5*0))),2)))
# print("strategy 6: 2 Pack 1, 2 Pack 3, 1 Pack 5 -> " + str(s6)+"%" +" - "+ str (round((((1*2)+(3*2)+(5*1))),2)))
# print("strategy 7: 3 Pack 1, 2 Pack 5           -> " + str(s7)+"%" +" - "+ str (round((((1*3)+(3*0)+(5*2))),2)))
# print("strategy 8: 1 Pack 1, 1 Pack 3, 2 Pack 5 -> " + str(s8)+"%" +" - "+ str (round((((1*1)+(3*1)+(5*2))),2)))
# print("strategy 9: 3 Pack 3, 1 Pack 5           -> " + str(s9)+"%" +" - "+ str (round((((1*0)+(3*3)+(5*1))),2)))
# print("strategy 10: 1 pack 1, 4 Pack 3          -> " + str(s10)+"%" +" - "+ str (round((((1*1)+(3*4)+(5*0))),2)))
# print("strategy 11: 4 pack 1, 3 Pack 3          -> " + str(s11)+"%" +" - "+ str (round((((1*4)+(3*3)+(5*0))),2)))


#run this code to print the conditional expectation of all sequences of option given that try success
# find_combinations()



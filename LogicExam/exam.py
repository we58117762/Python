# 答案检查
def test1(anserList):
    return True


def test2(anserList):
    result = True
    if anserList[1] == 0:
        if anserList[4] == 2:
            result = True
        else:
            result = False

    elif anserList[1] == 1:
        if anserList[4] == 3:
            result = True
        else:
            result = False

    elif anserList[1] == 2:
        if anserList[4] == 0:
            result = True
        else:
            result = False

    elif anserList[1] == 3:
        if anserList[4] == 1:
            result = True
        else:
            result = False
    return result


def test3(anserList):
    result = True
    if anserList[2] == 0:
        if 0 != anserList[5] and 0 != anserList[1] and 0 != anserList[3]:
            result = True
        else:
            result = False

    elif anserList[2] == 1:
        if 1 != anserList[5] and 1 != anserList[1] and 1 != anserList[3]:
            result = True
        else:
            result = False

    elif anserList[2] == 2:
        if 2 != anserList[5] and 2 != anserList[1] and 2 != anserList[3]:
            result = True
        else:
            result = False

    elif anserList[2] == 3:
        if 3 != anserList[5] and 3 != anserList[1] and 3 != anserList[3]:
            result = True
        else:
            result = False
    return result


def test4(anserList):
    result = True
    if anserList[3] == 0:
        if anserList[0] == anserList[4]:
            result = True
        else:
            result = False

    elif anserList[3] == 1:
        if anserList[1] == anserList[6]:
            result = True
        else:
            result = False

    elif anserList[3] == 2:
        if anserList[0] == anserList[8]:
            result = True
        else:
            result = False

    elif anserList[3] == 3:
        if anserList[5] == anserList[9]:
            result = True
        else:
            result = False
    return result


def test5(anserList):
    result = True
    if anserList[4] == 0:
        if 0 == anserList[7]:
            result = True
        else:
            result = False

    elif anserList[4] == 1:
        if 1 == anserList[3]:
            result = True
        else:
            result = False

    elif anserList[4] == 2:
        if 2 == anserList[8]:
            result = True
        else:
            result = False

    elif anserList[4] == 3:
        if 3 == anserList[6]:
            result = True
        else:
            result = False
    return result


def test6(anserList):
    result = True
    if anserList[5] == 0:
        if anserList[7] == anserList[1] and anserList[7] == anserList[3]:
            result = True
        else:
            result = False

    elif anserList[5] == 1:
        if anserList[7] == anserList[0] and anserList[7] == anserList[5]:
            result = True
        else:
            result = False

    elif anserList[5] == 2:
        if anserList[7] == anserList[2] and anserList[7] == anserList[9]:
            result = True
        else:
            result = False

    elif anserList[5] == 3:
        if anserList[7] == anserList[4] and anserList[7] == anserList[8]:
            result = True
        else:
            result = False
    return result


def test7(anserList):
    result = True
    countA = anserList.count(0)
    countB = anserList.count(1)
    countC = anserList.count(2)
    countD = anserList.count(3)
    lessAnserArray = [countA, countB, countC, countD]
    lessAnserIndex = lessAnserArray.index(min(lessAnserArray))

    # 如果去重后的最小值不等于去重前的最小值，则不通过测试
    if lessAnserArray.count(min(lessAnserArray)) != 1:
        return False

    if anserList[6] == 0:
        if lessAnserIndex == 0:
            result = True
        else:
            result = False

    elif anserList[6] == 1:
        if lessAnserIndex == 1:
            result = True
        else:
            result = False

    elif anserList[6] == 2:
        if lessAnserIndex == 2:
            result = True
        else:
            result = False

    elif anserList[6] == 3:
        if lessAnserIndex == 3:
            result = True
        else:
            result = False
    return result


def test8(anserList):
    result = True
    if anserList[7] == 0:
        if abs(anserList[6] - anserList[0]) != 1:
            result = True
        else:
            result = False

    elif anserList[7] == 1:
        if abs(anserList[4] - anserList[0]) != 1:
            result = True
        else:
            result = False

    elif anserList[7] == 2:
        if abs(anserList[1] - anserList[0]) != 1:
            result = True
        else:
            result = False

    elif anserList[7] == 3:
        if abs(anserList[9] - anserList[0]) != 1:
            result = True
        else:
            result = False
    return result


def test9(anserList):
    result = True
    if anserList[8] == 0:
        if (anserList[0] == anserList[5]) ^ (anserList[5] == anserList[4]):
            result = True
        else:
            result = False

    elif anserList[8] == 1:
        if (anserList[0] == anserList[5]) ^ (anserList[9] == anserList[4]):
            result = True
        else:
            result = False

    elif anserList[8] == 2:
        if (anserList[0] == anserList[5]) ^ (anserList[1] == anserList[4]):
            result = True
        else:
            result = False

    elif anserList[8] == 3:
        if (anserList[0] == anserList[5]) ^ (anserList[8] == anserList[4]):
            result = True
        else:
            result = False
    return result


def test10(anserList):
    result = True
    countA = anserList.count(0)
    countB = anserList.count(1)
    countC = anserList.count(2)
    countD = anserList.count(3)
    lessAnserArray = [countA, countB, countC, countD]
    div = max(lessAnserArray) - min(lessAnserArray)

    if anserList[9] == 0:
        if div == 3:
            result = True
        else:
            result = False

    elif anserList[9] == 1:
        if div == 2:
            result = True
        else:
            result = False

    elif anserList[9] == 2:
        if div == 4:
            result = True
        else:
            result = False

    elif anserList[9] == 3:
        if div == 1:
            result = True
        else:
            result = False
    return result


# 题目数量
questionsNum = 10

# 循环生成所有可能的答案
# 将ABCD用0123代替便于运算
"""以三层为例
   N1 = 1 1 1 1   1 1 1 1   1 1 1 1   1 1 1 1    2 2 2 2   2 2 2 2   2 2 2 2   2 2 2 2    3 3 3 3   3 3 3 3   3 3 3 3   3 3 3 3    4 4 4 4   4 4 4 4   4 4 4 4   4 4 4 4
   N2 = 1 1 1 1   2 2 2 2   3 3 3 3   4 4 4 4    1 1 1 1   2 2 2 2   3 3 3 3   4 4 4 4    1 1 1 1   2 2 2 2   3 3 3 3   4 4 4 4    1 1 1 1   2 2 2 2   3 3 3 3   4 4 4 4
   N3 = 1 2 3 4   1 2 3 4   1 2 3 4   1 2 3 4    1 2 3 4   1 2 3 4   1 2 3 4   1 2 3 4    1 2 3 4   1 2 3 4   1 2 3 4   1 2 3 4    1 2 3 4   1 2 3 4   1 2 3 4   1 2 3 4 
   """

'''
    观察得到，每一层都是1234的循环，
    N1 最小单元是16个1，16个2，16个3，16个4组成了一个循环，循环了1次
    N2 最小单元是 4个1， 4个2， 4个3， 4个4组成了一个循环，循环了4次
    N3 最小单元是 1个1， 1个2， 1个3， 1个4组成了一个循环，循环了16次
    ……
    Nn 最小单元是4的(N - n)次方个1,(N - n)次方个2,(N - n)次方个3,(N - n)次方个4,循环4的（n - 1）次方
    '''
# 生成每一层所有答案
# 存储答案
anserArrayTList = []
for currentQuestionIndex in range(questionsNum):
    tempArry = []

    # 生成每一层的最小单元
    for anser in range(4):
        tempArry.extend([anser] * (4 ** (questionsNum - currentQuestionIndex - 1)))

    # 循环每一层最小单元
    tempArry = (tempArry * (4 ** currentQuestionIndex))
    # 合并每一层
    anserArrayTList.extend(tempArry)

# 整理答案
# 计算答案种数
anserCount = len(anserArrayTList) // questionsNum
anserArryListFinal = [0] * anserCount
# 拆分开每一个答案
for currentAnserIndex in range(anserCount):
    anserArryListFinal[currentAnserIndex] = anserArrayTList[currentAnserIndex::anserCount]

# 寻找答案
correctAnserArray = []

for each in anserArryListFinal:
    if not test1(each):
        continue

    if not test2(each):
        continue

    if not test3(each):
        continue

    if not test4(each):
        continue

    if not test5(each):
        continue

    if not test6(each):
        continue

    if not test7(each):
        continue

    if not test8(each):
        continue

    if not test9(each):
        continue

    if not test10(each):
        continue
    correctAnserArray.extend(each)

formatCorrectAnser = []
for each in correctAnserArray:
    if each == 0:
        formatCorrectAnser.extend("A")
    elif each == 1:
        formatCorrectAnser.extend("B")
    elif each == 2:
        formatCorrectAnser.extend("C")
    elif each == 3:
        formatCorrectAnser.extend("D")
print(correctAnserArray)
print(formatCorrectAnser)


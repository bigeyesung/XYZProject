import collections

arr =[1,6,9,11,55,58,67,70,74,88]
set1=set(arr)
if 6 in set1!=None:
    print("found")
if 98 in set1!=None:
    print("found")
module1= {1:1, 11:11, 67:11, 88:88}
module2= {6:1, 55:11, 70:11}
module3= {9:1, 58:11, 74:11}
curRange=0
maxRange=arr[-1]-arr[0]
def IsValid(arr):
    mod1=0
    mod2=0
    mod3=0
    for num in arr:
        if module1.get(num)!=None:
            mod1+=1
        elif module2.get(num)!=None:
            mod2+=1
        else:
            mod3+=1
    if mod1>0 and mod2>0 and mod3>0:
        return True
    else:
        return False
table = collections.defaultdict(list)
curArr=[arr[0],arr[1],arr[2]]
for ind in range(3,len(arr)-2):
    curArr.append(arr[ind])
    print("cur: ",curArr)
    #check current is vali: all modules get involved
    if IsValid(curArr) and len(curArr)>=3:
        #check range:
        curRange=curArr[-1]-curArr[0]
        if curRange<=maxRange:
            table[curRange].extend(curArr)
        #pop first num
        curArr.pop(0)
        #check rest is valid 
        if IsValid(curArr) and len(curArr)>=3:
            curRange=curArr[-1]-curArr[0]
            if curRange<=maxRange:
                table[curRange].extend(curArr)
print(table)    
n=5
for i  in range(1,n+1):
    #print(i)
    for j in range((n+1)-i):
        print(n,end=' ')
    print()

data=[2,4,1,5,7,9,8]
#print(sorted(data))
for i in range(len(data)):
    #print(i)
    for j in range(i + 1, len(data)):
      #  print(data[i])
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print(data)

#3.Find the missing number in a list of 1 to N

# Input: [1, 2, 4, 5], N = 5
# Output: 3
num=[1,2,4,5]
N=5
total = N*(N+1)/2
data=sum(num)
missingnum = total-data
print("The missing number in a list is ",int(missingnum))



#Find the majority element in a list (element that appears more than n/2 times)

# Input: [3, 3, 4, 2, 3, 3, 3]
# Output: 3
a=[3,3,4,2,3,3,3]
b=len(a)/2
for i in range(len(a)):
    count = 1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count=count+1
    if count>b:
        print("The number is ",a[i])
        break

print(count)

#4.Find all pairs in a list that sum up to a target

# Input: [1, 2, 3, 4, 5], Target = 6
# Output: [(1, 5), (2, 4)]

d=[1,2,3,4,5]
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        e=d[i]+d[j]
        if e==6:
            print([(d[i],d[j])])
#Fibonacci series
n=10
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#6.Rotate a list by K positions
# Input: [1, 2, 3, 4, 5], K=2
# Output: [4, 5, 1, 2, 3]
s = [1, 2, 3, 4, 5]
k = 2
m = []

for i in range(len(s)-k,len(s)):
    m.append(s[i])
for i in range(len(s)-k):
    m.append(s[i])

print(m)
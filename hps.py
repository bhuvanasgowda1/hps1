import re
def addsort(arr,n,numberOfEmployees):
    result=+214783647
    re=result
    arr.sort()
    for i in range(len(arr)):
       for j in range(i+1,len(arr)):
          if arr[i]>arr[j]:
             arr[i],arr[j]=arr[j],arr[i]
#    a=10
    for i in range(n-numberOfEmployees+1):
        result=(min(result,arr[i+numberOfEmployees-1]-arr[i]))
        if(result<=re):
            a=arr[i:(i+numberOfEmployees-1)+1]
    employees=("Number of the employees:" ,numberOfEmployees )
    goodiesPrice=("Here the goodies that are selected for distribution are:",a )
    priceDiffrence=("And the difference between the chosen goodie with highest price and the lowest price is" ,result)
    file1 = open("output.txt", "w")
    file1.write(str(employees))
    file1.write(str("\n"))
    file1.write(str(goodiesPrice))
    file1.write(str("\n"))
    file1.write(str(priceDiffrence))
    file1.close()
with open('myfile.txt','r') as file:
    fileContent = file.read()
arr = re.findall(r"[-+]?\d*\.\d+|\d+", fileContent)
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
numberOfEmployees=int(input("Enter no. of employee: \n"))
addsort(arr,len(arr),numberOfEmployees)

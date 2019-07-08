# Python program for implementation of json quick Sort 
import json
import sys

def partition(myList, start, end):
    pivot = myList[start]["score"]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left]["score"] >= pivot:
            left += 1
        while myList[right]["score"] <= pivot and right >= left:
            right -= 1
        if right < left:
            done= True
        else:
            # swap places
            myList[left], myList[right] = myList[right],myList[left]
    # swap start with myList[right]
    myList[start], myList[right] = myList[right], myList[start]
    return right
    


# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
#high  --> Ending index

def quickSort(arr,low,high):
    if (low < high): 
        #pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high); 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 

def getInput(filename):
    try:
        json_list = []
        with open(filename) as json_file:  
            data = json.load(json_file)
            for key in data:
                try:
                    json_list.append({"score":int(key),"id":data[key]["id"]})
                except KeyError as e:
                    print('I got a KeyError - reason "%s"' % str(e))
                    exit(2)
        return json_list
    except OSError as e:
        print('I got a FileInputError - reason "%s"' % str(e))
        exit(1)


arr = getInput(sys.argv[1])
n = len(arr)
quickSort(arr,0,n-1)
last = int(sys.argv[2])
print(arr[:last])
exit(0)
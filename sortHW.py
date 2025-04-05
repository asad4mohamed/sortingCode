
def insertionSort(elements):
   
    size = len(elements)  
    
    for i in range(size): 
           key =  elements[i] 
           j = i-1 
           while j<0 and key<elements[j]: 
                elements[j+1] = elements[j] 
                j = j-1 
           elements[j+1] = key 
    

    return elements
        
def bubbleSort(elements2):
    size = len(elements2)
     
    for i in range(size-1):
          for j in range(1,size-1):
               if elements2[j] < elements2[i]:
                    temp = elements2[i] 
                    elements2[i] = elements2[j]
                    elements2[j] = temp
    return elements2


def SelectionSort(elements3):
    size = len(elements3)
    for i in range(size-1):
        min_number = elements3[i]
        for j in range(i+1, size):
            if elements3[j] > min_number:
                min_number = elements3[j]
                elements3[i],elements3[j] = elements3[j],elements3[i]
        return elements3
     
     
     


    
               
               
     



if __name__  == "__main__":
    nums = [9,919,292,1,11,38,10,20,481,82,1,90]
    insertionSort(nums)
    bubbleSort(nums)
    SelectionSort(nums)
    print(insertionSort(nums))
    print( bubbleSort(nums))
    print(SelectionSort(nums))

    



    












def mergesort(elements):
    if len(elements) <= 1:
        return elements
    mid = len(elements)//2
    left_half = mergesort(elements[:mid])
    right_half = mergesort(elements[mid:])
    return merge(left_half,right_half)


def merge(list_1, list_2):
    sorted_array = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            sorted_array.append(list_1[i])
            i = i+1
        else:
            sorted_array.append(list_2[j])
            j = j+1
    sorted_array.extend(list_1[i:])
    sorted_array.extend(list_1[j:])
    return sorted_array         
        


    

if __name__ == "__main__":
    nums =  [1,2,4,5,6,7,9,24,56,67,68,80,100,211]
    final_answer = mergesort(nums)
    print(final_answer)






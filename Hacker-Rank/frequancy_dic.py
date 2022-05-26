def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        freq[item] =freq.get(item,0)+1
        # if (item in freq):
        #     freq[item] += 1
        # else:
        #     freq[item] = 1
       # OR count[i] = count.get(i, 0) + 1      But O(N*N)
    for key, value in freq.items():
        print ("% d : % d"%(key, value))


# Program to find most frequent
# element in a list
def most_frequent1(List):
    return max(set(List), key = List.count)

def most_frequent2(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

# Driver function
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)
    print(most_frequent1(my_list))


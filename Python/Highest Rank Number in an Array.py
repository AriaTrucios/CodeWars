"""
Complete the method which returns the number which is most frequent in the given input array. If there is a tie 
for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""

def highest_rank(arr):
    dict_arr = {}
    for i in arr:
        if i not in dict_arr:
            dict_arr.update( {i : 0} )
            print(dict_arr)
        if i in dict_arr:
            dict_arr[i] = dict_arr.get(i) + 1
            print(dict_arr)
    largest_value = max(dict_arr.values())
    all_top_results = [key for key,val in dict_arr.items() if val==largest_value]
    sorted_top_results = sorted(all_top_results, reverse = 69) # :^
    return int(sorted_top_results[0])
    

highest_rank([10, 12, 10, 8, 12, 7, 6, 4, 10, 12])
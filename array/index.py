# array = [1,2,3,4,5,6,7,8]
  
#   ///// array access  ////

# print(array[::2])

#   ///// array insertion  ////

# array = [1,2,3,4,5,6,7,8]

# array.append(9)
# array.insert(10,11) 
# print(array)

#   ///// array deletaion  ////

# array = [1,2,3,4,5,6,7,8,9]

# array.remove(2)
# # array.remove(9)
# array.reverse()
# print(array)


#  ///// array traversal  ////

# array = [1,2,3,4,5,6,7,8,9]

# for i in array:
#     print(i)
# i = 1
# while i <= len(array):
#     print(i)
#     i +=1

# lists = [i for i in array if i > 4]
# print(lists)
    
# for i,j in enumerate(array):
#     print(i,j)
    
    
#  ///// array searching  ////

# array = [1,2,3,4,5,6,7,8,9]






#  ///// two dimensional array  ////


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# def sumCros(matrix):
#     t = 0
#     su = 0
#     for i in matrix:
#         for j,k in enumerate(i):
#             if j == t:
#                 su +=k
#         t +=1
#     print(su)
        
    
# sumCros(matrix)

# total_matrix = matrix[0][0] + matrix[1][1] + matrix[2][2]
# print(total_matrix)
        
    
    
    
    
    
    
#    //////  array leetcode chanllenges /////


# array = [1,2,3,4,5,6,7,8,4,6,9]

# def twoSum(nums, target):
#     # Create a hashmap to store the indices of numbers
#     num_indices = {}

#     # Iterate through the array
#     for i, num in enumerate(nums):
#         # Calculate the complement
#         complement = target - num

#         # Check if the complement exists in the hashmap
#         if complement in num_indices:
#             # Return the indices of the current element and the complement
#             return [num_indices[complement], i]
#         else:
#             # Add the current element and its index to the hashmap
#             num_indices[num] = i

#     # If no solution is found, return an empty list
#     return []

# # Example usage
# array = [1,2,3,4,5,6,7,8,9]
# target = 7
# print(twoSum(array, target))  # Output should be [0, 1] because nums[0] + nums[1] = 2 + 7 = 9

# def single(arr):
    
#     singel_arr = []
#     repeated_number = []
    
#     for i in arr:
#         if i not in singel_arr:
#             singel_arr.append(i)
#         else:
#             repeated_number.append(i)
#     return [singel_arr,repeated_number]

# print(single(array))

# array = [5,6,7,8,4,6,2]

# def sellbuy(arr):
#     low = 0 # Initialize low with the first element of the array
#     high = 0
#     lowest_index = 0
#     heighest_index = 0
#     for i,k in enumerate(arr):
#         if k > high:
#             high = k
#             heighest_index = i
#         elif low == 0 or k < low :
#             low = k
#             lowest_index = i
            
#     maximum_profit = high - low
            
#     return [lowest_index,heighest_index,maximum_profit]

# print(sellbuy(array))


# def test(nums):
#     result = []
#     element = 1
#     n = len(nums)
#     for i in range(n,0, -1):
#         element *=i
        
        
#     print(element)
    

        
# array = [1,2,3,4]
# test(array)
        
        
# def product_except_self(nums):
#     n = len(nums)
    
#     # Initialize the answer array with ones
#     answer = [1] * n
  
#     # Compute the left products and store in answer
#     left_product = 1
#     for i in range(n):
#         answer[i] = left_product
#         left_product *= nums[i]
#     print(answer)
#     # return
#     # Compute the right products and multiply with the current value in answer
#     right_product = 1
#     for i in range(n - 1, -1, -1):
       
#         answer[i] *= right_product
#         right_product *= nums[i]
   
#     # return answer
#     print(answer)
#     return

# Example usage
# nums = [1, 2, 3, 4]
# # print(product_except_self(nums))  # Output: [24, 12, 8, 6]
# product_except_self(nums)

# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0

#     for price in prices:
#         # print(price)
#         if price < min_price:
#             # print(price)
#             min_price = price
#         elif price - min_price > max_profit:
#             print(price)
#             max_profit = price - min_price
#     return max_profit

# # Example usage
# prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))  # Output: 5
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(max(1,-2))

# def maxSubArray(nums):
#     current_sum = max_sum = nums[0]
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         print(current_sum,'cur')
#         max_sum = max(max_sum, current_sum)
#         print(max_sum,'mxa')
#     return max_sum

# # Example usage
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))  # Output: 6

def winner(andrea, maria, s):
    andrea_score = 0
    maria_score = 0
    
    if s == "Even":
        start_index = 0
    else:
        start_index = 1

    for i in range(start_index, len(andrea), 2):
        andrea_card = andrea[i]
        maria_card = maria[i]

        andrea_score += (andrea_card - maria_card)
        maria_score += (maria_card - andrea_card)

    if andrea_score > maria_score:
        return "Andrea"
    elif maria_score > andrea_score:
        return "Maria"
    else:
        return "Tie"

# Example usage:
andrea = [1, 2, 3]
maria = [2, 1, 3]
s = "Even"
print(winner(andrea, maria, s))  # Output: "Maria"

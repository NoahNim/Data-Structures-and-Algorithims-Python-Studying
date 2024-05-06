# plan
# make a low variable equaal to zero and a high variable equal to length of matrix - 1]
# calculate mid as low + (high - low) // 2
# make a in_low variable set to 0 and in_high set to length of matrix at mid - 1
# while low is less than or equal to high high and in_low is less than or equal to high
# # calculate mid again
# # check if matrix at mid index at in_low index is less than/equal to target and
# # that matrix at mid index at in_high index is greater than target
# # # if so, make a variable in_mid equal to in_low + (in_high - in_low) divided by 2
# # # check if that element at in_mid is target if so eeturn True
# # # else check if that element at in_mid is greater than target
# # # if it is set in_high to be in_mid - 1
# # # else check if in_mid element is less than target
# # # if so set in_low to be in_mid + 1
# # check if the 0th index elekement of the calculated mid is > target
# # if it is then set high to be mid - 1
# # else check if that element is less than target
# # if it is then set high to be mid + 1
# if loop exits return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        mid = low + (high - low) // 2
        in_low, in_high = 0, len(matrix[mid]) - 1
        while low <= high and in_low <= in_high:
            mid = low + (high - low) // 2
            if matrix[mid][in_low] <= target and matrix[mid][in_high] >= target:
                in_mid = in_low + (in_high - in_low) // 2
                if matrix[mid][in_mid] == target:
                    return True
                elif matrix[mid][in_mid] > target:
                    in_high = in_mid - 1
                else:
                    in_low = in_mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
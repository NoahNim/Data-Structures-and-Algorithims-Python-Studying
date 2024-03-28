# stacks are a last in, first out data structure
# Arrays are very efficient when used for stacks, as you only need to remove and insert at the same end. So popping and pushing are O(1)

# Use a stack when:
# You want to an ensure a system does not move onto another action before completing actions that come before
# When you want to do something in reverse order
# Doing an undo or redo feature
# To backtrack in a searching algorithim
# When using recursion it utilizes the call stack

# Baseball Game
# https://leetcode.com/problems/baseball-game/description/
# a hint that we can use a stack here is that we must record a new score that is double of the previous score

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []  # creates the stack
        for op in operations:
            if op == "+":
                # takes the last two elements in the stack and adds them, for recording the sum of two previous scores which are the last two elements in the stack
                stack.append(stack[-1]+stack[-2])
            elif op == "C":
                stack.pop()  # invalidates the previous score by removing it from the stack, the previous score is the last element in the stack
            elif op == "D":
                # record a new score that is double of the previous score, the previous score being the last element
                stack.append(2*stack[-1])
            else:
                # record a new score by just append it to the stack if if it's an integer
                stack.append(int(op))
        return sum(stack)  # adds all the scores (elements) up

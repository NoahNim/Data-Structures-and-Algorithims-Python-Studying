# Given a list sample input of [0, 1, 0, 3, 12] design an algorithim that will move all of the zeros to the end of the list in place. Return the mutated list.

# pointer j equal to 0
# loop through inputted list
# check if j at input is a zero and i is not a 0, switch them if that's the case
# if j at input is not a zero then increment j by 1
# return the mutated list input

def moves_zero(input):
    j = 0
    for i in range(0, len(input)):
        if input[i] != 0 and input[j] == 0:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
        if input[j] != 0:
            j += 1
    return input


print(moves_zero([0, 1, 0, 3, 12]))

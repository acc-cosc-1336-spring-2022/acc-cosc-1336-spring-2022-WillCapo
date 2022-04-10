import dictionary

list1 = input('\nPlease enter a DNA string: ')
list2 = input('\nPlease enter a DNA string: ')
list3 = input('\nPlease enter a DNA string: ')
list4 = input('\nPlease enter a DNA string: ')

result = dictionary.get_p_distance_matrix(list1, list2, list3, list4)

print('Here is your matrix: ' + str(result))
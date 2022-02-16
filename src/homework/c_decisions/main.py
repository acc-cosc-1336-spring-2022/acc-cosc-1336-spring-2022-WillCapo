import decisions

print('Please enter a number for \'Options\'')
options = int(input())

print('Please enter a number for \'Total\' (NOTE: Number must be larger than \'Options\')')
total = int(input())

result = decisions.get_options_ratio(options, total)
strResult = str(result)

print('The rating is ' + strResult + ' which is ' + decisions.get_faculty_rating(result))
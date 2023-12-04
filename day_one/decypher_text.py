file_path = 'C:\\Users\\bryan\\Christmas_Challenges\\day_one\\dayone_1.txt'

import re

def numbers_in_string(string):
    dict = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

    matched_digits = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', string)
    digits = [dict[digit] if not digit.isdigit() else digit for digit in matched_digits]

    combined_num = int("".join([digits[n] for n in (0, -1)]))

    return combined_num

def sum_each_line(file_path):

    lines = open(file_path, "r").read().splitlines()
    calibration_values = [numbers_in_string(line) for line in lines]
    calibration_sum = sum(calibration_values)

    return calibration_sum

total_sum = sum_each_line(file_path)

print("The sum of all calibration values is:", total_sum)


#print(file_content)
#Steps to solve:
#1: Open file and read [x]
#2: Read a single line of text[x]
#3: Separate string into char[x]
#4: Check if char is a digit, if it is then save it if not then pass[x]
#5: Add numbers that are first and last of the string [x] 
#6: Do it for everysingle line of text [x]
#7: add all of them together and print [x]

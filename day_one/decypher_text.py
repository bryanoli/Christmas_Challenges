file_path = 'C:\\Users\\bryan\\Christmas_Challenges\\day_one\\dayone_1.txt'

def numbers_in_string(input_string):
    num_arr = []
    first_num = None
    last_num = None
    combine_num = ""
    for char in input_string:
        if char.isdigit():
            num_arr.append(int(char))
    if len(num_arr) != 0:
        last = len(num_arr) - 1
        first_num = num_arr[0]
        last_num = num_arr[last]
    else:
        num_arr[0] = 0
    combine_num = str(first_num) + str(last_num)
    return (int(combine_num))

num_arr = []
combine_num = 0
with open(file_path,'r') as file:
    #file_content = file.read()
    for line in file:
        combine_num = numbers_in_string(line)
        num_arr.append(combine_num)
    sum_together = sum(num_arr)
    print(sum_together)
    

#print(file_content)
#Steps to solve:
#1: Open file and read [x]
#2: Read a single line of text[x]
#3: Separate string into char[x]
#4: Check if char is a digit, if it is then save it if not then pass[x]
#5: Add numbers that are first and last of the string [x] 
#6: Do it for everysingle line of text [x]
#7: add all of them together and print [x]

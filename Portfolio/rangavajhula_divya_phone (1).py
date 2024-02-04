input_number = int(input("Please enter your phone number: "))

area_code = input_number // 10000000

prefix = input_number // 10000 % 1000

line_number = input_number % 10000

#print(prefix)
#print(area_code)
#print(line_number)

print("Phone Number: ", "(", area_code, ") ", prefix, "-", line_number )
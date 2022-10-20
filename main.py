user_num = int(input())
x = int(input())

first_div = (user_num // x)
second_div = (first_div // x)
third_div = (second_div // x)

print(first_div, second_div, third_div)

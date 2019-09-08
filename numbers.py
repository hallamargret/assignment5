
# 1) 
for num in range(10, 100):
    digit_sum=0
    num_str = str(num)
    
    for digit in num_str:
        digit_sum += int(digit)

    if digit_sum**2 == num:
        print(num)


# 2)

for number in range(1, 100):
    
    num_of_divisors = 0
    for divisor in range(1, number+1):
        if number % divisor == 0:
            num_of_divisors+=1

    if num_of_divisors == 10:
        print(number)


number=int(input())
a=str(number)
first_digit=int(a[0])
second_digit=int(a[1])
third_digit=int(a[2])
fourth_digit=int(a[3])
sum_of_cubes=(first_digit**4)+(second_digit**4)+(third_digit**4)+(fourth_digit**4)
is_armstrong=sum_of_cubes==number
if is_armstrong:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

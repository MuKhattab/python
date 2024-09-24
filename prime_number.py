def prime(num):
    prime_num=True
    for i in range (2, num):
        if num % i == 0:
            prime_num=False
    if prime_num:
        print(f"the number {num} is prime number")
    else:
        print(f"the number {num} is not prime number")

num_sample=int(input("Enter the number you want to check if prime or not:"))
prime(num_sample)
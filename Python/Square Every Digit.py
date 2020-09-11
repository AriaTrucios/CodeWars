def square_digits(num):
    list = [int(d)**2 for d in str(num)]
    result = int ("".join(map(str, list)))
    print(result)

square_digits(9119)
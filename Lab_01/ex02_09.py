def check_snt(n):
    if n<1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
         return False
    return True
number = int(input("Nhập vào số cần check: "))
if check_snt(number):
    print(number,"là snt.")
else:
    print(number, "không phải snt.")
def daonguoc_list(lst):
    return lst[::-1]
input_list = input("Nhap danh sach cac so, cach nhau dau phay: ")
numbers = list(map(int, input_list.split(',')))
list_daonguoc = daonguoc_list(numbers) 
print("List sau khi sao nguoc:", list_daonguoc)
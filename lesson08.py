# Tạo mảng các số nguyên
arr = [3, 15, 20, 90, 10,20,30,40]
# Duyệt qua các phần tử và in ra các phần tử chia hết cho 5 và 
print("Các phần tử chia hết cho 5 và 3:")
for i in range(len(arr)):
    if arr[i] % 5 == 0 and arr[i] % 3 == 0:
        print(arr[i])

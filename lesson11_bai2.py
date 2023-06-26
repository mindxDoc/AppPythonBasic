s = input("Nhập vào một xâu ngày tháng (dd/mm/yyyy): ")


# Thay thế '/' bằng ' ngày '
result = "Ngày "  + s
# Thay thế '/' tiếp theo bằng ' tháng '
result = result.replace('/', ' tháng ', 1)
# Thay thế '/' cuối cùng bằng ' năm '
result = result.replace('/', ' năm ')


print(result)
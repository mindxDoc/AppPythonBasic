shopping_cart = []

while True:
    print("1. Xem Giỏ Hàng")
    print("2. Thêm vào Giỏ Hàng")
    print("3. Cập nhật Giỏ Hàng")
    print("4. Xóa khỏi Giỏ Hàng")
    print("5. Thoát")
    choice = input("Nhập lựa chọn của bạn (1-5): ")

    if choice == "1":
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn:")
            for item in shopping_cart:
                print(item)
    elif choice == "2":
        item = input("Nhập mặt hàng bạn muốn thêm vào giỏ hàng: ")
        shopping_cart.append(item)
        print(f"{item} đã được thêm vào giỏ hàng của bạn.")
    elif choice == "3":
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn:")
            for index, item in enumerate(shopping_cart):
                print(f"{index}. {item}")
            item_index = int(
                input("Nhập chỉ mục của mặt hàng bạn muốn cập nhật: "))
            if item_index >= 0 and item_index < len(shopping_cart):
                new_item = input("Nhập mặt hàng mới: ")
                shopping_cart[item_index] = new_item
                print("Giỏ hàng của bạn đã được cập nhật.")
            else:
                print("Chỉ mục mặt hàng không hợp lệ.")
    elif choice == "4":
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn:")
            for index, item in enumerate(shopping_cart):
                print(f"{index}. {item}")
            item_index = int(input("Nhập chỉ mục của mặt hàng bạn muốn xóa: "))
            if item_index >= 0 and item_index < len(shopping_cart):
                deleted_item = shopping_cart.pop(item_index)
                print(f"{deleted_item} đã được xóa khỏi giỏ hàng của bạn.")
            else:
                print("Mặt hàng không hợp lệ.")
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

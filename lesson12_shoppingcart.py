def print_product_list(product_list):
    print("=========MENU========")
    for i in range(len(product_list)):
        print(f"{i + 1}. {product_list[i]}")
    print("====================")

def print_shopping_cart(shopping_cart):
    if not shopping_cart:
        print("Giỏ hàng của bạn đang trống.")
    else:
        print("Các mặt hàng trong giỏ hàng của bạn:")
        for i in range(len(shopping_cart)):
            print(f"{i + 1}. {shopping_cart[i]}")

def add_to_cart(product_list, shopping_cart):
    print("Danh sách sản phẩm:")
    print_product_list(product_list)
    item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn thêm vào giỏ hàng: ")) - 1
    if item_index >= 0 and item_index < len(product_list):
        selected_item = product_list[item_index]
        shopping_cart.append(selected_item)
        print(f"{selected_item} đã được thêm vào giỏ hàng của bạn.")
    else:
        print("Chỉ mục sản phẩm không hợp lệ.")

def remove_from_cart(shopping_cart):
    if not shopping_cart:
        print("Giỏ hàng của bạn đang trống.")
    else:
        print("Các mặt hàng trong giỏ hàng của bạn:")
        print_shopping_cart(shopping_cart)
        item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn xóa khỏi giỏ hàng: ")) - 1
        if item_index >= 0 and item_index < len(shopping_cart):
            deleted_item = shopping_cart.pop(item_index)
            print(f"{deleted_item} đã được xóa khỏi giỏ hàng của bạn.")
        else:
            print("Chỉ mục sản phẩm không hợp lệ.")

def main():
    product_list = ["Quần", "Áo", "Rau, củ", "Thịt", "Cá", "Gạo"]
    shopping_cart = []

    while True:
        print("==========SHOPPING CART==========")
        print("1. Xem danh sách sản phẩm")
        print("2. Xem giỏ hàng")
        print("3. Thêm sản phẩm vào giỏ hàng")
        print("4. Xóa sản phẩm khỏi giỏ hàng")
        print("5. Thoát")
        choice = input("Nhập lựa chọn của bạn (1-5): ")

        if choice == "1":
            print_product_list(product_list)
        elif choice == "2":
            print_shopping_cart(shopping_cart)
        elif choice == "3":
            add_to_cart(product_list, shopping_cart)
        elif choice == "4":
            remove_from_cart(shopping_cart)
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

main()

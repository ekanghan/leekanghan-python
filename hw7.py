shopping_bag = []
count = {}

print("[구입]")

while True:
    item = input("상품명? ")
    if item == "":
        break
    name = input("수량은? ")
    shopping_bag.append(item)
    count[item] = name
    print(f"장바구니에 {item} {name}개가 담겼습니다.")
    print()

print()
print(f">>>장바구니 보기:{count}")
print()
print("[검색]")
search = input(f"장바구니에서 확인하고자 하는 상품은? ")
print(f'{search}은(는) {count[search]}개 담겨 있습니다.')

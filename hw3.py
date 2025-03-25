
def get_fixed_price(price):
   p = int(price/(1-(exchange_rate/100)))
   return p

def main():
   global exchange_rate
   exchange_rate=(int(input('할인율은? ')))
   a_price = int(input('A 상품의 할인된 가격은? '))
   b_price = int(input('B 상품의 할인된 가격은? '))
   print(f'A 상품의 정가는 {get_fixed_price(a_price)} 원')
   print(f'B 상품의 정가는 {get_fixed_price(b_price)} 원')

main()
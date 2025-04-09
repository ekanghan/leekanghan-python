def read_single_digit(digit):
    한글숫자 = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    print(한글숫자[digit], end=' ')

def read_number(number):
    if number >= 100:
        read_single_digit(number // 100)         
        read_single_digit((number % 100) // 10)     
        read_single_digit(number % 10)              
    elif number >= 10:
        read_single_digit(number // 10)
        read_single_digit(number % 10)
    else:
        read_single_digit(number)

num = int(input("세 자리 정수 입력: "))
read_number(num)

def exchange(a):
    b = a//500
    c = (a%500)//100
    d = ((a%500)%100)//50
    e = (((a%500)%100)%50)//10
    print(f'500원 동전의 개수: {b}\n100원 동전의 개수: {c}\n50원 동전의 개수: {d}\n10원 동전의 개수: {e}')


def get_integer(prompt):
    n = int(input(prompt))
    return n


x=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(x)

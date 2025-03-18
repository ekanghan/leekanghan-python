def get_radius(prompt):
  r = int(input(prompt))
  return r

x=get_radius('넓이를 구하고자 하는 원의 반지름은? ')

def get_circle_area(x):
  a = 3.14*x*x
  return a
result=get_circle_area(x)
print("반지름",str(x) + "인","원의 넓이 =","3.14","x",x,"x",x,"=",result)

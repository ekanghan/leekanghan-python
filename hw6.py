def gugudan():
    for s in [2,6]:
        for i in range(1, 10):
            for dan in range(s, s + 4):
                print(f'{dan} x {i} = {dan * i:2d}', end='\t')
            print()
        print()


gugudan()

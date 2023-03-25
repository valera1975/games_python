# импортируем необходимый модуль и задаем глобальные переменные
import random
cow = 0
bk = 0
step = 0


# генерим код, котрый будем угадывать
code = []

while len(code) < 4:
#for i in range(0,4):
    a = random.randrange(10)
    if a not in code:
        code.append(a)
#        print(a)

# Вступительное слово и правила
print('Я загадал код из 4-х цифр')
print('Попробуй угадать!')
print('##################')
print('цифры вводи через пробел')
print('bk - правильная цифра на правильном месте, cow - правильная цифра')

# print(code) # for debag

# сравниваем введенную комбинацию с загаданным кодом
while bk != 4:
    answer = [int(s) for s in input('Ваш вариант: ').split()]

    #print(code)
    #print(answer)
    bk = 0
    cow = 0

    for q in range (4):
        for j in range (4):
#            print(answer[j],';',j,' | ',code[q],';',q)  # for debag
            if answer[j] == code[q] and j == q:
                bk += 1
                break
            elif answer[j] == code[q] and j != q:
                cow += 1
                #break
    step += 1
#    print('bk = ', bk, 'cow = ', cow)
    print(bk,' bk; ',cow,' cow')

print('Вы угадали код за', step, 'попыток. Поздравляю!!!')
#def make_code():
#    for i in range (0, 4):
#        new_el = random.randrange(10)
#        code.append(new_el)
#        print (code)
#    return(code)

#print('code is ', code)

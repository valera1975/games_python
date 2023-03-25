# Это игра: из колоды 52 карты верхняя открывается.
# Игрок должен сказать какая будет следующая карта - выше или ниже по рангу
# Если игрок угадывает, получает 20 очков, если ошибается - списывает 15. На
# старте каждый игрок имеет 50 очков

# HigherOrLower
import random

# Задаем константы карт (масти - первый кортеж, ранг - второй кортеж)
# НО! тут нет третьего важного параметра - value - 'веса карты'

SUIT_TUPLES = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RUNK_TUPLES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9',
'10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Функция, которая достает карту из колоды. В качестве параметра испльзуется
# список (колода)

def getCard(deckListIn):
    thisCard = deckListIn.pop() # метод pop достает из списка последний
                                # элемент и удаляет его из списка
    return thisCard

# Эта функция возвращает перемешанную копию колоды, переданной на вход в
# качестве параметра. И похоже, что функция эта рекурсивная (1 раз)

def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # в deckListOut передаем копию колоды
                                    # deckListIn
    random.shuffle(deckListOut)
    return deckListOut

# Основной код

print('Добро пожаловать в Higher Or Lower.')
print('Вам необходимо угадать будет ли следующая карта выше или ниже текущей открытой карты')
print('Правильный ответ даст вам 20 очков, неверный ответ спишет 15.')
print('В начале игры у Вас 50 очков')
print()

score = 50

# 1
# Сформируем полную колоду из 52 карт. У каждой карты есть параметры: масть,
# ранг и вес

startingDeckList = [] # Объявили список, который будет полной колодой

for suit in SUIT_TUPLES:
    for thisValue, rank in enumerate(RUNK_TUPLES):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1} # еслии бы
        # тут не было +1, Туз весил бы 0. а осттальные карты на единицу меньше
        # их номинала
        startingDeckList.append(cardDict) # в этом листе живет колода 52 карты

# 2
# Начинаем игру. Для этого "перемешаем колоду" и выберем "верхнюю карту"
#
while True: # обеспечиваем возможность играть больше одного раза
    print()
    gameDeckList = shuffle(startingDeckList)  # перемешали колоду
    currentCardDict = getCard(gameDeckList)   # выбрали карту (и убрали из колоды)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Открытая карта: ', currentCardRank + ' ' + currentCardSuit)
    print()

# 3
# Этот блок кода обеспечивает ввод выбора игрока (выше или ниже)

    for cardNumber in range(0, NCARDS):
        answer = input('Следующая карта будет выше (h) или ниже (l)? ')
# тут я сократил код описания ввода выбора игрока
        answer = answer.casefold() # если ввели заглавные буквы, преобразует в строчные

# Этот кусочек кода проверяет валидность введенного игроком выбора.
# Игрок вынужден делать выбор, пока не воспользуется правильными символами h || l

        while not ((answer == 'h') or (answer == 'l')):
            answer = input('Вы сделали неправильный выбор. Нажмите (h) или (l): ')
            answer = answer.casefold()
            print(answer)

# 4
# Получаем следующую карту из колоды, чтобы сравнить ее с открытой

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuit = nextCardDict['suit']
        print('Следующая карта: ', nextCardRank + ' ' + nextCardSuit)

# 5
# производим сравнение открытой и следующей карты и сравниваем с ответом
# игрока, чтобы расчитать его очки (угадал или нет)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Вы угадали, она выше')
                score += 20
            else:
                print('Сожалею, она не выше')
                score -= 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('Вы угадали, она ниже')
                score += 20
            else:
                print('Сожалею, она не ниже')
                score -= 15

        print('Ваш счет', score)
        print()

        curentCardRank = nextCardRank
        currentCardSuit = nextCardSuit
        currentCardValue = nextCardValue

    goAgain = input('Чтобы продолжить игру, нажмите ENTER, или "q" чтобы выйти: ')
    goAgain = goAgain.casefold()

    if goAgain == 'q':
        break

print('Хорошо, до встречи!')

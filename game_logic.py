from words import _WORDS
import random


class Win_Lose():
    ''' Класс для управления игрой. Запуск, выбор слова, проверка буквы, подсчет очков, остановка.
    по умолчанию у пользователя 3 попытки, при инициализации класса можно поменять их количество
    через аргумент chances = int '''

    def __init__(self):
        self.__chances = 0
        self.__is_game_started = False
        self.__fails = 0
        self.__corrects = 0
        self.__CURRENT_WORD = ''
        self.guessed = []
        self.current_word_listed = []

    def letters_counter(self):
        return len(self.__CURRENT_WORD)

    def get_chances(self):
        """ Получаем количество попыток """
        try:
            chances_input = input(
                'Number of tries? (leave blank for number of letters in word): ')
            self.__chances = int(
                chances_input) if (chances_input and int(chances_input) > 0) else self.letters_counter()
        except ValueError:
            print('Enter POSITIVE INTEGER NUMBER of tries..')
            self.get_chances()

    def start_game(self):
        start_message = input('Want to start a game? Y/N: ')

        if start_message.capitalize() == 'Y':

            """ Если начинаем игру - выбираем слово, зашифровываем, меняем статус игры и возвращаем шифрованное слово """

            self.__CURRENT_WORD = random.choice(_WORDS)
            self.current_word_listed = (self.__CURRENT_WORD)
            self.guessed = [i.replace(i, '_') for i in self.__CURRENT_WORD]
            self.get_chances()
            self.__is_game_started = True
            self.game_process()
        else:
            return print('See ya!')

    def win(self):
        self.__is_game_started = False
        return print('All right, u win!')

    def lose(self):
        self.__is_game_started = False
        return print('Oh no, u lose!')

    def decipher(self, letter):
        """ Бежит по слову и проверяет на вхождения буквы. Меняет _ в cipher на букву.
        Вызывается в self.check_letter при введении правильной буквы """
        for i, l in enumerate(self.current_word_listed):
            if l.lower() == letter.lower():
                self.guessed[i] = l

    def check_letter(self, letter, word):
        if letter in self.guessed:
            # Уже отгадано
            return print(f'You already guessed letter {letter} ')
        if letter in word:
            # УГАДАЛ
            # Количество победных очков увеличивается на количество отгаданных букв
            self.__corrects += word.count(letter)
            self.decipher(letter)
            return print('Right! ')

        else:
            # НЕ УГАДАЛ
            self.__chances -= 1
            return print('Wrong! ')

    def guess_process(self, letter):
        if self.__is_game_started:
            self.check_letter(letter, self.__CURRENT_WORD)
            if self.__chances <= 0:
                return self.lose()
            if self.__corrects == self.letters_counter():
                return self.win()
        else:
            self.start_game()

    def game_process(self):
        # игра идёт пока __is_game_started = True. В код передаётся только первый введённый символ.

        while self.__is_game_started:
            guess = input(
                f'{" ".join(self.guessed)} choose a letter!: Tries left {self.__chances} ')
            if len(guess) > 1:
                print('Hey! Only one letter per try! I will get first letter as answer')
            if guess:
                self.guess_process(guess[0].lower())

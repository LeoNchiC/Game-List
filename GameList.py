import pickle
from colorama import init, Fore, Style
import random


init()

class Game:
    def __init__(self, title):
        self.title = title
        self.completed = False

class GameList:
    def __init__(self):
        self.games = []

    def add_game(self, title):
        game = Game(title)
        self.games.append(game)
        print(Fore.GREEN + f"Игра '{title}' добавлена в список."+ Style.RESET_ALL)

    def mark_completed(self, title):
        for game in self.games:
            if game.title == title:
                game.completed = True
                print(Fore.GREEN + f"Игра '{title}' отмечена как пройденная."+ Style.RESET_ALL)
                return
        print(Fore.RED + f"Игра '{title}' не найдена в списке." + Style.RESET_ALL)

    def remove_game(self, title):
        for game in self.games:
            if game.title == title:
                self.games.remove(game)
                print(Fore.LIGHTYELLOW_EX + f"Игра '{title}' удалена из списка." + Style.RESET_ALL)
                return
        print(Fore.RED + f"Игра '{title}' не найдена в списке." + Style.RESET_ALL)

    def get_random_uncompleted_game(self):
        uncompleted_games = [game for game in self.games if not game.completed]
        if not uncompleted_games:
            return None  
        return random.choice(uncompleted_games)

    def display_list(self):
        if not self.games:
            print(Fore.LIGHTBLACK_EX + "Список игр пуст." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Список игр:" + Style.RESET_ALL)
            for game in self.games:
                status = Fore.LIGHTGREEN_EX + "Пройдено" + Style.RESET_ALL if game.completed else Fore.LIGHTRED_EX +  "Не пройдено" + Style.RESET_ALL
                print(f"- {game.title} ({status})")

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.games, file)
        print(Fore.GREEN + "Список игр сохранен." + Style.RESET_ALL)

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                self.games = pickle.load(file)
            print(Fore.GREEN + "Список игр загружен." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "Файл со списком игр не найден." + Style.RESET_ALL)

def main():
    game_list = GameList()

    filename = "gamelist.dat"
    game_list.load_from_file(filename)

    while True:
        print(Fore.BLUE + "\nВыберите действие:" + Style.RESET_ALL)
        print("1. Добавить игру")
        print("2. Отметить игру как пройденную")
        print("3. Показать список игр")
        print("4. Удалить игру из списка")
        print("5. Выбрать рандомную игру")
        print("6. Сохранить и выйти")

        choice = input(Fore.BLUE + "Введите номер действия: " + Style.RESET_ALL)

        if choice == "1":
            title = input("Введите название игры: ")
            game_list.add_game(title)

        elif choice == "2":
            title = input("Введите название игры, которую хотите отметить как пройденную: ")
            game_list.mark_completed(title)

        elif choice == "3":
            game_list.display_list()

        elif choice == "4":
            title = input("Введите название игры, которую хотите удалить: ")
            game_list.remove_game(title)

        elif choice == "5":
            uncompleted_game = game_list.get_random_uncompleted_game()
            if uncompleted_game:
                print(Fore.CYAN + "Выбрана случайная не пройденная игра: " + Style.RESET_ALL + Fore.MAGENTA + f"{uncompleted_game.title}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "Все игры пройдены или список пуст." + Style.RESET_ALL)

        elif choice == "6":
            game_list.save_to_file(filename)
            print(Fore.MAGENTA + "Программа завершена." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Некорректный ввод. Пожалуйста, выберите действие из списка." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
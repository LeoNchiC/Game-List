import pickle

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

    def mark_completed(self, title):
        for game in self.games:
            if game.title == title:
                game.completed = True
                print(f"Игра '{title}' отмечена как пройденная.")
                return
        print(f"Игра '{title}' не найдена в списке.")

    def remove_game(self, title):
        for game in self.games:
            if game.title == title:
                self.games.remove(game)
                print(f"Игра '{title}' удалена из списка.")
                return
        print(f"Игра '{title}' не найдена в списке.")

    def display_list(self):
        if not self.games:
            print("Список игр пуст.")
        else:
            print("Список игр:")
            for game in self.games:
                status = "Пройдено" if game.completed else "Не пройдено"
                print(f"- {game.title} ({status})")

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.games, file)
        print("Список игр сохранен.")

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                self.games = pickle.load(file)
            print("Список игр загружен.")
        except FileNotFoundError:
            print("Файл со списком игр не найден.")

def main():
    game_list = GameList()

    filename = "gamelist.dat"
    game_list.load_from_file(filename)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить игру")
        print("2. Отметить игру как пройденную")
        print("3. Показать список игр")
        print("4. Удалить игру из списка")
        print("5. Сохранить и выйти")

        choice = input("Введите номер действия: ")

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
            game_list.save_to_file(filename)
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()

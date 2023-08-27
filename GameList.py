import pickle
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from colorama import init, Fore, Style

init()

class Game:
    def __init__(self, title):
        self.title = title
        self.completed = False

class GameList:
    def __init__(self):
        self.games = []

    def add_game(self, title):
        self.games.append(Game(title))

    def mark_completed(self, title):
        for game in self.games:
            if game.title == title:
                game.completed = True
                print(Fore.GREEN + f"Игра '{title}' отмечена как пройденная." + Style.RESET_ALL)
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

    def sort_by_status(self):
        sorted_games = sorted(self.games, key=lambda game: (game.completed, game.title))
        return sorted_games

    def display_list(self):
        if not self.games:
            print(Fore.LIGHTBLACK_EX + "Список игр пуст." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Список игр (по статусу):" + Style.RESET_ALL)
            sorted_games = self.sort_by_status()
            for game in sorted_games:
                status = Fore.LIGHTGREEN_EX + "Пройдено" + Style.RESET_ALL if game.completed else Fore.LIGHTRED_EX + "Не пройдено" + Style.RESET_ALL
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

    def sort_by_title(self):
        sorted_games = sorted(self.games, key=lambda game: game.title.lower())
        return sorted_games

class GameListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер списка игр")

        self.game_list = GameList()

        self.filename = "gamelist.dat"
        self.game_list.load_from_file(self.filename)

        self.label = tk.Label(root, text="Менеджер списка игр", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Добавить игру", command=self.add_game)
        self.add_button.pack()

        self.mark_button = tk.Button(root, text="Отметить как пройденную", command=self.mark_completed)
        self.mark_button.pack()

        self.show_button = tk.Button(root, text="Показать список", command=self.display_list)
        self.show_button.pack()

        self.random_button = tk.Button(root, text="Случайная непройденная игра", command=self.random_uncompleted_game)
        self.random_button.pack()

        self.quit_button = tk.Button(root, text="Сохранить и выйти", command=self.save_and_quit)
        self.quit_button.pack()

    def add_game(self):
        title = simpledialog.askstring("Добавить игру", "Введите название игры:")
        if title:
            self.game_list.add_game(title)

    def mark_completed(self):
        title = simpledialog.askstring("Отметить как пройденную", "Введите название игры, чтобы отметить как пройденную:")
        if title:
            self.game_list.mark_completed(title)

    def display_list(self):
        list_window = tk.Toplevel(self.root)
        list_window.title("Список игр")
        list_text = tk.Text(list_window)
        list_text.pack()

        sorted_games = self.game_list.sort_by_title()
        for game in sorted_games:
            status = "Пройдено" if game.completed else "Не пройдено"
            list_text.insert(tk.END, f"- {game.title} ({status})\n")

    def random_uncompleted_game(self):
        uncompleted_game = self.game_list.get_random_uncompleted_game()
        if uncompleted_game:
            messagebox.showinfo("Случайная непройденная игра", f"Случайная непройденная игра: {uncompleted_game.title}")
        else:
            messagebox.showinfo("Случайная непройденная игра", "Все игры пройдены или список пуст.")

    def save_and_quit(self):
        self.game_list.save_to_file(self.filename)
        messagebox.showinfo("Сохранение и выход", "Список игр сохранен.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameListApp(root)
    root.mainloop()

import os

class Menu:
    menu_list = ["Press for adding searched jobs tags",
                 "Press for listing search tags",
                 "Press to update offers internal memory",
                 "Press to export offers to exel file",
                 "Press to add mailing and specify hour of automatic every day alerts",
                 "backup data to txt",
                 "load data from txt",
                 "exit"]

    @classmethod
    def show_menu(self):
        for idx,menu_item in enumerate(self.menu_list):
            print(f"{idx+1}. {menu_item} ")

    @classmethod
    def get_input(self):
        while True:
            try:
                choice_nr=int(input("You menu choice is : "))
                if not(len(self.menu_list) >= choice_nr >= 1):
                    raise ValueError
                break
            except:
                print(f"wrong choice must be number from 1 to {len(self.menu_list)}")
        return choice_nr

    @classmethod
    def clear_menu(self):
        cls = lambda: print('\n' * 100)
        cls()

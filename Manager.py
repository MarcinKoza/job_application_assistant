import Menu
import Jobs

class Manager:

    @classmethod
    def start_program(self):
        Menu.Menu.clear_menu()
        Menu.Menu.show_menu()
        choice = Menu.Menu.get_input()
        if choice == 1:
            my_tag=input("input your job tag and press enter : ")
            Jobs.Jobs.add_job_tag(my_tag)
        elif choice == 2:
            Jobs.Jobs.get_all_tags()

        elif choice == 3:
            Jobs.Jobs.get_jobs_from_pracujpl()
        elif choice == 4:
            Jobs.Jobs.export_to_xml()
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
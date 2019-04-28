from .show_info import ShowInfo
from .work_book import Workbook
from .colour import Colour
from .split_sheet import SplitSheet
from .banner import banner, description

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import os
import click


class FrameWork:
    def __init__(self, compy, workbook):
        self.compy_origial = compy
        self.compy_script = compy
        self.workbook = Workbook(workbook)
        self.constant_tab_words = [
            "show", "compy", "info", "current", "headers", "select", "unique", "from",
            "sheet", "remove", "where", "is", "set", "os", "windows", "linux", "save",
            "back", "help", "!", "exit", "extension"
        ]
        self.os = "linux"
        self.current_sheet = 0
        self.dynamic_tab_words = self.update_tab()
        #ShowInfo(self.compy_origial, self.compy_script, self.workbook).display_info()
        self.command()

    def update_tab(self):
        values = []
        for sheet in self.workbook.sheets:
            for headings in sheet.columns.values:
                values.append(headings)
        return list(set(values) | set(self.constant_tab_words))

    def command(self):
        main_tab = WordCompleter(self.dynamic_tab_words, ignore_case=True)
        first = True
        try:
            while 1:
                print()
                if not first:
                    banner()
                first = True
                self.script_info()
                self.show_header_compy()
                self.show_header_sheet()
                print(Colour.YELLOW + "Currently selected sheet " + str(self.current_sheet) + "->" + Colour.END)
                user_input = prompt("",
                                    history=FileHistory('history.txt'),
                                    auto_suggest=AutoSuggestFromHistory(),
                                    completer=main_tab,
                                    )
                self.clear()
                banner()
                description()
                print()
                if user_input == "show compy":
                    self.show_compy()

                elif user_input == "":
                    continue

                elif user_input == "show sheets":
                    self.show_sheets()

                elif user_input == "show info":
                    ShowInfo(self.compy_origial, self.compy_script, self.workbook.sheets).display_info()

                elif user_input == "show sheet":
                    self. show_current_sheet()

                elif user_input == "show extension compy" or user_input == "show extensions compy":
                    self.show_extension_compy()

                elif user_input == "show compy extension" or user_input == "show compy extensions":
                    self.show_extension_compy()

                elif "drop sheet" in user_input:
                    self.drop_sheet(user_input)

                elif "select sheet" in user_input:
                    self.select_sheet(user_input)

                elif "select unique from sheet" in user_input:
                    self.select_unique_from_sheet(user_input)

                elif "select unique from compy" in user_input:
                    self.select_unique_from_compy(user_input)

                elif "select empty from sheet" in user_input:
                    self.select_empty_sheet(user_input)

                elif "remove where sheet " in user_input and "is" in user_input:
                    self.remove_where_sheet()

                elif "remove where compy " in user_input and "is" in user_input:
                    self.remove_where_compy()

                elif "set os windows" in user_input:
                    self.set_os_windows()

                elif "set os linux" in user_input:
                    self.set_os_linux()

                elif "save" in user_input:
                    self.save()

                elif "split sheet" in user_input:
                    self.split_sheet()

                elif "back" in user_input:
                    self.back()

                elif "help" in user_input:
                    self.help()

                elif "exit" in user_input:
                    print("Exiting")
                    exit()
                elif user_input[0] == "!":
                    self.linux_cmd(user_input)
                else:
                    print("Command not found")

        except KeyboardInterrupt:
            print("\nExiting")

    def show_compy(self):
        click.echo_via_pager(self.compy_script.to_string())
        print(self.compy_script.head().to_string())

    def show_sheets(self):
        self.workbook.show_sheets()

    def show_current_sheet(self):
        self.workbook.show_sheet(self.current_sheet)

    def show_header_compy(self):
        headers = self.compy_script.columns.values
        print(Colour.GREEN + "Compy Headers: " + Colour.END + Colour.DIM + ", ".join(headers) + Colour.END)

    def show_header_sheet(self):
        headers = self.workbook.sheets[self.current_sheet].columns.values
        print(Colour.GREEN + "Sheet Headers: " + Colour.END + Colour.DIM + ", ".join(headers) + Colour.END)

    def show_extension_compy(self):
        try:
            extensions = self.compy_script.groupby(["Extension"]).count()
            print(extensions["Name"])
        except KeyError as e:
            print("Dataframe seems to be corrupted")
            print(str(e))
            print(self.compy_script)
            return False

    def drop_sheet(self, user_input):
        try:
            sheet_number = int(user_input.lower().split("drop sheet")[1])
            if self.workbook.sheet_len != 1:
                self.workbook.pop_sheet(sheet_number)
                print("Sheet dropped")
                if sheet_number <= self.current_sheet:
                    if sheet_number != 0:
                        self.current_sheet -= 1
            else:
                print(Colour.UNDERLINE + "WARNING: Cannot drop sheet when there is only one sheet left!!" + Colour.END)
        except (IndexError, ValueError):
            print("usage: drop sheet <id>")
            print("use: 'show sheets' to find the <id>")
            return False

    def select_sheet(self, user_input):
        try:
            number = int(user_input.lower().split("sheet")[1])
            if 0 <= number <= self.workbook.sheet_len:
                self.current_sheet = number
            else:
                print("Worksheet available: " + str(self.workbook.sheet_len))
        except TypeError:
            print("select sheet <sheet number>")

    def select_unique_from_sheet(self, user_input):
        col = user_input.split("sheet ")[1]
        sheet = self.workbook.sheets[self.current_sheet]
        try:
            result = list(set(sheet[col]))
            for i in result:
                print('"' + str(i) + '"' + Colour.DIM +
                      "\n\tselect from sheet where " + col + " is \"" + str(i) + "\"" + Colour.END + "\n")
        except KeyError as e:
            print(str(e) + " not found, have you selected the right sheet?")
            return False

    def select_unique_from_compy(self, user_input):
        col = user_input.split("compy ")[1]
        sheet = self.compy_script
        try:
            result = list(set(sheet[col]))
            for i in result:
                print('"' + str(i) + '"' + Colour.DIM +
                      "\n\tselect from compy where " + col + " is \"" + str(i) + "\"" + Colour.END + "\n")
        except KeyError as e:
            print(str(e) + " not found, have you selected the right sheet?")
            return False

    def select_empty_sheet(self, user_input):
        #user_input = user_input.split("from sheet")[1]
        try:
            col = user_input.split('"')[1]
        except IndexError:
            print("Usage: select empty from sheet \"column\"      print all rows where the column is empty/NaN")


    def remove_where_sheet(self):
        pass

    def remove_where_compy(self):
        pass

    def set_os_windows(self):
        print("OS has been set to Windows")
        self.os = "windows"

    def set_os_linux(self):
        print("OS has been set to Windows")
        self.os = "linux"

    def clear(self):
        print("\n" * 80)

    def save(self):
        pass

    def split_sheet(self):
        current_sheet = self.workbook.sheets[self.current_sheet]
        new = SplitSheet(current_sheet)

    def back(self):
        pass

    def help(self):
        with open("other/commands", "r") as f:
            for line in f.readlines():
                new = line.strip("\n")
                try:
                    new = new.replace("<", Colour.YELLOW + "<")
                    new = new.replace(">", ">" + Colour.END)
                    if new[0] == "*":
                        print(Colour.RED + new[1:] + Colour.END)
                    elif new[0] == "#":
                        print(Colour.YELLOW + new[1:] + Colour.END)
                    elif new[0] + "£":
                        print("\t" + new[1:])
                    else:
                        print("\n")
                except IndexError:
                    pass

    def linux_cmd(self, user_input):
        os.system(user_input[1:])

    def banner(self, reverse=True):
        if reverse:
            print("             />__________________________________")
            print("[]###########[]___________________________________>")
            print("             \\>")
        else:
            print(" _________________________________<\\\\")
            print("<__________________________________[]###########[]")
            print("                                 <//")

    def script_info(self):
        og_len = len(self.compy_origial)
        delete_len = len(self.compy_script)
        diff = delete_len - og_len

        print(Colour.RED + "Compy original length: " + Colour.END + str(og_len))
        print(Colour.RED + "Compy new length: " + Colour.END + str(delete_len))
        print(Colour.RED + "Files removed from delete script: " + Colour.END + str(diff))

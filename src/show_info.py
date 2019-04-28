from .colour import Colour
class ShowInfo:
    def __init__(self, compy_original, compy_script, workbook):
        """
        Displays information about the project delete script
        :param compy_original: Original delete dataframe found by compy
        :param compy_script: Updated delete dataframe
        :param workbook: List of work sheets containing dependencies
        """
        self.compy_original = compy_original
        self.compy_script = compy_script
        self.workbook = workbook
        self.workbook_len = len(workbook)

    def display_info(self):
        self.display_info_workbook()
        self.display_info_original()
        self.display_info_script()
        self.display_info_compy()

    def display_info_workbook(self):
        print()
        print("Number of Worksheets: " + str(self.workbook_len) + "\n")
        for sheet in range(self.workbook_len):
            self.heading("Worksheet: " + str(sheet))
            self.line()
            print("Worksheet has " + str(len(self.workbook[sheet])) + " rows")
            print("Worksheet has the following headers:")
            self.print_col_values(self.workbook[sheet])
            self.line()
            print(self.workbook[sheet].head(5).to_string() + "\n")
            print("\n"*2)

    def display_info_original(self):
        pass

    def display_info_script(self):
        pass

    def display_info_compy(self):
        self.heading("Compy")
        self.line()
        print("Compy has the following headers:")
        self.print_col_values(self.compy_original)
        self.line()
        og_len = len(self.compy_original)
        script_len = len(self.compy_script)
        print("Original compy results: " + str(og_len))
        print("Delete script results: " + str(script_len))

    @staticmethod
    def print_col_values(df):
        x = 0
        for i in df.columns.values:
            print("\t" + "[" + str(x) + "] " + i)
            x += 1

    @staticmethod
    def heading(text):
        print(Colour.RED + text + Colour.END)

    @staticmethod
    def line():
        print("-"*65)

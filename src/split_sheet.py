from .colour import Colour
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter


class SplitSheet:
	def __init__(self, df):
		self.sheet = df
		self.headers = df.columns.values
		self.failed = False
		self.column = self.find_column()
		self.split_paths()

	def find_column(self):
		if len(self.headers != 0):
			for i in range(0, len(self.headers)):
				example = str(list(self.sheet[self.headers[i]])[1])
				print(Colour.RED + "[" + str(i + 1) + "]\t" + Colour.END + self.headers[i] + "\n\t: " + Colour.YELLOW + example + "\n" + Colour.END)
			print(Colour.RED + "[" + str(i + 2) + "]\t" + Colour.END + "Exit")
			header_position = self.get_number(1, i + 2, "Select the path column:")
			if header_position == i + 2:
				self.failed = True
				return False
			else:
				header_position -= 1

			return self.headers[header_position]

	def get_number(self, low, high, message):
		numbers = [str(x) for x in range(low, high + 1)]
		numbers_completer = WordCompleter(numbers)
		selection = prompt(message + " ", completer=numbers_completer)
		#selection = input(message + "\t")
		if selection.isdigit():
			selection = int(selection)
			if low <= selection <= high:
				return selection
		return self.get_number(low, high, message)

	def split_paths(self):
		if not self.failed:
			paths = list(self.sheet[self.column])
			os = self.find_split_char(paths)
			if os:
				current_path = paths[1]
				print("\n" + Colour.RED + os + " paths detected" + Colour.END)
				split_loc, split_char = self.user_split(current_path, os)
				self.create_new_column(split_loc, split_char)

	def find_split_char(self, paths):
		windows = 0
		unix = 0
		for path in paths:
			path = str(path)
			unix += len(path.split("/"))
			windows += len(path.split("\\"))
		if windows < unix:
			return "unix"
		elif unix < windows:
			return "windows"
		else:
			self.failed = True
			if len(paths) == 0:
				print(Colour.UNDERLINE + "There are no paths!!" + Colour.END)
			else:
				print(Colour.UNDERLINE + "Could not determine if the paths are unix or windows based!!" + Colour.END)
			return False

	def user_split(self, path, os):
		if os == "windows":
			char = "\\"
		else:
			char = "/"
		dirs = path.split(char)
		print("Select the root directory")
		for x in range(0, len(dirs)):
			split_path = dirs[x:]
			split_path = "/".join(split_path)
			print(Colour.RED + "[" + str(x + 1) + "]\t" + Colour.END + split_path)
		split_loc = self.get_number(1, len(dirs) + 2, "Select the root directory") - 1
		if split_loc == x + 2:
			self.failed = True
			return
		else:
			return split_loc, char

	def create_new_column(self, split_loc, split_char):
		print(split_loc, split_char)
		paths = list(self.sheet[self.column])
		new_paths = []
		for path in paths:
			try:
				new_path = split_char.join(path.split(split_char)[split_loc:])
			except IndexError:
				new_path = path
			new_paths.append(new_path)
		self.drop_old_column()
		self.sheet[self.column] = new_paths

	def drop_old_column(self):
		self.sheet.drop(self.column, axis=1, inplace=True)

	def get_df(self):
		return self.sheet
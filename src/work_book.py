from .colour import Colour
import click

class Workbook:
	def __init__(self, workbook):
		self.sheets = workbook
		self.sheet_len = len(workbook)

	def pop_sheet(self, number):
		if number <= self.sheet_len:
			self.sheets.pop(number)
			self.sheet_len -= 1
		else:
			self.warning("Sheet not found")


	def show_sheets(self):
		for sheet in range(self.sheet_len):
			self.heading("Work-sheet: " + str(sheet))
			print(self.sheets[sheet].head().to_string())
			print("")

	def show_sheet(self, sheet):
		click.echo_via_pager(self.sheets[sheet].to_string())
		print(self.sheets[sheet].head().to_string())
		print("")

	@staticmethod
	def heading(text):
		print(Colour.BLUE + text + Colour.END)

	@staticmethod
	def warning(text):
		print(Colour.RED + text + Colour.END)
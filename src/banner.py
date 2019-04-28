from .colour import Colour

def banner():
	print("")
	print(Colour.RED + " ██░ ██  █    ██  ▄▄▄       █     █░▓█████  ██▓    ██░ ██  ▄▄▄       ██▀███  ▓█████▄     ███▄ ▄███▓ ▒█████  ▓█████▄ ▓█████ " + Colour.END)
	print(Colour.RED + " ▓██░ ██▒ ██  ▓██▒▒████▄    ▓█░ █ ░█░▓█   ▀ ▓██▒   ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌   ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ " + Colour.END)
	print(Colour.RED + " ▒██▀▀██░▓██  ▒██░▒██  ▀█▄  ▒█░ █ ░█ ▒███   ▒██▒   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌   ▓██    ▓██░▒██░  ██▒░██   █▌▒███ " + Colour.END)
	print(Colour.RED + " ░▓█ ░██ ▓▓█  ░██░░██▄▄▄▄██ ░█░ █ ░█ ▒▓█  ▄ ░██░   ░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌   ▒██    ▒██ ▒██   ██░░▓█▄   ▌▒▓█  ▄ " + Colour.END)
	print(Colour.RED + " ░▓█▒░██▓▒▒█████▓  ▓█   ▓██▒░░██▒██▓ ░▒████▒░██░   ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▓    ▒██▒   ░██▒░ ████▓▒░░▒████▓ ░▒████▒ " + Colour.END)
	print(Colour.RED + "  ▒ ░░▒░▒░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▓░▒ ▒  ░░ ▒░ ░░▓      ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▒░   ░  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░ " + Colour.END)
	print(Colour.RED + "  ▒ ░▒░ ░░░▒░ ░ ░   ▒   ▒▒ ░  ▒ ░ ░   ░ ░  ░ ▒ ░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒    ░  ░      ░  ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░ " + Colour.END)
	print(Colour.RED + "  ░  ░░ ░ ░░░ ░ ░   ░   ▒     ░   ░     ░    ▒ ░    ░  ░░ ░  ░   ▒     ░░   ░  ░ ░  ░    ░      ░   ░ ░ ░ ▒   ░ ░  ░    ░ " + Colour.END)
	print(Colour.RED + "  ░  ░  ░   ░           ░  ░    ░       ░  ░ ░      ░  ░  ░      ░  ░   ░        ░              ░       ░ ░     ░       ░  ░ " + Colour.END)
	print(Colour.RED + "                                                                               ░                              ░ " + Colour.END)

def description():
	print("This tool is used to help stream line the creation of completeness check delete scripts")
	print("Rather than creating a unique one off script to parse Compy's output and then Huawei dependent bin list")
	print("This tool can be used to generate cross compatible delete scripts that allow you to")
	print("revert any deletions on the local machine without the need for SCP, NFT, FTP or SMB\n")
	print(Colour.YELLOW + " * No need to keep track of what has been delete and what has been restored" + Colour.END)
	print(Colour.YELLOW + " * No more LAN spraying delete scripts" + Colour.END)
	print(Colour.YELLOW + " * No more Creating one off delete scripts in your temp folder" + Colour.END)
	print(Colour.YELLOW + " * No programming knowledge needed" + Colour.END)
	print(Colour.YELLOW + " * No need to SCP files back to the local machine" + Colour.END)

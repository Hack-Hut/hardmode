from src.framework import FrameWork
from src.colour import Colour
from src.banner import banner, description
import sys
import pandas as pd
import os
import xlrd


def usage():
    print("python3 hardmode.py <dep_bin_list.excel> <compy_component_result_loc>")
    exit(-1)


def valid_csv(loc):
    if not os.path.exists(loc):
        print(Colour.UNDERLINE + "Could not find location: " + loc + Colour.END)
        exit(-1)
    try:
        return pd.read_csv(loc)
    except pd.errors.EmptyDataError:
        print(Colour.UNDERLINE + "File at location " + loc + " is empty." + Colour.END)
        exit(-1)
    except Exception as e:
        print(Colour.UNDERLINE + str(e) + Colour.END)
        exit(-1)


def valid_excel(loc, sheet):
    if not os.path.exists(loc):
        print(Colour.UNDERLINE + "Could not find location: " + loc + Colour.END)
        exit(-1)
    try:
        df = pd.read_excel(loc, sheet_name=sheet)
        return True, df
    except xlrd.biffh.XLRDError:
        print(Colour.UNDERLINE + "File at location " + loc + " does not seem to be a valid excel document." + Colour.END)
        exit(-1)
    except IndexError:
        return False, False
    except Exception as e:
        print(str(e))
        exit(-1)
    return False, False


def bye():
    print("Exiting")
    exit()


def main(excel_loc, compy_loc):
    sheet_num = 0
    workbook = []

    banner()
    description()

    print(Colour.RED + "\nStarting" + Colour.END)
    print("Hard Mode -- Generate delete scripts")
    print("Reading Compy Results: " + compy_loc)
    compy = valid_csv(compy_loc)

    print("Reading Excel Workbook: " + excel_loc)
    while True:
        status, sheet = valid_excel(excel_loc, sheet_num)
        if status:
            workbook.append(sheet)
            sheet_num += 1
        else:
            break
    print("Initialization " + Colour.RED + "Successful!\n" + Colour.END)
    FrameWork(compy, workbook)


try:
    excel = sys.argv[1]
    compy = sys.argv[2]
except IndexError:
    usage()
main(excel, compy)

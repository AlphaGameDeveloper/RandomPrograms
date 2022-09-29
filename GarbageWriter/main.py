import random
from os import path, remove
from sys import stdout

global allowedChars
allowedChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def rptUntlValid(initVal, command, minInt, maxInt):
    if initVal in range(minInt, maxInt+1):
        return initVal
    else:
        valid = False
        while valid == False:
            val = command()
            if val in range(minInt, maxInt+1):
                return val
            else:
                print("Invalid value, restarting...")
                return rptUntlValid(initVal, command, minInt, maxInt)

def writablePathInput(prompt="> "):
    p = input(prompt)
    try: 
        o = open(p, "w")
        o.close()
        remove(p)
        return p
    except FileNotFoundError as fnfe:
        print(str(fnfe) + ": Unable to write to this path.")
        return writablePathInput(prompt)

def pathInput(prompt="> "):
    p = input(prompt)
    if path.isfile(p) == True:
        return p
    else:
        print("Invalid path: " + p)
        return pathInput(prompt=prompt)

def ynInput(prompt="> "):
    yes = ["y", "yes"]
    no = ["n", "no"]

    i = input(prompt)
    if i.lower() in yes:
        return True
    elif i.lower() in no:
        return False
    else:
        print("ValueError: Invalid input.")
        return ynInput(prompt)

def intInput(prompt="> "):
    try:
        i = int(input(prompt))
        return i
    except ValueError as valerr:
        print(str(valerr) + ": Please enter a valid input.")
        return intInput(prompt)

def floatInput(prompt="> "):
    try:
        i = float(input(prompt))
        return i
    except ValueError as valerr:
        print(str(valerr) + ": Please enter a valid input.")
        return intInput(prompt)

def main():
    print("""
    Big-File Sizer,
    by AlphaGameDev

    [-- OPTIONS --]

    1 ----- Find exact file size of a file
    2 ----- Create a junk file with a specified size.

    Enter selection $
    """)
    curInpt = "-"*22+">"
    sel = rptUntlValid(intInput(curInpt), lambda:intInput(curInpt), 1, 2)
    if sel == 1:
        p = pathInput()
        size = path.getsize(p)
        print("Size = " + str(size) + " bytes.")
        print("     = " + str(size/1024) + " kilobytes")
        print("     = " + str(size/1048576) + " megabytes")
        print("     = " + str(size/1073741824) + " gigabytes")

        input("Press ENTER to continue.")
        main()
    elif sel == 2:
        print("""
        File size:
        1  ----- File size in bytes (B)
        2  ----- File size in kilobytes (KB)
        3  ----- File size in megabytes (MB)
        4  ----- File size in gigabytes (GB) <-- TAKES A LONG TIME.

        Enter selection:
        """)
        curInpt = "> "
        sel = rptUntlValid(floatInput(curInpt), lambda:floatInput(curInpt), 1, 2)
        if sel == 1:
            unit = "bytes"
            curInpt = "Please enter the file size you want, in bytes >>> "
            ogsize = floatInput(curInpt)
            size = ogsize
            print(str(ogsize) + " bytes = " + str(size) + "bytes.")
        elif sel == 2:
            unit = "kilobytes"
            curInpt = "Please enter the file size you want, in kilobytes >>> "
            ogsize = floatInput(curInpt)
            size = ogsize
            size = size * 1024
            print(str(ogsize) + " kilobytes = " + str(size) + "bytes.")
        elif sel == 3:
            unit = "megabytes"
            curInpt = "Please enter the file size you want, in megabytes >>> "
            ogsize = floatInput(curInpt)
            size = ogsize
            size = size * 1048576
            print(str(ogsize) + " megabytes = " + str(size) + "bytes.")
        elif sel == 4:
            unit = "gigabytes"
            curInpt = "Please enter the file size you want, in gigabytes >>> "
            ogsize = floatInput(curInpt)
            size = ogsize
            size = size * 1073741824
            print(str(ogsize) + " gigabytes = " + str(size) + " bytes.")
        
        print("Should the file be a garbage string? (y/n)")
        garbage = ynInput()

        print("Enter the output path:")
        pth = writablePathInput()

        print("""
Making a file with:
    Garbage = """ + str(garbage) + """.
    OGSize  = """ + str(ogsize) + " " + unit + """.
    
    Size    = """ + str(size) + """ bytes.
    OutPath = """ + pth + """.
    OK to continue? (y/n)
        """)
    cont = ynInput("> ")
    if cont == False:
        print("Exiting...")
        input("ENTER to exit.")
        return
    
    with open(pth, "w") as f:
        final = ""
        size = int(size)
        if garbage == True:
            for nextI in range(size):
                stdout.write("Getting char (Char #" + str(nextI) + ".)... ")
                final = final + random.choice(allowedChars)
                stdout.write("Done.\n")
            
            f.write(final)
            print("Program has completed.")
            input("Press ENTER to exit.")
            return
        elif garbage == False:
            pass
        else:
            raise ValueError("Variable 'garbage' not in valid state.")



if __name__ == "__main__":
    main()

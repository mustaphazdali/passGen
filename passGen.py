#!/bin/python3
from itertools import product
from colorama import Fore, Style
import sys, argparse, os, cursor

# Setup arguments
parser = argparse.ArgumentParser(
    description="This script generate password from given probs"
)
parser.add_argument("-l", "--length", type=int, help="lenght of password")
parser.add_argument("-r", "--repeat", type=int, help="repeated words from 1 to N", required=True)
parser.add_argument("-w", "--words", type=str, help='words space separated "foo bar"', required=True)
parser.add_argument("-o", "--output", help="output path file name")
parser.add_argument(
    "-v", "--verbose", action="store_true", help="print the password to stdout"
)
parser.add_argument("-q", "--quit", action="store_true", help="print only psswords")

args = parser.parse_args()

# Check if non args montioned to print help menu
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit()

wordlist = []
banner = """
-----------------------
|    ..:PASSGEN:..    |
-----------------------
"""
words = [w.replace("\s", " ") for w in args.words.split()]

if __name__ == "__main__":
    # Header
    if not args.quit:
        print(f"\n{Fore.BLUE}{banner}{Style.RESET_ALL}")
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Password length\t{Style.RESET_ALL}{args.length or '-'}"
        )
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Repeated words\t{Style.RESET_ALL}{args.repeat or '-'}"
        )
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Given word list\t{Style.RESET_ALL}{words or '-'}"
        )
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Output file name\t{Style.RESET_ALL}{args.output or '-'}\n"
        )
        print(
            f"{Fore.YELLOW}[!] {Fore.MAGENTA}Generating Passwords..\t{Style.RESET_ALL}"
        )

    cursor.hide()
    for r in range(args.repeat):
        for p in product(words, repeat=r + 1):
            password = "".join(p)
            if args.length == None:
                wordlist.append(password)
                if args.verbose:
                    print(password)
                    continue
                else:
                    print(password, end="\r")
                    continue
            if len(password) <= args.length:
                wordlist.append(password)
                if args.verbose:
                    print(password)
                else:
                    print(password, end="\r")
    cursor.show()

    # Create output file
    if args.output != None and not args.quit:
        print(f"{Fore.GREEN}[+] Password generated sucsessfully.{Style.RESET_ALL}\n")
        print(f"\n{Fore.YELLOW}[!] {Fore.MAGENTA}Creating wordlist..{Style.RESET_ALL}")
        with open(args.output, "w") as outputFile:
            outputFile.write("\n".join(wordlist))
        print(
            f"{Fore.GREEN}[+] Wordlist created:\t{Style.RESET_ALL}{args.output or '-'}"
        )
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Total size of wordlist:\t{Style.RESET_ALL}{os.path.getsize(args.output):,} bytes\n"
        )
    if not args.quit:
        print(
            f"{Fore.YELLOW}[*] {Fore.CYAN}Total number of passwords:\t{Style.RESET_ALL}{len(wordlist)}"
        )
        print(f"{Fore.GREEN}[+] DONE.{Style.RESET_ALL}")

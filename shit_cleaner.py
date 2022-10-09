import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# import os
# import platform
# # os.system("") # enables ansi escape characters
# if platform.system().lower() == 'windows' or os.name == 'nt':
#      print("Changing to Windows Setting...")
#      from ctypes import windll, c_int, byref
#      k = windll.kernel32
#      stdout_handle = k.GetStdHandle(c_int(-11))
#      mode = c_int(0)
#      k.GetConsoleMode(c_int(stdout_handle), byref(mode))
#      mode = c_int(mode.value | 4)
#      k.SetConsoleMode(c_int(stdout_handle), mode)

try:
     from colorama import Fore, init
     init(autoreset=True)
except:
     print('正在下載 colorama...')
     install('colorama')
     print('請過一陣子 再重新跑一次')

red     = Fore.RED     # '\x1b[31m' # '\033[1;31m' # Fore.RED       # '\x1b[31m'   '\033[91m'
green   = Fore.GREEN   # '\x1b[32m' # '\033[1;32m' # Fore.GREEN     # '\x1b[32m'   '\033[92m'
yellow  = Fore.YELLOW  # '\x1b[33m' # '\033[5;33m' # Fore.YELLOW    # '\x1b[33m'   '\033[93m'
blue    = Fore.BLUE    # '\x1b[34m' # '\033[1;34m' # Fore.BLUE      # '\x1b[34m'   '\033[94m'
magenta = Fore.MAGENTA # '\x1b[35m' # '\033[1;35m' # Fore.MAGENTA   # '\x1b[35m'   '\033[95m'
cyan    = Fore.CYAN    # '\x1b[36m' # '\033[1;36m' # Fore.CYAN      # '\x1b[36m'   '\033[96m'
default = Fore.RESET   # '\x1b[0m'  # '\033[1;39m' # Fore.RESET     # '\x1b[39m'   '\033[99m'

print(f'''{blue}
╭━━━╮╱╱╱╱╱╱╱╱╱╱╭┳╮╱╭╮╱╱╭━━━╮╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃┃╱┃┃╱╱┃╭━━╯╱┃┃
┃╰━━┳━━┳━━┳━━┳━╯┃┃╱┃┣━━┫╰━━┳━╯┣╮╭╮
╰━━╮┃╭╮┃┃━┫┃━┫╭╮┃┃╱┃┃╭╮┃╭━━┫╭╮┃┃┃┃
┃╰━╯┃╰╯┃┃━┫┃━┫╰╯┃╰━╯┃╰╯┃╰━━┫╰╯┃╰╯┃
╰━━━┫╭━┻━━┻━━┻━━┻━━━┫╭━┻━━━┻━━┻━━╯
╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯{default}''')
print(f'{red}正在帮你整理文件以达到checker的style要求:')
f = open(input_file_name, 'r', encoding='utf-8')
s = f.read()
f.close()
print(f"{cyan}读取文件: {magenta}{input_file_name}{default}")
print(f"{cyan}存档文件: {magenta}{input_file_name}")


import re
import hashlib
def hash(s): return hashlib.md5(s.encode()).hexdigest()

operators = (
     '->', '>>>', '+=', '-=', '*=', '/=',
     '<=', '>=', '==', '!=', '>', '<',
     '=', '+', '-', '*', '/', '%',
)

# make sure there is exactly 1 space around operators
for o in operators: s = s.replace(o, hash(o))
for o in operators: s = re.sub(fr' *{hash(o)} *', f' {o} ', s)
s = re.sub(r' +or +', ' or ', s)
s = re.sub(r' +and +', ' and ', s)
print(f'✅ {green}确保:{blue} 每个operator 前后刚好一个空格{yellow} ...... 已完成')

# make sure there is exactly 4 spaces before '>>>' and 1 space after
s = re.sub(r' *>>> *', '    >>> ', s)
print(f'✅ {green}确保:{blue} >>> 后刚好一个空格{yellow} ................. 已完成')

# make sure there is 0 space before ':' or ',' and 1 space after
s = re.sub(r' *: *', ': ', s)
s = re.sub(r' *, *', ', ', s)
# in case of slicing, i.e. '[i:]', remove the space after ':'
s = s.replace(': ]', ':]')
print(f'✅ {green}确保:{blue} 逗号\',\' 和 冒号\':\' 后刚好一个空格{yellow} .. 已完成')

# make sure the file ends with 1 black line
s = s.rstrip() + '\n'
print(f'✅ {green}确保:{blue} 文件最后是一个空行结尾{yellow} ............. 已完成')

# remove trailing white space
s = re.sub(r' +\n', '\n', s)
print(f'✅ {green}确保:{blue} 沒有任何 trailing white space{yellow} ...... 已完成')

# make sure there are 2 blank lines between each function
headers = [x.group().lstrip()[:-1] for x in re.finditer(r'(#.*\n)*\n*def .+\(', s)]
for header in headers: s = re.sub(fr'\n*{header}', f'\n\n\n{header}', s)
print(f'✅ {green}确保:{blue} 每个function 之间都刚好空两行{yellow} ...... 已完成')

# save to file
with open(output_file_name, 'w') as f:
     f.write(s)

print(f'{red}完成啦~ 记得在跑一次 {magenta}a1_checker.py')
# ==============================================================

print(f'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⣶⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣬⡻⣿⣿⣿⣦⣮⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⡿⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣷⣆⡙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠿⠟⠛⠋⠉⠉⠁⠠⣠⣿⣿⣟⣼⡟⣱⣿⣿⣿⠏⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣮⠠⡀⠈⠉⠉⠉⠛⠛⠿⣿
⣿⣇⠀⠀⠀⠀⠀⢀⡄⣴⣿⣿⣿⣾⢏⣼⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡉⢿⣿⣿⣿⣷⡅⣤⠀⠀⠀⠀⠀⠀⣼
⣿⣿⡀⠀⠀⠀⢀⡌⣼⡿⢿⣿⣿⢃⣾⣟⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⢿⣿⣮⣻⣿⣌⢤⡀⠀⠀⠀⢠⣿
⣿⣿⡇⠀⠀⠀⠛⢸⣼⣿⣿⣿⡏⣼⣿⡞⢱⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡎⢻⣿⣿⣿⣿⡎⡇⠀⠀⠀⣼⣿
⣿⣿⣿⠀⠀⡔⢠⣇⣿⣿⣿⣿⢰⣿⣿⢱⣿⣿⠇⢿⣿⣿⣿⣿⣿⣿⠻⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⣿⣷⡙⣿⣿⡔⢆⠀⢠⣿⣿
⣿⣿⣿⡇⠀⠀⣾⠰⣿⣿⣿⡇⣾⣿⢇⣿⣿⠃⣠⢸⣿⣿⣿⣿⣿⣿⣧⠃⢹⣿⣿⣷⠘⣿⣿⣿⣿⣿⣧⢹⣿⣿⡘⣿⣿⡄⠀⣼⣿⣿
⣿⣿⣿⣿⠀⣸⣿⣑⣿⣿⣿⢰⣿⣿⢸⣿⢏⣘⣛⣃⢿⡏⣿⣿⣿⣿⣿⣇⠀⠙⣿⣿⣧⠘⢿⣿⣿⣿⣿⣆⢿⣿⣇⢻⣿⣷⡀⠻⣿⣿
⣿⣿⣿⡟⢠⢻⣿⢌⣿⣿⡏⣸⣿⠃⣾⢏⡾⠿⠿⣿⣆⢻⡜⣿⣿⣿⣿⣿⣦⠳⣤⣙⢿⣎⢦⡙⢿⣿⡜⣿⡜⣿⣿⡸⣿⣷⡰⠰⣤⡩
⣿⣿⡟⡌⣼⢸⣿⡮⣿⣿⡇⣿⢣⡶⠙⠐⢊⣉⡙⠳⣯⣣⡻⣌⠻⢿⣿⣿⣿⣷⡍⠷⠒⠊⠀⠮⣌⠻⣷⢸⣧⢹⣿⡇⣿⣿⡇⣧⢹⣿
⣿⠟⣼⢡⣿⡎⣿⡇⣿⣿⡇⢣⡟⠀⣠⡾⣯⡀⠈⠳⡌⢿⣿⣮⣇⣐⣶⣮⣭⡝⢠⣾⣧⠀⠉⢲⣄⠓⢈⠘⣿⡌⣿⣗⢻⣿⡷⣹⡆⢿
⢣⣾⠃⣸⣿⣷⢹⣷⢹⣿⡇⣯⠁⣼⣿⠀⢩⠉⢂⠀⣿⠘⣿⣿⣿⣿⣿⣿⣿⠁⣿⠈⠉⠈⠆⠀⣿⡆⢁⡁⡿⠁⢿⣿⢸⣿⡇⣿⣿⡜
⠟⢁⡃⢾⣿⣿⣆⢻⡎⣿⡇⣯⠄⣿⣿⠀⠰⠀⠘⡀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⠀⡀⠀⡀⠄⣿⣿⢈⣡⣶⠐⢸⡿⢸⣿⠇⣿⣿⣧
⠀⢢⠁⣿⣿⣿⣿⡌⣷⡸⣇⢿⣆⢻⣿⣧⡸⠯⢗⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠫⠽⢇⣼⣿⡇⣬⣽⡏⡀⢸⡏⣿⡿⢸⣿⣿⣿
⠈⠤⠃⣿⣿⣿⣿⣿⣜⢷⡹⡸⣿⣷⣝⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢻⣴⣾⡿⢈⡔⠨⢇⣿⢃⣿⣿⣿⣿
⡈⠢⠁⢻⣿⣿⣿⣿⣿⣮⠳⡁⢿⣿⣿⣿⣿⣿⣿⠟⢩⣭⣭⣭⣭⣭⣭⣭⣭⣙⣛⠻⣿⣿⣾⣾⣿⣿⣿⢣⣤⠔⠈⣼⢃⣾⣿⣿⣿⣿
⣇⠀⠇⠸⣿⣿⣿⣿⣿⣿⣿⡜⠸⣿⣿⣿⣿⣿⡇⠀⢀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⢸⣿⣿⣿⣿⣿⡇⠘⡀⡀⢠⢇⣼⣿⣿⣿⣿⡿
⠘⣧⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣆⠹⣿⣿⣿⣿⣷⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣾⣿⣿⣿⣿⡟⢀⠃⢆⠁⢠⣾⣿⣿⣿⣿⣿⡇
⣷⣾⣷⣄⢂⢻⣿⣿⣿⣿⣿⣿⣿⣧⡙⣿⣿⣿⣿⣿⣬⡙⢿⣿⣿⣿⣿⣿⡿⢟⣡⣾⣿⣿⣿⡿⠋⠠⢌⡘⠄⢂⣿⣿⣿⣿⣿⣿⡿⢐
⠀⠉⠛⠻⠆⢂⠹⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⢿⣿⣿⣿⣿⣷⣬⣭⣭⣭⣥⣶⣿⣿⣿⡿⠟⠋⡐⢌⠡⠀⠈⠆⢸⣿⣿⣿⣿⣿⡿⠁⡌
⠀⠀⠀⠀⠀⠀⠐⣈⠻⣿⣿⣿⣿⣿⣿⣿⣆⠀⠈⠭⠙⡛⠛⠟⠿⠻⠟⠛⠛⠋⠉⡄⢂⠄⠑⠨⠄⡃⠄⢠⡁⢸⣿⣿⣿⣿⡿⢁⠒⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠂⠌⡙⠿⣿⣿⣿⣿⣿⣆⢰⣾⣶⣬⣙⠶⢶⣤⠦⠖⣊⡥⣖⣌⠂⠂⠃⠀⠁⠈⠈⠀⠀⣹⣿⣿⣿⠟⠁⠄⠁⠀''')

print(f'                                            ^ Anya')
from numbersystem import decimalToBinary, decimalToHexa
from termcolor import colored
from pyfiglet import figlet_format

from Modules.Lab.utils import app_sum

x = 9
print(decimalToBinary(x))
print(decimalToHexa(x))

print(colored(str(x), 'red', attrs=['bold', 'underline']))
print(figlet_format('OK', font='isometric1'))


print(app_sum(1, 3))
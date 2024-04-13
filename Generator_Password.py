# Генерация паролей на Python

from colorama import Back, Fore, Style
import random
import string


print(f"{Fore.GREEN}Пароли будут сохранены в password.txt{Style.RESET_ALL}")
length = int(input(f"{Fore.GREEN}Введите длинну пароля:{Style.RESET_ALL} "))
print(f"{Fore.BLUE}---------------------------------------------{Style.RESET_ALL}")

total = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(total, length))
with open("password.txt", "a") as output:
    output.write(f"{password}\n")
    output.close()


if length > 10:
    print(f"{Fore.GREEN}Надёжный пароль:")
    print(f"{Fore.GREEN}{password}{Style.RESET_ALL}")

elif length > 6:
    print(f"{Fore.YELLOW}Нормальный пароль:")
    print(f"{Fore.YELLOW}{password}{Style.RESET_ALL}")

elif length > 4:
    print(f"{Fore.RED}Плохой пароль:")
    print(f"{Fore.RED}{password}{Style.RESET_ALL}")

else:
    print(f"{Fore.RED}Вообще плохой пароль:")
    print(f"{Fore.RED}{password}{Style.RESET_ALL}")

print(f"{Fore.BLUE}---------------------------------------------{Style.RESET_ALL}")
print(f"{Fore.RED}Сохранино в password.txt{Style.RESET_ALL}")
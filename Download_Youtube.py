from pytube import YouTube
from colorama import Back, Fore, Style



link = input(f"{Fore.GREEN}Введите ссылку на видео с YouTube:{Style.RESET_ALL} ")
print(f"{Fore.BLUE}---------------------------------------------{Style.RESET_ALL}")


try:
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    print(f"{Fore.GREEN}Загрузка...{Style.RESET_ALL}")
    ys.download(r"YoTube_Video")
    print(f"{Fore.GREEN}Загрузка завершена!!{Style.RESET_ALL}")

except:
    print(f"{Fore.RED}Ошибка{Style.RESET_ALL}")


print(f"{Fore.BLUE}---------------------------------------------{Style.RESET_ALL}")
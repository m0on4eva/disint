from colorama import Fore
import json
import requests
import os


token = "token value of a Discord account (not a bot)"

if token == "token value of a Discord account (not a bot)":
   peint("change the token value")


def lotsow():
    os.system('CLS')
    os.system('clear')
    print(Fore.LIGHTMAGENTA_EX + """
 ____  _     ___       _   
|  _ \(_)___|_ _|_ __ | |_ 
| | | | / __|| || '_ \| __|
| |_| | \__ \| || | | | |_ 
|____/|_|___/___|_| |_|\__|   
    """)
    print(Fore.LIGHTRED_EX + "Github : L0tsow ")
    print(Fore.LIGHTBLUE_EX + "         Twitter : 0xL0tsow")
    print(Fore.LIGHTGREEN_EX + "                    Telegram : L0tsow")
    print(Fore.LIGHTYELLOW_EX + "                               Discord : 0xL0tsow")
    print(Fore.WHITE + "-" * 50)

lotsow()

id_ds = input("Enter victim's discord id : ")

url = "http://canary.discord.com/api/v9/users/" + id_ds

headers = {
    "Authorization": token,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    user_id = data['id']

    user = requests.get(f"http://canary.discord.com/api/v9/users/{user_id}", headers=headers).text

    lotsow()

    print("Account Data:")
    print("-" * 50)
       
    user_data = json.loads(user)
    for key, value in user_data.items():
        print(f"{key} : {value} \n")
    print(f"avatar link: https://cdn.discordapp.com/avatars/{user_id}/{user_data['avatar']} \n")

    print(f"banner link: https://cdn.discordapp.com/banners/{user_id}/{user_data['banner']}.gif?size=480 \n")
    print("-" * 50)

    with open(f"output/{user_data['username']}" +'.txt', "a+") as discord_output:
        discord_output.write(str(user_data))
        discord_output.write("\n\n")
        discord_output.write("        Follow me on : \n")
        discord_output.write("Twitter - https://twitter.com/0xl0tsow \n")
        discord_output.write("Github - https://github.com/0xL0tsow \n")                                      
        discord_output.write("Telegram - https://t.me/L0tsow \n")        
        discord_output.close()
exit()

import requests
import time
import os
from colorama import Fore, Back, Style, init

init()

contadorGeral = 0
contadorSucesso = 0
contadorPerdido = 0

while True:
    urlUser = input("Digite um url: \n").strip()

    if not urlUser:
        print("[!] Valor esperado. ")
        continue
    
    escolha = input("1- Https\n2- Http\n").strip()

    if escolha not in ["1", "2"]:
        print("[!] Escolha de protocolo é necessária (1 ou 2)")
        continue
    break

try:
    print("\nAperte Ctrl + C para parar. \n")

    while True: 
        try:
            if escolha == "1": 
                url = requests.get("https://" + urlUser, auth=('user', 'pass'), timeout=5)
            elif escolha == "2":
                url = requests.get("http://" + urlUser, auth=('user', 'pass'), timeout=5)
            
            # O sleep e as checagens precisam ficar DENTRO do try interno
            time.sleep(0.3)
            
            if url.status_code == 200:
                contadorSucesso += 1
                print(Fore.GREEN + "[ONLINE]" + Style.RESET_ALL)
            elif url.status_code in [401, 403]:
                contadorPerdido += 1
                print(Fore.RED + "Acesso negado" + Style.RESET_ALL)
            elif url.status_code == 404:
                contadorPerdido += 1
                print(Fore.RED + "Não encontrado" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "[!] Erro. " + Style.RESET_ALL)
                contadorPerdido += 1

        except requests.exceptions.RequestException:
            contadorPerdido += 1
            print(Fore.LIGHTYELLOW_EX + "[!] Host inacessível / Erro de conexão." + Style.RESET_ALL)

        contadorGeral += 1

except KeyboardInterrupt:
    print("\n" + "=" * 25)
    print(f"Pacotes enviados: {contadorGeral}")
    print(f"Pacotes recebidos com sucesso: {contadorSucesso}")
    print(f"Pacotes perdidos: {contadorPerdido}")
    print("=" * 25)

if os.name == "nt":
    input("\n[+] Aperte Enter para fechar ") #Necessario para que o programa não feche sozinho no Windows
import requests
import time
import os

contadorGeral = 0
contadorSucesso = 0
contadorPerdido = 0

if os.name == "nt":
    os.system("cls")
else :   
    os.system("clear")
while True:
    urlUser = input("Digite um url (ex: youtube.com): ").strip().lower()

    if not urlUser:
        print("[!] Valor esperado. ")
        continue

    if urlUser.startswith("https://"):
        urlUser = urlUser.replace("https://", "")
    elif urlUser.startswith("http://"):
        urlUser = urlUser.replace("http://", "")
    
    escolhaProtocolo = input("1- Https\n2- Http\n").strip()

    if escolhaProtocolo not in ["1", "2"]:
        print("[!] Escolha de protocolo é necessária (1 ou 2)")
        continue

    if escolhaProtocolo == "1": 
        protocolo = "https://"
    elif escolhaProtocolo == "2":
        protocolo = "http://"
            

    urlFinal = protocolo + urlUser
    break

try:
    print("\nAperte Ctrl + C para parar. \n")

    while True: 
        try:
            url = requests.get(urlFinal, auth=('user', 'pass'), timeout=5)    
            time.sleep(0.3)
            
            if url.status_code == 200:
                contadorSucesso += 1
                print("[ONLINE]")
            elif url.status_code in [401, 403]:
                contadorPerdido += 1
                print("Acesso negado")
            elif url.status_code == 404:
                contadorPerdido += 1
                print("Não encontrado")
            else:
                print("[!] Erro.")
                contadorPerdido += 1

        except requests.exceptions.RequestException:
            contadorPerdido += 1
            print("[!] Host inacessível / Erro de conexão." )
            time.sleep(0.6)
        contadorGeral += 1

except KeyboardInterrupt:
    print("\n" + "=" * 25)
    print(f"Pacotes enviados: {contadorGeral}")
    print(f"Pacotes recebidos com sucesso: {contadorSucesso}")
    print(f"Pacotes perdidos: {contadorPerdido}")
    print("=" * 25)

if os.name == "nt":
    input("\n[+] Aperte Enter para fechar ") #Necessario para que o programa não feche sozinho no Windows
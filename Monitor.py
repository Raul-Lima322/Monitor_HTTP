import requests
import time

contadorGeral = 0
contadorSucesso = 0
contadorPerdido = 0

while True:
    urlUser = input("Digite um url: \n").strip()

    if not urlUser:
        print("[!] Valor esperado. ")
        continue
    
    escolha = input("1- Https\n2- Http\n")

    if not escolha:
        print("[!] Escolha de protocolo é necessaria")
        continue
    break

try:
    print("\nAperte Ctrl + C para parar. \n")
    while True: 
        if escolha == "1": 
            url = requests.get("https://" + urlUser, auth=('user', 'pass'))
        elif escolha == "2":
            url = requests.get("http://" + urlUser, auth=('user', 'pass'))
        try:
            time.sleep(0.3)
            if url.status_code == 200:
                contadorSucesso += 1
                print("[ONLINE]")
            elif url.status_code == 401 or url.status_code == 403:
                contadorPerdido += 1
                print("Acesso negado")
            elif url.status_code == 404:
                 contadorPerdido += 1
                 print("Não encontrado")
            else:
                print("[!] Erro. ")
                contadorGeral += 1
        except requests.exceptions.RequestException:
            contadorPerdido +=1
            print("[+] Host inacesivel / Erro de conexão. \n")

        contadorGeral +=1

except KeyboardInterrupt:
   print("\n" +"=" * 25)
   print(f"Pacotes enviados: {contadorGeral}")
   print(f"Pacotes recebidos com sucesso: {contadorSucesso}")
   print(f"Pacotes perdidos: {contadorPerdido}")
   print("\n" +"=" * 25)

   
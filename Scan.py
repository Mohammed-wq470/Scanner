import requests 
import time

def sok(url,input_file):
    with open(input_file, "r") as file: 
        paths= file.readlines() 

    for path in paths:
        path= path.strip()  
        new_url=f"{url}/{path}"  
        try :
            response=requests.get(new_url, headers= {'User-Agent': 'Mozilla/5.0'}) 
            time.sleep(1)  
            if response.status_code==200:
                print(f"Found :,{new_url}- Status : {response.status_code}")
            elif response.status_code==404:
                print(f"Not found:, {new_url} - Status: {response.status_code}") 

            else :
                print(f"Unkown :,{new_url}-status: {response.status_code} ")

        except requests.exceptions.RequestException as e:
            print(f"[!] {new_url}. Fel: {e}")
         

url="https://0a3b00af048b7a7d81e7394400730045.web-security-academy.net" 
input_file="common.txt" 
 
sok(url,input_file) 



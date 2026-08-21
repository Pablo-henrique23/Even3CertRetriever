import requests
from bs4 import BeautifulSoup
from json5 import loads

# CHANGE ME
COOKIE = ''

EVEN3 = "https://www.even3.com.br"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Cookie": COOKIE,
    "Content-Type": "application/json"
}

def get_certificate_list():
    r = requests.get(f"{EVEN3}/participante/certificates/", headers=HEADERS).content
    sopa = BeautifulSoup(r, "html.parser")
    sufix = sopa.find_all("a", class_="btn btn-primary")[0]['href']
    
    return EVEN3 + sufix

def get_select_for_payment_page(first_page):
    r = requests.get(first_page, headers=HEADERS).content
    sopa = BeautifulSoup(r, "html.parser")
    sufix = sopa.find_all("a", class_="btn btn-primary btn-sm")[0]['href']
    
    return EVEN3 + sufix

def find_data(select_page):
    r = requests.get(select_page, headers=HEADERS).content
    sopa = BeautifulSoup(r, "html.parser")
    data = sopa.find_all("script")[-2].text
    d = loads(data.strip()[16:-1])
    
    return d['certificates']

def create_output(data: list):
    for certificate in data:
        print(certificate['titulo'])
        print(f"\t{EVEN3}/documentos/imprimir?i={certificate['identificador']}&cc={certificate['code']}\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
from time import sleep

class pagsww:
    def __init__(self):
        self.lista = ["acer", "asus", "dell", "lenovo", "samsung"]
        #mnotebook
        self.site1 = 'https://www.magazineluiza.com.br/notebook/informatica/s/in/note/brand---acer/'
        self.site2 = 'https://www.magazineluiza.com.br/notebook/informatica/s/in/note/brand---asus/'
        self.site3 = 'https://www.magazineluiza.com.br/notebook/informatica/s/in/note/brand---dell/'
        self.site4 = 'https://www.magazineluiza.com.br/notebook/informatica/s/in/note/brand---lenovo/'
        self.site5 = 'https://www.magazineluiza.com.br/notebook/informatica/s/in/note/brand---samsung/'


        self.map = {
                'celular': {
                        'xpath': '//*[@id="__next"]/div/main/section[4]/div[2]/div/ul/li[$messi$]/a/div[3]/h2'
                },
                'preço': {
                    'xpathdin': '//*[@id="__next"]/div/main/section[4]/div[2]/div/ul/li[$felipe$]/a/div[3]/div/div/p[2]',
                    'xpathtt': '//*[@id="__next"]/div/main/section[4]/div[2]/div/ul/li[$felipe$]/a/div[3]/div/div/p[1]'
                },
            }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.connect()
        #self.teste()

    def connect(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="banquinho"
        )
        self.cursor = self.conexao.cursor()
        return self.cursor

    def teste(self):
        list = []
        count = 0
        marca = ""

        for j in range(5):
            eval(f"self.driver.get(self.site{j+1})")

            # try:
            for i in range(1, 11):

                self.note = self.driver.find_element(By.XPATH, self.map['celular']['xpath'].replace("$messi$", f"{i}")).text
                print(self.note)
                list.append(self.note)
                self.preco = self.driver.find_element(By.XPATH,self.map['preço']['xpathdin'].replace('$felipe$', f"{i}")).text
                if self.preco[0] == "R":
                    print(self.preco)
                    list.append(self.preco)
                else:
                    self.preco = self.driver.find_element(By.XPATH,self.map['preço']['xpathtt'].replace('$felipe$', f"{i}")).text
                    print(self.preco)
                    list.append(self.preco)
                marca = self.lista[j]
                # command = f""" INSERT INTO notes (Modelo, Preco, Marca)
                #                             VALUES (%s, %s, %s)"""
                # self.cursor.execute(command, (self.note, self.preco, marca))
                # self.conexao.commit()
                # count += 1
                # if count <= 10:
                #     marca = "Acer"
                # elif count <= 20:
                #     marca = "Asus"
                # elif count <= 30:
                #     marca = "Dell"
                # elif count <= 40:
                #     marca = "Lenovo"
                # elif count <= 50:
                #     marca = "samsung"

            print("=" * 50)
            # command = f""" INSERT INTO notes (Modelo, Preco, Marca)
            #                 VALUES (%s, %s, %s)"""
            # self.cursor.execute(command, (self.note, self.preco, marca))
            # self.conexao.commit()
















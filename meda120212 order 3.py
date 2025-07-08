from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl
import random
# Lokasi file Excel
excel_file_path = 'C:/Users/GIGABYTE/Downloads/2 belum run/meda120212 order 3/meda120212 order 3.xlsx'

# Inisialisasi driver WebDriver
web = webdriver.Edge()

try:
    web.get('https://forms.gle/cexyTBVo3Ukmqw9N6')

    time.sleep(0.5)

    # Mengisi formulir dan menghapus baris kedua berulang kali:
    while True:
        # Muat ulang DataFrame dari Excel untuk mendapatkan baris terbaru
        df = pd.read_excel(excel_file_path)

        # Periksa apakah masih ada data yang harus diproses
        if df.empty:
            print("Semua baris telah diproses dan dihapus.")
            break

        # Ambil data dari baris kedua (indeks 0-based di pandas)

        try:
            # # Konversi nilai ke string


            eval1 = df.loc[0, 'eval1']
            Evaluasi = eval1
            if Evaluasi == 1:
                PilihanEval = web.find_element(By.XPATH, '//*[@id="i6"]')
            if Evaluasi == 2:
                PilihanEval = web.find_element(By.XPATH, '//*[@id="i9"]')
            PilihanEval.click()
            time.sleep(0.1)

            eval2 = df.loc[0, 'eval2']
            eval2_str = str(eval2)
            Na = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
            Na.send_keys(eval2_str)
            time.sleep(0.1)

            eval3 = df.loc[0, 'eval3']
            eval3_str = str(eval3)
            Na = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
            Na.send_keys(eval3_str)
            time.sleep(0.1)

            eval4 = df.loc[0, 'eval4']
            eval4_str = str(eval4)
            Na = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
            Na.send_keys(eval4_str)
            time.sleep(0.1)

            eval5 = df.loc[0, 'eval5']
            Evaluasi = eval5
            if Evaluasi == 1:
                PilihanEval = web.find_element(By.XPATH, '//*[@id="i35"]')
            if Evaluasi == 2:
                PilihanEval = web.find_element(By.XPATH, '//*[@id="i38"]')
            PilihanEval.click()
            time.sleep(0.1)

            # Next Page A action (page transition/submission) for eval6
            time.sleep(0.5)  # Tunggu sebentar sebelum klik
            TombolAction = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            TombolAction.click()
            time.sleep(0.5)  # Tunggu halaman berikutnya termuat atau form tersubmit

            eval6 = df.loc[0, 'eval6']
            jawab = eval6
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')      
            elif jawab == 5:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div') 
            pilihan.click()
            time.sleep(0.1)

            eval7 = df.loc[0, 'eval7']
            jawab = eval7
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')      
            elif jawab == 5:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div') 
            pilihan.click()
            time.sleep(0.1)

            eval8 = df.loc[0, 'eval8']
            jawab = eval8
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval9 = df.loc[0, 'eval9']
            jawab = eval9
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval10 = df.loc[0, 'eval10']
            jawab = eval10
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval11 = df.loc[0, 'eval11']
            jawab = eval11
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval12 = df.loc[0, 'eval12']
            jawab = eval12
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval13 = df.loc[0, 'eval13']
            jawab = eval13
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval14 = df.loc[0, 'eval14']
            jawab = eval14
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval15 = df.loc[0, 'eval15']
            jawab = eval15
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval16 = df.loc[0, 'eval16']
            jawab = eval16
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval17 = df.loc[0, 'eval17']
            jawab = eval17
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval18 = df.loc[0, 'eval18']
            jawab = eval18
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval19 = df.loc[0, 'eval19']
            jawab = eval19
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval20 = df.loc[0, 'eval20']
            jawab = eval20
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval21 = df.loc[0, 'eval21']
            jawab = eval21
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval22 = df.loc[0, 'eval22']
            jawab = eval22
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval23 = df.loc[0, 'eval23']
            jawab = eval23
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval24 = df.loc[0, 'eval24']
            jawab = eval24
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval25 = df.loc[0, 'eval25']
            jawab = eval25
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval26 = df.loc[0, 'eval26']
            jawab = eval26
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval27 = df.loc[0, 'eval27']
            jawab = eval27
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval28 = df.loc[0, 'eval28']
            jawab = eval28
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval29 = df.loc[0, 'eval29']
            jawab = eval29
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval30 = df.loc[0, 'eval30']
            jawab = eval30
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval31 = df.loc[0, 'eval31']
            jawab = eval31
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval32 = df.loc[0, 'eval32']
            jawab = eval32
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval33 = df.loc[0, 'eval33']
            jawab = eval33
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval34 = df.loc[0, 'eval34']
            jawab = eval34
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval35 = df.loc[0, 'eval35']
            jawab = eval35
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval36 = df.loc[0, 'eval36']
            jawab = eval36
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval37 = df.loc[0, 'eval37']
            jawab = eval37
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval38 = df.loc[0, 'eval38']
            jawab = eval38
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval39 = df.loc[0, 'eval39']
            jawab = eval39
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval40 = df.loc[0, 'eval40']
            jawab = eval40
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval41 = df.loc[0, 'eval41']
            jawab = eval41
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval42 = df.loc[0, 'eval42']
            jawab = eval42
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval43 = df.loc[0, 'eval43']
            jawab = eval43
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval44 = df.loc[0, 'eval44']
            jawab = eval44
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval45 = df.loc[0, 'eval45']
            jawab = eval45
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval46 = df.loc[0, 'eval46']
            jawab = eval46
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval47 = df.loc[0, 'eval47']
            jawab = eval47
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval48 = df.loc[0, 'eval48']
            jawab = eval48
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval49 = df.loc[0, 'eval49']
            jawab = eval49
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval50 = df.loc[0, 'eval50']
            jawab = eval50
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval51 = df.loc[0, 'eval51']
            jawab = eval51
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval52 = df.loc[0, 'eval52']
            jawab = eval52
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval53 = df.loc[0, 'eval53']
            jawab = eval53
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval54 = df.loc[0, 'eval54']
            jawab = eval54
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval55 = df.loc[0, 'eval55']
            jawab = eval55
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval56 = df.loc[0, 'eval56']
            jawab = eval56
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval57 = df.loc[0, 'eval57']
            jawab = eval57
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval58 = df.loc[0, 'eval58']
            jawab = eval58
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval59 = df.loc[0, 'eval59']
            jawab = eval59
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval60 = df.loc[0, 'eval60']
            jawab = eval60
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval61 = df.loc[0, 'eval61']
            jawab = eval61
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[57]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[57]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[57]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[57]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[57]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            # Next Page B action (page transition/submission) for eval62
            time.sleep(0.5)  # Tunggu sebentar sebelum klik
            TombolAction = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            TombolAction.click()
            time.sleep(0.5)  # Tunggu halaman berikutnya termuat atau form tersubmit

            eval62 = df.loc[0, 'eval62']
            jawab = eval62
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')      
            elif jawab == 5:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div') 
            pilihan.click()
            time.sleep(0.1)

            eval63 = df.loc[0, 'eval63']
            jawab = eval63
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')      
            elif jawab == 5:                           
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div') 
            pilihan.click()
            time.sleep(0.1)

            eval64 = df.loc[0, 'eval64']
            jawab = eval64
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval65 = df.loc[0, 'eval65']
            jawab = eval65
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval66 = df.loc[0, 'eval66']
            jawab = eval66
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval67 = df.loc[0, 'eval67']
            jawab = eval67
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval68 = df.loc[0, 'eval68']
            jawab = eval68
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval69 = df.loc[0, 'eval69']
            jawab = eval69
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval70 = df.loc[0, 'eval70']
            jawab = eval70
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval71 = df.loc[0, 'eval71']
            jawab = eval71
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval72 = df.loc[0, 'eval72']
            jawab = eval72
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval73 = df.loc[0, 'eval73']
            jawab = eval73
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval74 = df.loc[0, 'eval74']
            jawab = eval74
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval75 = df.loc[0, 'eval75']
            jawab = eval75
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval76 = df.loc[0, 'eval76']
            jawab = eval76
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval77 = df.loc[0, 'eval77']
            jawab = eval77
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval78 = df.loc[0, 'eval78']
            jawab = eval78
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval79 = df.loc[0, 'eval79']
            jawab = eval79
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval80 = df.loc[0, 'eval80']
            jawab = eval80
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval81 = df.loc[0, 'eval81']
            jawab = eval81
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval82 = df.loc[0, 'eval82']
            jawab = eval82
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval83 = df.loc[0, 'eval83']
            jawab = eval83
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval84 = df.loc[0, 'eval84']
            jawab = eval84
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval85 = df.loc[0, 'eval85']
            jawab = eval85
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval86 = df.loc[0, 'eval86']
            jawab = eval86
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval87 = df.loc[0, 'eval87']
            jawab = eval87
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval88 = df.loc[0, 'eval88']
            jawab = eval88
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval89 = df.loc[0, 'eval89']
            jawab = eval89
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval90 = df.loc[0, 'eval90']
            jawab = eval90
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval91 = df.loc[0, 'eval91']
            jawab = eval91
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval92 = df.loc[0, 'eval92']
            jawab = eval92
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval93 = df.loc[0, 'eval93']
            jawab = eval93
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval94 = df.loc[0, 'eval94']
            jawab = eval94
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval95 = df.loc[0, 'eval95']
            jawab = eval95
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval96 = df.loc[0, 'eval96']
            jawab = eval96
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval97 = df.loc[0, 'eval97']
            jawab = eval97
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval98 = df.loc[0, 'eval98']
            jawab = eval98
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval99 = df.loc[0, 'eval99']
            jawab = eval99
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval100 = df.loc[0, 'eval100']
            jawab = eval100
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            eval101 = df.loc[0, 'eval101']
            jawab = eval101
            if jawab == 1:
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
            elif jawab == 2:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
            elif jawab == 3:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
            elif jawab == 4:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')     
            elif jawab == 5:                                   
                pilihan = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
            pilihan.click()
            time.sleep(0.1)

            # Next Page C action (page transition/submission) for eval102
            time.sleep(0.5)  # Tunggu sebentar sebelum klik
            TombolAction = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
            TombolAction.click()
            time.sleep(0.5)  # Tunggu halaman berikutnya termuat atau form tersubmit

            # Hapus baris yang telah diproses dari Excel
            workbook = openpyxl.load_workbook(excel_file_path)
            sheet = workbook.active

            # Hapus baris kedua (baris pertama dengan data, karena header adalah baris pertama)
            sheet.delete_rows(2) 

            # Simpan perubahan ke Excel
            workbook.save(excel_file_path)
        except Exception as e:
            print(f'Terjadi kesalahan saat mengisi data dari Excel: {e}')
            break

        # Kembali ke halaman formulir awal untuk mengisi baris berikutnya
        web.get('https://forms.gle/cexyTBVo3Ukmqw9N6')
        time.sleep(0.5)

finally:
    # Tutup browser setelah selesai
    web.quit()

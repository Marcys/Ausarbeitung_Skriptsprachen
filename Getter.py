#Import um Zugriff auf das Frame zuerhalten
from selenium import webdriver
#Numpy zum extrahieren der Inhalte
import numpy as np



driver = webdriver.Firefox(executable_path='/Users/marcel/PycharmProjects/AusarbeitungGetter/Ausarbeitung/Ausarbeitung/'
                                           'spiders/geckodriver')
#driver.get('https://en.sudoku-online.net/sudoku-easy/') #Einfaches Sudoku
#driver.get('https://en.sudoku-online.net/') #Mittelschweres Sudoku
#driver.get('https://en.sudoku-online.net/sudoku-difficult/') #Schweres Sudoku
driver.get('https://en.sudoku-online.net/sudoku-very-difficult/') #Sehr schweres Sudoku
clicker = driver.find_element_by_class_name('sudoku-start-btn')
clicker.click()

sudoku_array = np.array([[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]])

for i in range(1,10):
    j=0
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
            sudoku = driver.find_element_by_xpath(xpath)
            sudoku_array[j,(i-1)]=int(sudoku.text)




for i in range(1,10):
    j=1
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)



for i in range(1,10):
    j=2
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)

        sudoku_array[j,(i-1)]=int(sudoku.text)


for i in range(1,10):
    j=3
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)


for i in range(1,10):
    j=4
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[5]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
            sudoku = driver.find_element_by_xpath(xpath)
            sudoku_array[j,(i-1)]=int(sudoku.text)



for i in range(1,10):
    j=5
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[6]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)


for i in range(1,10):
    j=6
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[7]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)


for i in range(1,10):
    j=7
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[8]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)


for i in range(1,10):
    j=8
    xpath='/html/body/div/div/div/main/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[9]/td[{0}]'.format(i)
    element = driver.find_element_by_xpath(xpath).get_attribute('tabindex')
    if(element==None):
        sudoku = driver.find_element_by_xpath(xpath)
        sudoku_array[j,(i-1)]=int(sudoku.text)

print("Zu lösendes Sudoku:")
#Sudoku des finnischen Mathematikers
sudoku_array = np.array([[8,0,0,0,0,0,0,0,0],
                            [0,0,3,6,0,0,0,0,0],
                            [0,7,0,0,9,0,2,0,0],
                            [0,5,0,0,0,7,0,0,0],
                            [0,0,0,0,4,5,7,0,0],
                            [0,0,0,1,0,0,0,3,0],
                            [0,0,1,0,0,0,0,6,8],
                            [0,0,8,5,0,0,0,1,0],
                            [0,9,0,0,0,0,4,0,0]])

#Sudoku von Peter Norvig
"""sudoku_array = np.array([[4,0,0,0,0,0,8,0,5],
                            [0,3,0,0,0,0,0,0,0],
                            [0,0,0,7,0,0,0,0,0],
                            [0,2,0,0,0,0,0,6,0],
                            [0,0,0,0,8,0,4,0,0],
                            [0,0,0,0,1,0,0,0,0],
                            [0,0,0,6,0,3,0,7,0],
                            [5,0,0,2,0,0,0,0,0],
                            [1,0,4,0,0,0,0,0,0]])"""



print(sudoku_array)
print()


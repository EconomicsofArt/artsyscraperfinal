from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

import time

def array_reorganize(yee):
    start_val = 6
    for i in range(0, len(yee) - 1):
        element = yee[i]
        if element.startswith(',') & element[2:6].isdigit():
            #print(yee.index(element))
            yee_front = yee[0:i - 1]
            yee_middle = [''] * (start_val - i + 1)
            year = [element[len(element)-4:len(element)]]
            yee_back = yee[i+1:len(yee) - 1]

            yee = yee_front + yee_middle + year +yee_back

            break
    return yee


def filtering(array, name_array):
    start_ind = 0#array.index('Past Auctions') + 2
    end_ind = array.index('Get the Artsy app')
    array = array[start_ind:end_ind]
    array2 = array.copy()
    # print(new_array)
    # remove non title elements from name_array
    last = None
    while last is None:
        try:
            name_array.remove('Bought In')
        except:
            last = not None
    last = None
    while last is None:
        try:
            name_array.remove('Price not available')
        except:
            last = not None
    last = None
    while last is None:
        try:
            name_array.remove('Skip to Main Content')
        except:
            last = not None

    while last is None:
        try:
            name_array.remove('')
        except:
            last = not None


    #print(name_array)
    start_ind_piece = []
    for piece in name_array:
        # loop through array to find matching elements to each name_array
        for v in array2:
            if v.startswith(piece):
                piecee = v
                #print(v)
                start_ind_piece.append(array2.index(piecee))
                break
        for kk in range(0, start_ind_piece[len(start_ind_piece) - 1]+1):
            array2[kk] = ""
    final_array = []
    this_array = []
    #print(start_ind_piece)
    for i in range(0, len(start_ind_piece) - 1):
        if i + 1 == len(start_ind_piece):
            end_ind = len(array) - 1
        else:
            end_ind = start_ind_piece[i + 1] - 1
        this_array = array_reorganize(array[start_ind_piece[i]:end_ind])

        final_array.append(this_array)
    this_array = array_reorganize(array[start_ind_piece[len(start_ind_piece)-1]:len(array)-1])
    final_array.append(this_array)
    #print(final_array)
    return final_array

loginurl=('https://www.artsy.net/log_in')
finalurl=('https://www.artsy.net/')

username = ('ygao328@emory.edu')
password = ('Password1')

#init driver
driver = webdriver.Chrome()

def extract_elements(input_elements):
    element_arr = []
    for input_element in input_elements:
        element_arr.append(driver.execute_script("""
                    var parent = arguments[0];
                    var child = parent.firstChild;
                    var ret = "";
                    while(child) {
                    if (child.nodeType === Node.TEXT_NODE)
                        ret += child.textContent;
                        child = child.nextSibling;
                    }
                    return ret;
                    """, input_element))
    return element_arr

#login
driver.get(loginurl)
driver.find_element("name", "email").send_keys(username)
password_element = driver.find_element("name", "password")
password_element.send_keys(password)
password_element.send_keys(Keys.RETURN)
#wait time in case of authentication
time.sleep(10)

#list of names
#names = ['rita-mcbride','matthew-benedict','mona-hatoum','ree-morton']

#read csv and make it names array names = .....
#loop start
for name in names:
    #artist url
    artisturl = ('https://www.artsy.net/artist/' + name + '/auction-results?hide_upcoming=false&metric=in')
    #redirect to artist url
    driver.get(artisturl)
    #time.sleep(10)
    #while loop to click through pages
    last_page = None
    page_count = 1
    piece_title = []
    price = []
    final_array = []
    while last_page is None:
        try:
            time.sleep(5)
            # save page data
            # title & "bought in"
            title_elements = driver.find_elements(By.TAG_NAME, "i")
            piece_title = extract_elements(title_elements)

            price_elements = driver.find_elements(By.XPATH, "//div[starts-with(@class,'Box-sc-15se88d-0 "
                                                            "Text-sc-18gcpao-0')]")
            price = extract_elements(price_elements)

            final_array = final_array + filtering(price, piece_title)

            # clicking next
            next_element = driver.find_element(By.XPATH, "//a[@data-testid='next']")
            next_element.click()
            page_count = page_count + 1
        except NoSuchElementException:
            print(final_array)
            print('done scraping for artist:' + name + ', pages: ' + str(page_count))
            file_name = name + ".csv"
            with open(file_name, "w+") as my_csv:
                csvWriter = csv.writer(my_csv, delimiter=',')
                csvWriter.writerows(final_array)
            last_page = not None




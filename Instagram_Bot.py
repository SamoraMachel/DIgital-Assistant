from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from collections import OrderedDict
import selenium.webdriver.support.ui as ui
import time 
from tkinter import messagebox as msg

class InstaBot:
    """
    Arg:
        string: username
        string: password

    when an instance of the object is created the webdriver for firefox 
    is initiated opening up firefox and navigating to the base url
    """
    def __init__(self, username=None, password=None, path_to_driver=None, browser=None):
        self.username = username
        self.password = password
        try:
            exec("from selenium.webdriver.{}.options import Options".format(browser.lower()))
        except Exception as E:
            print(E) 
            msg.showerror("Import Error", "{}".format(E))

        # File location for the ddriver path
        driverPath = "//home/Code/Documents/IG_BOT/geckodriver"

        # open up the url in the webpage
        self.base_url = "https://www.instagram.com"
        try:
            if browser == "Firefox":
                self.driver = webdriver.Firefox(executable_path=path_to_driver)
            elif browser == "Edge":
                self.driver = webdriver.Edge(executable_path=path_to_driver)
            elif browser == "Chrome":
                self.driver = webdriver.Chrome(executable_path=path_to_driver)
            elif browserr == "Safari":
                self.driver = webdriver.Safari(executable_path=path_to_driver)
            
        except Exception as E:
            print(f"Failed to execute webdriver Error : {E}")
            msg.showerror("Error", "{}".format(E))
            exit(3)


        self.driver.get(self.base_url)

        # ---------------------------------  wait until the page load till the sign up link become clickable -------------------------
        # element = WebDriverWait(self.driver, 30).until(EC.           \
                # element_to_be_clickable((By.LINK_TEXT, 'Log in')))



    def LogIn(self):
        """
        Autofill the Username section and the password section of the 
        website and then automatically logs in into the account 
        
        """
        time.sleep(2)
                     # uncomment if you have filled out the username and password in the code section
        username = self.driver.find_element_by_name("username").send_keys(self.username)
        password = self.driver.find_element_by_name("Password").send_keys(self.password)

        time.sleep(2)
        try:
            logIn = self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        except Exception as e:
            print(e)
            print('Will continue if you have clicked the Log In button')

    def Suggested_Nav(self):
        """
        This navigates to the suggested section
        automatically scrools to t he bottom 

        """
        time.sleep(5)
        see_all = "/explore/people/suggested/"

        suggests = self.driver.get(self.base_url+see_all)
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(1.5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                break
            
            last_height = new_height

    def people(self, counter):
        """
        gCollects all the suggested people and 
        then store them in a list 
        """
        sugPage = self.driver.page_source

        soup = BeautifulSoup(sugPage, "html.parser")


        suggested = soup.body.main.div.find_all('a')
        duplicate_links = [suggest.get('href') for suggest in suggested if suggest != '']
        self.counter = counter
        self.links = list(OrderedDict.fromkeys(duplicate_links))
    
    def Follow_and_view_people(self, pictures_to_like, restrict_people_over):
        for link in self.links:
            time.sleep(2)
            self.driver.get(self.base_url+link)

            userPage = self.driver.page_source
            soup = BeautifulSoup(userPage, "html.parser")

            followers = int(self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text)

            count = pictures_to_like
            if followers > restrict_people_over:
                continue
            else:
                try:
                    for i in range(10):
                        for j in range(3):
                            try:
                                # scroll element into view
                                element = self.driver.find_element_by_xpath("//article/div/div/div[{x}]/div[{y}]/a/div".format(x=i+1, y=j+1))
                                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                                time.sleep(2)
                                element.click()
                                time.sleep(1.5)

                                self.driver.find_element_by_xpath("//section/span/button[@type = 'button']").click()
                                time.sleep(1.8)
                                self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
                                time.sleep(1.5)
                                count -= 1
                            except Exception as e:
                                print(e)
                                break
                        if count == 0:
                            break
                    time.sleep(2.5)
                    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                    time.sleep(3)
                except Exception as e:
                    print(e)


                if self.counter != 0 :
                    self.counter -= 1
                    continue
                else:
                    break
                 
                time.sleep(3)
# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------- Still Working on this fixeses --------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

            
            #     followersPage = driver.page_source
            #     soup = BeautifulSoup(followersPage, 'html.parser')

            #     userFollowers = driver.find_element_by_css_selector("li.Y8-fY:nth-child(2) > a:nth-child(1) > span:nth-child(1)").click()


            #     time.sleep(2)
            #     userFollowers = driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
            #     print(userFollowers)

            #     try:
            #         userFollowers = userFollowers[:60]
            #     except Exception as e:
            #         print(e)
            #         print("List does no exceed 60")
            #         pass

            #     for x in userFollowers:
            #         try:
                        
            #             time.sleep(10.25467)
            #             follower = x.find_element_by_tag_name("a")
            #             time.sleep(5.44562)
                    
                
            #             follower.send_keys(Keys.CONTROL + Keys.RETURN)
            #             time.sleep(15.7311)
            #             driver.switch_to.window(driver.window_handles[1])
                        
            #             print(follower)
            #             time.sleep(5)
                        
            #         except:
            #             print("Tring Again")
            #             continue


            #         for i in range(3):
            #                 for j in range(3):
            #                     try:
            #                         # scroll element into view
            #                         time.sleep(1.39347)
            #                         element = driver.find_element_by_xpath(f"//article/div/div/div[{i+1}]/div[{j+1}]/a/div")
            #                         driver.execute_script("arguments[0].scrollIntoView(true);", element)
            #                         time.sleep(2.23973)
            #                         element.click()

            #                         time.sleep(2.4321)
            #                     except Exception as e:
            #                         print(e)
            #                         break
            #         driver.close()

                
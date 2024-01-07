from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"


scraped_data=[]
def scrape():
    
    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index, li_tag in enumerate(li_tags):
                if index==0:  
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:  
                        temp_list.append('')
            scraped_data.append(temp_list) 
            ## ADD CODE HERE ##
        browser.find_element(By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



        
# Calling Method    
scrape()

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df1=pd.DataFrame(scraped_data,columns=headers)

# Convert to CSV
planet_df1.to_csv("scraped_data.csv",index=True,index_label="id")


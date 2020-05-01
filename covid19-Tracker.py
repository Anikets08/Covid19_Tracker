import bs4
import requests

def get_html_data(url):
 data = requests.get(url)
 return data

def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data=get_html_data(url)
    bs =  bs4.BeautifulSoup(html_data.text,'html.parser')
    print("*********************************************************************")
    print()
    print("Covid19 India Report")
    print()
    infodiv =bs.find("li", class_ = "bg-blue")
    print("Active cases : ",infodiv.strong.text)
    infodiv2 = bs.find("li",class_ = "bg-green")
    print("Discharged : ", infodiv2.strong.text)
    infodiv3 = bs.find("li",class_ = "bg-red")
    print("Deaths : ", infodiv3.strong.text)
    infodiv4 = bs.find("li",class_ = "bg-orange")
    print("Migrated : ", infodiv4.strong.text)
    print()
    print("*********************************************************************")
    a = input("enter any key to exit")
get_corona_detail_of_india()

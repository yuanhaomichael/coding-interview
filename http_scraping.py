from urllib.request imr
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://etherscan.io/txsPending'
req = Request(url, headers={'User-Agent':'Mozilla/7.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})   # I got this line from another post since "uClient = uReq(URL)" and "page_html = uClient.read()" would not work (I beleive that etherscan is attemption to block webscraping or something?)
response = urlopen(req, timeout=200).read()
response_close = urlopen(req, timeout=200).close()
# print(response)
page_soup = soup(response, "html.parser")
# print(page_soup)
# result = page_soup.find("table", {"class": "table table-md-text-normal table-hover mb-4"})
result = page_soup.find("table", {"class": "table table-hover"})
# print(result)
df=pd.read_html(str(result))[0]
print(df)
# df.to_csv("TransferTable.csv",index=False)
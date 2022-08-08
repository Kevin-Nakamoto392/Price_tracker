
#1 Extract data from internet (URL, API setup)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO7 @Backupworks
# FUJI
URL = "https://www.backupworks.com/Fujifilm-LTO-7-tape-media-16456574.aspx"
pageBWFFL7 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL7.content, "html.parser")
priceBWFF7 = soup.find("span", class_="prod-detail-cost-value").text
# HPE
URL = "https://www.backupworks.com/HP-LTO-7-tape-cartridge-C7977A.aspx"
pageBWHPEL7 = requests.get(URL)
soup = BeautifulSoup(pageBWHPEL7.content, "html.parser")
priceBWHPE7 = soup.find("span", class_="prod-detail-cost-value").text
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-7-tape-cartridge-MR-L7MQN-01.aspx"
pageBWQTML7 = requests.get(URL)
soup = BeautifulSoup(pageBWQTML7.content, "html.parser")
priceBWQTM7 = soup.find("span", class_="prod-detail-cost-value").text
# IBM
URL = "https://www.backupworks.com/IBM-LTO-7-tape-media-38L7302.aspx"
pageBWIBML7 = requests.get(URL)
soup = BeautifulSoup(pageBWIBML7.content, "html.parser")
priceBWIBM7 = soup.find("span", class_="prod-detail-cost-value").text

# Data extraction for LTO7 @Tape4Backup
# FUJI
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/fuji-16456574-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFF7_3 = soup.find("span", class_="price")
pricet4bFF7_2 = list(pricet4bFF7_3.stripped_strings)
pricet4bFF7 = "\n\n".join(pricet4bFF7_2) #if pricet4bFF7_2 else ""
# HPE
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/hpe-c7977a-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPE7_3 = soup.find("span", class_="price")
pricet4bHPE7_2 = list(pricet4bHPE7_3.stripped_strings)
pricet4bHPE7 = "\n\n".join(pricet4bHPE7_2) #if pricet4bHPE7_2 else ""
# QTM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/quantum-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTM7_3 = soup.find("span", class_="price")
pricet4bQTM7_2 = list(pricet4bQTM7_3.stripped_strings)
pricet4bQTM7 = "\n\n".join(pricet4bQTM7_2) #if pricet4bQTM7_2 else ""
# IBM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/ibm-38l7302-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBM7_3 = soup.find("span", class_="price")
pricet4bIBM7_2 = list(pricet4bIBM7_3.stripped_strings)
pricet4bIBM7 = "\n\n".join(pricet4bIBM7_2) #if pricet4bIBM7_2 else ""

# Data extraction for LTO7 @Tape&Media
# FUJI
URL = "https://tapeandmedia.com/ibm-lto-7-tape-ultrium-tapes.asp"
pagetamFFL7 = requests.get(URL)
soup = BeautifulSoup(pagetamFFL7.content, "html.parser")
pricetamFF7 = soup.find("span", class_="price price--withoutTax price--main").text
# HPE
URL = "https://www.backupworks.com/HP-LTO-7-tape-cartridge-C7977A.aspx"
pagetamHPEL7 = requests.get(URL)
soup = BeautifulSoup(pagetamHPEL7.content, "html.parser")
pricetamHPE7 = soup.find("span", class_="prod-detail-cost-value").text
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-7-tape-cartridge-MR-L7MQN-01.aspx"
pagetamQTML7 = requests.get(URL)
soup = BeautifulSoup(pagetamQTML7.content, "html.parser")
pricetamQTM7 = soup.find("span", class_="prod-detail-cost-value").text
# IBM
URL = "https://www.backupworks.com/IBM-LTO-7-tape-media-38L7302.aspx"
pagetamIBML7 = requests.get(URL)
soup = BeautifulSoup(pagetamIBML7.content, "html.parser")
pricetamIBM7 = soup.find("span", class_="prod-detail-cost-value").text


# Create list
L7price_list = [
    [priceBWFF7, priceBWHPE7, priceBWQTM7, priceBWIBM7],
    [pricet4bFF7, pricet4bHPE7, pricet4bQTM7, pricet4bIBM7],
    [pricetamFF7, pricetamHPE7, pricetamQTM7, pricetamIBM7]
]

index = ["BackupWorks", "Tape4Backup", "Tape&Media"]
columns = ["FUJI", "HPE", "QTM", "IBM"]


#2 Convert bs4 element into dataframe

import pandas as pd
df = pd.DataFrame(L7price_list, index=index,columns=columns)
# df = df.replace({"FUJI":{"$":""}, "HPE":{"$":""}, "QTM":{"$":""}, "IBM":{"$":""}})
df['FUJI'] = df['FUJI'].str.replace("$","", regex=True).astype(float)
df['HPE'] = df['HPE'].str.replace("$","", regex=True).astype(float)
df['QTM'] = df['QTM'].str.replace("$","", regex=True).astype(float)
df['IBM'] = df['IBM'].str.replace("$","", regex=True).astype(float)
pd.options.display.float_format = "${:,.2f}".format


writer = pd.ExcelWriter("internet_pricing.xlsx", engine = "xlsxwriter")
df.to_excel(writer, sheet_name="LTO7")

workbook = writer.book
worksheet = writer.sheets["LTO7"]

format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

writer.save()

# df = pd.DataFrame(L7price_dict, index=index, columns=["Backup Works"])
print(type(df))
print(df)





## Product part #s

# LTO7: Fuji(16456574), HPE(C7977A), IBM(38L7302), QUANTUM(MR-L7MQN-01)
# LTO8: Fuji(16551221), HPE(Q2078A), IBM(01PL041), QUANTUM(MR-L8MQN-01)
# LTO9: Fuji(16659047), HPE(Q2079A), IBM(02XW568), QUANTUM(MR-L9MQN-01)


#3 Sortout Data



#4 Store onto excel(online) file


#5 Automate process using Heroku (monthly)


#6 Send update with URL by email (monthly)


#7 Add dashboard to email??
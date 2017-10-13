import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active
all_links = []
country_list = ['african','america','arabic','australian','christian','english','french','german','indian','iranian','irish']
gender_list = ['boy','girl']
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
my_url = 'https://www.babynamesdirect.com/baby-names'
for i in country_list:
	for j in gender_list:
		for k in letter:
			new_url = my_url+"/"+i+"/"+j+"/"+k
			uClient = uReq(new_url)
			page_html = uClient.read()
			uClient.close()
			page_soup = soup(page_html, "html.parser")
			containers_outer_div = page_soup.findAll("small")
			# pages_number = containers_outer_div[-1].string
			if len(containers_outer_div)!=0:
				pages_number = containers_outer_div[-1].string
				pages_number = pages_number.split("of ")
				lastpage = pages_number[-1]
				lastpage = int(lastpage)+1
				for every in range(1,lastpage):
					inner_new_url = new_url+"/"+str(every)
					print (inner_new_url)
					all_links.append(inner_new_url)
			else:
				print (new_url)
				all_links.append(new_url)
count = 1
for my_url in all_links:
	# my_url = 'https://www.babynamesdirect.com/baby-names/indian/boy/a/1'
	uClient = uReq(str(my_url))
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")

	containers_outer_div = page_soup.findAll("dt",{"class":"nvar"})

	for babyname in containers_outer_div:
		if babyname.string != 'Name':
			print babyname.string
			# sheet.append(babyname.string)
			sheet["A"+ str(count) ] = str(babyname.string)
			sheet["b"+ str(count) ] = str(my_url.split("/")[5])
			count = count + 1
			book.save("babyname.xlsx")

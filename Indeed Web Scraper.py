# import module
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

import cloudscraper 

#import tkinter as tk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, StringVar
from tkinter.ttk import Frame, Label, Entry, Button
#import tkinter as tk






## Remote
#URL = "https://www.indeed.com/jobs?q=" + "engineer" + "&l=" + "Boston%2C%20MA" + "&sc=0kf%3Aattr(DSQF7)%3B&vjk=0bfb9182bc823104"
class User_Input(Frame):
	def __init__(self):
		super().__init__()
		self.output1=""
		self.output2="Boston, MA" #"Boston%2C%20MA" 

		self.master.title("Indeed Scrape!")
		self.pack(fill=BOTH, expand=True)

		frame1 = Frame(self)
		frame1.pack(fill=X)
		lbl1 = Label(frame1, text="Position", width=20)
		lbl1.pack(side=LEFT, padx=5, pady=10)
		self.entry1 = Entry(frame1, textvariable=self.output1)
		self.entry1.pack(fill=X, padx=5, expand=True)

		frame2 = Frame(self)
		frame2.pack(fill=X)
		lbl2 = Label(frame2, text="Location (City,State)", width=20)
		lbl2.pack(side=LEFT, padx=5, pady=10)
		self.entry2 = Entry(frame2, textvariable = self.output2)
		self.entry2.pack(fill=X, padx=5, expand=True)

		frame3 = Frame(self)
		frame3.pack(fill=X)
		btn = Button(frame3, text="Search!", command=self.Submit)
		btn.pack(padx=5, pady=10)		

	def Submit(self):
		self.output1 = self.entry1.get()
		self.output2 = self.entry2.get()
		self.quit()


class Indeed_Scraper():
	def __init__(self, job, loc):
		scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})

		#location = "Boston%2C%20MA"
		location = loc.replace(" ", "%")

		URL = "https://www.indeed.com/jobs?q=" + job + "&l=" + location 
		req = scraper.get(URL)
		soup = BeautifulSoup(req.content, 'lxml')
		results = soup.find(id="resultsBodyContent")
		if results != None:
			job_list = results.find_all("li")
			for job in job_list:
				#title_string = job.find("h2", class_="jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0")
				title_string = job.find("h2", class_= lambda text:'jobTitle' in text)
				company_string = job.find("span", class_="companyName")
				address_string = job.find("div", class_="companyLocation")
				descrip_string = job.find("div", class_="job-snippet")
				salary_string = job.find("span", class_="estimated-salary")
				links = job.find_all("a")


				if salary_string == None:
					salary_string = job.find("div", class_="attribute_snippet") 

				if title_string !=None and company_string != None:
					listing_string = title_string.text.strip() + '\n'+ company_string.text.strip() 
					print(listing_string)
					if address_string !=None:
						address_string2 = (str(address_string.text.strip()).replace(u'\xa0',""))			
						print(address_string2)

					print(descrip_string.text.strip())

					if salary_string !=None:
						print(salary_string.text.strip() )
					else:
						print('TBD')

					link_string = links[0]["href"]
					#print(link_string)
					#print('https://www.indeed.com' + link_string)

					print() 
		else:
			print('Connection issue; try again')



def main():
	ROOT = Tk()
	ROOT.geometry("300x150+400+400")

	#ROOT.withdraw() ##Creates window
	#USER_INP = simpledialog.askstring(title="Indeed Scraper", prompt="Position:") ## User input
	Input = User_Input()	

	text = StringVar()
	text.set("Boston, MA")
	textBox = Entry(ROOT, textvariable = text)	

	ROOT.mainloop()
	Indeed_Scraper(Input.output1,Input.output2) ## Input.output1

main()
#if __name__ =='__main__':
	#m
#print(res)
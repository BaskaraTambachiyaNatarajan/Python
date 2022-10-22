import requests
from bs4 import BeautifulSoup

#Function takes url, tag and attribute to locate element and return array of elements
def getURLdata(url,tag,attr):
  r  = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  links = soup.find_all(tag)
  res=[]

  for i in links:
    res.append(i.get(attr))

  return res

#Function accepts job link and returns details of that job 
def getJobdata(link):
  r  = requests.get(link)
  soup = BeautifulSoup(r.text, "html.parser")
  title = soup.find(attrs={"class":"app-title"}).text.strip()
  location = soup.find(attrs={"class":"location"}).text.strip()
  job_desc = soup.find(attrs={"class":"content-intro"}).next_siblings
  res = {"Title":title, "Location":location}
  key = "Key"

  for i in job_desc:
    if len(str(i))>1 and len(i.get_text())>1:  #To remove empty lines
      if "If this opportunity interests you, you might like these courses on Coursera:" in i.get_text() or "#LI" in i.get_text(): #To remove unnecessary lines after description
        break
      if len(i.get_text())<30 and i.get_text().strip()!="Company Overview": #Irrelevant Comapny overview was removed
        key = i.get_text().strip().replace(":","")
      elif key!="Key" and i.get_text().strip()!="Company Overview":
        if key in res:
          res[key] = res[key]+"\n"+i.get_text().strip()
        else:
          res[key] = i.get_text().strip()

  return res                                    # return dictionary of job description

if __name__=="__main__":
  main_link = 'https://boards.greenhouse.io/embed/job_board?for=coursera'
  jobs_links = getURLdata(main_link,'a','href')
  data = []

  for i in jobs_links:
    i = i.split("=")[1]                         # split job id 
    data.append(getJobdata("https://boards.greenhouse.io/embed/job_app?for=coursera&token="+i)) #using that job id call getJobdata and retrive data

#printing the output
  for i in data:
    for x,y in i.items():
      print(x)
      print(y)
      print("\n")
    print("<!-------------------------------------END-------------------------------------!>")

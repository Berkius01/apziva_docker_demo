from ast import keyword
#from distutils.log import info
#1import string
from time import sleep
from django.shortcuts import render
from .models import Github
#from lib2to3.pgen2 import driver
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#trying bypassing stackoverflow recapctha
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    return render(request, "index.html")

def records(request):
    data={
        "infos":Github.objects.all
    }
    return render(request, "records.html",data)

def stack(request):
    return render(request, "stack.html")


@csrf_exempt
def stackSearch(request):
    try:
        op = Options()
        #ua = UserAgent()
        #useragent = ua.random
            #op.headless=True
        #op.add_argument(f'user-agent={useragent}')
        op.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
        url = "https://stackoverflow.com/"
        topic = request.POST.get("topic")
        driver.get(url)
        sleep(1)
        p=driver.find_element(By.NAME,"q")
        p.send_keys(topic)
        p.submit()
        
        #source = driver.page_source
            #print(source)
        open('github/templates/source.html','wb').write((driver.page_source).encode())
        
        return render(request,"stackres.html")
    except:
        return render(request,"error.html")


#def extract_infos():


@csrf_exempt
def searchkeyword(request):
    try:
        op=Options()
        #op.headless=True

        op.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
        url = "https://github.com"
        keyword = request.POST.get("keyword")
        driver.get(url)
        p=driver.find_element(By.NAME,"q")
        p.send_keys(keyword)
        p.submit()
        source = driver.page_source
        soup = BeautifulSoup(source)
        info = soup.find_all(class_="v-align-middle")
        #open('github/templates/source.html','wb').write((driver.page_source).encode())
        #info = driver.find_element(By.CLASS_NAME,"UnderlineNav UnderlineNav--full d-md-none mb-2 border-top")
        #info = soup.find_all(By.CLASS_NAME,"v-align-middle")
        #print(type(info[8]))
        link = "https://github.com/"
        searchinfo=str(info[8])
        #print(searchinfo)
        start = searchinfo.find(link)
        #print(start)
        end = searchinfo.find('"},"')
        user = searchinfo[start:end]
        index=user.rfind("/")
        user = user[:index]
        #print(user)
        driver.close()

        op = Options()
        op.headless=True
        op.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)

        
        driver.get(user)
        source = driver.page_source
        soup = BeautifulSoup(source)
        #print(driver.find_element(By.CLASS_NAME,"text-bold color-fg-default")) headles olduu için çekemiyor
        #print("geliyo")
        #print(source.find("text-bold color-fg-default"))
        infoList =[]
        #print(soup.find_all(class_="text-bold color-fg-default"))

        infoFollow = soup.find_all(class_="text-bold color-fg-default")
        followKeywords = (" followers"," following")
        i=0

        for res in infoFollow:
            #print(res.text[:7]+followKeywords[i])
            infoList.append(res.text[:7]+followKeywords[i])
            i=i+1


        infoRepoAndStar=soup.find_all(class_="Counter")

        repos=infoRepoAndStar[0]
        star=infoRepoAndStar[7]
        infoList.append(repos.text[:7]+" repos")

        infoList.append(star.text[:7]+" stars")
        #print(infoRepoAndStar[0])
        #print(info.find_all(">"))
        infoContrb=soup.find_all(class_="f4 text-normal mb-2")
        #print(infoContrb)
        #infoList.append(infoContrb[0].text.strip())
        infoList.append(infoContrb[0].text[7:-5])
        driver.save_screenshot("test.png")

        print(infoList)
        indexusername=user.rfind("/")
        username = user[indexusername+1:]
        print(username)
        data = {
            "keyword":keyword,
            "userName":username,
            "followers":infoList[0],
            "following":infoList[1],
            "repos":infoList[2],
            "stars":infoList[3],
            "contrib":infoList[4]
        }
        
        obj = Github(username=username,followers=infoList[0],following=infoList[1],repos=infoList[2],stars=infoList[3],contrb=infoList[4])
        obj.save()

        return render(request,"search.html",data)
        #return render(request,"searchkeyword.html",data)
    except:
        return render(request,"error.html")

@csrf_exempt
def search(request):
    try:
        op = Options()
        op.headless=True
        op.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)

        url = "https://github.com/"
        username = request.POST.get("username")
        url = url +  username
        driver.get(url)
        source = driver.page_source
        soup = BeautifulSoup(source)
        #print(driver.find_element(By.CLASS_NAME,"text-bold color-fg-default")) headles olduu için çekemiyor
        #print("geliyo")
        #print(source.find("text-bold color-fg-default"))
        infoList =[]
        #print(soup.find_all(class_="text-bold color-fg-default"))

        infoFollow = soup.find_all(class_="text-bold color-fg-default")
        followKeywords = (" followers"," following")
        i=0

        for res in infoFollow:
            #print(res.text[:7]+followKeywords[i])
            infoList.append(res.text[:7]+followKeywords[i])
            i=i+1


        infoRepoAndStar=soup.find_all(class_="Counter")

        repos=infoRepoAndStar[0]
        star=infoRepoAndStar[7]
        infoList.append(repos.text[:7]+" repos")

        infoList.append(star.text[:7]+" stars")
        #print(infoRepoAndStar[0])
        #print(info.find_all(">"))
        infoContrb=soup.find_all(class_="f4 text-normal mb-2")
        #print(infoContrb)
        #infoList.append(infoContrb[0].text.strip())
        infoList.append(infoContrb[0].text[7:-5])
        driver.save_screenshot("test.png")
        print(infoList)
        data = {
            "keyword":username,
            "userName":username,
            "followers":infoList[0],
            "following":infoList[1],
            "repos":infoList[2],
            "stars":infoList[3],
            "contrib":infoList[4]
        }
        
        obj = Github(username=username,followers=infoList[0],following=infoList[1],repos=infoList[2],stars=infoList[3],contrb=infoList[4])
        obj.save()
        return render(request,"search.html",data)
    except:
        return render(request,"error.html")
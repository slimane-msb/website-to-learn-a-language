
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def getUrl(urly): ##urly is for url youtube (the original one) this fucntion to get the url we need for html to work

    urlsimpleA="https://www.youtube.com/embed/"
    urlsimpleB="?mute=0&amp;showinfo=1&amp;controls=1&amp;start=0"

    start=urly.find('=',0)
    end=urly.find('=',start+1)

    if (end!=(-1)):
       urlId=urly[start+1:end]   ## urlId is the id exemple id=vmEHCJpfslg
    else :
         urlId=urly[start+1:]

    if(urlId[-5]=='&'):
        urlId=urlId[:-5]

    urlVid=urlsimpleA + urlId + urlsimpleB  ## urlVid one to get the url we need for html vid

    return urlVid


def index(request):

    urlVid="https://www.youtube.com/embed/vmEHCJofslg?mute=0&amp;showinfo=1&amp;controls=1&amp;start=0"
   
    return render(request, 'index.html', {'urlVid2':urlVid})


def playVid(request):

    urly = ""
    urly = str(request.POST['urly'])                 ## we gonna get the url with post methode from the search bare and put it to video url to run the video 

    urlVid2=getUrl(urly)   ## urlVid2 = "https://www.youtube.com/embed/vmEHCJofslg?mute=0&amp;showinfo=1&amp;controls=1&amp;start=0"
    
    return render(request, 'index.html', {'urlVid2': urlVid2})






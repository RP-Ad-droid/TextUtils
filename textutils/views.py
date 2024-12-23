#this is the  file that i have created -- rohini

#our view return http request
from django.http import HttpResponse

from django.shortcuts import render
import  os

# #define the path to the file
# file_path = "../one.txt"
#
# #opening the file  and checkinng whethter the file exist or not
# if os.path.exists(file_path):
#     with open("../one.txt", 'r') as f:
#         content = f.read()
#
# else:
#     content = "file not found"

#this is the exercise personal naviagator

# def index(request):
#
#     return HttpResponse('''<h1>PERSONAL NAVIGATOR</h1> <a href = "https://monkeytype.com/">
#     Monkeytype</a><br>
#     <a href = "https://hianime.to/watch/haikyu-movie-battle-of-the-garbage-dump-18922?ep=128840&ep=128840&ep=128840&ep=128840&ep=128840&ep=128840">
#     Haikyu Movie-Battle of the garbage dump</a><br>
#     <a href = "https://chatgpt.com/?oai-dm=1"> Chatgpt \n</a><br>
#     <a href = "https://www.youtube.com/watch?v=MfUsyUq5awY&list=PLwqCsahO7nSJ6TVFhD8AYYyOYN9caEZ2v&index=4">
#     MAthematics-Differntial Eqn</a><br>
#
#
#     ''')#we can put the html in the double quotes
#
#
# def about(request):
#     return HttpResponse("about larry")




#adding pipeline
def index(request):

    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text' , 'default')
    print(djtext)

    #checkboxes values check
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    extraspaceremover = request.POST.get('extraspaceremover' , 'off')
    charactercounter = request.POST.get('charactercounter','off')
    counter = 0
    space_counter = 0

    #analyze the text
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''.,?!:;'"()[]{}<>-–—.../\|_~@#$%^*&=+><||`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose' : 'Remove Punctuations','analyzed_text' : analyzed}
        djtext = analyzed


    if  fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed =  analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " ") :
                analyzed = analyzed + char


        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed



    if charactercounter == "on":
        for char in djtext:
            if char == " " :
                space_counter += 1
            else:
                counter += 1
        analyzed = "Character counted = " + str(counter) + "\n"+ "Space counted = "+ str(space_counter)
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover !="on" and charactercounter !="on":
        return HttpResponse("Error ! please select any operation and try again")


    return render(request, 'analyze.html', params)

def contactus(request):
    return render(request,"contactus.html")



def aboutus(request):
    return render(request,"aboutus.html")


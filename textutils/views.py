#Created by me...
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinereomove = request.POST.get('newlinereomove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    #remove punctuation
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #uppercase all
    elif(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #new line remover
    elif(newlinereomove =="on"):
        analyzed =""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed+char
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #new line remover
    elif(extraspaceremove =="on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char
        params = {'purpose': 'Removed extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the checkbox...!!!")
#def capfirst(request):
#    return HttpResponse("Capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremover(request):
#     return HttpResponse("spaceremover")
#
# def charcount(request):
#     return HttpResponse("charcount")
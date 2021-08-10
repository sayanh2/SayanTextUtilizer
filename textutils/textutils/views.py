from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyzer(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
    charCounter = request.POST.get('charCounter', 'off')


    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        djtext = analyzed
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    # print(djtext)


    if uppercase == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        djtext = analyzed
        params = {'purpose': 'Converting to uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)



    if newLineRemover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!= '\r':
                analyzed += char

        djtext = analyzed
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)


    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char


        djtext = analyzed
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)


    if charCounter == 'on':
        count = 0
        for char in djtext:
            count += 1

        # djtext = analyzed
        params = {'purpose': 'Character Counter', 'analyzed_text': count}
        # return render(request, 'analyze.html', params)


    if(removepunc != 'on' and uppercase != 'on' and newLineRemover != 'on' and extraSpaceRemover != 'on' and charCounter != 'on'):
        return HttpResponse('Please check the removed punctuation checkbox')

    return render(request, 'analyze.html', params)




from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordcountdict = {}

    for word in wordlist:
        if word in wordcountdict:
            wordcountdict[word] += 1
        else: 
            wordcountdict[word] = 1
    
    sorted_words = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordcountdict': sorted_words})
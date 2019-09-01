from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('<h1>This is my home page</h1>')
    return render(request,'home.html')
# ,{'name':'Hi there raju'}

def count(request):
    data = request.GET['fulltextarea']
    word_list =data.split()
    list_length =len(word_list)
    # print(data)

    worddictionary = {}


    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

        sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)





    return render(request,'count.html',{'fulltext':data, 'words':list_length,'worddictionary':sorted_list})

    

# def contac(request):
#     return HttpResponse('<h1>Contact Page</h1></br>This is our contact page')

# def about(request):
#      return HttpResponse('<h1>About Page</h1></br>This is our about page')
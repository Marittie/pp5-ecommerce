from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
    

def Subscribe(request):
    """ A view to return the mailchimp page """

    return render(request, 'home/subscribe.html')
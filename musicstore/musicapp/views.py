from django.shortcuts import render
from .models import Artist
from .models import Record
from .models import Review
from django.shortcuts import render, get_object_or_404
from .forms import RecordForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'musicapp/index.html')

def records (request):
    records_list=Record.objects.all()
    return render (request, 'musicapp/records.html' , {'records_list': records_list})

def artists (request):
    artist_list=Artist.objects.all()
    return render (request, 'musicapp/artists.html' , {'artist_list': artist_list})

def reviews (request):
    review_list=Review.objects.all()
    return render (request, 'musicapp/reviews.html' , {'review_list': review_list})

def recorddetail (request, id): 
    detail=get_object_or_404(Record, pk=id)
    context = {'detail': detail}
    return render (request, 'musicapp/details.html' , context=context)


@login_required
def newRecord(request):
    form=RecordForm
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=RecordForm()

    else:
        form=RecordForm()
    return render(request, 'musicapp/newrecord.html', {'form': form})

def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()

    else:
        form=ReviewForm()
    return render(request, 'musicapp/newreview.html', {'form': form})

def loginmessage(request):
     return render(request, 'musicapp/loginmessage.html')

def logoutmessage(request):
     return render(request, 'musicapp/logoutmessage.html')
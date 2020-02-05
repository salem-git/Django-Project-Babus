from django.shortcuts import render
from .models import Journey
from django.core.paginator import Paginator
import io 
from django.http import FileResponse 

# Create your views here.
def index(response,id):
    ls = Journey.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")

def cutomer_reserve_submission(request):
    print("ticket successfully reserved")
    journey_departure = request.POST["journey_departure"]
    journey_destination = request.POST["journey_destination"]
    journey_date = request.POST["journey_date"]
    journey_numberOfTicket = request.POST["journey_numberOfTicket"]
    journey_seatReserve = request.POST["journey_seatReserve"]

    journey = Journey(departure=journey_departure,destination=journey_destination,date=journey_date,number_of_ticket=journey_numberOfTicket,seat_number=journey_seatReserve )
    journey.save()
    return render(request,"CustomerHome/CustomerHome.html")

def fetch_journey(request): 
    all_journey = Journey.objects.all()

    paginator = Paginator(all_journey,3)
    page = request.GET.get('page')
    journies =  paginator.get_page(page)
    context = {'all_journey':journies}
    return render(request,"CustomerHome/recentJourney.html",context)

def recent_journey_detail(request,rjourney_id):
    single_journey = Journey.objects.get(id=rjourney_id)
    context = {'single_journey':single_journey}
    return render(request,'CustomerHome/recentJourneyDetail.html',context)

def logged(request):
    return render(request,'CustomerHome/CustomerHome.html')
def create(response):
    if response.method == "POST":
        if form.is_valid():
            d=form.cleaned_data["destination"]
            j = Journey(destination=d)
            j.save()
            response.user.journey.add(j)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"CustomerHome/recentJourney.html",{"form":form})
from django.shortcuts import render,redirect
from .models import*
from .forms import*
from django.contrib import messages
from django.db.models import Sum
from .filters import*

# Create your views here.
def home(request):
	form=GetFoodinfoForm()
	if request.method=='POST':
	    form=GetFoodinfoForm(request.POST)
	    if form.is_valid():
	    	a=request.POST.get('food')
	    	foo=str(a)
	    	print(foo)
	    	calcal=foodcal.objects.get(id=foo)
	    	print(calcal)
	    	getcal=calcal.foodcal
	    	print(getcal)
	    	form.save()

	fcal=getfoodinfo.objects.aggregate(cal_sum=Sum('cal'))
	print(fcal)
	items=getfoodinfo.objects.all()		
	context={'form':form,'items':items,'fcal':fcal} 
	return render(request,'calorie/home.html',context)

def dashboard(request):
	items=foodcal.objects.all()
	myfilter=FoodcalFilter(request.GET,queryset=items)
	items=myfilter.qs
	context={'items':items,'myfilter':myfilter}
	return render(request,'calorie/dashboard.html',context)

def view(request,pk):
	views=getfoodinfo.objects.get(id=pk)

	context={'views':views}

	return render(request,'calorie/view.html',context)

def remove(request,pk):
	items=getfoodinfo.objects.get(id=pk)
	if request.method=='POST':
		items.delete()
		return redirect('home')

	context={'items':items}
	return render(request,'calorie/delete.html',context)	
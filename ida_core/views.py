from django.shortcuts import render

def ida_home(request):
	return render(request, 'ida_home.html', {})

def ida_add_internal_microdata(request):
	return render(request, 'ida_add_internal_microdata.html', {})	

def irma_home(request):
	return render(request, 'irma_home.html', {})

def dsm_home(request):
	return render(request, 'dsm_home.html', {})
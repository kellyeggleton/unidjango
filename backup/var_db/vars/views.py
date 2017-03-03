from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import GeneName
from .models import Sequencing
from .models import Classification
from .models import Condition
from .models import Patient_Details
from .models import Variant_Details
from .models import Patient_Variant
from .forms import *
from django.template import RequestContext

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handle_uploaded_file(f):
	print 'WAYHEY'


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['results'], request.POST.get('chromosome'), request.POST.get('gene'))
            return render(request, 'home.html')
        else:
            form = UploadFileForm()
            return render_to_response('home.html')
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form':form})
	

def variants(request): 
    variants = Variant_Details.objects.all()
    return render_to_response('variants.html', {'variants':variants})


def search(request):
	if request.method == 'GET': # If the form is submitted
	        search_query = request.GET.get('search_box')
		variants = Variant_Details.objects.filter(GeneName_ID__GeneName=search_query)
   		return render_to_response('search.html', {'variants':variants})

'''def search(request):
	if request.method == 'POST':
	    form = Variant_DetailsSearchForm(request.POST)
	    if form.is_valid():
		return render(request, 'search.html')'''

def contact (request):
    return render(request,'contact.html')






#def get_variants(request):
 #   gene = request.GET.get('GeneName')
  #  variants = Variant_Details.objects.filter(genename__genename=gene)
  #  return render (request, 'vars/get_variants.html', {GeneName=gene, Variant_Genome=variants})

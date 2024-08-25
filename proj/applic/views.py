from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from applic.form import CustomUserForm
from django.contrib import messages
from applic.form import InstitutionForm
from .models import Institution
from django.contrib.auth.decorators import login_required
from applic.form import DocumentUploadForm
from .models import DocumentUpload
# Create your views here.
def home(request):
    return render(request,'homepg.html')

@login_required
def institution_dashboard(request):
    institutions = Institution.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'institution_dashboard.html', {'institutions': institutions})

@login_required
def institution_detail(request, pk):
    institution = Institution.objects.get(pk=pk)
    return render(request, 'institution_detail.html', {'institution': institution})

def upload_documents(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document_upload = form.save(commit=False)
            document_upload.user = request.user  # Associate with the logged-in user
            document_upload.save()
            messages.success(request, 'Documents uploaded successfully!')
            return redirect('upload_documents')
    else:
        form = DocumentUploadForm()

    return render(request, 'upload_documents.html', {'form': form})

def dashboard(request):
    # Retrieve documents uploaded by the currently logged-in user
    documents = DocumentUpload.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'documents': documents})

def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"login.html")
  
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
  
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
      form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
    return render(request,"register.html",{'form':form})
    
def institution_form_view(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            institution = form.save(commit=False)
            institution.user = request.user  # Associate the form data with the current user
            institution.save()
            return redirect('login')
    else:
        form = InstitutionForm()

    return render(request, 'institution_form.html', {'form': form})

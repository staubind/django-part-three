from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        # print(request.POST)
        form = forms.FormName(request.POST)

    if form.is_valid():
        # DO SOMETHING CODE
        print("VALIDATION SUCCESS!")
        print('NAME is: ', form.cleaned_data['name'])
        print('EMAIL is: ', form.cleaned_data['email'])
        print('TEXT is: ', form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', {'form': form})
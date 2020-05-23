from django.shortcuts import render
from . forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request,'contact/contact.html',context=context)


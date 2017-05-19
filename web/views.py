from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from web.form import AddContactUs


def show_home(request):
    return render(request, "intro.html", {})


def show_about(request):
    return render(request, 'about.html', {})


def view_contact(request):
    form = AddContactUs(request.POST or None)
    context = {'form': form, }
    print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(request.path)

    return render(request, "contact_us.html", context)

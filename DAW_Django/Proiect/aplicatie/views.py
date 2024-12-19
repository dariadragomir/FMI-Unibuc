from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("Primul raspuns")

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Instrument
from aplicatie.forms import InstrumentFilterForm

def filter_instruments(request):
    form = InstrumentFilterForm(request.GET)
    
    if form.is_valid():
        instruments = Instrument.objects.all()

        if form.cleaned_data['nume']:
            instruments = instruments.filter(nume__icontains=form.cleaned_data['nume'])
        if form.cleaned_data['categorie']:
            instruments = instruments.filter(categorie=form.cleaned_data['categorie'])
        if form.cleaned_data['brand']:
            instruments = instruments.filter(brand=form.cleaned_data['brand'])
        if form.cleaned_data['pret_min']:
            instruments = instruments.filter(pret__gte=form.cleaned_data['pret_min'])
        if form.cleaned_data['pret_max']:
            instruments = instruments.filter(pret__lte=form.cleaned_data['pret_max'])
        if form.cleaned_data['stoc_min']:
            instruments = instruments.filter(stoc__gte=form.cleaned_data['stoc_min'])
        if form.cleaned_data['stoc_max']:
            instruments = instruments.filter(stoc__lte=form.cleaned_data['stoc_max'])
        if form.cleaned_data['data_adaugare_min']:
            instruments = instruments.filter(data_adaugare__gte=form.cleaned_data['data_adaugare_min'])
        if form.cleaned_data['data_adaugare_max']:
            instruments = instruments.filter(data_adaugare__lte=form.cleaned_data['data_adaugare_max'])

        # Paginare
        page = request.GET.get('page', 1)
        paginated_instruments = instruments[(page-1)*5:page*5]

        data = {
            'instruments': list(paginated_instruments.values('nume', 'categorie__nume', 'brand__nume', 'pret', 'stoc', 'data_adaugare'))
        }

        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid form data'}, status=400)

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from aplicatie.models import Instrument
from .forms import InstrumentFilterForm

def filter_instruments(request):
    form = InstrumentFilterForm(request.GET)
    
    if form.is_valid():
        instruments = Instrument.objects.all()

        if form.cleaned_data['nume']:
            instruments = instruments.filter(nume__icontains=form.cleaned_data['nume'])
        if form.cleaned_data['categorie']:
            instruments = instruments.filter(categorie=form.cleaned_data['categorie'])
        if form.cleaned_data['brand']:
            instruments = instruments.filter(brand=form.cleaned_data['brand'])
        if form.cleaned_data['pret_min']:
            instruments = instruments.filter(pret__gte=form.cleaned_data['pret_min'])
        if form.cleaned_data['pret_max']:
            instruments = instruments.filter(pret__lte=form.cleaned_data['pret_max'])
        if form.cleaned_data['stoc_min']:
            instruments = instruments.filter(stoc__gte=form.cleaned_data['stoc_min'])
        if form.cleaned_data['stoc_max']:
            instruments = instruments.filter(stoc__lte=form.cleaned_data['stoc_max'])
        if form.cleaned_data['data_adaugare_min']:
            instruments = instruments.filter(data_adaugare__gte=form.cleaned_data['data_adaugare_min'])
        if form.cleaned_data['data_adaugare_max']:
            instruments = instruments.filter(data_adaugare__lte=form.cleaned_data['data_adaugare_max'])

        # Paginare
        page = request.GET.get('page', 1)
        paginated_instruments = instruments[(page-1)*5:page*5]

        data = {
            'instruments': list(paginated_instruments.values('nume', 'categorie__nume', 'brand__nume', 'pret', 'stoc', 'data_adaugare'))
        }

        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid form data'}, status=400)


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Salvăm datele în fișier JSON
            return HttpResponseRedirect('/contact/success/')  # Redirecționăm utilizatorul după trimiterea formularului
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect
from .forms import InstrumentForm

def adauga_instrument(request):
    if request.method == "POST":
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirectăm după salvare
    else:
        form = InstrumentForm()
    return render(request, "adauga_instrument.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirecționează către pagina principală sau altă pagină dorită
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)
            return redirect('index')  # Redirecționează către pagina principală sau altă pagină dorită
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def custom_login_view(request):
    form = CustomAuthenticationForm(data=request.POST or None, request=request)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user is not None and user.is_active:
            login(request, user)
            request.session.set_expiry(0 if not form.cleaned_data.get('remember_me') else 86400)  # 1 zi în secunde
            request.session['user_data'] = {
                'username': user.username,
                'email': user.email,
                'phone_number': getattr(user, 'phone_number', ''),
                'address': getattr(user, 'address', ''),
                'city': getattr(user, 'city', ''),
                'birth_date': getattr(user, 'birth_date', ''),
                'bio': getattr(user, 'bio', ''),
            }
            return redirect('profile')
        else:
            messages.error(request, 'Contul este inactiv.')
    else:
        messages.error(request, 'Nume de utilizator sau parolă incorecte.')
    return render(request, 'login.html', {'form': form})
@login_required
def custom_logout(request):
    logout(request)
    return redirect('index')  # Redirecționează către pagina principală sau altă pagină dorită

@login_required
def profile_view(request):
    user_data = request.session.get('user_data', {})
    return render(request, 'profile.html', {'user_data': user_data})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Parola a fost schimbată cu succes!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
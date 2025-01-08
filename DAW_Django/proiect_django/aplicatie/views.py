from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
def index(request):
    return render(request, 'index.html')

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
    else:
        instruments = Instrument.objects.none()

    return render(request, 'filter_instruments.html', {'form': form, 'instruments': instruments})

from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/contact/success/') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect, get_object_or_404
from .forms import InstrumentForm
from django.contrib.auth.decorators import permission_required, login_required
@login_required
@permission_required('aplicatie.add_instrument', raise_exception=True)
def adauga_instrument(request):
    if not request.user.has_perm('aplicatie.add_instrument'):
        context = {
            'titlu': 'Eroare adaugare produse',
            'mesaj_personalizat': 'Nu ai voie să adaugi produse.',
        }
        return render(request, '403.html', context, status=403)
    
    if request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produsul a fost adăugat cu succes.')
            return redirect('index')
    else:
        form = InstrumentForm()
    return render(request, 'adauga_instrument.html', {'form': form})

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_confirmation_email(user):
    subject = 'Confirmare e-mail'
    html_message = render_to_string('confirmare_email.html', {
        'user' : user,
        'cod': user.cod,
        'site_url': settings.SITE_URL,
    })
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.html import strip_tags
import uuid

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.cod = str(uuid.uuid4())
            if user.username.lower() == 'admin':
                subject = "cineva incearca sa ne preia site-ul"
                message = f"Email: {user.email}"
                html_message = f"<h1 style='color:red;'>cineva incearca sa ne preia site-ul</h1><p>Email: {user.email}</p>"
                mail_admins(subject, message, html_message=html_message)
                messages.error(request, 'Nu puteți folosi acest username.')
                logger.critical("Nu puteți folosi acest username.")
            else:
                user = form.save(commit=False)
                user.is_active = False
                logger.info(f"Utilizatorul  {user.username} inregistrat cu succes! ")
                messages.info(request,f"Utilizatorul  {user.username} inregistrat cu succes! ")
                user.save()
                send_confirmation_email(user)
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def custom_logout(request):
    try:
        permission = Permission.objects.get(codename='vizualizeaza_oferta')
        request.user.user_permissions.remove(permission)
        logger.info(f"Permisiunea 'vizualizeaza_oferta' a fost eliminată pentru utilizatorul {request.user.username}.")
        messages.info(request, f"Permisiunea 'vizualizeaza_oferta' a fost eliminată pentru utilizatorul {request.user.username}.")
    except Permission.DoesNotExist:
        ("Permisiunea 'vizualizeaza_oferta' nu există.")
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    user_data = request.session.get('user_data', {})
    logger.debug(f"user_data: {user_data}")
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

from .models import CustomUser

def confirma_mail(request, cod):
    user = get_object_or_404(CustomUser, cod=cod)
    user.email_confirmat = True
    user.is_active = True 
    user.cod = ''
    user.save()
    return render(request, 'confirmare_succes.html')

from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
failed_logins = {}

def custom_login_view(request):
    form = CustomAuthenticationForm(data=request.POST or None, request=request)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            if user.email_confirmat:
                login(request, user)
                request.session.set_expiry(0 if not form.cleaned_data.get('remember_me') else 86400)
                request.session['user_data'] = {
                    'username': user.username,
                    'email': user.email,
                    'phone_number': getattr(user, 'phone_number', ''),
                    'address': getattr(user, 'address', ''),
                    'city': getattr(user, 'city', ''),
                    'birth_date': user.birth_date.isoformat() if user.birth_date else '',
                    'bio': getattr(user, 'bio', ''),
                }
                return redirect('profile')
            else:
                logger.critical('Trebuie să confirmați emailul înainte de a vă putea autentifica.')
                messages.error(request, 'Trebuie să confirmați emailul înainte de a vă putea autentifica.')
        else:
            logger.critical('Contul este inactiv.')
            messages.error(request, 'Contul este inactiv.')
    elif request.method == 'POST':
        username = request.POST.get('username')
        ip_address = request.META.get('REMOTE_ADDR')
        now = timezone.now()

        if username not in failed_logins:
            failed_logins[username] = []

        failed_logins[username].append(now)

        failed_logins[username] = [time for time in failed_logins[username] if now - time < timedelta(minutes=2)]

        if len(failed_logins[username]) >= 3:
            logger.warning(f"S-a încercat conectarea de 3 ori in 2 minute.")
            messages.warning(request, 'S-a încercat conectarea de 3 ori in 2 minute.')
            subject = "Logari suspecte"
            message = f"Username: {username}\nIP: {ip_address}"
            html_message = f"<h1 style='color:red;'>Logari suspecte</h1><p>Username: {username}</p><p>IP: {ip_address}</p>"
            mail_admins(subject, message, html_message=html_message)
            failed_logins[username] = []  

    return render(request, 'login.html', {'form': form})

from .forms import CustomAuthenticationForm, CustomUserCreationForm, PromotieForm
from django.core.mail import send_mass_mail
from .models import Vizualizare

@login_required
def adauga_promotie(request):
    try:
        if request.method == 'POST':
            form = PromotieForm(request.POST)
            if form.is_valid():
                promotie = form.save()
                categorii = form.cleaned_data['categorii']
                utilizatori = CustomUser.objects.filter(
                    vizualizare__instrument__categorie__in=categorii
                ).distinct()
            #K=1, N=3
                messages_list = []
                for user in utilizatori:
                    html_message = render_to_string('promo_template_1.html', {
                        'subiect': promotie.subiect,
                        'data_expirare': promotie.data_expirare,
                        'mesaj': promotie.mesaj,
                        'cod_promotie': promotie.cod_promotie
                    })
                    plain_message = strip_tags(html_message)
                    messages_list.append((promotie.subiect, plain_message, 'dragomirdariaaa@gmail.com', [user.email]))

                send_mass_mail(messages_list)
                messages.success(request, 'Promoția a fost adăugată și emailurile au fost trimise.')
                return redirect('index')
        else:
            form = PromotieForm()
        return render(request, 'adauga_promotie.html', {'form': form})
    except Exception as e:
        logger.error(f"Eroare în adauga_promotie: {str(e)}")
        subject = "Eroare în aplicație"
        message = f"Eroare: {str(e)}"
        html_message = f"<p style='background-color:red;'>Eroare: {str(e)}</p>"
        mail_admins(subject, message, html_message=html_message)
        messages.error(request, 'A apărut o eroare. Administratorii au fost notificați.')
        return render(request, 'error.html')

import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

logger = logging.getLogger('django')

from django.core.mail import mail_admins
def some_view(request):
    try:
        logger.debug("some_view has been called")
        result = 1 / 0 
    except Exception as e:
        logger.error(f"Eroare în some_view: {str(e)}")
        subject = "Eroare în aplicație"
        message = f"Eroare: {str(e)}"
        html_message = f"<p style='background-color:red;'>Eroare: {str(e)}</p>"
        mail_admins(subject, message, html_message=html_message)
        messages.error(request, 'A apărut o eroare. Administratorii au fost notificați.')
        return render(request, 'error.html')
    
    logger.debug("some_view has completed successfully")
    return render(request, 'login.html')
    
from django.contrib.auth.models import Permission
@login_required
def aloca_permisiune_oferta(request):
    permission = Permission.objects.get(codename='vizualizeaza_oferta')
    request.user.user_permissions.add(permission)
    logger.info(f"Permisiunea 'vizualizeaza_oferta' a fost alocată utilizatorului {request.user.username}.")
    return redirect('oferta')

@login_required
def oferta_view(request):
    if not request.user.has_perm('aplicatie.vizualizeaza_oferta'):
        logger.warning(f"Utilizatorul {request.user.username} a încercat să vizualizeze oferta fără permisiune.")
        messages.error(request, 'Nu ai voie să vizualizezi oferta.')
        context = {
            'titlu': 'Eroare afisare oferta',
            'mesaj_personalizat': 'Nu ai voie să vizualizezi oferta.',
        }
        return render(request, '403.html', context, status=403)
    
    oferte = Promotie.objects.all()
    context = {
        'oferte': oferte,
    }
    return render(request, 'oferta.html', context)


def custom_403_view(request, exception):
    context = {
        'titlu': 'Eroare 403',
        'mesaj_personalizat': 'Nu este permis accesul la resursa curentă.',
    }
    return render(request, '403.html', context, status=403)

handler403 = custom_403_view

from .models import Instrument, Promotie

def instrument_detail(request, id):
    instrument = get_object_or_404(Instrument, id=id)
    return render(request, 'instrument_detail.html', {'instrument': instrument})

def instrument_list(request):
    instruments = Instrument.objects.all()
    return render(request, 'instrument_list.html', {'instruments': instruments})

def promotie_detail(request, id):
    promotie = get_object_or_404(Promotie, id=id)
    return render(request, 'promotie_detail.html', {'promotie': promotie})


from .models import Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    instrument = get_object_or_404(Instrument, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, instrument=instrument)
    if not created:
        if cart_item.quantity < instrument.stoc:
            cart_item.quantity += 1
        else:
            messages.error(request, 'Nu puteți adăuga mai multe produse decât sunt disponibile în stoc.')
            return redirect('instrument_detail', id=product_id)
    else:
        cart_item.quantity = 1
    cart_item.save()
    messages.success(request, f"{instrument.nume} a fost adăugat în coș.")
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    sort_by = request.GET.get('sort_by', 'nume')

    if sort_by == 'pret':
        cart_items = cart.cartitem_set.all().order_by('instrument__pret')
    else:
        cart_items = cart.cartitem_set.all().order_by('instrument__nume')

    return render(request, 'cart_detail.html', {'cart': cart, 'cart_items': cart_items, 'sort_by': sort_by})

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0 and quantity <= cart_item.instrument.stoc:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            messages.error(request, 'Cantitatea introdusă nu este validă.')
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, 'Produsul a fost eliminat din coș.')
    return redirect('cart_detail')

@login_required
def increment_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity < cart_item.instrument.stoc:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.error(request, 'Nu puteți adăuga mai multe produse decât sunt disponibile în stoc.')
    return redirect('cart_detail')

@login_required
def decrement_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

from .models import Order, OrderItem
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.cartitem_set.exists():
        messages.error(request, "Cosul este gol.")
        return redirect('cart_detail')

    total_price = sum(item.quantity * item.instrument.pret for item in cart.cartitem_set.all())
    order = Order.objects.create(user=request.user, total_price=total_price)

    for cart_item in cart.cartitem_set.all():
        OrderItem.objects.create(
            order=order,
            instrument=cart_item.instrument,
            quantity=cart_item.quantity,
            price=cart_item.instrument.pret
        )
        cart_item.instrument.stoc -= cart_item.quantity
        cart_item.instrument.save()

    cart.cartitem_set.all().delete()

    pdf_path = generate_invoice(order)

    send_invoice_email(request, order, pdf_path)

    messages.success(request, "Comanda a fost plasata cu succes! Confirmarea a fost trimisa pe email.")
    return redirect('cart_detail')
import os
import time

def generate_invoice(order):
    user_folder = f"temporar-facturi/{order.user.username}/"
    os.makedirs(user_folder, exist_ok=True)
    pdf_path = os.path.join(user_folder, f"factura-{int(time.time())}.pdf")

    with open(pdf_path, "wb") as pdf_file:
        c = canvas.Canvas(pdf_file, pagesize=letter)

        c.drawString(100, 800, f"Factura pentru comanda {order.id}")
        c.drawString(100, 780, f"Data: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        c.drawString(100, 760, f"Client: {order.user.username} ({order.user.email})")

        y = 720
        cnt = 0
        for item in order.items.all():
            nume_instrument = item.instrument.nume
            cnt += item.quantity

            c.drawString(100, y, f"{nume_instrument} (x{item.quantity}) - ${item.price}")

            y -= 20

        y -= 20
        c.drawString(100, y, f"Total: ${order.total_price}")
        c.drawString(100, y - 20, f"Total produse: {cnt}")
        c.drawString(100, y - 40, f"Contact administrator: dragomirdarianicoleta@gmail.com")
        c.save()

    return pdf_path

from django.core.mail import EmailMessage

def send_invoice_email(request, order, pdf_path):
    subject = f"Factura pentru comanda {order.id}"
    message = render_to_string('email/invoice_email.html', {'order': order, 'settings': settings})
    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [request.user.email],
    )
    email.content_subtype = "html" 
    email.attach_file(pdf_path)
    email.send()

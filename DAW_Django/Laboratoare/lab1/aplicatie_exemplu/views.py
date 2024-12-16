from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import date
import re

nr_acc = 0
def index(request):
    global nr_acc
    nr_acc+=1
    return HttpResponse("Primul raspuns")

def pag1(request):
    global nr_acc
    nr_acc+=1
    return HttpResponse(2+3)

def mesaj(request):
    global nr_acc
    nr_acc+=1
    return HttpResponse("Buna ziua!")
def data(request):
    global nr_acc
    nr_acc+=1
    return HttpResponse(str(date.today()))

def nr_accesari(request):
    global nr_acc
    nr_acc+=1
    return HttpResponse(str(nr_acc))

def suma(request):
    global nr_acc
    nr_acc+=1
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    sum=a+b
    return HttpResponse(str(sum))

#se apleaza in bara de cautare  suma?a=2&b=25

valori_valide = []
def text(request):
    cuv = str(request.GET.get('t', ''))
    if cuv.isalpha():
        valori_valide.append(cuv)

    paragraf = ""
    for valoare in valori_valide:
        paragraf += f"<p>{valoare}</p>"
    return HttpResponse(paragraf)

def nr_parametri(request):
    global nr_acc
    nr_acc+=1
    parametri = request.GET
    numar_parametri = len(parametri)
    return HttpResponse(f"Numarul de parametri primiti este: {numar_parametri}")

#request.GET: este o instanta a unui dicționar care contine toti parametrii trimisi printr-o cerere GET

def operatie(request):
    a = int(request.GET.get('a', 0)) 
    b = int(request.GET.get('b', 0))
    operatie = str(request.GET.get('operatie', ''))

    if operatie == 'sum':
        rezultat = a + b
    elif operatie == 'dif':
        rezultat = a - b
    elif operatie == 'mul':
        rezultat = a * b
    elif operatie == 'div':
        if b == 0:
            return HttpResponse("eroare: Împărimpartireațirea la 0 nu este permisa.")
        rezultat = a / b
    elif operatie == 'mod':
        if b == 0:
            return HttpResponse("eroare: impartirea la 0 nu este permisa.")
        rezultat = a % b
    else:
        return HttpResponse("operatie invalida")
    return HttpResponse(f"rezultatul operației {operatie} este: {rezultat}")

def tabel(request):
    matrice = [
        [1, 1, 2, 3],
        [5, 8, 13, 21],
        [34, 55, 89, 144]
    ]
    html = "<table border='1' cellpadding='7' cellspacing='2'>"
    
    for linie in matrice:
        html += "<tr>"
        for elem in linie:
            html += f"<td>{elem}</td>"
        html += "</tr>"
    html += "</table>"
    return HttpResponse(html)

def lista(request):
    list = ["unu", "doi", "trei", "patru", "cinci", "sase", "sapte"]
    param = request.GET.getlist('cuvinte')
    html = ""
    for cuvant in list:
        if cuvant in param:
            html += f"<span style='color:red'>{cuvant}</span> "
        else:
            html += f"{cuvant} "
    return HttpResponse(html)

#request.GET.getlist('cuvinte') returneaz ao lista cu toti parametrii
#request.GET.get('cuvinte') returneaza o singura valoare

elevi = []
elevi_clasa_minima = []
elevi_clasa_maxima = []
def elev(request):
    nume = request.GET.get('nume', '')
    prenume = request.GET.get('prenume', '')
    clasa = int(request.GET.get('clasa', 0))
    elevi.append({'nume': nume, 'prenume': prenume, 'clasa': clasa})

    clasa_min = 13
    clasa_max = -1
    for elev in elevi:
        if elev['clasa'] < clasa_min:
            clasa_min = elev['clasa']
            elevi_clasa_minima = [elev]
        if elev['clasa'] > clasa_max:
            clasa_max=elev['clasa']
            elevi_clasa_maxima = [elev]
            
    for elev in elevi:
        if elev['clasa']==clasa_min and elev not in elevi_clasa_minima:
            elevi_clasa_minima.append(elev)
        if elev['clasa']==clasa_max and elev not in elevi_clasa_maxima:
            elevi_clasa_maxima.append(elev)

    text = ""
    for elev in elevi_clasa_minima:
        text += f"{elev['nume']} {elev['prenume']}, clasa {elev['clasa']}\n"

    text += "\n"
    for elev in elevi_clasa_maxima:
        text += f"{elev['nume']} {elev['prenume']}, clasa {elev['clasa']}\n"
    return HttpResponse(text)


l=[]
def pag2(request):
    global l
    a=request.GET.get("a",10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit</b>: {l}")

def afis_cod(request,id):
    return HttpResponse(f"<b>Am primit codul:</b> {id}")

#Laborator2 - regex
#1
numar_cereri = 0
suma_numerelor = 0
def aduna_numere(request):
    global numar_cereri, suma_numerelor

    if re.search(r'/pag/\w*\d+$', request.path):
        numar = int(re.findall(r'\d+$', request.path)[0])
        suma_numerelor += numar
        numar_cereri += 1
        response_text = f"numar cereri: {numar_cereri} suma numere: {suma_numerelor}"
        return HttpResponse(response_text)
    else:
        numar_cereri += 1
        return HttpResponse("")
    
#2
def afiseaza_liste(request):
    param_a = request.GET.getlist('a')
    param_b = request.GET.getlist('b')
    response_html = '<html><body>'

    if param_a:
        response_html += '<h3>a:</h3>'
        response_html += '<ul>'
        for value in param_a:
            response_html += f'<li>{value}</li>'
        response_html += '</ul>'

    if param_b:
        response_html += '<h3>b:</h3>'
        response_html += '<ul>'
        for value in param_b:
            response_html += f'<li>{value}</li>'
        response_html += '</ul>'

    response_html += '</body></html>'
    return HttpResponse(response_html)

#3
numar_nume = 0
def numara_nume(request, path):
    global numar_nume
    pattern = r'^[A-Z][a-z]*(?:-[A-Z][a-z]*)?\s*\+\s*[A-Z][a-z]*$'
    if re.match(pattern, path):
        numar_nume += 1
        response_text = f"Numarul de nume primite: {numar_nume}"
    else:
        response_text = "Nume invalid"
    return HttpResponse(response_text)

#4
#accesare http://127.0.0.1:8000/aplicatie_exemplu/subsir/123ab456/
def cauta_subsir(request, parametru):
    pattern = r'^\d*[ab]+\d*$'
    match = re.fullmatch(pattern, parametru)
    if match:
        subsir = re.search(r'[ab]+', parametru).group()
        lungime = len(subsir)
        return HttpResponse(f"Lungimea subsirului este: {lungime}")
    else:
        return HttpResponse("Format incorect de URL.")
#5
def operatii_view(request):
    d = {
        "lista": [
            {"a": 10, "b": 20, "operatie": "suma"},
            {"a": 40, "b": 20, "operatie": "diferenta"},
            {"a": 25, "b": 30, "operatie": "suma"},
            {"a": 40, "b": 30, "operatie": "diferenta"},
            {"a": 100, "b": 50, "operatie": "diferenta"}
        ]
    }

    for item in d["lista"]:
        if item["operatie"] == "suma":
            item["rezultat"] = item["a"] + item["b"]
        elif item["operatie"] == "diferenta":
            item["rezultat"] = item["a"] - item["b"]

    return render(request, 'operatii.html', {'d': d})

from django.contrib.auth.forms import CustomUserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inregistrare.html', {'form': form})

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not form.cleaned_data.get('ramane_logat'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(2*7*24*60*60)  # 2 săptămâni în secunde            
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


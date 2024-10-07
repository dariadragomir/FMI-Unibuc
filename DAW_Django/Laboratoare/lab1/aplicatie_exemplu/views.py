from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import date

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
def elev(request):
    nume = request.GET.get('nume', '')
    prenume = request.GET.get('prenume', '')
    clasa = int(request.GET.get('clasa', 0))
    elevi.append({'nume': nume, 'prenume': prenume, 'clasa': clasa})

    clasa_min = 13
    clasa_max = -1
    for elev in elevi:
        clasa_min = min(elev['clasa'], clasa_min)
        clasa_max = max(elev['clasa'], clasa_max)
    elevi_clasa_minima = [elev for elev in elevi if elev['clasa'] == clasa_min]
    elevi_clasa_maxima = [elev for elev in elevi if elev['clasa'] == clasa_max]

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

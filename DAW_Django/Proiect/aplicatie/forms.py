from django import forms
from aplicatie.models import Instrument, Categorie, Brand

class InstrumentFilterForm(forms.Form):
    nume = forms.CharField(max_length=100, required=False)
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), required=False)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False)
    pret_min = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    pret_max = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    stoc_min = forms.IntegerField(required=False)
    stoc_max = forms.IntegerField(required=False)
    data_adaugare_min = forms.DateField(widget=forms.SelectDateWidget(), required=False)
    data_adaugare_max = forms.DateField(widget=forms.SelectDateWidget(), required=False)

from django import forms
import re
from django.core.exceptions import ValidationError
from datetime import datetime

# Validare pentru nume, prenume și subiect
def validate_name(value):
    if not re.match(r'^[A-Z][a-zA-Z]*$', value):
        raise ValidationError(f'{value} trebuie să înceapă cu literă mare și să conțină doar litere.')

# Validare pentru mesaj
def validate_message(value):
    if len(value.split()) < 5 or len(value.split()) > 100:
        raise ValidationError('Mesajul trebuie să conțină între 5 și 100 cuvinte.')
    if re.search(r'(http://|https://)', value):
        raise ValidationError('Mesajul nu poate conține linkuri.')
    return value

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=10, required=True, validators=[validate_name])
    prenume = forms.CharField(max_length=50, required=False, validators=[validate_name])
    data_nasterii = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, datetime.now().year+1)))
    email = forms.EmailField(required=True)
    confirmare_email = forms.EmailField(required=True)
    tip_mesaj = forms.ChoiceField(choices=[('reclamatie', 'Reclamație'), ('intrebare', 'Întrebare'),
                                          ('review', 'Review'), ('cerere', 'Cerere'), ('programare', 'Programare')])
    subiect = forms.CharField(max_length=100, required=True, validators=[validate_name])
    zile_asteptare = forms.IntegerField(min_value=1, required=True)
    mesaj = forms.CharField(widget=forms.Textarea, required=True, validators=[validate_message])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirmare_email = cleaned_data.get("confirmare_email")
        nume = cleaned_data.get("nume")
        mesaj = cleaned_data.get("mesaj")

        if email != confirmare_email:
            raise ValidationError("Email-ul și confirmarea email-ului nu coincid.")

        # Verificăm semnătura la finalul mesajului
        if mesaj and not mesaj.endswith(nume):
            raise ValidationError(f"Mesajul trebuie să se semneze cu {nume}.")

        # Verificăm dacă expeditorul este major
        data_nasterii = cleaned_data.get("data_nasterii")
        if data_nasterii:
            birth_date = datetime.strptime(str(data_nasterii), '%Y-%m-%d')
            age_in_months = (datetime.now() - birth_date).days // 30
            if age_in_months < 18 * 12:
                raise ValidationError("Trebuie să fii major pentru a trimite un mesaj.")

        return cleaned_data

    def save(self):
        # Preprocesare: calculăm vârsta în ani și luni
        data_nasterii = self.cleaned_data['data_nasterii']
        birth_date = datetime.strptime(str(data_nasterii), '%Y-%m-%d')
        age_in_months = (datetime.now() - birth_date).days // 30
        age_years = age_in_months // 12
        age_months = age_in_months % 12

        # Preprocesarea mesajului
        mesaj = self.cleaned_data['mesaj']
        mesaj = re.sub(r'\s+', ' ', mesaj.replace('\n', ' ')).strip()

        # Salvarea într-un fișier JSON
        import json
        import os
        from time import time

        data = {
            "nume": self.cleaned_data['nume'],
            "prenume": self.cleaned_data['prenume'],
            "data_nasterii": f"{age_years} ani și {age_months} luni",
            "email": self.cleaned_data['email'],
            "tip_mesaj": self.cleaned_data['tip_mesaj'],
            "subiect": self.cleaned_data['subiect'],
            "zile_asteptare": self.cleaned_data['zile_asteptare'],
            "mesaj": mesaj,
            "semnatura": self.cleaned_data['nume']
        }

        folder = 'aplicatie/mesaje'
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = int(time())
        with open(f"{folder}/mesaj_{timestamp}.json", 'w') as f:
            json.dump(data, f)

        return data

from django import forms
from .models import Instrument

class InstrumentForm(forms.ModelForm):
    # Campuri din model care vor fi afișate
    nume = forms.CharField(
        max_length=50,
        label="Nume instrument",
        help_text="Introduceți un nume unic pentru instrument.",
        error_messages={
            "required": "Numele instrumentului este obligatoriu.",
            "max_length": "Numele nu poate depăși 50 de caractere.",
        }
    )
    pret = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        label="Preț instrument",
        error_messages={
            "required": "Prețul este obligatoriu.",
            "invalid": "Introduceți un număr valid pentru preț.",
        }
    )

    # Campuri adiționale care nu există în model
    reducere = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        label="Reducere (%)",
        required=False,
        initial=0,
        help_text="Introduceți reducerea în procente (dacă există).",
        error_messages={
            "invalid": "Reducerea trebuie să fie un număr valid.",
        }
    )
    cantitate_adaugata = forms.IntegerField(
        label="Cantitate adăugată în stoc",
        min_value=1,
        required=True,
        error_messages={
            "required": "Introduceți o cantitate.",
            "invalid": "Cantitatea trebuie să fie un număr întreg.",
            "min_value": "Cantitatea trebuie să fie mai mare decât 0.",
        }
    )
    data_adaugare = forms.DateTimeField(
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    required=True,
    label="Data adăugării"
    )
    
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        label="Brand",
        required=True,
        help_text="Selectați un brand pentru instrument.",
        error_messages={
            "required": "Brand-ul este obligatoriu."
        }
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        label="Categorie",
        required=True,
        help_text="Selectați o categorie pentru instrument.",
        error_messages={
            "required": "Categoria este obligatorie."
        }
    )


    class Meta:
        model = Instrument
        fields = ['nume', 'pret', 'brand', 'categorie']  # Nu afișăm toate câmpurile modelului
        labels = {
            "nume": "Nume instrument",
            "pret": "Preț (în RON)",
            "brand": "Brand",
            "categorie": "Categorie"
        }

    def clean_pret(self):
        pret = self.cleaned_data.get("pret")
        if pret and pret <= 0:
            raise forms.ValidationError("Prețul trebuie să fie mai mare decât 0.")
        return pret

    def clean_reducere(self):
        reducere = self.cleaned_data.get("reducere")
        if reducere and (reducere < 0 or reducere > 100):
            raise forms.ValidationError("Reducerea trebuie să fie între 0 și 100%.")
        return reducere

    def clean(self):
        cleaned_data = super().clean()
        pret = cleaned_data.get("pret")
        reducere = cleaned_data.get("reducere")

        # Validare între câmpuri: reducerea să nu fie mai mare decât 50% din preț
        if pret and reducere and reducere > 50:
            raise forms.ValidationError("Reducerea nu poate depăși 1/2 din preț.")
        
        return cleaned_data

    def save(self, commit=True):
        instrument = super().save(commit=False)
        reducere = self.cleaned_data.get("reducere")
        cantitate_adaugata = self.cleaned_data.get("cantitate_adaugata")

        # Calculăm prețul final în funcție de reducere
        if reducere:
            pret_initial = instrument.pret
            instrument.pret = pret_initial - (pret_initial * reducere / 100)

        # Adăugăm cantitatea la stoc
        instrument.stoc += cantitate_adaugata

        # Setăm data adăugării dacă nu există
        instrument.data_adaugare = self.cleaned_data.get("data_adaugare")


        if commit:
            instrument.save()
        return instrument
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'address', 'city', 'birth_date', 'bio')
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Numărul de telefon trebuie să conțină doar cifre.")
        return phone_number

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address and len(address) < 10:
            raise forms.ValidationError("Adresa trebuie să conțină cel puțin 10 caractere.")
        return address

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date.year < 1900:
            raise forms.ValidationError("Data nașterii trebuie să fie după anul 1900.")
        return birth_date

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label="Ține-mă minte")
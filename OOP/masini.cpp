#include <iostream>
#include <vector>
#include <memory>
#include <unordered_map>
using namespace std;

class Masina {
protected:
    int an;
    string nume;
    int vmax, greutate;
    float autonomie;
public:
    Masina();
    Masina(int an, string nume, int vmax, int greutate);
    virtual ~Masina() {};
    void setAutonomie(float a)
    {
        this->autonomie = a;
    }
    float getAutonomie() const{
        return autonomie;
    }
    int getgreutate() const{
        return greutate;
    }
    void setViteza(int v){
        this->vmax=v;
    }
    int getViteza(){
        return vmax;
    }
    string getMarca() const{
        return nume;
    }
    friend istream &operator>> (istream &in, Masina& masina);
    friend ostream &operator<< (ostream &out, Masina& masina);
};

istream &operator>> (istream &in, Masina& masina) {
    cout << "Introduceti anul" << '\n';
    in >> masina.an;
    cout << "Introduceti numele modelului" << '\n';
    in >> masina.nume;
    cout << "Introduceti viteza maxima" << '\n';
    in >> masina.vmax;
    cout << "Introduceti greutatea" << '\n';
    in >> masina.greutate;
    return in;
}

ostream &operator<< (ostream &out, Masina& masina) {
     out << masina.an << '\n';
     out << masina.nume << '\n';
     out << masina.vmax << '\n';
     out << masina.greutate << '\n';
    return out;
}

Masina::Masina(){
    this->an = 0;
    this->nume = "nedefinit";
    this->vmax = 0;
    this->greutate = 0;
}
Masina::Masina(int an, string nume, int vmax, int greutate){
    this->an = an;
    this->nume = nume;
    this->vmax = vmax;
    this->greutate = greutate;
}

class Combustibil : virtual public Masina{
protected:
    int tip;
    int capacitate;
    
public:
    Combustibil();
    Combustibil(int an, string nume, int vmax, int greutate, int tip, int capacitate);
    float getcapacitate()const{
        return capacitate;
    }
    friend istream &operator>>(istream &in, Combustibil& masina);
    friend ostream &operator<<(ostream &out, const Combustibil& masina);
};

istream &operator>>(istream &in, Combustibil& masina){
    in>>(Masina&) masina;
    cout<<"Tipul: ";
    in>>masina.tip;
    cout<<"Capacitate: ";
    in>>masina.capacitate;
    return in;
}
ostream &operator<<(ostream &out, const Combustibil& masina){
    out<<(Masina&) masina;
    out<<masina.tip<<'\n';
    out<<masina.capacitate<<'\n';
    return out;
}
Combustibil::Combustibil():Masina(){
    this->tip = 1;
    this->capacitate = 0;
}
Combustibil::Combustibil(int an, string nume, int vmax, int greutate, int tip, int capacitate):Masina(an, nume, vmax, greutate)
{
    this->tip = tip;
    this->capacitate = capacitate;
}

class Electric : virtual public Masina{
protected:
    int capacitate_baterie;
public:
    Electric();
    Electric(int an, string nume, int vmax, int greutate,int capacitate_baterie);

    friend istream &operator>>(istream &in, Electric& masina);
    friend ostream &operator<<(ostream &out, const Electric& masina);
};

istream &operator>>(istream &in, Electric& masina){
    in>>(Masina&) masina;
    cout<<"Introdu capacitate baterie ";
    in>>masina.capacitate_baterie;

    return in;
}
ostream &operator<<(ostream &out, const Electric& masina){
    out<<(Masina&) masina;
    out<<"Capacitate baterie: ";
    out<<masina.capacitate_baterie;
    out<<'\n';

    return out;
}
Electric::Electric():Masina(){
    this->capacitate_baterie = 0;
}
Electric::Electric(int an, string nume, int vmax, int greutate,int capacitate_baterie):Masina(an, nume, vmax, greutate)
{
    this->capacitate_baterie = 0;
}

class Hibrid : public Combustibil, public Electric{
public:
    Hibrid();
    Hibrid(int an, string nume, int vmax, int greutate, string tip, int capacitate, int capacitate_baterie);

    friend istream &operator>>(istream &in, Hibrid& drum);
    friend ostream &operator<<(ostream &out, Hibrid& drum);
};
Hibrid::Hibrid():Combustibil(), Electric(){};


istream &operator>>(istream &in, Hibrid& masina){
    in>>(Combustibil&) masina;
    in>>(Electric&) masina;
    
    return in;
}

ostream &operator<<(ostream &out, const Hibrid& masina){
    out<<(Combustibil&) masina;
    out<<(Electric &) masina;
    return out;
}

class Tranzactie{
private:
    string nume_c;
    string data;
    int nr_masini;
    vector<shared_ptr<Masina>> masiniv;
public:
    Tranzactie(){};
    ~Tranzactie(){};
    const vector<shared_ptr<Masina>>& getMasiniv() const{
        return masiniv;
    }
    friend istream &operator>>(istream &in, Tranzactie& tranzactie);
    friend ostream &operator<<(ostream &out, const Tranzactie& tranzactie);
};
istream &operator>>(istream &in, Tranzactie& tranzactie){
    cout<<"nume\n";
    in>>tranzactie.nume_c;
    cout<<"data\n";
    in>>tranzactie.data;
    cout<<"nrmasini\n";
    cin>>tranzactie.nr_masini;
    cout<<"masinile\n";
    for(int i=0; i<tranzactie.nr_masini; i++)
    {
        shared_ptr<Masina> omasina;
        omasina = make_shared<Masina>();
        cin>>*omasina;
        tranzactie.masiniv.push_back(omasina);
    }
    return in;
}

ostream &operator<<(ostream &out, const Tranzactie& tranzactie){
    out<<tranzactie.nume_c<<endl;
    out<<tranzactie.data<<endl;
    for(int i=0; i<tranzactie.nr_masini; i++)
    {
        out<<tranzactie.masiniv[i]<<endl;
    }
    return out;
}
int main() {
    vector<shared_ptr<Masina>> masini;
    vector<shared_ptr<Tranzactie>> tranzactii;
    unordered_map<string, int> fr;
    while (true) {
        cout << "1.Afisare masini\n";
        cout << "2.Adauga o masina\n";
        cout << "3. Adauga o tranzactie\n";
        cout << "4. Afiseaza cel mai vandut model\n";
        cout << "5. optimizare viteza\n";
        cout << "0. Exit \n";
        int optiune;
        cin >> optiune;
        switch (optiune) {
            case 1: {
                for (const auto &masina: masini)
                    cout << *masina << endl;
                break;
            }
            case 2:
            {
                cout << "introduceti tipul de masina\n";
                cout << "1. Masina pe combustibil\n";
                cout << "2. Masina electrica\n";
                cout << "3. Masina hibrid\n";
                int tip;
                cin >> tip;
                if (tip == 1) {
                    shared_ptr<Combustibil> masina;
                    masina = make_shared<Combustibil>();
                    cin >> *masina;
                    masina->setAutonomie(masina->getcapacitate() / masina->getgreutate());
                    masini.push_back(masina);
                    cout<<masina->getAutonomie();
                    masini.push_back(masina);
                } else if (tip == 2) {
                    shared_ptr<Electric> masina;
                    masina = make_shared<Electric>();
                    cin >> *masina;
                    masini.push_back(masina);
                } else if (tip == 3) {
                    shared_ptr<Hibrid> masina;
                    masina = make_shared<Hibrid>();
                    cin >> *masina;
                    masini.push_back(masina);
                }
                //masini.push_back(masina);
                break;
            }
            case 3:
            {
                shared_ptr<Tranzactie> otranzactie;
                otranzactie = make_shared<Tranzactie>();
                cin>>*otranzactie;
                for(auto const &m: otranzactie->getMasiniv())  //otranzactie->getMasiniv() e vector de masiniv
                {
                    fr[m->getMarca()]++;
                }
                break;
            }
            case 4:
            {
                int mx=0;
                string marca;
                for(auto& i: fr){
                    if(i.second>mx)
                    {
                        mx= i.second;
                        marca=i.first;
                    }
                }
                cout<<marca;
                    
                break;
            }
            case 5:
                {
                    int procent;
                    cout<<"procent: ";
                    cin>>procent;
                    cout<<"introdu marca";
                    string marca;
                    cin>>marca;
                    for(auto const &masina: masini){
                        if(masina->getMarca() == marca){
                            masina->setViteza(masina->getViteza()*(100+procent));
                        }
                    }
                    break;
                }
        }
    }
}

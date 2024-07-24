//2014 seria 13
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <memory>
using namespace std;
class Pacient
{
protected:
    std::string nume;
    std::string prenume;
    int varsta;
    std::string adresa;
    std::unordered_map<std::string, int> afectiuni;
    std::string data1;
    string risc = "NU";
public:
    virtual ~Pacient() {};  //dynamic cast
    Pacient() {};
    Pacient(int varsta){
        this->varsta = varsta;
    }
    friend ostream &operator<<(ostream &os, const Pacient &pacient);
    friend istream &operator>>(istream &is, Pacient &pacient);
    string getNume()
    {
        return nume;
    }
    string getRisc()
    {
        return risc;
    }

};
ostream &operator<<(ostream &os, const Pacient &pacient)
{
    os << "Nume: " << pacient.nume << endl;
    os << "Prenume: " << pacient.prenume << endl;
    os << "Varsta: " << pacient.varsta << endl;
    os << "Adresa: " << pacient.adresa << endl;
    os << "Risc Cardiovascular: " << pacient.risc << endl;
    return os;
}
istream &operator>>(istream &is, Pacient &pacient)
{
    cout << "Nume:";
    is >> pacient.nume;
    cout<< "Prenume: ";
    is >> pacient.prenume;
    cout<< "Adresa: ";
    is >> pacient.adresa;
    cout<< "Colesterol: ";
    is >> pacient.afectiuni["colesterol"];
    cout<< "Tensiune arteriala: ";
    is >> pacient.afectiuni["tensiune"];
    cout<< "Data: ";
    is >> pacient.data1;
    
    if(pacient.afectiuni["colesterol"]>200 && pacient.afectiuni["colesterol"] <239)
        pacient.risc = "DA";
    else if (pacient.afectiuni["colesterol"]>239)
        pacient.risc = "RIDICAT";
    if(pacient.afectiuni["tensiune"]>139)
        pacient.risc = "RIDICAT";
    
    return is;
}

class PacientAdult : public Pacient{
public:
    PacientAdult(int varsta) : Pacient(varsta) {}
};

class PacientAdultBatran : public PacientAdult
{
private:
    bool fumator;
    string sedentarism;
public:
    PacientAdultBatran(int varsta) : PacientAdult(varsta) {
        fumator = 0;
        sedentarism = "mediu";
    }
};

class Copil : public Pacient
{
private:
    shared_ptr<Pacient> parinte[2];
    void findParents(vector<shared_ptr<Pacient>> pacienti)
    {
        for(auto &pacient: pacienti)
        {
            if(pacient->getNume() == this->nume)
            {
                if(parinte[0] == nullptr)
                    parinte[0] = std::move(pacient);
                else parinte[1] = std::move(pacient);
            }
        }
    }
public:
    Copil (int varsta, vector<shared_ptr<Pacient>> pacienti) : Pacient(varsta)
    {
        afectiuni["Proteina C"]=6;
        findParents(pacienti);
        if((parinte[0] !=nullptr && parinte[0]->getRisc() == "RIDICAT")||
           (parinte[1] !=nullptr && parinte[1]->getRisc() =="RIDICAT"))
                this->risc = "DA";
    }
};
int main() {
    vector<shared_ptr<Pacient>> pacienti;
    while (true)
        {
            string comanda;
            cout << "Introduceti comanda:\n";
            cout << "1. Adauga pacient" << endl;
            cout << "2. Afiseaza toti pacientii" << endl;
            cout << "3. Afiseaza pacientii adulti cu risc ridicat" << endl;
            cout << "4. Afiseaza pacientii copii cu risc ridicat" << endl;
            cout << "5. Afiseaza informatii dupa nume" << endl;
            cout << "6. Iesire" << endl;
            cin >> comanda;
            shared_ptr<Pacient> p;
            int age;
            string nume;
            switch (comanda[0])
            {
                case '1':
                cout << "Introduceti varsta pacientului: ";
                cin >> age;
                if (age < 18)
                    p = make_shared<Copil>(age, pacienti);
                else if (age < 40)
                    p = make_shared<PacientAdult>(age);
                else
                    p = make_shared<PacientAdultBatran>(age);

                cin >> *p;
                pacienti.push_back(p);

                break;

            case '2':
                for (const auto &pacient : pacienti)
                    cout << *pacient << endl;
                break;

            case '3':
                for (const auto &pacient : pacienti)
                {
                    if (pacient->getRisc() == "RIDICAT" && dynamic_pointer_cast<PacientAdult>(pacient))
                    {
                        cout << *pacient << endl;
                    }
                }
                break;

            case '4':
                for (const auto &pacient : pacienti)
                {
                    if (pacient->getRisc() == "DA" && dynamic_pointer_cast<Copil >(pacient))
                    {
                        cout << *pacient << endl;
                    }
                }
                break;

            case '5':
                cout << "Introduceti numele pacientului: ";
                cin >> nume;
                for (const auto &pacient : pacienti)
                {
                    if (pacient->getNume() == nume)
                    {
                        cout << *pacient << endl;
                    }
                }
                break;
            case '6':
                cout << "Goodbye!\n";
                return 0;
            }
        }
}

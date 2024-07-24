#include <iostream>
#include <string>
using namespace std;

class Bilet {
protected:
    static int nr_ordine;
    string stplecare;
    string stsosire;
    string data;
    string ora;
    int durata;
    int distanta;
    float pret;
    int cod; //tip clasa nr_ordine

public:
    Bilet(){
        nr_ordine++;
        cod = nr_ordine;
    };
    
    virtual ~Bilet(){};

    friend istream& operator >> (istream& in, Bilet& b) {
        cout << "Introduceti urmatoarele date: \n";
        cout << "Statie plecare: ";
        in >> b.stplecare;
        cout << "Statie sosire: ";
        in >> b.stsosire;
        cout << "Data plecarii: ";
        in >> b.data;
        cout << "Ora plecarii: ";
        in >> b.ora;
        cout << "Durata calatorie: ";
        in >> b.durata;
        cout << "Distanta calatorie: ";
        in >> b.distanta;
        
        return in;
    }

    friend ostream& operator << (ostream& out, const Bilet& b) {
        out << "Date bilet: \n";
        out << "Statie plecare: " << b.stplecare << '\n';
        out << "Statie sosire: " << b.stsosire << '\n';
        out << "Data plecarii: " << b.data << '\n';
        out << "Ora plecarii: " << b.ora << '\n';
        out << "Durata calatorie: " << b.durata << '\n';
        out << "Distanta calatorie: " << b.distanta << '\n';
        return out;
    }
};

class BiletR() : public Bilet(){
private:
    string tip; //R
    int clasa;
};
class BiletIR() : public Bilet(){
private:
    
};

int main() {
    // Example usage:
    Bilet myTicket("Bucuresti", "Cluj", "12-12-2024", "15:00", 6, 450, 150.0);
    cout << myTicket;  // Display ticket info
}

#include <iostream>
#include <memory>
#include <vector>
using namespace std;
class Drum
{
protected:
    string nume;
    float lungime;
    int nr_tronsoane;
public:
    Drum();
    Drum(string nume, float lungime, int nr_tronsoane);
    virtual ~Drum() {};
    
    float getlungime(){
        return lungime;
    }
    
    friend istream &operator>>(istream &in, Drum& drum);
    friend ostream &operator<<(ostream &out, Drum& drum);
};
istream &operator>>(istream &in, Drum& drum){
    cout<<"Nume: ";
    in>>drum.nume;
    cout<<"\nLungime: ";
    in>>drum.lungime;
    cout<<"\nNr tronsoane: ";
    in>>drum.nr_tronsoane;

    return in;
}
ostream &operator<<(ostream &out, Drum& drum){
    out<<"Nume: ";
    out<<drum.nume;
    out<<"\nLungime: ";
    out<<drum.lungime;
    out<<"\nTronsoane: ";
    out<<drum.nr_tronsoane;
    out<<"\n";
    
    return out;
}
Drum::Drum(){
    this->nume = "predefinit";
    this->lungime = 0;
    this->nr_tronsoane = 0;
}
Drum::Drum(string nume, float lungime, int nr_tronsoane){
    this->nume = nume;
    this->lungime = lungime;
    this->nr_tronsoane = nr_tronsoane;
}

class DrumNational : public Drum{
private:
    int nr_judete;
public:
    DrumNational();
    DrumNational(string nume, float lungime, int nr_tronsoane, int nr_judete);
    
    friend istream &operator>>(istream &in, DrumNational& drum);
    friend ostream &operator<<(ostream &out, DrumNational& drum);
};
istream &operator>>(istream &in, DrumNational& drum){
    in>>(Drum&)drum;
    cout<<"Nr judete: ";
    in>>drum.nr_judete;

    return in;
}
ostream &operator<<(ostream &out, DrumNational& drum){
    out<<(Drum&) drum;
    cout<<"Nr judete: ";
    out<<drum.nr_judete;
    
    return out;
}
DrumNational::DrumNational():Drum(){
    this->nr_judete = 0;
}
DrumNational::DrumNational(string nume, float lungime, int nr_tronsoane, int nr_judete):Drum(nume, lungime, nr_tronsoane)
{
    this->nr_judete = nr_judete;
}

class DrumEuropean : virtual public Drum{
protected:
    int nr_tari;
public:
    DrumEuropean();
    DrumEuropean(string nume, float lungime, int nr_tronsoane, int nr_tari);
    
    int getnr_tari() const {
        return nr_tari;
    }
    
    friend istream &operator>>(istream &in, DrumEuropean& drum);
    friend ostream &operator<<(ostream &out, const DrumEuropean& drum);
};

istream &operator>>(istream &in, DrumEuropean& drum){
    in>>(Drum&) drum;
    cout<<"Nr tari: ";
    in>>drum.nr_tari;
    
    return in;
}
ostream &operator<<(ostream &out, const DrumEuropean& drum){
    out<<(Drum&) drum;
    out<<"Nr tari: ";
    out<<drum.nr_tari;
    out<<'\n';
    
    return out;
}
DrumEuropean::DrumEuropean():Drum(){
    this->nr_tari = 0;
}
DrumEuropean::DrumEuropean(string nume, float lungime, int nr_tronsoane, int nr_tari):Drum(nume, lungime, nr_tronsoane)
{
    this->nr_tari = nr_tari;
}
class Autostrada : virtual public Drum{
protected:
    int nr_benzi;
public:
    Autostrada();
    Autostrada(string nume, float lungime, int nr_tronsoane, int nr_benzi);
    int getnr_benzi() const {
        return nr_benzi;
    }
};
Autostrada::Autostrada():Drum(){
    nr_benzi = 0;
}
Autostrada::Autostrada(string nume, float lungime, int nr_tronsoane, int nr_benzi)
:Drum(nume, lungime, nr_tronsoane){
    this->nr_benzi=nr_benzi;
}


class AutostradaEuropean : public DrumEuropean, public Autostrada{
public:
    AutostradaEuropean();
    AutostradaEuropean(string nume, float lungime, int nr_tronsoane,int nr_benzi, int nr_tari);
    
    friend istream &operator>>(istream &in, AutostradaEuropean& drum);
    friend ostream &operator<<(ostream &out, AutostradaEuropean& drum);
};
AutostradaEuropean::AutostradaEuropean():DrumEuropean(), Autostrada(){};
AutostradaEuropean::AutostradaEuropean(string nume, float lungime, int nr_tronsoane,int nr_benzi, int nr_tari):DrumEuropean(nume, lungime, nr_tronsoane, nr_tari),
Autostrada(nume, lungime, nr_tronsoane, nr_benzi){};

istream &operator>>(istream &in, AutostradaEuropean& drum){
    in>>(Drum&) drum;
    cout<<"nr benzi: ";
    in>>drum.nr_benzi;
    cout << "nr tari: ";
    in>>drum.nr_tari;

    return in;
}

ostream &operator<<(ostream &out, const AutostradaEuropean& drum){
    out<<(Drum&)drum;
    out<<"Nr benzi: ";
    out<<drum.getnr_benzi();
    out<<'\n';
    out << "nr tari: ";
    out<<drum.getnr_tari();
    out <<'\n';
    
    return out;
}

class Contract{
private:
    const int id;
    static int idCnt;
    string nume;
    string cif;
    float cost;
    shared_ptr<Drum> drum;
    
public:
    Contract();
    Contract(string nume, string cif, float cost, shared_ptr<Drum> drum);
    ~Contract(){};
    
    friend istream &operator>>(istream &in, Contract& contract);
    friend ostream &operator<<(ostream &out, const Contract& contract);
    
    void setCost(float newCost) {
        this->cost = newCost;
    }
    
    float getCost()
    {
        return cost;
    }

};
istream &operator>>(istream &in, Contract& contract){
    cout<<"nume:";
    in>>contract.nume;
    cout<<"cif";
    in>>contract.cif;
    
    return in;
}

ostream &operator<<(ostream &out, const Contract& contract){
    out<<contract.nume;
    out<<contract.cif;
    
    return out;
}
int Contract::idCnt = 0;
Contract::Contract():id(++idCnt){
    nume="predefinit";
    cif="predefinit";
    cost=0;
}
Contract::Contract(string nume, string cif, float cost,shared_ptr<Drum> drum):id(++idCnt)
{
    this->nume = nume;
    this->cif = cif;
    this->cost = cost;
    this->drum = drum;
}

int main() {
    vector<shared_ptr<Contract>> contracte;
    vector<shared_ptr<Drum>> drumuri;
    int optiune;
    while(true)
    {
        cout<<"1.Afisare Drumuri si contracte \n";
        cout<<"2.Lungime totala \n";
        cout<<"3.Reziliere \n";
        cout<<"4.Cost total \n";
        cout <<"5. Adaugare Drum la un contract\n";
        cout<<"0. Exit \n";
        
        cin>>optiune;
        switch(optiune){
            case 1:{
                for(const auto &drum: drumuri)
                    cout<<*drum<<endl;
                for(const auto &contract: contracte)
                    cout<<*contract<<endl;
                break;
            }
            case 5:{
                shared_ptr<Drum> undrum;
                cout<<"introduceti tipul de drum\n";
                cout<<"1. drum national\n";
                cout<<"2. drum eruopean\n";
                cout<<"3. autostrada\n";
                cout<<"4. autostrada europeana\n";
                int tip;
                cin>>tip;
                shared_ptr<Contract> uncontract;
                if(tip==1)
                {
                    undrum = make_shared<DrumNational>();
                    uncontract->setCost(3000*undrum->getlungime());
                }
                else if(tip==2)
                {
                    undrum = make_shared<DrumEuropean>();
                    uncontract->setCost(3000*undrum->getlungime());
                }
                else if(tip==3)
                {
                    undrum = make_shared<Autostrada>();
                    uncontract->setCost(2500*undrum->getlungime()*dynamic_pointer_cast<Autostrada>(undrum)->getnr_benzi());
                }
                else if(tip==4)
                {
                    undrum = make_shared<AutostradaEuropean>();
                    uncontract->setCost(uncontract->getCost()+500*dynamic_pointer_cast<AutostradaEuropean>(undrum)->getnr_tari());
                }
                
                cin>>*undrum;
                drumuri.push_back(undrum); 
                cin>>*uncontract;
                contracte.push_back(uncontract);
                break;
            }
                
        }
    }
    return 0;
}

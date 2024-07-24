#include <iostream>
#include <memory>
#include <vector>
#include <climits>
using namespace std;
class Unealta{
protected:
    const string serie;
    const int nr_serie;
    string culoare;
    float timp;
    float energie;
    float suprafata;
public:
    Unealta():serie("default"), nr_serie(0){};
    Unealta(float suprafata):serie("default"), nr_serie(0){
        this->suprafata = suprafata;
    };
    friend istream &operator>>(istream &in, Unealta& unealta);
    friend ostream &operator<<(ostream &out, const Unealta& unealta);
    virtual ~Unealta(){};
    float gettimp(){
        return timp;
    }
    float getenergie(){
        return energie;
    }
};
istream &operator>>(istream &in, Unealta& unealta){
    cout<<"culoare\n";
    in>>unealta.culoare;
    cout<<"timp\n";
    in>>unealta.timp;
    cout<<"energie\n";
    in>>unealta.energie;
    cout<<"suprafata\n";
    in>>unealta.suprafata;
    cout<<endl;
    
    return in;
}
ostream &operator<<(ostream &out, const Unealta& unealta){
    out<<unealta.serie<<endl;
    out<<unealta.nr_serie<<endl;
    out<<unealta.culoare<<endl;
    out<<unealta.timp<<endl;
    return out;
}
class LopataElectrica: public Unealta{
private:
    float suprafata_faras;
    float baterie;
    float timp_lopata;
    float consum_energie;
public:
    LopataElectrica():Unealta(){};
    LopataElectrica(float suprafata_faras, float baterie):Unealta(){
        this->suprafata_faras = suprafata_faras;
        this->baterie = baterie;
    };
    friend istream &operator>>(istream &in, LopataElectrica& lopataelectrica);
    friend ostream &operator<<(ostream &out, const LopataElectrica& lopataelectrica);
    ~LopataElectrica(){};
};
istream &operator>>(istream &in, LopataElectrica& lopataelectrica){
    in>>(Unealta&)lopataelectrica;
    cout<<"sup faras";
    in>>lopataelectrica.suprafata_faras;
    cout<<"baterie";
    in>>lopataelectrica.baterie;
    lopataelectrica.timp_lopata = lopataelectrica.suprafata / sqrt(lopataelectrica.suprafata_faras);
    lopataelectrica.consum_energie = pow(lopataelectrica.suprafata, 2)*lopataelectrica.baterie;
    return in;
}
ostream &operator<<(ostream &out, const LopataElectrica& lopataelectrica){
    out<<(Unealta&)lopataelectrica;
    out<<lopataelectrica.suprafata_faras;
    return out;
}
class Drona: public Unealta{
    float alt_max;
    int nr_motoare;
public:
    Drona():Unealta(){};
    friend istream &operator>>(istream &in, Drona& drona);
    friend ostream &operator<<(ostream &out, const Drona& drona);
    
    ~Drona(){};
};
istream &operator>>(istream &in, Drona& drona){
    in>>(Unealta&) drona;
    cout<<"alt max\n";
    in>>drona.alt_max;
    cout<<"nr_motoare\n";
    in>>drona.nr_motoare;
    
    drona.timp = std::log(drona.suprafata) * std::tanh(drona.alt_max);
    
    drona.energie = drona.suprafata * std::pow(drona.nr_motoare, 3);
    return in;
}
ostream &operator<<(ostream &out, const Drona& drona){
    out<<(Unealta&) drona;
    out<<drona.alt_max<<endl;
    out<<drona.nr_motoare<<endl;
    
    return out;
}
class Prototip: public Unealta{
private:
    float atribut1;
    float atribut2;
public:
    Prototip(){};
    friend istream &operator>>(istream &in, Prototip& prototip);
    friend ostream &operator<<(ostream &out, const Prototip& prototip);
    ~Prototip(){};
};
istream &operator>>(istream &in, Prototip& prototip){
    in>>(Unealta&) prototip;
    cout<<"atribut 1 ";
    in>>prototip.atribut1;
    cout<<"atribut 2 ";
    in>>prototip.atribut2;
    return in;
}
ostream &operator<<(ostream &out, const Prototip& prototip){
    out<<(Unealta&) prototip;
    out<<prototip.atribut1;
    out<<prototip.atribut2;
    return out;
}
class Echipa{
private:
    string nume;
    string motto;
    vector<shared_ptr<Unealta>> unelte;
    float timp_echipa;
    float consum_echipa;
public:
    Echipa(){};
    friend istream &operator>>(istream &in, Echipa& echipa);
    friend ostream &operator<<(ostream &out, const Echipa& echipa);
    float gettimp() const{
        return timp_echipa;
    }
    float getconsum() const{
        return consum_echipa;
    }
    ~Echipa(){};
    
};
istream &operator>>(istream &in, Echipa& echipa){
    cout<<"nume ";
    in>>echipa.nume;
    cout<<"motto";
    in>>echipa.motto;
    return in;
}
ostream &operator<<(ostream &out, const Echipa& echipa){
    out<<echipa.nume<<endl;
    out<<echipa.motto;
    return out;
}
int main() {
    vector<shared_ptr<Echipa>> echipe;
    int timp_minim=INT_MAX, consum_minim=INT_MAX;
    shared_ptr<Echipa> echipatimpmin;
    echipatimpmin = make_shared<Echipa>();
    shared_ptr<Echipa> echipaconsummin;
    echipaconsummin = make_shared<Echipa>();
    int optiune;
    while(true){
        cout<<"introdu optiunea";
        cout<<"1. adauga o echipa\n";
        cout<<"2. afiseaza echipa cu timp minim\n";
        cout<<"3. afiseaza echipa cu consum minim\n";
        cout<<"4. exit\n";
        cin>>optiune;
        switch(optiune){
            case 1:{
                shared_ptr<Echipa> echipa;
                echipa = make_shared<Echipa>();
                cin>>*echipa;
                cout<<"introduceti nr unelte\n";
                int nr_unelte;
                cin>>nr_unelte;
                int timp1=0, consum1=0;
                for(int i=0; i<nr_unelte; i++)
                {
                    cout<<"introduceti tip unealta\n";
                    cout<<"1. lopata electrica\n";
                    cout<<"2. drona\n";
                    cout<<"3. prototip\n";
                    int tip_unealta;
                    cin>>tip_unealta;
                    switch(tip_unealta){
                        case 1:{
                            shared_ptr<LopataElectrica> lopel;
                            lopel = make_shared<LopataElectrica>();
                            cin>>*lopel;
                            timp1+=lopel->gettimp();
                            consum1+=lopel->getenergie();
                            break;
                        }
                        case 2:{
                            shared_ptr<Drona> drona;
                            drona = make_shared<Drona>();
                            cin>>*drona;
                            timp1+=drona->gettimp();
                            consum1+=drona->getenergie();
                            break;
                        }
                        case 3:{
                            shared_ptr<Prototip> prototip;
                            prototip = make_shared<Prototip>();
                            cin>>*prototip;
                            timp1+=prototip->gettimp();
                            consum1+=prototip->getenergie();
                            break;
                        }
                        default:
                            return 0;
                            
                    }
                    if(timp1<timp_minim){
                        echipatimpmin = std::move(echipa);
                    }
                    if(consum1<consum_minim){
                        echipaconsummin = std::move(echipa);
                    }
                }
                break;
            }
            case 2:
            {
                cout<<*echipatimpmin;
                break;
            }
            case 3:
            {
                cout<<*echipaconsummin;
                break;
            }
            case 4:
                return 0;
        }
    }
    return 0;
}

import Entitati.*;
import Servicii.Magazin;
import Util.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        Client client1 = new Client(0,"Andrei Popescu", "andrei@email.com");
        Client client2 = new Client(1,"Maria Ionescu", "maria@email.com");

        Instrument chitara = new Instrument("Chitara Acustica", 750, CategorieInstrument.CORZI, BrandInstrument.YAMAHA);
        Instrument pian = new Instrument("Pian Electric", 1500, CategorieInstrument.CLAPE, BrandInstrument.FENDER);
        Accesoriu corzi = new Accesoriu("Set corzi", 50, "Chitara Acustica");

        Magazin.getInstance().adaugaInstrument(chitara);
        Magazin.getInstance().adaugaInstrument(pian);
        Magazin.getInstance().adaugaAccesoriu(corzi);

        Furnizor furnizor1 = new Furnizor("MuzicaPlus", "contact@muzicaplus.ro");
        furnizor1.adaugaProdus(chitara);
        furnizor1.adaugaProdus(pian);

        System.out.println(furnizor1);
        System.out.println("Produse furnizate: " + furnizor1.getProduseFurnizate());

        Comanda comanda1 = new Comanda(client1);
        comanda1.adaugaProdus(chitara);
        comanda1.adaugaProdus(corzi);

        Comanda comanda2 = new Comanda(client2);
        comanda2.adaugaProdus(pian);

        Magazin.getInstance().plaseazaComanda(comanda1);
        Magazin.getInstance().plaseazaComanda(comanda2);

        System.out.println("\n=== Comenzi ===");
        Magazin.getInstance().afiseazaComenzi();

        System.out.println("\n=== Clienți (sorted, din colecția TreeSet) ===");
        Magazin.getInstance().afiseazaClienti();


        System.out.println("\n=== Clienți sortați alfabetic ===");
        List<Client> clientiSortati = Magazin.getInstance().sorteazaClientiAlfabetic();
        for (Client c : clientiSortati) {
            System.out.println(c);
        }

        System.out.println("\n=== Produse din Comanda 1 înainte de sortare ===");
        for (Produs p : comanda1.getProduse()) {
            System.out.println(p);
        }
        comanda1.sorteazaProduseDupaPret();
        System.out.println("\n=== Produse din Comanda 1 după sortare crescătoare după preț ===");
        for (Produs p : comanda1.getProduse()) {
            System.out.println(p);
        }

        Magazin.getInstance().aplicaPromotie(CategorieInstrument.CORZI, BrandInstrument.YAMAHA, 10);
        System.out.println("\n=== Comenzi dupa aplicarea promoției ===");
        Magazin.getInstance().afiseazaComenzi();

        System.out.println("\nCauta clientul cu email-ul 'maria@email.com':");
        Client clientGasit = Magazin.getInstance().cautaClientDupaEmail("maria@email.com");
        System.out.println(clientGasit);

        System.out.println("\nCauta comanda cu ID 1:");
        Comanda comandaGasita = Magazin.getInstance().cautaComandaDupaId(1);
        System.out.println(comandaGasita);

        System.out.println("\nTotalul comenzii 2:");
        System.out.println(Magazin.getInstance().calculeazaTotalComanda(comanda2) + " RON");

        System.out.println("\nInstrumente din categoria CLAPE:");
        List<Instrument> instrumenteClape = Magazin.getInstance().getProduseByCategorie(CategorieInstrument.CLAPE);
        for (Instrument i : instrumenteClape) {
            System.out.println(i);
        }

        System.out.println("\nAccesorii compatibile cu Chitara Acustica:");
        List<Accesoriu> accesoriiCompatibile = Magazin.getInstance().getAccesoriiCompatibile("Chitară Acustica");
        for (Accesoriu a : accesoriiCompatibile) {
            System.out.println(a);
        }


        // genereaza factura pentru comanda 1
        Magazin.getInstance().genereazaFactura(comanda1);
        Magazin.getInstance().afiseazaFacturi();

        // raport de vanzari pe o perioada (ex: ultimele 24 de ore)
        Calendar cal = Calendar.getInstance();
        Date end = cal.getTime();
        cal.add(Calendar.HOUR, -24);
        Date start = cal.getTime();
        double vanzari = Magazin.getInstance().raportVanzariPePerioada(start, end);
        System.out.println("\nRaport vanzari ultimele 24 de ore: " + vanzari + " RON");

        // filtreaza produse cu pret intre 100 și 1000 RON
        System.out.println("\nProduse cu pret intre 100 si 1000 RON:");
        List<Produs> produseFiltrate = Magazin.getInstance().filtreazaProduseDupaPret(100, 1000);
        for (Produs p : produseFiltrate) {
            System.out.println(p);
        }

        // raport clienți fideli (care au cel puțin 1 comandă)
        System.out.println("\nClienți fideli (minim 1 comanda):");
        List<Client> clientiFideli = Magazin.getInstance().raportClientiFideli(1);
        for (Client c : clientiFideli) {
            System.out.println(c);
        }

        // grupeaza instrumentele dupa brand
        System.out.println("\nInstrumente grupate dupa brand:");
        Map<BrandInstrument, List<Instrument>> grupare = Magazin.getInstance().grupeazaInstrumenteDupaBrand();
        for (BrandInstrument brand : grupare.keySet()) {
            System.out.println("Brand: " + brand);
            for (Instrument i : grupare.get(brand)) {
                System.out.println("   " + i);
            }
        }
    }
}
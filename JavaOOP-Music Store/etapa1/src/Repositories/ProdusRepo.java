package Repositories;

import Entitati.Accesoriu;
import Entitati.Instrument;
import Entitati.Produs;
import Util.TipProdus;

import java.util.ArrayList;
import java.util.List;

public class ProdusRepo {
    private List<Produs> produse;

    public ProdusRepo() {
        this.produse = new ArrayList<>();
    }

    // Insert a new Produs
    public void insert(Produs produs) {
        produse.add(produs);
    }

    // Get a Produs by ID (assuming 'nume' is unique identifier)
    public Produs get(String nume) {
        for (Produs produs : produse) {
            if (produs.getNume().equals(nume)) {
                return produs;
            }
        }
        return null;
    }

    // Delete a Produs by ID
    public void delete(String nume) {
        produse.removeIf(produs -> produs.getNume().equals(nume));
    }

    // Update a Produs
    public void update(String nume, Produs produsActualizat) {
        for (int i = 0; i < produse.size(); i++) {
            if (produse.get(i).getNume().equals(nume)) {
                produse.set(i, produsActualizat);
                break;
            }
        }
    }

    // Get all Produse (deep copy to avoid direct reference)
    public List<Produs> getAll() {
        List<Produs> copiaProduse = new ArrayList<>();
        for (Produs produs : produse) {
            copiaProduse.add(new Produs(produs));
        }
        return copiaProduse;
    }

    public List<Instrument> getAllInstruments(){
        List<Instrument> instruments = new ArrayList<>();
        for (Produs produs : produse) {
            if (produs.getTip_produs() == TipProdus.INSTRUMENT) {
                instruments.add(new Instrument((Instrument)produs));
            }
        }
        return instruments;
    }

    public List<Accesoriu> getAllAccesoris(){
        List<Accesoriu> accesoris = new ArrayList<>();
        for (Produs produs : produse) {
            if (produs.getTip_produs() == TipProdus.ACCESORIU) {
                accesoris.add(new Accesoriu((Accesoriu)produs));
            }
        }
        return accesoris;
    }
}

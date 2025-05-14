package Servicii;

import Entitati.Accesoriu;
import Entitati.Instrument;
import Entitati.Produs;
import Repo.ProdusRepo;
import java.util.List;

public class ProdusServiciu implements ProdusServiciuInterfata {
    private ProdusRepo repo;

    private ProdusServiciu() {
        this.repo = new ProdusRepo();
    }

    private static final class SINGLETON{
        private static final ProdusServiciu instance = new ProdusServiciu();
    }

    public static ProdusServiciu getInstance(){return SINGLETON.instance;}

    @Override
    public void adaugaProdus(Produs produs) {
        repo.insert(produs);
    }

    @Override
    public Produs cautaProdus(String nume) {
        return repo.get(nume);
    }

    @Override
    public void stergeProdus(String nume) {
        repo.delete(nume);
    }

    @Override
    public void actualizeazaProdus(String nume, Produs produsActualizat) {
        repo.update(nume, produsActualizat);
    }

    @Override
    public List<Produs> obtineToateProdusele() {
        return repo.getAll();
    }

    @Override
    public List<Instrument> obtineToateInstrumentele() {return repo.getAllInstruments();}

    @Override
    public List<Accesoriu> obtineToateAccesoriile() {return repo.getAllAccesoris();}
}

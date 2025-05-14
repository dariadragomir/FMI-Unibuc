package Servicii;

import Entitati.Recenzie;
import Repositories.RecenzieRepo;
import java.util.List;

public class RecenzieServiciu implements RecenzieServiciuInterfata {
    private RecenzieRepo repo;

    private RecenzieServiciu() {
        this.repo = new RecenzieRepo();
    }

    private static final class SINGLETON{
        private static final RecenzieServiciu instance = new RecenzieServiciu();
    }

    public static RecenzieServiciu getInstance(){return SINGLETON.instance;}

    @Override
    public void adaugaRecenzie(Recenzie recenzie) {
        repo.insert(recenzie);
    }

    @Override
    public Recenzie cautaRecenzie(String numeClient) {
        return repo.get(numeClient);
    }

    @Override
    public void stergeRecenzie(String numeClient) {
        repo.delete(numeClient);
    }

    @Override
    public void actualizeazaRecenzie(String numeClient, Recenzie recenzieActualizata) {
        repo.update(numeClient, recenzieActualizata);
    }

    @Override
    public List<Recenzie> obtineToateRecenziile() {
        return repo.getAll();
    }
}

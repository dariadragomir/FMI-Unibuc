package Servicii;

import Entitati.Client;
import Entitati.Comanda;
import Entitati.Produs;
import Repositories.ComandaRepo;

import java.util.List;

public class ComandaServiciu implements ComandaServiciuInterfata {
    private final ComandaRepo comandaRepo;

    private ComandaServiciu() {
        this.comandaRepo = new ComandaRepo();
    }
    private static final class SINGLETON {
        private static final ComandaServiciu instance = new ComandaServiciu();
    }

    public static ComandaServiciu getInstance() {return SINGLETON.instance;}

    @Override
    public void adaugaComanda(Client client) {
        Comanda comanda = new Comanda(client);
        comandaRepo.insert(comanda);
        client.plaseazaComanda(); // actualizează și categoria automat
    }
    @Override
    public void adaugaComanda(Comanda comanda) {
        comandaRepo.insert(comanda);
    }

    @Override
    public void adaugaProdusLaComanda(int idComanda, Produs produs) {
        Comanda c = comandaRepo.get(idComanda);
        if (c != null) {
            c.adaugaProdus(produs);
            comandaRepo.update(c);
        }
    }

    @Override
    public void proceseazaComanda(int idComanda) {
        Comanda c = comandaRepo.get(idComanda);
        if (c != null) {
            c.proceseazaComanda();
            comandaRepo.update(c);
        }
    }

    @Override
    public Comanda gasesteComanda(int id) {
        return comandaRepo.get(id);
    }

    @Override
    public boolean stergeComanda(int id) {
        return comandaRepo.delete(id);
    }

    @Override
    public boolean actualizeazaComanda(Comanda comanda) {
        return comandaRepo.update(comanda);
    }

    @Override
    public List<Comanda> getToateComenzile() {
        return comandaRepo.getAll();
    }

    public double calculeazaTotalComanda(Comanda comanda) {
        double total = 0;
        for (Produs p : comanda.getProduse()) {
            total += p.getPret();
        }
        return total;
    }
}

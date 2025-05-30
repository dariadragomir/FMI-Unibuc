package Entitati;

import Util.TipProdus;

public class Produs {
    private String nume;
    private double pret;
    private TipProdus tip_produs;

    public Produs(String nume, double pret) {
        this.nume = nume;
        this.pret = pret;
    }

    public Produs(Produs other) {
        this.nume = other.nume;
        this.pret = other.pret;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public double getPret() {
        return pret;
    }

    public void setPret(double pret) {
        this.pret = pret;
    }

    public TipProdus getTip_produs() {
        return tip_produs;
    }

    protected void setTip_produs(TipProdus tip_produs) {
        this.tip_produs = tip_produs;
    }

    @Override
    public String toString() {
        return nume + " - " + pret + " RON";
    }
}

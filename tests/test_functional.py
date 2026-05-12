
import pytest
from src.manager import Manager
from src.models import Parameters, Tenant, Transfer, Apartment




def test__due_pln ():

    parameters = Parameters()
    manager = Manager(parameters)
    rozliczenie = manager.get_settlement('apart-polanka', 2025, 1)
    rozliczenia_najemcow = manager.create_tenants_settlements(rozliczenie)
    
    suma = 0

    for x in rozliczenia_najemcow:
        suma += x.total_due_pln

    assert suma == rozliczenie.total_due_pln

def test_get_debtors_functional():
    manager = Manager(Parameters())
    
    manager.apartments = {
        "apt-1": Apartment(
            key="apt-1", 
            name="M", 
            location="P", 
            area_m2=50.0, 
            rooms={}
        )
    }
    
    manager.tenants = {
        "t1": Tenant(
            name="Jan Kowalski", 
            apartment="apt-1", 
            rent_pln=2000.0,
            room="Room 1",               
            deposit_pln=2000.0,          
            date_agreement_from="2026-01-01", 
            date_agreement_to="2026-12-31"    
        )
    }
    
    manager.transfers = [
        Transfer(
            tenant="Jan Kowalski", 
            amount_pln=1500.0, 
            date="2026-05-10", 
            settlement_year=2026, 
            settlement_month=5
        )
    ]
    
    debtors = manager.get_debtors("apt-1", 5, 2026)
    assert "Jan Kowalski" in debtors

def test_get_tax_functional():
    manager = Manager(Parameters())
    manager.transfers = [
        Transfer(tenant="L1", amount_pln=1000.0, date="2026-05-01", settlement_year=2026, settlement_month=5),
        Transfer(tenant="L2", amount_pln=2000.0, date="2026-05-15", settlement_year=2026, settlement_month=5)
    ]
    tax = manager.get_tax(2026, 5, 0.085)
    assert tax == 255
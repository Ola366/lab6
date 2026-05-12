
import pytest
from src.manager import Manager
from src.models import Parameters



def test__due_pln ():

    parameters = Parameters()
    manager = Manager(parameters)
    rozliczenie = manager.get_settlement('apart-polanka', 2025, 1)
    rozliczenia_najemcow = manager.create_tenants_settlements(rozliczenie)
    
    suma = 0

    for x in rozliczenia_najemcow:
        suma += x.total_due_pln

    assert suma == rozliczenie.total_due_pln


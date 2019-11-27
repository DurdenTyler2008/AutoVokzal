

from src.AutoVokzal import AutoVokzal,Route,Kassa
from src.TicketInspector import TicketInspector
from src.RepairZoone import RepairZone


def test_AutoVokzal():
    autovokzal = AutoVokzal()
    assert autovokzal

def test_Route():
    route = Route()
    assert route

def test_Kassa():
    kassa = Kassa()
    assert kassa

def test_RepairZone():
    repairzone = RepairZone()
    assert repairzone


def test_TicketInspector():
    ticketinspector = TicketInspector()
    assert ticketinspector




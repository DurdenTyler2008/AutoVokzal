class AutoVokzal:
    #permission_AutoVokzal = []
    '''после проверки наличия license,route_list,med дать разрешение перейти к Route '''
    def __init__(self, license, route_list, med):
        self.license = license
        self.route_list = route_list
        self.med = med

    def check(self):
        assert self.license
        assert self.route_list
        assert self.med
        #return self.permission_AutoVokzal()

    def permission_autovokzal(self):
        assert self.permission_autovokzal
        if self.license and self.route_list and self.med:
            return

class Route:
    permission_Route = []
    '''после выбора типа маршрута дать разрешение перейти к Kassa'''
    def __init__(self, municipal_route, intercity_route, regional_route):
        self.municipal_route = municipal_route
        self.intercity_route = intercity_route
        self.regional_route = regional_route


class Kassa:
    def __init__(self, tickets, passenger):
        self.tickets = tickets
        self.passenger = passenger

    def sale(self, passenger = bool, tickets = int):
        assert self.passenger == passenger
        '''проверяю наличие пассажира'''
        assert self.tickets >= tickets
        '''проверяю наличие билетов'''

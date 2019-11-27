

class RepairZone:
    def __init__(self, diagnostic, tire_service, auto_repair):
        self.diagnostic = diagnostic #диагоностика
        self.tire_service = tire_service #шиномонтаж
        self.auto_repair = auto_repair  #авторемонт

    def get_diagnostic_rezult(self):
        return str(self.diagnostic) #возвращает значение(результат) diagnostic

    def get_tire_service(self):
        return str(self.tire_service) #возвращает значение(результат)tire_service

    def get_auto_repair(self):
        return str(self.auto_repair) #возвращает значение(результат)auto_repair

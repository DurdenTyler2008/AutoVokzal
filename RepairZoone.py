class RepairZone:
    def __init__(self, diagnostic, tire_service, auto_repair):
        self.diagnostic = diagnostic #диагоностика
        self.tire_service = tire_service #шиномонтаж
        self.auto_repair = auto_repair  #авторемонт

    def get_diagnostic_rezult(self):
        return str(self.diagnostic) #возвращает значение(результат) diagnostic

    def work_tire_service(self):
        self.work_tire_service =

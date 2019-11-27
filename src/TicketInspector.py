

class TicketInspector:
    def __init__(self, TicketInspector, ticketcontrol):
        self.TicketInspector = TicketInspector
        self.ticketcontrol = ticketcontrol #контроль билетов

    def get_ticketcontrol_rezult(self):
        return str(self.ticketcontrol) #возвращает значение(результат) проверки билетов

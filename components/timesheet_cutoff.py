from meya import Component

import datetime

class TextComponent(Component):
    def start(self):
        date_zero_cutoff = datetime.date(2018, 4, 27)
        pay_period_day_number = (datetime.date.today()-date_zero_cutoff).days%14
        pay_period_number = (datetime.date.today()-date_zero_cutoff).days/14
        if pay_period_day_number > 5:
            date_cutoff = date_zero_cutoff+datetime.timedelta(days=pay_period_number*14)
        else:
            date_cutoff = date_zero_cutoff+datetime.timedelta(days=pay_period_number*14-14)

        self.db.flow.set("timesheet_date_cutoff", date_cutoff.strftime("%A %d. %B %Y"))
        return self.respond(action="next")
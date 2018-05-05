from django.db import models
from datetime import datetime

class Flights(models.Model):
    
    outboundDepartureAirportIataCode = models.CharField(max_length = 3)
    outboundDepartureDateFrom = models.DateField("Date")
    outboundDepartureDateTo = models.DateField("Date")
    inboundDepartureDateFrom = models.DateField("Date")
    inboundDepartureDateTo = models.DateField("Date")
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.outboundDepartureAirportIataCode, self.outboundDepartureDateFrom, self.outboundDepartureDateTo, self.inboundDepartureDateFrom, self.inboundDepartureDateTo)
    
    class Meta:
        verbose_name_plural = 'Flights'
     
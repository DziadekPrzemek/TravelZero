from django.db import models

class Flights(models.Model):
    
    outboundDepartureAirportIataCode = models.CharField(max_length = 3)
    outboundDepartureDateFrom = models.DateField()
    outboundDepartureDateTo = models.DateField()
    inboundDepartureDateFrom = models.DateField()
    inboundDepartureDateTo = models.DateField()
    
    
    def __str__(self):
        return self.outboundDepartureAirportIataCode, self.outboundDepartureDateFrom, self.outboundDepartureDateTo, self.inboundDepartureDateFrom, self.inboundDepartureDateTo
    
    class Meta:
        verbose_name_plural = 'Flights'
     
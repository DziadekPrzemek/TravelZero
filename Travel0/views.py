import requests
from django.shortcuts import render
from .models import Flights
from .forms import FlightsForm

def index(request):
    
    apikey = "mBZ3XsuiZc6cuqT0cu8xPJt50wZcqxRG"
    url = 'http://apigateway.ryanair.com/pub/v1/farefinder/3/roundTripFares?departureAirportIataCode={}&outboundDepartureDateFrom={}&outboundDepartureDateTo={}&currency=PLN&language=pl&inboundDepartureDateFrom={}&inboundDepartureDateTo={}&apikey={}'


    if request.method == 'POST': # If the form has been submitted...
        form = FlightsForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            
            departureAirportIataCodes = form.cleaned_data['outboundDepartureAirportIataCode']
            outboundDepartureDateFrom = form.cleaned_data['outboundDepartureDateFrom']
            outboundDepartureDateTo = form.cleaned_data['outboundDepartureDateTo']
            inboundDepartureDateFrom = form.cleaned_data['inboundDepartureDateFrom']
            inboundDepartureDateTo = form.cleaned_data['inboundDepartureDateTo']
            response = requests.get(url.format(departureAirportIataCodes, outboundDepartureDateFrom, 
                                    outboundDepartureDateTo, inboundDepartureDateFrom, inboundDepartureDateTo,
                                    apikey)).json()
           
            items = len(response["fares"])


            fares = []

            for i in range(0,items):
                
                fares_info = {
                    "outboundDepartureAirportIataCode" :  departureAirportIataCodes,
                    "outboundDepartureAirportName" : response["fares"][i]['outbound']['departureAirport']['name'],
                    "outboundDepartureAirportSeoName" : response["fares"][i]['outbound']['departureAirport']['seoName'],
                    "outboundDepartureAirportCountryName" : response["fares"][i]['outbound']['departureAirport']['countryName'],
                    "outboundArrivalAirportIataCode" : response["fares"][i]['outbound']['arrivalAirport']['iataCode'],
                    "outboundArrivalAirportName" : response["fares"][i]['outbound']['arrivalAirport']['name'],
                    "outboundArrivalAirportSeoName" : response["fares"][i]['outbound']['arrivalAirport']['seoName'],
                    "outboundArrivalAirportCountryName" : response["fares"][i]['outbound']['arrivalAirport']['countryName'],
                    "outboundDepartureDate" : response["fares"][i]['outbound']['departureDate'],
                    "outboundArrivalDate" : response["fares"][i]['outbound']['arrivalDate'],
                    "outboundPriceValue" : response["fares"][i]['outbound']['price']['value'],
                    "outboundCurrencyCode" : response["fares"][i]['outbound']['price']['currencyCode'],
                    
                    "inboundDepartureAirportIataCode" : response["fares"][i]['inbound']['departureAirport']['iataCode'],
                    "inboundDepartureAirportName" : response["fares"][i]['inbound']['departureAirport']['name'],
                    "inboundDepartureAirportSeoName" : response["fares"][i]['inbound']['departureAirport']['seoName'],
                    "inboundDepartureAirportCountryName" : response["fares"][i]['inbound']['departureAirport']['countryName'],
                    "inboundArrivalAirportIataCode" : response["fares"][i]['inbound']['arrivalAirport']['iataCode'],
                    "inboundArrivalAirportName" : response["fares"][i]['inbound']['arrivalAirport']['name'],
                    "inboundArrivalAirportSeoName" : response["fares"][i]['inbound']['arrivalAirport']['seoName'],
                    "inboundArrivalAirportCountryName" : response["fares"][i]['inbound']['arrivalAirport']['countryName'],
                    "inboundDepartureDate" : response["fares"][i]['inbound']['departureDate'],
                    "inboundArrivalDate" : response["fares"][i]['inbound']['arrivalDate'],
                    "inboundPriceValue" : response["fares"][i]['inbound']['price']['value'],
                    "inboundCurrencyCode" : response["fares"][i]['inbound']['price']['currencyCode'],

                    "summaryPriceValue" : response["fares"][i]['summary']['price']['value'],
                    "summaryCurrencyCode" : response["fares"][i]['summary']['price']['currencyCode'],
                    "summaryNewRoute" : response["fares"][i]['summary']['newRoute'],
                }
            
                fares.append(fares_info)
        
            context = {'form': form,'fares' : fares}
            return render(request, 'travel0/index.html',context)
    
    else:
        form = FlightsForm() # An unbound form
        context = {'form': form}
        return render(request, 'travel0/index.html',context)

    

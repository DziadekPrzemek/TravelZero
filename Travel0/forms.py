from django import forms  
from django.forms import ModelForm, TextInput, DateInput
from .models import Flights
from datetime import date, timedelta



class FlightsForm(forms.ModelForm):


    AIRPORTS =  (
                ('WMI', 'Warsaw Modlin'), ('KRK', 'Krakow'), ('LUZ', 'Lublin'), ('RZE', 'Rzeszow'), ('GDN', 'Gdansk'), 
                ('POZ', 'Poznan'), ('CPH', 'Copenhagen'), ('OLB', 'Olbia'), ('VNO', 'Vilnius'), ('FCO', 'Rome Fiumicino'), 
                ('NCL', 'Newcastle'), ('DUS', 'Dusseldorf Int.'),('RMI', 'Rimini'), ('KIR', 'Kerry'), 
                ('SJU', 'San Juan'), ('BRU', 'Brussels'), ('TUF', 'Tours Loire Valley'), 
                ('VVI', 'Santa Cruz'), ('EDI', 'Edinburgh'), ('CCF', 'Carcassonne'), 
                ('REC', 'Recife International'), ('FSC', 'Figari'), ('BLL', 'Billund'), ('RBA', 'Rabat'), 
                ('KLX', 'Kalamata'), ('NAP', 'Naples'), ('AMS', 'Amsterdam'), ('RJK', 'Rijeka'), 
                ('LWO', 'Lviv'), ('DNR', 'Dinard'), ('VDA', 'Eilat'), ('MRS', 'Marseille'), 
                ('LBA', 'Leeds Bradford'), ('BVE', 'Brive'), ('GOT', 'Göteborg Landvetter'), 
                ('SZZ', 'Szczecin'), ('TFS', 'Tenerife South'), ('EFL', 'Kefalonia'), ('FMO', 'Münster'), 
                ('DLM', 'Dalaman'), ('MAH', 'Menorca'), ('MMX', 'Malmo'), ('VGO', 'Vigo'), 
                ('SXB', 'Strasbourg'), ('ABZ', 'Aberdeen'), ('SZY', 'Olsztyn - Mazury'), 
                ('CAG', 'Cagliari'), ('AAL', 'Aalborg'), ('OMR', 'Oradea'), ('STR', 'Stuttgart'), 
                ('LIL', 'Lille'), ('MUC', 'Munich'), ('PUJ', 'Punta Cana'), ('VAR', 'Varna'), 
                ('FAO', 'Faro'), ('MJV', 'Murcia'), ('NUE', 'Nuremberg'), ('DLE', 'Dole'), 
                ('SUF', 'Lamezia'), ('SAP', 'San Pedro Sula'), ('SOF', 'Sofia'), ('MST', 'Maastricht'), 
                ('ZAD', 'Zadar'), ('LDE', 'Lourdes'), ('SDQ', 'Santo Domingo'), ('CFU', 'Corfu'), 
                ('AOI', 'Ancona'), ('VCE', 'Venice M.Polo'), ('BRQ', 'Brno'), ('PDL', 'Ponta Delgada'), 
                ('TSF', 'Venice Treviso'), ('TER', 'Terceira Lajes'), ('BES', 'Brest'), ('RDZ', 'Rodez'), 
                ('EZE', 'Buenos Aires'),  ('OTP', 'Bucharest'),('MAN', 'Manchester'), 
                ('BOG', 'Bogota'), ('ASU', 'Asuncion'), ('SZG', 'Salzburg'), ('ORK', 'Cork'), 
                ('GRO', 'Barcelona Girona'), ('VLC', 'Valencia'), ('OPO', 'Porto'), 
                ('MXP', 'Milan Malpensa'), ('AGP', 'Malaga'), ('KBP', 'Kiev-Boryspil'), 
                ('PUY', 'Pula'),('CFE', 'Clermont'), ('PMF', 'Parma'), ('BLQ', 'Bologna'), ('CTA', 'Catania'), 
                ('TLS', 'Toulouse'), ('VXO', 'Växjö Småland'), ('XCR', 'Paris Vatry'), ('FEZ', 'Fez'), 
                ('CUN', 'Cancun'), ('AHO', 'Alghero'), 
                ('NRN', 'Dusseldorf Weeze'), ('TRN', 'Turin'), ('OUD', 'Oujda'), ('EGC', 'Bergerac'), 
                ('AMM', 'Amman Jordan'), ('ORY', 'Paris Orly'), ('GLA', 'Glasgow'), ('TFN', 'Tenerife North'), 
                ('LEI', 'Almeria'), ('CRV', 'Crotone'), ('BRI', 'Bari'), ('PEG', 'Perugia'), 
                ('VLL', 'Valladolid'), ('AQJ', 'Aqaba Jordan'), ('WAW', 'Warsaw Chopin'), ('LIS', 'Lisbon'), 
                ('LPL', 'Liverpool'), ('LYS', 'Lyon'), ('NQY', 'Newquay Cornwall'), ('ZAZ', 'Zaragoza'), 
                ('MVD', 'Montevideo'), ('REU', 'Barcelona Reus'), ('BIQ', 'Biarritz'), ('BOH', 'Bournemouth'), 
                ('TPS', 'Trapani'), ('ACE', 'Lanzarote'), ('STN', 'London Stansted'), ('AGA', 'Agadir'), 
                ('BRE', 'Bremen'), ('AAR', 'Aarhus'), ('TRS', 'Trieste'), ('IBZ', 'Ibiza'), ('ATH', 'Athens'), 
                ('JTR', 'Santorini'), ('TSR', 'Timisoara'), ('EBU', 'St Etienne'), ('PED', 'Pardubice'), 
                ('LUX', 'Luxembourg'), ('TGD', 'Podgorica'), ('CHQ', 'Chania'), ('SKG', 'Thessaloniki'), 
                ('NTE', 'Nantes'), ('PFO', 'Paphos'), ('LEJ', 'Leipzig'), ('FRA', 'Frankfurt International'), 
                ('CIA', 'Rome Ciampino'), ('SNN', 'Shannon'), ('CRL', 'Brussels Charleroi'), ('KUN', 'Kaunas'), 
                ('BRS', 'Bristol'), ('BGY', 'Milan Bergamo'), ('EIN', 'Eindhoven'), ('ZRH', 'Zurich'), 
                ('LIG', 'Limoges'), ('BHX', 'Birmingham'), ('OSL', 'Oslo'), ('LNZ', 'Linz'), 
                ('HER', 'Heraklion Crete'), ('INN', 'Innsbruck'), ('FUE', 'Fuerteventura'), 
                ('LRH', 'La Rochelle'), ('ALC', 'Alicante'), ('PAD', 'Paderborn'), ('INI', 'Nis'), 
                ('GRZ', 'Graz'),  ('CGN', 'Cologne'), ('BFS', 'Belfast International'), 
                ('XRY', 'Jerez'), ('VIT', 'Vitoria (Basque Country)'), ('TNG', 'Tangier'), ('GOA', 'Genoa'), 
                ('BSL', 'Basel'), ('SVQ', 'Seville'), ('LRT', 'Lorient'), ('NCE', 'Nice'), ('BCN', 'Barcelona'),
                ('MLA', 'Malta'), ('LCA', 'Larnaca'), ('TMP', 'Tampere'), ('LIM', 'Lima'), ('PIS', 'Poitiers'),
                ('PSA', 'Pisa'), ('HHN', 'Frankfurt Hahn'), ('RHO', 'Rhodes'), ('BOJ', 'Burgas'), 
                ('CCS', 'Caracas'), ('VST', 'Stockholm Västerås'), ('MIA', 'Miami'), ('TXL', 'Berlin Tegel'),
                ('HAM', 'Hamburg'), ('SXF', 'Berlin Schönefeld'), ('NOC', 'Knock'), ('HAV', 'Havana'), 
                ('MPL', 'Montpellier'), ('LCG', 'A Coruna'), ('BUD', 'Budapest'), ('LTN', 'London Luton'), 
                ('LPA', 'Gran Canaria'), ('BOD', 'Bordeaux'), ('JFK', 'New York (JFK)'), ('LCJ', 'Lodz'), 
                ('PLQ', 'Palanga'), ('PSR', 'Pescara'), ('WRO', 'Wroclaw'), ('VIE', 'Vienna'), 
                ('DOL', 'Deauville'), ('PDV', 'Plovdiv'), ('PGF', 'Perpignan'),  
                ('SSA', 'Salvador'), ('HAJ', 'Hannover'), ('FMM', 'Memmingen'), ('NDR', 'Nador'), 
                ('PIK', 'Glasgow Prestwick'), ('OSR', 'Ostrava'), ('BVA', 'Paris Beauvais'), 
                ('KTW', 'Katowice'), ('CIY', 'Comiso'), ('NYO', 'Stockholm Skavsta'), 
                ('FKB', 'Karlsruhe / Baden-Baden'), ('KGS', 'Kos'), ('RIX', 'Riga'), ('DTM', 'Dortmund'),
                ('BDS', 'Brindisi'), ('CWL', 'Cardiff'), ('CUF', 'Cuneo'), ('EMA', 'East Midlands'), 
                ('JMK', 'Mykonos'), ('SCQ', 'Santiago'), ('TRF', 'Oslo Torp'), ('GNB', 'Grenoble'), 
                ('LGW', 'London Gatwick'), ('TLL', 'Tallinn'), ('LPP', 'Lappeenranta'), ('PRG', 'Prague'), 
                ('HAU', 'Haugesund'), ('RAK', 'Marrakesh'), ('MAD', 'Madrid'), ('GYE', 'Guayaquil'), 
                ('LDY', 'Derry'), ('CDT', 'Castellon (Valencia)'), ('BTS', 'Bratislava'), ('FNI', 'Nimes'),
                ('BZG', 'Bydgoszcz'), ('BNX', 'Banja Luka'), ('VRN', 'Verona'), ('TLV', 'TelAviv'), 
                ('BZR', 'Beziers'), ('PMI', 'Palma de Mallorca'), ('GRU', 'Sao Paulo Guarulhos'), 
                ('PMO', 'Palermo'), ('DUB', 'Dublin'), ('SDR', 'Santander'), ('CRA', 'Craiova'), 
                ('BOS', 'Boston'))

    outboundDepartureAirportIataCode = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'btn'}),choices=AIRPORTS, required=True)
    
    outboundDepartureDateFrom = forms.DateField(initial=date.today(), widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'btn'}), required=True )

    outboundDepartureDateTo = forms.DateField(initial=date.today(), widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'btn'}), required=True )
 
    inboundDepartureDateFrom = forms.DateField(initial=date.today() + timedelta(days=1), widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'btn'}), required=True)
    
    inboundDepartureDateTo = forms.DateField(initial=date.today() + timedelta(days=1), widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'btn'}), required=True)

    class Meta:
        model = Flights
        fields = ['outboundDepartureAirportIataCode', 'outboundDepartureDateFrom', 'outboundDepartureDateTo',
                    'inboundDepartureDateFrom', 'inboundDepartureDateTo']   

    
    

        
        
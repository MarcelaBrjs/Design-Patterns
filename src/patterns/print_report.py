from array import array
from patterns.csv_utils import Ride

# Single Responsability
# Su única responsabilidad es dar formato al contenido del reporte impreso.

# Decorator Design Pattern
class PrintReport:

    def format_content(rides: array):
        # Title
        content = ['Taxi Report\n']
        # Column Names
        content.append('{}{}{}{}{}{}\n'
            .format('TaxiID'.ljust(8), 
                    'Pickup time'.ljust(21), 
                    'Dropoff time'.ljust(21), 
                    'Passenger count'.ljust(17), 
                    'Trip Distance'.ljust(15), 
                    'Total amount'.ljust(14)))
        # Data
        for ride in rides:
            content.append('{}{}{}{}{}{}\n'
                .format(ride.taxi_id.ljust(8), 
                        ride.pick_up_time.isoformat().ljust(21), 
                        ride.drop_of_time.isoformat().ljust(21), 
                        str(ride.passenger_count).ljust(17), 
                        str(ride.trip_distance).ljust(15), 
                        PrintReport.format_amount(ride.tolls_amount).ljust(14)))
        return "".join(content)
    
    def format_amount(amount):
        if amount < 0:
            return f'({amount})'
        return str(amount)

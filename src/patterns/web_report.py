from array import array
from patterns.csv_utils import Ride

# Single Responsability
# Su única responsabilidad es dar formato al contenido del reporte web.
class WebReport:

    def format_content(rides: array):
        # Title
        content = [f"<h1>{'Taxi Report'}</h1>"]
        # Column Names
        content.append("""
            <table>
                <tr>
                    <th> TaxiID </th>
                    <th> Pickup time </th>
                    <th> Dropoff time </th>
                    <th> Passenger count </th>
                    <th> Trip Distance </th>
                    <th> Total amount </th>
                </tr>
            """)
        # Data
        for ride in rides:
            content.append("".join([
                "<tr>",
                f"<td>{ride.taxi_id}</td>",
                f"<td>{ride.pick_up_time.isoformat()}</td>",
                f"<td>{ride.drop_of_time.isoformat()}</td>",
                f"<td>{ride.passenger_count}</td>",
                f"<td>{ride.trip_distance}</td>",
                f"<td>{WebReport.format_amount(ride.tolls_amount)}</td>",
                "</tr>"
            ]))
        content.append("</table>")

        return "".join(content)
    
    def format_amount(amount):
        if amount < 0:
            return f"<span style='color:red'>{amount}</span>"
        return str(amount)
import csv
from datetime import datetime

# Builder Design Pattern
class Ride:
    def __init__(self, error, taxi_id, pick_up_time, drop_of_time, passenger_count, trip_distance, tolls_amount):
        self.error = error
        self.taxi_id = taxi_id
        self.pick_up_time = pick_up_time
        self.drop_of_time = drop_of_time
        self.passenger_count = passenger_count
        self.trip_distance = trip_distance
        self.tolls_amount = tolls_amount

class RideBuilder:
    def __init__(self):
        self.error = ""
        self.taxi_id = 0
        self.pick_up_time = datetime(1, 1, 1, 0, 0)
        self.drop_of_time = datetime(1, 1, 1, 0, 0)
        self.passenger_count = 0
        self.trip_distance = 0.0
        self.tolls_amount = 0.0

    def with_error(self, error):
        self.error = error
        return self

    def with_taxi_id(self, taxi_id):
        self.taxi_id = taxi_id
        return self

    def with_pick_up_time(self, pick_up_time):
        self.pick_up_time = datetime.strptime(pick_up_time, '%Y-%m-%d %H:%M:%S')
        return self

    def with_drop_of_time(self, drop_of_time):
        self.drop_of_time = datetime.strptime(drop_of_time, '%Y-%m-%d %H:%M:%S')
        return self

    def with_passenger_count(self, passenger_count):
        self.passenger_count = passenger_count
        return self

    def with_trip_distance(self, trip_distance):
        self.trip_distance = trip_distance
        return self

    def with_tolls_amount(self, tolls_amount):
        self.tolls_amount = tolls_amount
        return self

    def build(self):
        self.ride = Ride(self.error, self.taxi_id, self.pick_up_time,self.drop_of_time, self.passenger_count, self.trip_distance, self.tolls_amount)
        return self.ride

def parse_file(csv_file: str):
    with open(csv_file) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        rides = []
        for row in csv_reader:
            ride = (RideBuilder()
                .with_error("")
                .with_taxi_id(row['TaxiID'])
                .with_pick_up_time(row['lpep_pickup_datetime'])
                .with_drop_of_time(row['lpep_dropoff_datetime'])
                .with_passenger_count(int(row["passenger_count"]))
                .with_trip_distance(float(row["trip_distance"]))
                .with_tolls_amount(float(row["total_amount"]))
            )
            rides.append(ride)
        return rides


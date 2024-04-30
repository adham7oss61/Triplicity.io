from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AirlineFlight(db.Model):
    _tablename_ = 'Airline_flght'
    Flight_ID = db.Column(db.String(8), primary_key=True)
    Airline_Name = db.Column(db.String(20), nullable=False)
    Flight_Number = db.Column(db.Integer, nullable=False)
    Departure_Airport = db.Column(db.String(20), nullable=False)
    Destination_Airport = db.Column(db.String(20), nullable=False)
    Departure_Time = db.Column(db.DateTime(6), nullable=False)
    Arrival_Time = db.Column(db.DateTime(6), nullable=False)
    Duration = db.Column(db.Time(6), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Tourist_id = db.Column(db.String(8), db.ForeignKey('Tourist.Tourist_id'), nullable=False)
    Agent_id = db.Column(db.String(8), db.ForeignKey('Travel_Agent.Agent_id'), nullable=False)

class Booking(db.Model):
    _tablename_ = 'Booking'
    Booking_id = db.Column(db.String(8), primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    trips = db.Column(db.Text, nullable=False)
    discount_percentage = db.Column(db.Integer, nullable=False)
    Agent_id = db.Column(db.String(8), db.ForeignKey('Travel_Agent.Agent_id'), nullable=False)
    Tourist_id = db.Column(db.String(8), db.ForeignKey('Tourist.Tourist_id'), nullable=False)

class BookingPackage(db.Model):
    _tablename_ = 'Booking_Package'
    Booking_id = db.Column(db.String(8), db.ForeignKey('Booking.Booking_id'), primary_key=True)
    Package_id = db.Column(db.String(8), db.ForeignKey('Package.Package_id'), primary_key=True)
    date = db.Column(db.Date, nullable=False)
    Discount_percentage = db.Column(db.Integer, nullable=False)

class CarRental(db.Model):
    _tablename_ = 'Car_rental'
    Rental_ID = db.Column(db.String(8), primary_key=True)
    Car_number = db.Column(db.String(7), nullable=False)
    Pickup_Date = db.Column(db.Date, nullable=False)
    Rental_Duration = db.Column(db.DateTime, nullable=False)
    Total_cost = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.Text, nullable=False)
    Tourist_id = db.Column(db.String(8), db.ForeignKey('Tourist.Tourist_id'), nullable=False)
    Agent_id = db.Column(db.String(8), db.ForeignKey('Travel_Agent.Agent_id'), nullable=False)

class HotelAccomodation(db.Model):
    _tablename_ = 'Hotel_accomedation'
    Hotel_ID = db.Column(db.String(8), primary_key=True)
    Hotel_Name = db.Column(db.String(20), nullable=False)

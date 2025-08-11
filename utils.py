from models import db, Expense, Trip, User, trip_participants
import sqlalchemy

def create_trip(name, participant_ids, creator_id ):
     new_trip = Trip(name = name,  creator_id= creator_id)
     db.session.add(Trip)
     
     db.session.flush()
     add_participants(new_trip.id, participant_ids)
     db.session.commit()
     return new_trip
#adds to the trip participants table. Will be used again to add individual users when they join a trip
def add_participants( trip_id, user_ids):
    for id in user_ids:
        db.session.add(trip_participants(trip_id = trip_id, user_id = id))
     


def create_user(username):
    new_user = User(name = username)
    db.session.add(User)
    
    db.session.flush()
    
    db.session.commit()
    return new_user



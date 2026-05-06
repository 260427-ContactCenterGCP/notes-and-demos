from flask import Flask, jsonify
import random

app = Flask(__name__)

# I want to define a ride class to describe our rides and then we'll create an API endpoint to return all
# of our ride information

class Ride:
    def __init__(self, name, thrill_level, description):
        self.name = name
        self.thrill_level = thrill_level
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "thrill_level": self.thrill_level,
            "description": self.description,
            "wait_time_minutes": random.randint(5, 120)
        }

rides = [
    Ride("Thunder Coaster", "high", "A fast, intense roller coaster with loops and drops."),
    Ride("Lazy River Boats", "low", "Relaxing boat ride through scenic views."),
    Ride("Drop Tower", "high", "Vertical drop ride for adrenaline seekers."),
    Ride("Pirate Swing", "medium", "Swinging ship ride with moderate thrills."),
    Ride("Carousel", "low", "Classic gentle carousel ride for all ages."),
    Ride("Volcano Run", "high", "A high-speed coaster that races through a volcanic eruption theme."),
    Ride("Mystic Rapids", "medium", "A water ride with twists, turns, and splash zones through ancient ruins."),
    Ride("Jungle Flyers", "low", "A slow aerial ride over jungle scenery and animal exhibits."),
    Ride("Neon Speedway", "high", "A futuristic indoor coaster with glowing tracks and sharp turns."),
    Ride("Tea Cup Twirl", "low", "A gentle spinning ride with colorful oversized teacups."),
    Ride("Haunted Manor", "medium", "A dark ride through a spooky mansion filled with surprises."),
    Ride("Sky Glider", "low", "A peaceful suspended ride offering views across the park."),
    Ride("Storm Chaser", "high", "An extreme motion simulator that mimics flying through storms."),
    Ride("Candy Carousel", "low", "A sweet-themed carousel with playful candy decorations."),
    Ride("Aqua Blasters", "medium", "An interactive water ride where guests can shoot targets.")
]

# Let's define a route using Flask to return this information
@app.route("/rides", methods=["GET"])
def get_ride():
    return jsonify([ride.to_dict() for ride in rides])


if __name__ == '__main__':
    app.run(debug=True, port=5000)

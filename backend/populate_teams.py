import json
from app import app, db
from models import Team

# Create an application context
app.app_context().push()

try:
    # Load team data from the JSON file
    with open("teams.json", "r") as file:
        teams_data = json.load(file)

    # Create Team objects and add them to the session
    for team_data in teams_data:
        team = Team(**team_data)
        db.session.add(team)

    # Commit the changes
    db.session.commit()

    # Log success
    print("Teams inserted successfully ✅")

except Exception as e:
    print(f"Error inserting data: {str(e)}")

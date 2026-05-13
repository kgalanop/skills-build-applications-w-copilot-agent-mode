from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from django.db import connection

from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        with connection.cursor() as cursor:
            cursor.db_conn["users"].delete_many({})
            cursor.db_conn["teams"].delete_many({})
            cursor.db_conn["activities"].delete_many({})
            cursor.db_conn["leaderboard"].delete_many({})
            cursor.db_conn["workouts"].delete_many({})

        # Teams
        marvel_id = ObjectId()
        dc_id = ObjectId()
        teams = [
            {"_id": marvel_id, "name": "Marvel", "description": "Marvel Superheroes"},
            {"_id": dc_id, "name": "DC", "description": "DC Superheroes"},
        ]
        with connection.cursor() as cursor:
            cursor.db_conn["teams"].insert_many(teams)

        # Users
        users = [
            {"_id": ObjectId(), "name": "Spider-Man", "email": "spiderman@marvel.com", "team_id": marvel_id},
            {"_id": ObjectId(), "name": "Iron Man", "email": "ironman@marvel.com", "team_id": marvel_id},
            {"_id": ObjectId(), "name": "Batman", "email": "batman@dc.com", "team_id": dc_id},
            {"_id": ObjectId(), "name": "Wonder Woman", "email": "wonderwoman@dc.com", "team_id": dc_id},
        ]
        with connection.cursor() as cursor:
            cursor.db_conn["users"].insert_many(users)
            cursor.db_conn["users"].create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"_id": ObjectId(), "user_email": "spiderman@marvel.com", "activity": "Running", "duration": 30},
            {"_id": ObjectId(), "user_email": "ironman@marvel.com", "activity": "Cycling", "duration": 45},
            {"_id": ObjectId(), "user_email": "batman@dc.com", "activity": "Swimming", "duration": 60},
            {"_id": ObjectId(), "user_email": "wonderwoman@dc.com", "activity": "Yoga", "duration": 40},
        ]
        with connection.cursor() as cursor:
            cursor.db_conn["activities"].insert_many(activities)

        # Workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Cardio", "suggested_by": "Spider-Man"},
            {"_id": ObjectId(), "name": "Strength Training", "suggested_by": "Iron Man"},
            {"_id": ObjectId(), "name": "Night Ops", "suggested_by": "Batman"},
            {"_id": ObjectId(), "name": "Amazon Circuit", "suggested_by": "Wonder Woman"},
        ]
        with connection.cursor() as cursor:
            cursor.db_conn["workouts"].insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user_email": "spiderman@marvel.com", "score": 120},
            {"_id": ObjectId(), "user_email": "ironman@marvel.com", "score": 110},
            {"_id": ObjectId(), "user_email": "batman@dc.com", "score": 130},
            {"_id": ObjectId(), "user_email": "wonderwoman@dc.com", "score": 125},
        ]
        with connection.cursor() as cursor:
            cursor.db_conn["leaderboard"].insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

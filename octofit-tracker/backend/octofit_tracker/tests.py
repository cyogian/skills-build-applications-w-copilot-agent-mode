from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, distance=5)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_by=self.user)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_user(self):
        self.assertEqual(self.activity.user, self.user)

    def test_workout_suggested_by(self):
        self.assertEqual(self.workout.suggested_by, self.user)

    def test_leaderboard_user(self):
        self.assertEqual(self.leaderboard.user, self.user)

from operator import attrgetter
import datetime

class Activity:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = datetime.time(hour=start_time, minute=30)
        self.end_time = datetime.time(hour=end_time)

    def conflicts_with(self, other_activity):
        if self.end_time <= other_activity.start:
            return False # No conflict
        elif self.start_time >= other_activity.end:
            return False # No conflict
        else:
            return True # Conflict

def activity_selector(activity_list):
    chosen_activities = []

    # Sort activities
    activity_list.sort(key = attrgetter('end_time'))

    # Add first activity to itinerary
    current_activity = activity_list[0]
    chosen_activities.append(current_activity)

    # Add next activity. Check for conflicts
    for next_activity in activity_list:
        if not next_activity.conflicts_with(current_activity):
            chosen_activities.append(next_activity)
            current_activity = next_activity

    return chosen_activities

# Program to test Activity Selection greedy algorithm. The
# start_time and finish_time are represented with integers
# (ex. "20" is 20:00, or 8:00 PM).
activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

itinerary = activity_selector(activities)
for activity in itinerary:
    print(f'{activity.name}: Start: {activity.start} End: {activity.end}')
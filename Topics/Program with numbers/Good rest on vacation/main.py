# put your python code here

duration = int(input())
food_cost = int(input())
flight_cost = int(input())
night_cost = int(input())

total_food_cost = food_cost * duration
total_flight_cost = flight_cost * 2
total_nights_cost = (duration - 1) * night_cost

print(total_food_cost + total_flight_cost + total_nights_cost)

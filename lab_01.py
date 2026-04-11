distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1 and not(is_raining):
    print(True)
elif 1 < distance_mi and distance_mi <= 6 and (not(has_bike) and is_raining):
    print(False)
elif 1 < distance_mi and distance_mi <= 6 and (not(has_bike) and not(is_raining)):
    print(False)
elif 1 < distance_mi and distance_mi <= 6 and (has_bike and not(is_raining)):
    print(True)
elif distance_mi > 6 and has_car or has_ride_share_app:
    print(True)
else:
    print(False)
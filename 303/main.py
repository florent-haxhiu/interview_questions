
def sol(time: str):
    # Return to the nearest degree
    arr = time.split(':')
    hour, min = int(arr[0]), int(arr[1])

    if (hour * 5) == 60 and min == 0:
        return 0

    if (hour * 5) == min:
        return 0

    angle_of_min_hand = min * 6
    angle_of_hour_hand = hour * 30

    angle_of_hour_hand = 0 if angle_of_hour_hand == 360 else angle_of_hour_hand

    biggest_angle = max(angle_of_min_hand, angle_of_hour_hand)
    smallest_angle = angle_of_min_hand if angle_of_min_hand < angle_of_hour_hand else angle_of_hour_hand

    return biggest_angle - smallest_angle


def test():
    assert sol("12:15") == 90
    assert sol("01:30") == 150
    assert sol("03:30") == 90
    assert sol("07:39") == 24
    assert sol("05:25") == 0

    print("TESTS SUCCESSFUL")


test()

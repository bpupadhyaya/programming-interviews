"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium,
and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:
- ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots
for each parking space are given as part of the constructor.
- bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into
the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3
respectively. A car can only park in a parking space of its carType. If there is no space available, return false,
else park the car in that size space and return true.

Example:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

Tag: 1603/2927 , R439/2935 , R21/50 (amz)
"""


class ParkingSystem:
    __slots__ = ['_parking']

    def __init__(self, big: int, medium: int, small: int):
        self._parking = {
            1: big,
            2: medium,
            3: small
        }

    def add_car(self, car_type: int) -> bool:
        available_spots = self._parking[car_type]
        if available_spots:
            self._parking[car_type] = available_spots - 1
            return True
        else:
            return False


class ParkingSystem1:
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big, medium, small]

    def add_car(self, car_type: int) -> bool:
        if car_type == 1:
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True
        elif car_type == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True
        elif car_type == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2] -= 1
                return True
        return False


def main():
    parking_system = ParkingSystem1(1, 1, 0)
    print(parking_system.add_car(1))  # return true because there is 1 available slot for a big car
    print(parking_system.add_car(2))  # return true because there is 1 available slot for a medium car
    print(parking_system.add_car(3))  # return false because there is no available slot for a small car
    print(parking_system.add_car(1))  # return false because there is no available slot for a big car. It is
    # already occupied.


if __name__ == "__main__":
    main()

"""
Explanation for ParkingSystem class:
Declare __slots__ at the class level to save a little memory. Use a dictionary to store the count of 
available spots.

When adding a car for a given type, first check the number of available spots via
 available_spots = self._parking[carType]. If it is true (e.g. > 0), then reduce availability by one 
 and return True. Otherwise the function just returns False.
"""
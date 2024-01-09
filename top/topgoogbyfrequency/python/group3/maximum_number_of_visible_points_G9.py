"""
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i]
= [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate.
 In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining
  how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise.
   Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
(visualization)
You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate
 east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these
 points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

Example:
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view,
 including [3,3] even though [2,2] is in front and in the same line of sight.

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100

"""
import math


def visible_points(points: list[list[int]], angle: int, location: list[int]) -> int:
    def angle_from_me(point):
        """ Returns the angle between you and point in degrees """
        x1, y1 = location
        x2, y2 = point
        height = y2 - y1
        width = x2 - x1
        alpha = math.atan2(height, width) * (180 / math.pi)
        return alpha if alpha >= 0 else alpha + 360

    # 1. Count and remove any points that are at your location.
    initial_length = len(points)
    points = [point for point in points if point != location]
    points_on_me = initial_length - len(points)

    # 2. Calculate the angle between you and each point.
    #    i.  Sort the angles from smallest to largest.
    #    ii. Extend angles [0, 40, 355] -> [0, 40, 355, 360, 400, 715]
    #        This allows us to see that 355 is close to 0 in step 3.
    angles = sorted((angle_from_me(point) for point in points))
    if not angles:
        return points_on_me
    angles += [a + 360 for a in angles]

    # 3. Use a sliding window to count the most points that can be observed.
    #    The sliding window [i,j] changes size so that all angles[i:j] are visible.
    most_points_observable = 0
    i = j = 0
    while j < len(angles):
        while j < len(angles) and angles[j] - angles[i] <= angle:
            j += 1

        most_points_observable = max(j - i, most_points_observable)

        while (j < len(angles)) and (i < j) and (angles[j] - angles[i] > angle):
            i += 1

    return points_on_me + most_points_observable


def main():
    points = [[2, 1], [2, 2], [3, 3]]
    angle = 90
    location = [1, 1]
    print(visible_points(points, angle, location))


if __name__ == "__main__":
    main()

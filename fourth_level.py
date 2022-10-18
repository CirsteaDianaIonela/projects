class Corners:
    def __init__(self, number_corners=0, number_90degrees_corners=0):
        self.number_corners = number_corners
        self.number_90degrees_corners = number_90degrees_corners

    def get_no_corners(self):
        return self.number_corners

    def get_number_90degrees_corners(self):
        return self.number_90degrees_corners

    def set_no_corners(self, number_corners):
        self.number_corners = number_corners
        return self.number_corners

    def set_number_90degrees_corners(self, number_90degrees_corners):
        self.number_90degrees_corners = number_90degrees_corners
        return self.number_90degrees_corners


# class Room(Corners):
#     pass

# room1 = Room()
# # print(room1)
# room1.set_no_corners(4)
# print(room1.get_no_corners())


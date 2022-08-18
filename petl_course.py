import petl as etl
import csv
from petl import appendcsv

# fruit_qty = (["apple", "orange", "mango"], [23, 56, 34])
# fruits = etl.fromcolumns(fruit_qty)
# print(fruits)
# print(type(fruits))

game_data = [["Rank", "Name"], [1, "WiiSport"], [2, "SuperMario Bros"]]

with open('./datasets.csv', 'w', newline='') as gamefile:
    writer = csv.writer(gamefile)
    writer.writerows(game_data)

video_game_details = etl.fromcsv('./datasets/game.csv')
print(etl.look(video_game_details))
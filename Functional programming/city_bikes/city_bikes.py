# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    stations = {}

    with open(filename,'r') as file:
        for line in file:
            line = line.strip().split(';')
            if line[0] == "Longitude":
                continue
            stations[str(line[3])] = (float(line[0]), float(line[1]))

        return stations

def distance(stations: dict, station1: str, station2: str) -> float:
        longitude1, latitude1 = stations[station1]
        longitude2, latitude2 = stations[station2]

        x_km = (longitude1 - longitude2) * 55.26
        y_km = (latitude1 - latitude2) * 111.2
        distance_km = math.sqrt(x_km**2 + y_km**2)

        return distance_km

def greatest_distance(stations: dict) -> tuple:
    greatest_dist = 0
    station1_name = ''
    station2_name = ''
    
    for station1, coords1 in stations.items():
        for station2, coords2 in stations.items():
            if station1 != station2:
                dist = distance(stations, station1, station2)  
                if dist > greatest_dist:
                    greatest_dist = dist
                    station1_name = station1
                    station2_name = station2
    
    return station1_name, station2_name, greatest_dist

if __name__ == '__main__':
    stations = (get_station_data('stations1.csv'))
    #d = distance(stations, "Designmuseo", "Hietalahdentori")
    #print(d)
    #d = distance(stations, "Viiskulma", "Kaivopuisto")
    #print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
states_needed = set(["mt", "wa", "ct", "ma", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["ma", "nv", "ut"])
stations["ktwo"] = set(["wa", "ma", "mt"])
stations["kthree"] = set(["ct", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = (
        set()
    )  # a set of all states this station covers that haven't been covered yet
    for station, states in stations.items():
        covered = states_needed & states  # set intersection!
        if len(covered) > len(
            states_covered
        ):  # does the covered station do a better job at covering states?
            best_station = station  # if so, make it the best station
            states_covered = covered
states_needed -= states_covered
final_stations.add(best_station)

print(final_stations)

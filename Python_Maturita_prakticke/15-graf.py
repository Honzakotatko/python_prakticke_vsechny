import csv
import heapq

def read_graph_from_csv(filename):
    """
    Načte data z CSV souboru a vytvoří graf.
    Předpokládáme, že CSV obsahuje záhlaví se sloupci:
    "city1", "city2", "distance"
    Graf je reprezentován slovníkem, kde klíč je název města
    a hodnota je seznam dvojic (soused, vzdálenost).
    """
    graph = {}
    # Otevření souboru CSV pro čtení s UTF-8 kódováním
    with open(filename, newline='') as csvfile:#TUHLE U MATURITY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        reader = csv.DictReader(csvfile)
        for row in reader:
            city1 = row['city1']
            city2 = row['city2']
            distance = float(row['distance'])
            # Přidání obousměrné hrany do grafu
            graph.setdefault(city1, []).append((city2, distance))
            graph.setdefault(city2, []).append((city1, distance))
    return graph

def dijkstra(graph, start, end):
    """
    Implementace Dijkstrova algoritmu pro nalezení nejkratší cesty.
    Používáme prioritní frontu (min-heap) pro efektivní výběr uzlu
    s nejmenší vzdáleností. Vrací tuple: (cesta, celková vzdálenost).
    """
    # Inicializace vzdáleností (nekonečno) a předchůdců (None)
    distances = {city: float('inf') for city in graph}
    previous = {city: None for city in graph}
    distances[start] = 0
    queue = [(0, start)]  # min-heap: (vzdálenost, město)

    while queue:
        current_distance, current_city = heapq.heappop(queue)
        # Jakmile narazíme na cílové město, můžeme ukončit
        if current_city == end:
            break
        # Přeskočíme, pokud jsme mezitím našli lepší cestu
        if current_distance > distances[current_city]:
            continue
        # Projeď sousedy
        for neighbor, weight in graph[current_city]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(queue, (distance, neighbor))

    # Rekonstrukce cesty: jdeme zpět od 'end' k 'start'
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path, distances[end]

def shortest_path_via(graph, start, via, end):
    """
    Najde nejkratší cestu z 'start' do 'end' s povinnou návštěvou 'via'.
    Postup: spočítáme dvě dijkstry a spojíme výsledné části.
    """
    path1, dist1 = dijkstra(graph, start, via)
    path2, dist2 = dijkstra(graph, via, end)
    # Spojíme bez duplikace města 'via'
    combined_path = path1 + path2[1:]
    total_distance = dist1 + dist2
    return combined_path, total_distance

def find_all_paths(graph, start, end, path=None):
    """
    Rekurzivní hledání všech jednoduchých (acyklických) cest
    mezi dvěma městy. Vrací seznam cest, kde každá cesta je list měst.
    """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor, _ in graph[start]:
        if neighbor not in path:
            newpaths = find_all_paths(graph, neighbor, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def path_distance(graph, path):
    """
    Vypočítá celkovou vzdálenost pro danou cestu (list měst).
    """
    distance = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i+1]:
                distance += weight
                break
    return distance

def longest_path_via(graph, start, via, end):
    """
    Najde nejdelší jednoduchou cestu mezi 'start' a 'end',
    která obsahuje 'via'. Prohledává všechny cesty (může být pomalé).
    """
    all_paths = find_all_paths(graph, start, end)
    # Filtrujeme jen ty, které obsahují 'via'
    valid_paths = [p for p in all_paths if via in p]
    if not valid_paths:
        return None, None
    # Vyber cestu s maximální vzdáleností
    longest = max(valid_paths, key=lambda p: path_distance(graph, p)) #tady zmenit maxna min MATURITA
    max_distance = path_distance(graph, longest)
    return longest, max_distance

if __name__ == "__main__":
    # Načtení grafu ze souboru cities.csv
    graph = read_graph_from_csv("cities.csv")

    # Nastavení měst
    start_city = "Praha"
    via_city   = "Brno"
    end_city   = "Ostrava"

    # Nejkratší cesta přes Brno
    shortest, short_dist = shortest_path_via(graph, start_city, via_city, end_city)
    print(f"Nejkratší cesta: {' -> '.join(shortest)}, vzdálenost: {short_dist}")

    # Nejdelší cesta přes Brno
    longest, long_dist = longest_path_via(graph, start_city, via_city, end_city)
    print(f"Nejdelší cesta: {' -> '.join(longest)}, vzdálenost: {long_dist}")
    
    


import csv

filename = "soubor.csv"

def otevreni():
    rows = []
    
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            rows.append(row)
        return rows
    
print(otevreni())
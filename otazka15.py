"""
import heapq

def dijkstra (graf, start):
    vzdalenosti = {vrchol: float('inf') for vrchol in graf}
    vzdalenosti[start] = 0
    predek = {vrchol: None for vrchol in graf}
    priorita = [(0, start)]


    while priorita:
        akt_vzdalenost, akt_vrchol = heapq.heappop(priorita)
        if akt_vzdalenost > vzdalenosti[akt_vrchol]:
            continue
        for soused, vaha in graf[akt_vrchol]:
            nova_vzdalenost = akt_vzdalenost + vaha

            if nova_vzdalenost < vzdalenosti[soused]:
                vzdalenosti[soused] = nova_vzdalenost
                predek[soused] = akt_vrchol
                heapq.heappush(priorita, (nova_vzdalenost,soused))

    return vzdalenosti, predek

graf = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

vzdalenosti, predek = dijkstra(graf, 'A')
print("Nejkratsi vzdalenosti: ", vzdalenosti)
print("Zpetna cesta: ", predek)

"""
# Reprezentace grafu měst se vzdálenostmi
graf = {
    "Praha": {"Brno": 205, "Plzeň": 90},
    "Brno": {"Praha": 205, "Ostrava": 170},
    "Plzeň": {"Praha": 90, "Karlovy Vary": 80},
    "Ostrava": {"Brno": 170},
    "Karlovy Vary": {"Plzeň": 80}
}

# Výpis měst a jejich sousedů
for mesto, sousede in graf.items():
    print(f"{mesto}:")
    for soused, vzdalenost in sousede.items():
        print(f"  -> {soused} ({vzdalenost} km)")

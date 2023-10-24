from typing import Dict

global_cities = {
    'Reykjavik': {'Reykjavik': 0, 'Akureyri': 388},
    'Akureyri': {'Reykjavik': 388, 'Akureyri': 0},
    'Kopavogur': {'Reykjavik': 6, 'Akureyri': 387},
    'Hafnarfjordur': {'Reykjavik': 12, 'Akureyri': 391},
    'Reykjanesbaer': {'Reykjavik': 48, 'Akureyri': 427},
    'Gardabaer': {'Reykjavik': 9, 'Akureyri': 389},
    'Mosfellsbaer': {'Reykjavik': 16, 'Akureyri': 371},
    'Arborg': {'Reykjavik': 64, 'Akureyri': 428},
    'Akranes': {'Reykjavik': 49, 'Akureyri': 350},
    'Fjardabyggd': {'Reykjavik': 659, 'Akureyri': 290},
    'Mulathing': {'Reykjavik': 603, 'Akureyri': 216},
    'Seltjarnarnes': {'Reykjavik': 4, 'Akureyri': 390}
}


def nearest(input_city: str, local_cities: Dict[str, Dict[str, int]]) -> str:
    closest_city = None

    if input_city not in local_cities:
        return "Akureyri"

    closest_city = (
        'Akureyri' if local_cities[input_city]['Reykjavik'] >
        local_cities[input_city]['Akureyri'] else 'Reykjavik'
    )

    return closest_city


def main() -> None:
    print(nearest(input(), global_cities))


if __name__ == "__main__":
    main()

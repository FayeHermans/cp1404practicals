"""
CP1404 Practical 05
wimbledon
Estimate: 30 min
Actual: 23 min
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and print details about wimbledon players and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    print_results(champion_to_count, countries)


def load_records(filename):
    """Load from file in list."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary with champions and countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def print_results(champion_to_count, countries):
    """Print champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()

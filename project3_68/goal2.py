from goal1 import *
from collections import defaultdict

def violation_count_by_make():
    makes_counts = defaultdict(int)

    for data in parse_data():
        makes_counts[data.vehicle_make] += 1

    return { make : cnt for make, cnt in sorted(makes_counts.items(), 
                            key = lambda x : x[1], 
                            reverse = True)
            }


if __name__ == "__main__":
    print("="*30)
    print("\n\n")
    print(violation_count_by_make())




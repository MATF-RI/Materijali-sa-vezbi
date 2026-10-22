import numpy as np

def read_line_of_ints(f) -> list[int]:
    return [int(x) for x in f.readline().split()]

def read_instance(file_path: str) -> tuple[int, int, list[list[int]], list[int]]:
    with open(file_path, "r") as f:
        m, n = [int(x) for x in f.readline().split()]
        cost = [[int(x) for x in f.readline().split()] for _ in range(m)]
        facility_cost = [int(x) for x in f.readline().split()]
        return m, n, np.array(cost), np.array(facility_cost)

def read_bk_instance(file_path : str) -> tuple[int, int, list[list[int]], list[int]]:
    with open(file_path, "r") as f:
        f.readline()
        num_resources, num_users, _ = read_line_of_ints(f)
        cost = [[None for _ in range(num_users)] for _ in range(num_resources)]
        facility_cost = [None for _ in range(num_resources)]
        for i in range(num_resources):
            ints = read_line_of_ints(f)
            cost[i] = ints[2:]
            facility_cost[i] = ints[1]
    return num_users, num_resources, np.array(cost).transpose(), np.array(facility_cost)

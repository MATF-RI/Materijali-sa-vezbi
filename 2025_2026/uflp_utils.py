import numpy as np


def read_instance(file_path: str) -> tuple[list[list[int]], list[int]]:
    with open(file_path, "r") as f:
        m, n = read_line_of_ints(f)
        cost = [read_line_of_ints(f) for _ in range(m)]
        facility_cost = read_line_of_ints(f)
        return cost, facility_cost


def read_line_of_ints(f) -> list[int]:
    return [int(x) for x in f.readline().split()]


def read_bk_instance(file_path: str = "BildeKrarup/B/B1.1") -> tuple[np.ndarray, np.ndarray]:
    with open(file_path, "r") as f:
        f.readline()
        num_resources, num_users, _ = read_line_of_ints(f)
        cost = [[None for _ in range(num_users)] for _ in range(num_resources)]
        facility_cost = [None for _ in range(num_resources)]
        for i in range(num_resources):
            ints = read_line_of_ints(f)
            cost[i] = ints[2:]
            facility_cost[i] = ints[1]
    return np.array(cost).transpose(), np.array(facility_cost)


def objective(s: np.ndarray, user_cost: np.ndarray, resource_cost: np.ndarray):
    open = np.where(s)[0]
    if len(open) == 0:
        return user_cost.sum() + resource_cost.sum()
    total_cost = resource_cost[open].sum()
    total_cost += user_cost[:, open].min(axis=1).sum()
    return total_cost

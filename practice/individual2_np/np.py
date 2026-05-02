import itertools
import random


def calculate_penalty(schedule):
    current_time = 0.0
    total_penalty = 0.0
    for _, t, d, p in schedule:
        current_time += t
        if current_time > d:
            total_penalty += p
    return total_penalty



def exact_brute_force(jobs):
    min_penalty = float('inf')
    best_order = None
    for perm in itertools.permutations(jobs):
        pen = calculate_penalty(perm)
        if pen < min_penalty:
            min_penalty = pen
            best_order = [j[0] for j in perm]
    return best_order, min_penalty



def heuristic_edd(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[2])
    order = [j[0] for j in sorted_jobs]
    pen = calculate_penalty(sorted_jobs)
    return order, pen



def heuristic_high_penalty_first(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[3], reverse=True)
    order = [j[0] for j in sorted_jobs]
    pen = calculate_penalty(sorted_jobs)
    return order, pen



def heuristic_local_search(jobs, iterations=1000):
    current = list(jobs)
    best_penalty = calculate_penalty(current)
    best_schedule = [j[0] for j in current]
    
    for _ in range(iterations):
        i, j = random.sample(range(len(current)), 2)
        current[i], current[j] = current[j], current[i]
        pen = calculate_penalty(current)
        if pen < best_penalty:
            best_penalty = pen
            best_schedule = [x[0] for x in current]
        else:
            current[i], current[j] = current[j], current[i]
    return best_schedule, best_penalty



if __name__ == "__main__":
    jobs = [
        (1, 2, 5, 10),
        (2, 3, 6, 20),
        (3, 1, 4, 5),
        (4, 4, 10, 15)
    ]
    
    print("Brute Force:", exact_brute_force(jobs))
    print("EDD:", heuristic_edd(jobs))
    print("High Penalty First:", heuristic_high_penalty_first(jobs))
    print("Local Search:", heuristic_local_search(jobs))
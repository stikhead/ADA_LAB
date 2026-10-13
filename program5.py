from typing import List

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x[2], reverse=True)
    
    max_profit = 0.0
    
    for value, weight, ratio in items:
        if capacity >= weight:
            capacity -= weight
            max_profit += value
        else:
            max_profit += value * (capacity / weight)
            break
            
    return max_profit


class Job:
    def __init__(self, job_id: int, deadline: int, profit: int):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    max_deadline = max((job.deadline for job in jobs), default=0)
    slots = [-1] * (max_deadline + 1)
    scheduled_jobs = []
    
    for job in jobs:
        for i in range(min(max_deadline, job.deadline), 0, -1):
            if slots[i] == -1:
                slots[i] = job.job_id
                scheduled_jobs.append(job.job_id)
                break
                
    return scheduled_jobs


if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    knapsack_profit = fractional_knapsack(weights, values, capacity)
    print(f"Maximum profit for Fractional Knapsack: {knapsack_profit}")
    jobs = [
        Job(job_id=1, deadline=4, profit=20),
        Job(job_id=2, deadline=1, profit=10),
        Job(job_id=3, deadline=1, profit=40),
        Job(job_id=4, deadline=1, profit=30)
    ]
    
    scheduled_jobs = job_scheduling(jobs)
    print(f"Optimal job sequence: {scheduled_jobs}")
import random

def estimate_pi(n):
    num_points_inside_circle = 0
    num_points_total = n

    for _ in range(num_points_total):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            num_points_inside_circle += 1

    return 4 * num_points_inside_circle / num_points_total

pi_estimate = estimate_pi(100000)
print(f"Estimated value of pi: {pi_estimate:.2f}")
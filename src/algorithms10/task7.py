import random
import matplotlib.pyplot as plt


num_simulations = 1000000
sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    dice_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[dice_sum] += 1


monte_carlo_probs = {k: (v / num_simulations) * 100 for k, v in sum_counts.items()}
theoretical_probs = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

print("Sum | Monte Carlo (%) | Theoretically (%)")
print("-----------------------------------")
for i in range(2, 13):
    print(f" {i:>2}  | {monte_carlo_probs[i]:>12.2f}  | {theoretical_probs[i]:>12.2f}")


plt.figure(figsize=(10, 5))
plt.bar(monte_carlo_probs.keys(), monte_carlo_probs.values(), color='blue', alpha=0.6, label='Monte Carlo')
plt.plot(theoretical_probs.keys(), theoretical_probs.values(), color='red', marker='o', linestyle='dashed', label='Theoretically')
plt.xlabel('Sum on two cubes')
plt.ylabel('Probability (%)')
plt.title('Comparison of probabilities (Monte Carlo vs Theoretically)')
plt.legend()
plt.grid()
plt.show()
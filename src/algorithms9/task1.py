from pulp import LpMaximize, LpProblem, LpVariable

# Create the model
model = LpProblem(name="maximize_drink_production", sense=LpMaximize)

# Define the variables
lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

# Add constraints
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit")
model += (1 * lemonade <= 50, "Sugar_Limit")
model += (1 * lemonade <= 30, "Lemon_Juice_Limit")
model += (2 * fruit_juice <= 40, "Fruit_Puree_Limit")

# Set the objective
model += lemonade + fruit_juice, "Total_Drinks"

# Solve the problem
model.solve()

# Print the results
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")
print(f"Total Drinks: {model.objective.value()}")
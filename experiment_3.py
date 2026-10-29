# WAP to implement hill climbing program

# objective function
def objective_function(x):
    return -(x**2) + 10

def hill_climbing(Start, step_size, max_iterations):
    Current = Start
    Current_value = objective_function(Current)
    
    for i in range(max_iterations):
        left = Current - step_size
        right = Current + step_size
        left_value = objective_function(left)
        right_value = objective_function(right)
        
        if left_value > Current_value:
            Current = left
            Current_value = left_value
        elif right_value > Current_value:
            Current = right
            Current_value = right_value
        else:
            break
            
    return Current, Current_value

Start = float(input("E…
print("Best position = ", best_position)
print("Best value = ", best_value)

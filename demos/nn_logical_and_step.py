'''
A Simple Perceptron for Logical AND using the Step Function.
This is the best model to run for initial understanding, as there isn't much 
complexity,and we're not using any libraries.
'''
# Define the logical AND function with training and testing phases
def logical_and_train():
    # Define initial weights and bias
    weight1 = 0.0
    weight2 = 0.0
    bias = 0.0
    learning_rate = 0.1

    # Training data for logical AND
    training_data = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]

    # Number of training iterations
    num_iterations = 1000

    # Training loop
    for _ in range(num_iterations):
        for x1, x2, target in training_data:
            # Calculate the weighted sum
            weighted_sum = x1 * weight1 + x2 * weight2 + bias

            # Apply the step function (thresholding)
            if weighted_sum > 0:
                output = 1  # True
            else:
                output = 0  # False

            # Calculate the error
            error = target - output

            # Update weights and bias using the perceptron learning rule
            weight1 += learning_rate * error * x1
            weight2 += learning_rate * error * x2
            bias += learning_rate * error

    # Return the trained weights and bias as a tuple
    return weight1, weight2, bias

# Define the logical AND function for testing
def logical_and_test(x1, x2, weights):
    weight1, weight2, bias = weights

    # Calculate the weighted sum
    weighted_sum = x1 * weight1 + x2 * weight2 + bias

    # Apply the step function (thresholding)
    if weighted_sum > 0:
        return 1  # True
    else:
        return 0  # False

# Train the perceptron and get the trained weights and bias
trained_weights = logical_and_train()

# Test the perceptron with different inputs
print("AND(0, 0) =", logical_and_test(0, 0, trained_weights))  # Should output 0
print("AND(0, 1) =", logical_and_test(0, 1, trained_weights))  # Should output 0
print("AND(1, 0) =", logical_and_test(1, 0, trained_weights))  # Should output 0
print("AND(1, 1) =", logical_and_test(1, 1, trained_weights))  # Should output 1
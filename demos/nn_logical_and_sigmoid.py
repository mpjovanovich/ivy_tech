'''
A Perceptron for Logical AND using the Sigmoid Function.
Adds a little more complexity, such as the numpy library and
dot products for efficient calculations.
'''
import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the logical AND function with training and testing phases
def logical_and_train():
    # Define training data for logical AND
    training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 0, 0, 1])

    # Initialize weights and bias
    num_features = 2
    weights = np.random.rand(num_features)
    bias = np.random.rand()

    # Set learning rate and number of training iterations
    learning_rate = 0.1
    num_iterations = 10000

    # Training loop
    for iteration in range(num_iterations):
        # Initialize gradients for weights and bias
        grad_weights = np.zeros(num_features)
        grad_bias = 0

        # Iterate through training examples
        for i in range(len(training_data)):
            # Forward pass
            weighted_sum = np.dot(training_data[i], weights) + bias
            prediction = sigmoid(weighted_sum)

            # Calculate error
            error = target[i] - prediction

            # Update gradients
            grad_weights += learning_rate * error * prediction * (1 - prediction) * training_data[i]
            grad_bias += learning_rate * error * prediction * (1 - prediction)

        # Update weights and bias after processing all examples
        weights += grad_weights
        bias += grad_bias

    # Return the trained weights and bias as a tuple
    return weights, bias

# Define the logical AND function for testing
def logical_and_test(inputs, weights, bias):
    weighted_sum = np.dot(inputs, weights) + bias
    prediction = sigmoid(weighted_sum)
    return 1 if prediction > 0.5 else 0

# Train the perceptron and get the trained weights and bias
trained_weights, trained_bias = logical_and_train()

# Test the perceptron with different inputs
test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for input_pair in test_inputs:
    result = logical_and_test(input_pair, trained_weights, trained_bias)
    print(f"AND({input_pair[0]}, {input_pair[1]}) = {result}")
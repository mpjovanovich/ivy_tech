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
    # Set the training constants
    LEARNING_RATE = 0.1
    NUM_ITERATIONS = 1000

    # Initialize weights and bias to random values
    num_features = 2
    weights = np.random.rand(num_features)
    bias = np.random.rand()

    # Training data for logical AND
    training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 0, 0, 1])

    # Training loop
    for iteration in range(NUM_ITERATIONS):
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

            # Update gradients per the chain rule:
            # Given derivative of sigmoid: σ'(x) = σ(x) * (1 - σ(x))
            # Roughly below: (LEARNING_RATE * error) * (σ'(x) * input)
                # Take a fraction of the error (determined by learning rate)
                # Multiply by the derivative of the sigmoid function
                # Multiply by the input (training data)
            grad_weights += LEARNING_RATE * error * prediction * (1 - prediction) * training_data[i]
            grad_bias += LEARNING_RATE * error * prediction * (1 - prediction)

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
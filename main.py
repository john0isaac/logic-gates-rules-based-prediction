import random
import sys

# Define first input pattern
x1 = [0, 0, 1, 1]
# Define second input pattern
x2 = [0, 1, 0, 1]
# Define a varibale to store the output in
desired_output = []
# Intialize a list with for the predicted output 
predicted_output = [0, 0, 0, 0]
# Intialize the first weight randomly and rounding it to the nearest digit
w1 = [round(random.uniform(-0.9, 0.9), 1)]
# Intialize the second weight randomly and rounding it to the nearest digit
w2 = [round(random.uniform(-0.9, 0.9), 1)]
# Intialize the learning rate alpha
alpha = 0.1
# Create a list to store the calculated errors 
errors = []

# A function to apply the TLU using specific threshold and input values
def activation(y_in, threshold):
    # Check if the value is larger than threshold then fire (activate)
    if y_in >= threshold:
        y_pred = 1
    # Check if the value is smaller than threshold then don't activate
    else:
        y_pred = 0
    return y_pred

# A funcion to calculate the weights in each iteration
def calculate_weights(a, b, y_desired, threshold, weight_1, weight_2):
    # Calculate the weighted sum of product
    y_in = (a * weight_1) + (b * weight_2)
    # Apply the TLU
    y_out = activation(y_in, threshold)

    # Calculate the error
    error = y_desired - y_out
    # Save the error in an array
    errors.append(error)

    # Update the weights and round them to the nearest two digits
    w_new_1 = round(weight_1 + (alpha * error * a), 2)
    w_new_2 = round(weight_2 + (alpha * error * b), 2)
    # Save the weights in an array
    w1.append(w_new_1)
    w2.append(w_new_2)

    return y_out

if __name__ == "__main__":
    # Input the user desired ouput
    for i in range(4):
        print("x1\tx2")
        print('{}\t{}'.format(x1[i], x2[i]))
        x = int(input("desired output: "))
        desired_output.append(x)
        print("______________")
    # Input the user threshold
    threshold = float(input("threshold value: "))

    # Set the number of epochs to maximum number in system
    no_of_epochs = sys.maxsize

    # Multiply them by 4
    epochs = no_of_epochs * 4
    # Iterate over each epoch in the epochs using step 4
    for epoch in range(0, epochs, 4):
        # Print the current number of the epoch
        print("epoch no", round(epoch/4))
        print("x1\tx2\tdesired output\tweight 1\tweight 2\terror\tpredicted output")
        # Iterate over the 4 input values
        for i in range(4):
            # Call the function to calculate the weights
            predicted_output[i] = calculate_weights(x1[i], x2[i], desired_output[i], threshold, w1[i+epoch], w2[i+ epoch])
            print('{}\t{}\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(x1[i],x2[i],desired_output[i],w1[i+ epoch],w2[i+ epoch], errors[i+epoch],predicted_output[i]))
        
        # Check if one full iteration results in no error
        complete = (errors[epoch: epoch+4] == [0,0,0,0])
        # Break when there is no error difference
        if complete:
            break
    print("Finished!!")
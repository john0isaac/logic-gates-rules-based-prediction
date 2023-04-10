import random
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
desired_output = []
predicted_output = [0, 0, 0, 0]
w1 = [round(random.uniform(-0.9, 0.9), 1)]
w2 = [round(random.uniform(-0.9, 0.9), 1)]
alpha = 0.1
errors = []


def activation(y_in, threshold):
    if y_in >= threshold:
        y_pred = 1
    else:
        y_pred = 0
    return y_pred

def calculate_weights(a, b, y_desired, threshold, weight_1, weight_2):
    y_in = (a * weight_1) + (b * weight_2)
    y_out = activation(y_in, threshold)

    error = y_desired - y_out
    errors.append(error)
    w_new_1 = round(weight_1 + (alpha * error * a), 2)
    w_new_2 = round(weight_2 + (alpha * error * b), 2)
    w1.append(w_new_1)
    w2.append(w_new_2)

    return y_out

if __name__ == "__main__":
    for i in range(4):
        print("x1\tx2")
        print('{}\t{}'.format(x1[i], x2[i]))
        x = int(input("desired output: "))
        desired_output.append(x)
        print("______________")
    threshold = float(input("threshold value: "))
    no_of_epochs = 10
    epochs = no_of_epochs * 4
    for epoch in range(0, epochs, 4):
        print("epoch no", round(epoch/4))
        print("x1\tx2\tdesired output\tweight 1\tweight 2\terror\tpredicted output")
        for i in range(4):
            predicted_output[i] = calculate_weights(x1[i], x2[i], desired_output[i], threshold, w1[i+epoch], w2[i+ epoch])
            print('{}\t{}\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(x1[i],x2[i],desired_output[i],w1[i+ epoch],w2[i+ epoch], errors[i+epoch],predicted_output[i]))
    

    
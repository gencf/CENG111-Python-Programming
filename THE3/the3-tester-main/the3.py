def forward_pass(Network, X):
    from math import exp

    def relu(a):
        output = []
        for i in a:
            output.append(max(0, i))
        return output

    def linear(a, w):
        output = []
        for i in range(len(w)):
            sum = 0
            for j in range(len(w[0])):
                sum += a[j] * w[i][j]
            output.append(sum)
        return output

    def sigmoid(a):
        output = []
        for x in a:
            if x <= -700:
                output.append(0)
            elif -700 < x and x < 700:
                output.append(1 / (1 + exp(-x)))
            elif 700 <= x:
                output.append(1)
        return output

    data = X[:]
    
    for i in range(len(Network)):
        if Network[i][0].split("_")[0] == "linear":
            weights = Network[i][1][:]
            output = linear(data, weights)

        elif Network[i].split("_")[0] == "relu":
            output = relu(data)

        elif Network[i].split("_")[0] == "sigmoid":
            output = sigmoid(data)        

        data = output[:]

    return output
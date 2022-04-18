from the3 import *
import test
import utils
dataset = utils.load_dataset("mnist.pkl")
network3 = utils.load_network("network_buraklayer.pkl")
test_data_length = len(dataset['X_test'])
true_count = 0
tot_count = 0
for i in range(test_data_length):
    if(test.berk[i]==forward_pass(network3,dataset['X_test'][i])):
        true_count +=1
    tot_count += 1


print("YOU HAVE MATCHED %"+str((true_count/tot_count)*100)+" ")
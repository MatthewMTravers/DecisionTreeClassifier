import argparse
import numpy as np
import sys
from node import Node

# 3.6) Calculate GINI index based on current node
def calculateGINI(data_idx):
    return

# 3.6) Calculate entropy based on current node
def calculateEntropy(data_idx):
    return

def main():
    # 1) Create UI that accepts all command line elements
    parser = argparse.ArgumentParser()

    # Capture command line arguments
    parser.add_argument("-train_data", required=True, type=str)
    parser.add_argument("-train_label", required=True, type=str)
    parser.add_argument("-test_data", required=True, type=str)
    parser.add_argument("-nlevels", required=True, type=int)                            
    parser.add_argument("-pthrd", required=True, type=float)                            
    parser.add_argument("-impurity", required=True, type=str, choices=["gini", "entropy"])        
    parser.add_argument("-pred_file", required=True, type=str, choices=["output.txt"])

    # Parse captured arguments
    args = parser.parse_args()

    # Input validation
    if args.nlevels <= 0:
        print("Error: 'nlevels' must be a positive integer")
        sys.exit(1)
    if args.pthrd <= 0:
        print("Error: 'pthrd' must be a positive float")
        sys.exit(1)

    # Create local variables
    train_file = args.train_data
    train_label = args.train_label
    test_data = args.test_data
    nlevels = args.nlevels
    pthrd = args.pthrd
    impurity = args.impurity

    # 2) Create matrices from input files
    try:
        mat_train_data = np.genfromtxt(train_file, delimiter='')
        mat_train_label = np.genfromtxt(train_label, delimiter='')
        mat_test_data = np.genfromtxt(test_data, delimiter='')
    except:
        print("Error loading matrices from input files")
        sys.exit(1)

    # decision_tree = buildDT(mat_train_data, mat_train_label, impurity, nlevels, pthrd)


# Run the main function
if __name__ == "__main__":
    main()







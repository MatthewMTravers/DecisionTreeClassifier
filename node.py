# 3.1) Create decision tree from training data
class Node:
    def __init__(self, data_idx, label, impurity, level):
        self.data_idx = data_idx            # 3.3) Build root node from data_idx    
        self.impurity_method = impurity     # impurity method to be used
        self.dfeature = None                # chosen decision rule
        self.impurity = None                # computed impurity value
        self.nlevel = level                 # level of each node
        self.mfeatures = None               # number of features
        self.class_label = label            # majority class label

        self.left = None                    # left child, attribute == 0
        self.right = None                   # right child, attribute == 1

    # 3.2) Function to build decision tree, starting at a root (level 0)
    def buildDT(self, data_idx, label, impurity_method, nl, p):
        #TODO: need to get the list of all training samples?
        
        decision_tree = Node(data_idx, label, impurity_method, 0)
        
        # Split nodes based on impurities
        decision_tree.splitNode(nl, p)

        return decision_tree
    
    # 3.4) Splits nodes based on their impurities
    def splitNode(self, nl, p):
        if self.levels < nl and self.impurity > p:
            maxGain = 1
            splitFeature = 1
            for feature in range(0, self.nfeatures):
                p_left = self.calculateIP(self.left.data_idx)
                p_right = self.calculateIP(self.right.data_idx)

                # TODO: calculate impurity after split
                M = None # ^^ Impurity above
                gain = self.impurity #???
                if gain > maxGain:
                    maxGain = gain
                    splitFeature = feature
            self.dfeature = splitFeature

            # TODO: Figure which data does on each side
            data_left = None
            data_right = None

            # Create children nodes with appropriate data
            self.left = Node(data_left, self.impurity_method, self.nlevel+1)
            self.right = Node(data_right, self.impurity_method, self.nlevel+1)

            # Recursively fill out remainder of tree
            self.left.splitNode(nl, p)
            self.right.splitNode(nl, p)

        return

    # 3.5) 
    def calculateIP(self, data_idx):
        if self.impuritiy_method == "gini":
            p = self.calculateGINI(data_idx)
        elif self.impuritiy_method == "entropy":
            p = self.calculateEntropy(data_idx)
        return p
    
    # 4) Classifies each point using tree and writes to output file
    def classify(test_data, output_file):        
        # Open and write to output file
        with open(output_file, "w") as f:
            for data in test_data:
                
                #TODO: Traverse tree and add
                predicted_label = None 
 
                f.write(f"{predicted_label}\n")
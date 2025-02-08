import math

def EntropyCalculator():
    total_observation = int(input("Enter the number of observations: "))
    num_of_classes = int(input("Enter number of classes: "))
    if num_of_classes ==1:
        print("the Entropy of this node: ",0)
        return [0,total_observation]
    p_value = []
    for i in range(num_of_classes-1):
        pval = float(input(f"Enter the number of occurrence of class {i+1}: "))
        
        pval = pval/total_observation
        p_value.append(pval)
    p_value.append(1-sum(p_value))

    sumation = round(sum(p * math.log(p,len(p_value)) for p in p_value),3) *-1
    print("the Entropy of this node: ",sumation)
    return [sumation ,total_observation]





if __name__ == '__main__':
    EntropyCalculator()



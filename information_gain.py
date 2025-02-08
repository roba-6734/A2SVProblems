import math
from entropy_calculator import EntropyCalculator

def InformationGain():
    print("Provide the following information about the parent node")
    parent_entropy,total = EntropyCalculator()

    branches = int(input("how many branches does the parent node have? "))
    output =0
    for i in range(branches):
        print(f"Provide the following information about node {i +1}")
        entropy,child_total = EntropyCalculator()
        output += ((child_total/total)*entropy )
        
    result = round(parent_entropy - output,3)
    print("the information gain: ",result)
    return result


if __name__ =='__main__':
    InformationGain()

    
        

    

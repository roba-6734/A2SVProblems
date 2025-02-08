import math

def EntropyCalculator():
    total_observation = int(input("Enter the number of observations: "))
    num_of_options = int(input("Enter number of options: "))
    p_value = []
    for i in range(num_of_options-1):
        pval = float(input(f"Enter the number of occurrence of option {i+1}: "))
        pval = pval/total_observation
        p_value.append(pval)
    p_value.append(1-sum(p_value))

    sumation = round(sum(p * math.log(p,len(p_value)) for p in p_value),3)
    print(-1*sumation)
    return -1 * sumation




if __name__ == '__main__':
    EntropyCalculator()



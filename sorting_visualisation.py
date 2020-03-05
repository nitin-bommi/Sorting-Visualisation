# Importing the required libraries.
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Defining Bubble Sort function (generator).
def bubbleSort(lst):
    
    if(len(lst)==1):
        return 
    
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
            yield lst

# calling the main function
if __name__ == "__main__":
    
    n = int(input("Enter the number of integers: "))
    
    lst = [x+1 for x in range(n)]
    random.shuffle(lst)
    
    generator = bubbleSort(lst)
    
    fig, ax = plt.subplots()
    
    ax.set_title("Bubble sort")
    
    rect_bars = ax.bar(range(len(lst)), lst, align="edge")
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, n+2)
    
    iteration = [0]
    def update_fig(lst, rects, iteration):
        for rect, val in zip(rects, lst):
            rect.set_height(val)
        iteration[0] += 1
        
    animation = FuncAnimation(fig, func=update_fig, fargs=(rect_bars, iteration), frames=generator, interval=1, repeat=False)
    
    plt.show()

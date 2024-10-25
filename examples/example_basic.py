# examples/example_basic.py
from itemlist import item

# Define sample flow functions
def flow1():
    print("Flow 1 is running...")

def flow2():
    print("Flow 2 is running...")

def flow3():
    print("Flow 3 is running...")

# Register items
@item
def flow_runner(description="Run the first flow"):
    flow1()

@item
def flow2_runner(description="Run the second flow"):
    flow2()

@item
def flow3_runner(description="Run the third flow"):
    flow3()

def main():
    selected = item.select()
    item.endwin()

    selected_name, selected_func, selected_func_description = selected

    if selected_func == item._cancel:
        print("Cancel was selected. Exiting the program.")
    else:
        print(f"Running: {selected_name}\n")
        print(f"Description: {selected_func_description}\n")
        selected_func()

if __name__ == '__main__':
    main()

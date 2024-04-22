import os

'''
Objective : Return a list of indices (0-indexed) of buildings that have a river view, sorted in increasing order.
Required Input : A input text file with building size as comma seperated Example : [4,2,8,1]. Input has to be positive integer

Time complexity
> The time complexity of this function is O(n), where n is the number of buildings. This is because we iterate through each building once to check if it has a river view.
> The space complexity of this function is O(n), where n is the number of buildings. This is because we use a stack to store the buildings that have a river view, and the size of the stack can be at most n.

'''

infile_path = 'inputPS01.txt'
outfile_path = 'outputPS01.txt'

# stack class to perform different stack operations
class Stack:
    ''''
    It holds the methods for validating stack operations.
    1) isEmpty > To check if the stack is empty
    2) Push > Insert the element into stack
    3) Pop > to remove the last inserted element from stack
    4) size > To get the total elements in the stack
    5) reverse > To reverse the elements in the stack
    6) display > To print the elements in the stack
    7) get > To get an element from the given index
    '''
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop")
    def size(self):
        return len(self.items)
    def reverse(self):
        return self.items.reverse()
    def display(self):
        return self.items
    def get(self,index_to_get):
        return self.items[index_to_get]
 
#function to obtain the position of the buildings from which the river can be viewed
def river(stack):
    '''
    Performs following operation 
    1) Get the stack variable as input
    2) Loops through the stack to identify which has a river view
    3) Performs a validation to ignore if the building element value is zero hight
    4) Reverse the stack to provide the output in the requested format
    '''
    stack_size = stack.size()
    bldng_pos = Stack()
    #we are setting this as zero so that the first building near the river will always
    #have the river view irrespective of height
    get_element_at_stack = stack.get(int(stack_size-1))
    if get_element_at_stack != float(0):
        bldng_pos.push(stack_size-1)
    if not stack.isEmpty():
        a = stack.pop()
        b = 0
        for i in range(1,stack_size):
            if not stack.isEmpty(): #remove
                b = stack.pop()
            if a > b:
                a = a
            elif a == b: ## if there is same size of builds then the builds left to the river facing building will not have access
                a = a
            else:
                a=b
                bldng_pos.push(stack.size())
    bldng_pos.reverse()
    return bldng_pos


 
# function to create stack from the input file 
def create_stack_from_set(data_set): 
    '''
    Used for creating a Stack from the list of inputs
    '''
    stack = Stack()
    for num in data_set:
        stack.push(num)
    return stack


#This is to check whether the input file is placed in right location or not
check_if_input_file_exists = os.path.isfile(infile_path)

if check_if_input_file_exists:
    '''
    This part of the code is reponsible to perform
    1) Open input file from the location defined in variable `infile_path`
    2) Loops through  each line and performs below operation
        2.1) Removes the symbols [] and split the given input by comma seperated
        2.2) Takes the elements if it is greater than or equal to zero. 
        2.3) We consider zero as input to retain its element index
        2.4) Uses, `create_stack_from_set` function to initialize the stack
        2.5) Uses , `river` function to perform core operation
    3) Writes the output into the file located in `outfile_path' path
        3.1) If the input is invalid, it writes back to the output file with appropriate msg.
        3.2) If all the input is zero, it writes a message that none of building height is > 0
    '''
    #opening and reading the elements of the file to create stack and inserting the result to a new file
    with open(infile_path, 'r') as file:
        if os.path.getsize(infile_path) == 0:
            print(f"The file '{infile_path}' is empty.")
        else:
            with open(outfile_path, 'a+') as output_file:
                for line in file:
                    try:
                        numbers = [float(num) for num in line.strip('[] \n').split(',') if float(num) >= 0] #Remove square brackets and split the line into a list of numbers
                        stack_for_set = create_stack_from_set(numbers) #calling the stack create to create stack from the read elements
                        result = river(stack_for_set) # calling the river function to obtain the positions of the buildings
                        if result.isEmpty():
                            output_file.write(str("[ None of the building's height is > 0 ]\n"))
                        else:
                            output_file.write(str(result.display()) + '\n') # writing the results to an output file
                        # print(result.display())
                    except ValueError as invalidInput:
                        output_file.write(f'[ Invalid Input {str(line).strip()} ]\n') # exception handling to capture errors for wrong input
else:
    print("Input file is not found, kindly update the variable at the top with file location or a place a file named inputPS01.txt with inputs ")

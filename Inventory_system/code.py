import re

class manageNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self.insert_rec(self.root, key)
    
    def insert_rec(self, root, key):
        if root is None:
            return manageNode(key)
        if key < root.key:
            root.left = self.insert_rec(root.left, key)
        elif key > root.key:
            root.right = self.insert_rec(root.right, key)
        return root
    
    def sum_of_range(self, root, low, high):
        if root is None:
            return 0
        sum_range = 0
        if root.key >= low and root.key <= high:
            sum_range += root.key
        if root.key > low:
            sum_range += self.sum_of_range(root.left, low, high)
        if root.key < high:
            sum_range += self.sum_of_range(root.right, low, high)
        
        return sum_range

def process_file(file_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        # Extract numbers within square brackets using regular expressions
                        tree_elements = re.findall(r'\[(.*?)\]', line)
                        # Convert the extracted string of numbers to a list of integers, skipping 'null' values
                        numbers = []
                        for bracket_content in tree_elements:
                            for num_str in bracket_content.split(','):
                                num_str = num_str.strip()
                                if num_str != 'null' and num_str != 'None':
                                    if float(num_str) >= 0:
                                        numbers.append(float(num_str))
                                    else:
                                        raise ValueError("Invalid number format")
                        # Extract low and high values
                        low_matches = re.findall(r'low\s*=\s*(-?\d+(?:\.\d+)?)', line)
                        low = float(low_matches[0]) if low_matches else None
                        high_matches = re.findall(r'high\s*=\s*(-?\d+(?:\.\d+)?)', line)
                        high = float(high_matches[0]) if high_matches else None

                        # Check for negative low or high values
                        if low is not None and low < 0:
                            #output_file.write('Invalid Minimum quantity threshold\n')
                            output_file.write('Invalid Input\n')
                            continue
                        if high is not None and high < 0:
                            #output_file.write('Invalid Maximum quantity threshold\n')
                            output_file.write('Invalid Input\n')
                            continue

                        # Construct BST and compute sum of range
                        bst = BST()
                        for num in numbers:
                            bst.insert(num)
                        sum_range = bst.sum_of_range(bst.root, low, high)
                        output_file.write(f'Output: {sum_range}\n')

                    except ValueError as e:
                        output_file.write('Invalid Input\n')
        except FileNotFoundError:
            output_file.write('Input file not found\n')

# Example usage:
file_path = 'inputPS01.txt'  # Provide the path to your input file
output_file_path = 'outputPS01.txt'  # Provide the path to your output file
process_file(file_path, output_file_path)

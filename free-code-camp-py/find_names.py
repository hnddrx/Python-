"""
Create an array of strings to store the first names of 10 people. 
Write a program to find the 1st, 5th and 10th person's name
"""

def _find_names(array):
    if len(array) < 10:
        raise ValueError("The array must contain at least 10 names.")

    print("Full list of names:", array)

    # Get the 1st (index 0), 5th (index 4), and 10th (index 9) names
    indices = {0, 4, 9}
    found_names = [array[i] for i in indices]

    return found_names

# Example with exactly 10 names
names = ['John', 'Joe', 'Alex', 'Alezandro', 'Wren', 'Justin', 'Nicole', 'Kraven', 'Nine', 'Eleven']
print(_find_names(names))  
# Output: ['John', 'Wren', 'Eleven']

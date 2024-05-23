import sys
from tkinter import *

def calculate(value1, *values):
  """
  Calculates the product of (1 + value) for all provided values.

  Args:
      value1: The first value.
      *values: An arbitrary number of values.

  Returns:
      The product of (1 + value) for all provided values.
  """
  value1 = value1.rstrip("%")
  value1 = value1.replace(",", ".")
  product = 1 + float(value1)/100
  for value in values:
    value = value.replace(",", ".")  
    value = value.rstrip("%")
    product *= (1 + float(value)/100)
  return product

def button_click():
  """
  Gets the input text from the Text widget and calls the calculate function.
  """
  # Get the input text
  input_text = text_box.get("1.0", END)  # Get all text from the widget

  # Split the text by newlines (assuming values are on separate lines)
  values = input_text.splitlines()

  # Check if any value was provided
  if not values:
    print("Error: Please enter at least one value.")
    return

  # Use the first value and remaining values as separate arguments
  result = calculate(values[0], *values[1:])

  # Display the result (you can modify this to show it in the GUI)
  result_round = round(((result)-1)*100,2)
  result_label.config(text=f"Result: {result_round}%")


# Create the main window
root = Tk()
root.title("Value Calculator")

# Create a Text widget for multi-line input
text_box = Text(root, height=5, width=50)  # Adjust height and width
text_box.pack(padx=10, pady=10)

result_label = Label(root, text="")  # Initially empty label
result_label.pack(pady=10)

# Create the button
button = Button(root, text="Calculate", command=button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()
















import sys
from tkinter import *

def calculate(value1, *values):
  """
  Calculates the product of (1 + value) for all provided values, handling percentages and comma separators.

  Args:
      value1: The first value (can be a percentage with comma separator).
      *values: An arbitrary number of values (can be percentages with comma separators).

  Returns:
      The product of (1 + value) for all provided values, removing percentages and converting commas to dots.
  """
  product = 1
  for value in values:
    # Remove the percentage sign (%) if present
    value = value.rstrip("%")
    # Replace comma with dot (assuming comma is used as decimal separator)
    value = value.replace(",", ".")
    product *= (1 + float(value) / 100)
  return product

def button_click():
  """
  Gets the input text from the Text widget, removes percentages, handles commas, calculates the result, and displays it on the label.
  """
  # Get the input text
  input_text = text_box.get("1.0", END)  # Get all text from the widget

  # Split the text by newlines (assuming values are on separate lines)
  values = input_text.splitlines()

  # Check if any value was provided
  if not values:
    print("Error: Please enter at least one value.")
    return

  # Remove percentages and replace commas with dots in each value
  values = [value.rstrip("%").replace(",", ".") for value in values]

  # Use the first value and remaining values as separate arguments
  result = calculate(values[0], *values[1:])

  # Display the result as a percentage with two decimal places on the label
  result_label.config(text=f"Result: {round(((result - 1) * 100), 2)}%")

# Create the main window
root = Tk()
root.title("Value Calculator (Percentage)")

# Create a Text widget for multi-line input
text_box = Text(root, height=5, width=50)  # Adjust height and width
text_box.pack(padx=10, pady=10)

# Create a label to display the result
result_label = Label(root, text="")  # Initially empty label
result_label.pack(pady=10)

# Create the button
button = Button(root, text="Calculate", command=button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()

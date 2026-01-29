def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)
  
def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
# display_color_failure()
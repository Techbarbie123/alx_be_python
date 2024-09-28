
from datetime import datetime, timedelta
def display_current_datetime():
    """
    Function to display the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """
    Function to calculate the date after a user-specified number of days.
    """
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate future date
        
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future Date (after {days_to_add} days): {formatted_future_date}")
    
    except ValueError:
        print("Please enter a valid integer for the number of days.")
if __name__ == "__main__":
    display_current_datetime()  # Display the current date and time
    calculate_future_date()     # Prompt user to calculate a future date

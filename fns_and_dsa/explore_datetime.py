 from datetime import datetime, timedelta
def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format and print as "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date():
    # Prompt user for number of days
    days = int(input("Enter number of days to add: "))
    # Calculate future date
    future_date = datetime.now() + timedelta(days=days)
    # Print in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

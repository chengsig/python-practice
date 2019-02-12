
def return_day(num):
    """takes in a number from 1-7 and returns the respective day of the week"""
    
    day_pair = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    # if num < 1 or num > 7:
    #     return None
    # else: cl
    if num > 0 and num < 8:
        return day_pair[num]

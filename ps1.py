
def dream_home_calculator():

    #Amount of savings I currently have
    current_savings = 0

    #User input to ask user for starting annual salary
    annual_salary = float(input("Enter starting annual salary: "))

    #User input to ask user for each portion to be saved from salary
    portion_saved = float(input("What percentage of your salary do you plan to save? "))

    #User input to ask user what is the total cost of dream home
    total_cost = float(input("What is the total cost of your dream home? "))

    #Portion of the cost needed for down payment
    portion_down_payment = 0.25 * total_cost

    #total amount the user makes each month
    monthly_salary = annual_salary / 12

    #variable to hold the amount that the user saves from their salary each month
    monthly_savings = monthly_salary * portion_saved

    #Loop that doesn't stop until current savings is equal or greater than the cost of the down payment
    while portion_down_payment >= current_savings:
        
        investment = current_savings*0.04 / 12
        total_savings = monthly_savings + investment
        current_savings += total_savings
        
        total_months += 1

    print(f"Number of Months: {total_months}")


dream_home_calculator()
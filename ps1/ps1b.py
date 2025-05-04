
def dream_home_calculator():

    #Amount of savings I currently have
    current_savings = 0

    #User input to ask user for starting annual salary
    annual_salary = float(input("Enter your starting annual salary: "))

    #User input to ask user for each portion to be saved from salary
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

    #User input to ask user what is the total cost of dream home
    total_cost = float(input("Enter the cost of your dream home: "))

    #User input to ask user what is the amount of semi-annual raise
    semi_annual_raise = float(input("Enter the semi-­annual raise, as a decimal: "))

    #Portion of the cost needed for down payment
    portion_down_payment = 0.25 * total_cost

    #total amount the user makes each month
    monthly_salary = annual_salary / 12

    #variable to hold the amount that the user saves from their salary each month
    monthly_savings = monthly_salary * portion_saved
    
    #variable to tradck months
    total_months = 0
    
    #variable to track months for raise
    months_for_raise = 0
    
    #variable to track how much promotion amount
    salary_promotion_amount = 0

    #Loop that doesn't stop until current savings is equal or greater than the cost of the down payment
    while portion_down_payment >= current_savings:
        
        investment = current_savings*0.04 / 12
        total_savings = monthly_savings + investment
        current_savings += total_savings
        
        total_months += 1

        months_for_raise += 1

        #loop that checks to see if 6 months has passed to add a raise to user's salary.
        #If true then the counter to check for 6 months is reset back to 0. Then
        #the salary promotion amount is calculated by multiplying the annual salary by the semi
        #annual raise amount. The promotion amount is then added to the annual salary, and then
        #a new monthly salary can be calculated. Once a new monthly salary is calculated, we can now find a new
        #monthly savings amount. 
        if months_for_raise == 6:
            months_for_raise = 0
            salary_promotion_amount = annual_salary * semi_annual_raise
            annual_salary += salary_promotion_amount
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary * portion_saved

    print(f"Number of Months: {total_months}")


dream_home_calculator()

def dream_home_calculator():

    #Amount of savings I currently have
    current_savings = 0

    #User input to ask user for starting annual salary
    starting_salary = float(input("Enter your starting annual salary: "))

    annual_salary = starting_salary

    #Semi annual raise is automatically set to .07 in this scenario
    semi_annual_raise = 0.07

    #total amount the user makes each month
    monthly_salary = annual_salary / 12

    #variable to track months
    total_months = 0
    
    #variable to track months for raise
    months_for_raise = 0
    
    #variable to track how much promotion amount
    salary_promotion_amount = 0
    
    total_savings = 0

#Counter to track number of steps it takes for bisection search to work
    counter = 0
    
    low = 0
    high = 10000
    guess = (high + low) / 2
    bisectional_savings_rate = guess / 10000

    #variable to hold the amount that the user saves from their salary each month
    monthly_savings = monthly_salary * bisectional_savings_rate
    
    #while loop to repeatedly simulate 36 months of saving with different savings rates 
    #using bisection search. The loop resets necessary variables each time 
    #until total savings are within $100 of the down payment.
    while not (249900 <= total_savings <= 250100):
        current_savings = 0
        max_savings = 0
        total_savings = 0
        total_months = 0
        months_for_raise = 0
        annual_salary = starting_salary
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * bisectional_savings_rate

        #while loop to ensure that we run each simulation a total of 36 months
        while total_months < 36:
            investment = current_savings*0.04 / 12
            current_savings += investment + monthly_savings
            
            total_months += 1

            months_for_raise += 1       
        
            if months_for_raise == 6:
            #find the amount you make from a 36 month period
                months_for_raise = 0
                salary_promotion_amount = annual_salary * semi_annual_raise
                annual_salary += salary_promotion_amount
                monthly_salary = annual_salary / 12
                monthly_savings = monthly_salary * bisectional_savings_rate
            
        total_savings = current_savings

        #If statement to check if the 100% of the given salary 
        # can even be saved for the down payment in 3 years
        if bisectional_savings_rate == 1 and max_savings < 249900:
            print("It is not possible to pay the down payment in 3 years")
            return
        #elif statement to adjust the low bound because current savings are too low, 
        # meaning we need a higher savings rate.
        elif total_savings < 249900:
            counter += 1
            monthly_salary = annual_salary / 12
            low = guess
            guess = (high + low) / 2
            bisectional_savings_rate = guess / 10000
            monthly_savings = monthly_salary * bisectional_savings_rate
        #elif statement to adjust the high bound because current savings are too high, 
        # meaning we need a lower savings rate.
        elif total_savings > 250100:
            counter += 1
            monthly_salary = annual_salary / 12
            high = guess
            guess = (high + low) / 2
            bisectional_savings_rate = guess / 10000
            monthly_savings = monthly_salary * bisectional_savings_rate

    #if the total savings falls in between 100 dollars lower or greater than the desired down payment
    #then the best savings rate is printed as well as the steps it took for bisection search to work
    if 249900 < total_savings < 250100:
        print(f"Best savings rate: {bisectional_savings_rate:.4f}")
        print(f"Steps in bisection search: {counter}")



dream_home_calculator()
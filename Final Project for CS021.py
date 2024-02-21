
'''
William Oates, Gavin Cotter
Net Id's: woates,gcotter
CS021-D
Desc: A budgeting program that allows a user to create and modify a budget with in a text documant
'''
def main():
    BUDGET = {}  # define dictionary for budget
    try:
        BUDGET = read_budget(BUDGET)  # call read_budget function in order to make a dictionary of current budget text file
    except FileNotFoundError:
        write_budget_file(BUDGET)  # If there is no file call the write function to create a file in the correct directory
    display_title()  # call display title function
    users_choice = 0  # define users choice for while loop validation
    while users_choice != 6:  # while loop validation only ends if user selects exit program
        users_choice = user_input()  #call user_input function and set users_choice to the return value
        if users_choice == 1:
            view_budget(BUDGET)
        elif users_choice == 2:
            add_expense(BUDGET)
        elif users_choice == 3:
            add_income_source(BUDGET)
        elif users_choice == 4:
            remove_expense(BUDGET)
        elif users_choice == 5:
            remove_income_source(BUDGET)
        elif users_choice == 6:
            exit_program(BUDGET)
       
    
def display_title():
    '''
    display_title displays program title
    '''
    print('-'*20)
    print('Budget Calculator Program')
    print('-'*20)
    
def user_input():
    '''
    user_input asks user which task tehy want to use the budget calculator for
    '''
    print('Please Select an option from below: (1,2,3, etc..)')
    print('1. View Budget')
    print('2. Add Expense')
    print('3. Add Income Source')
    print('4. Remove Expense')
    print('5. Remove Income Source')
    print('6. Exit Program')
    try:
        result = 0
        while result > 6 or result <= 0:
            result = int(input('>>>'))
            return_validation = True  # define return validation
            if result > 6 or result < 0:
                print('Invalid option please enter an integer within the inclusive range 1-6\n')
    except ValueError:
        print('Invalid option please enter an integer within the inclusive range 1-6\n')
        return_validation = False  # if non valid value is gived set return_validation to false
    if return_validation == True:
        return result  #return users choice if return_validation is true


        
    

def view_budget(BUDGET):
    '''
    view_budget taket the BUDGET dictionary as its only parameter and displays the dictionarys contents for the user
    '''
    count = 0
    print('')
    print('Your Budget:')
    print('\nExpenses:')
    for key in BUDGET:  # print each key classified as an expense key
        key_list = key.split(':')
        if key_list[0] == 'expense':
            print(key_list[1],  end='    ')
            print(f'${BUDGET[key]:,.2f}')
    print('')
    print('Income Sources:')
    for key in BUDGET:  # print each key classified as an income source
        key_list_2 = key.split(':')
        if key_list_2[0] == 'income':
            print(key_list_2[1], end='    ')
            print(f'${BUDGET[key]:,.2f}')
    print('\nYour total weekly income flow is:')
    print(f'{income_flow(BUDGET)} dollars per week')
    print('')
    
def add_expense(BUDGET):
    '''
    Define an add_expense function that takes the BUDGET dictionart as a parameter and  adds a new expense key into the BUDGET dictionary 
    '''
    print('What expense would you like to add? (Enter expense name)')  # Retrieve expense key
    expense = 'expense:'  # define expense for while loop validation
    while expense == 'expense:':
        expense = 'expense:' + str(input('>>>'))
        if expense == 'expense:':
            print('Please input a valid name for the expense')
    print('What is the value of the expense?(dollars per week)')  # Retrieve value for expense key
    expense_validation = False  # define expense_validation variable that detects if an exception is raised or not
    while expense_validation == False:
        try:
            expense_value = float(input('>>> '))
            expense_validation = True  # change expense_validation to True after user input
        except ValueError:
            print('Please enter a float value for expense value')
            expense_validation = False  # if exception is raised keep expense_validation False
    BUDGET[expense] = expense_value  # update dictionary with new expense

def add_income_source(BUDGET):
    '''
    Define an add_income_source function that takes the BUDGET dictionary and adds a new income source key into the dictionary
    '''
    print('What income source would you like to add? (Enter income name)')
    income_source = 'income:'  # define income_source for while loop validation
    while income_source == 'income:':
        income_source = 'income:' + str(input('>>>'))
        if income_source == 'income:':
            print('Please input a valid name for the income source')
    print('What is the value of the income source?(dollars per week)')
    income_validation = False  # define income_validation variable that detects if an exception is raised or not
    while income_validation == False:
        try:
            income_source_value = float(input('>>> '))
            income_validation = True  # change expense_validation to True after user input
        except ValueError:
            print('Please enter a float value for income source value')
            income_validation = False  # if exception is raised keep expense_validation False
    BUDGET[income_source] = income_source_value  # update dictionary with new expense
    

def remove_expense(BUDGET):
    '''
    remove_expense takes the BUDGET dictionary as a parameter and removes an expense key in the dictionary
    '''
    print('')
    print('What expense would you like to remove?')
    removed_expense = str(input('>>>'))
    for key in BUDGET:  # loop that identifies if the expense to be removed is in the BUDGET dictionary
        key_list = key.split(':')
        if key_list[0] == 'expense':
            if key_list[1] == removed_expense:
                key_to_remove = key
    try:
        del BUDGET[key_to_remove]
    except UnboundLocalError:
        print(f'That expense is not a valid expense to remove')
        

def remove_income_source(BUDGET):
    '''
    remove_income_source takes BUDGET as its only parameter and will remove an income source that the user wants to remove
    '''
    print('')
    print('What income source would you like to remove?')
    removed_income_source = str(input('>>>'))
    for key in BUDGET:  # loop that identifies if the income source to be removed is in the BUDGET dictionary
        key_list = key.split(':')
        if key_list[0] == 'income':
            if key_list[1] == removed_income_source:
                key_to_remove = key
    try:
        del BUDGET[key_to_remove]
    except UnboundLocalError:
        print(f'That income source is not a valid income source to remove')
        

def income_flow(BUDGET):
    '''
    income_flow is calulated by adding the total expenses and income sources from the budget dictionary
    '''
    total_income_sources = 0  #Define the total value for income sources
    for key in BUDGET:  #Expense print for loop
        key_list = key.split(':')
        if key_list[0] == 'income':
            total_income_sources += BUDGET[key]
    total_expenses = 0  #Define the total value for income sources
    for key in BUDGET:  #Expense print for loop
        key_list = key.split(':')
        if key_list[0] == 'expense':
            total_expenses += BUDGET[key]
    return total_income_sources - total_expenses

def read_budget(BUDGET):
    '''
    read_budget adds cureent contents of text file into a dictionary and returns that dictionary
    '''
    budget_file = open('budget_calculator.txt', 'r')
    expense_validation = True  # define variable that detects if a line is an expense key
    income_validation = False  # define variable that detects if a line is an income key
    for line in budget_file:  # define for loop that review each line of budget_file
        if line == 'Income Sources:\n':  # if the line is equivalent to 'Income Sources:' it is signified that the expense keys are done being listed and the income keys will be listed now
            expense_validation = False
            income_validation = True
        if expense_validation == True:  # if expense_validation is still true add keys to expense dictionary
            if line != 'Expenses:\n' and line != 'Income Sources:\n' and line != '\n':  # if statement that ensures only expense keys are being added into the dictionary
                line_list = line.split('-' * 10)  # split key from key value using ".split"
                BUDGET['expense:' + line_list[0][4::]] = float(line_list[1][:-1])  # Add key into BUDGET dictionary
        if income_validation == True:  # is income validation is True keys are assigned as income keys
            if line != 'Income Sources:\n' and line != '\n':
                line_list = line.split('-' * 10)
                try:
                    BUDGET['income:' + line_list[0][4:]] = float(line_list[1][:-1])  # add key to BUDGET dictionary
                except IndexError:
                    error = 0
    budget_file.close
    return BUDGET

def write_budget_file(BUDGET):
    '''
    write_budget_file writes all the contents of the budget into the textfile
    '''
    budget_file = open('budget_calculator.txt', 'w')  # open budget calculator text file in write mode
    budget_file.write('Expenses:' + '\n')  # label expense section fo text file
    for key in BUDGET:  # for each key in the BUDGET dictionary add to textfile only if it is an expense key
            key_name = key.split(':')
            if key_name[0] == 'expense':
                budget_file.write(f'    {key_name[1]}' + '-' * 10 + str(BUDGET[key]) + '\n')
    budget_file.write('\n' + 'Income Sources:' + '\n')  # label income section for text file
    for key in BUDGET:  # for each key in the BUDGET dictionary add it to the textfile only if it is an income key
            key_name = key.split(':')
            if key_name[0] == 'income':
                budget_file.write(f'    {key_name[1]}' + '-' * 10 + str(BUDGET[key]) + '\n')
    budget_file.write('\n' + f'Your total weekly income flow is {income_flow(BUDGET)} dollars per week')  # after all expenses and incomes are written into the file add the total income flow
    budget_file.close
        


def exit_program(BUDGET):
    '''
    exit_program take BUDGET as the only parameter and ends program by writing BUDGET dictionary into a text file if the user decides to close the program
    '''
    answer = 'u'     # define answer for while loop validation
    while answer != 'y' and answer != 'n':
        answer = str(input('Are you sure you want to exit? (y/n):'))
        if answer == 'y':
            write_budget_file(BUDGET)  # once user is done with program write the BUDGET dictionary into the budget_calculator file
            print('Thank you for using Our Budget Program')
        elif answer == 'n':
            main()  # if user doesn't want to end program run user_input again
if __name__ == '__main__':
    main()

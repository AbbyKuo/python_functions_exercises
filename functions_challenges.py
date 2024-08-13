#############################################################################################################
# Challenge 1 -> A Function to get a float from the user

def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are 
            prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    converted_input = float(input(prompt_string))

    return converted_input





#############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments: 
        - distance_in_miles: A float representing a distance in miles
    
    Returns
        - a float representing the distance in kilometers
    """
    
    converted_km = distance_in_miles * 1.60934
    return converted_km

#############################################################################################################
# Challenge 3 -> A function to calculate the total distance run in a relay

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.
    
    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team
    
    Returns:
        - A float representing the total distance run.
    """
    
    total_distance = distance_per_runner * number_of_runners
    return total_distance

#############################################################################################################
# Challenge 4 (extra tricky, no tests for this one!)
# 
# See if you can write a single function that USES all three of the functions 
# you wrote for the above challenges.
#
# It should:
# - prompt the user for the distance each runner in the relay race will run (in miles)
# - prompt the user for the number of runners in a team
# - print the total distance run by the team, in kilometers!
# 
# No need for this function to accept any arguments or return any values.

def cal():

    # step 1: prompt the user for the distance each runner in the relay race will run (in miles)
    distance_in_miles = get_float("What is the distance in miles?: ")

    # step 2:prompt the user for the number of runners in a team
    no_of_runners = get_float("How many runners in a team?: ")

    # step 3: convert miles to kms
    distance_in_kms = miles_to_km(distance_in_miles)

    # step 4: calculate relay distance  
    total_team_distance =  relay_distance(no_of_runners, distance_in_kms)

    # step 5: print total distance run by the team, in kilometers!
    print(f"The total distance run by the team: ${total_team_distance}kms")


cal()
    

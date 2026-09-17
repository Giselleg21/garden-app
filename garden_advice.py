# User input values for the season and plant type
season = input("Please enter the current season: ")
plant_type = input("Please enter the type of plant you are growing: ")


# Determine advice based on the season
def advice_based_on_season(season):
    '''This code block uses the season provided by the user to
    determine what advice to return to the user.'''
    if season == "summer":
        season_advice = ("water your plants regularly and "
                         "provide some shade.\n")
        return f"\nDuring summer, it is best to {season_advice}"
    elif season == "winter":
        season_advice = "protect your plants from frost with covers.\n"
        return f"\nDuring winter, it is best to {season_advice}"
    else:
        season_advice = "\nNo advice for this season.\n"
        return season_advice


# Determine advice based on the plant type
def advice_based_on_plant_type(plant_type):
    '''This code block uses the plant type provided by the user to
    determine what advice to return to the user.'''
    if plant_type == "flower":
        plant_advice = "use fertiliser to encourage blooms."
        return f"For flowers, it is best to {plant_advice}\n"
    elif plant_type == "vegetable":
        plant_advice = "keep an eye out for pests!"
        return f"for vegetables, it is best to {plant_advice}\n"
    else:
        plant_advice = "No advice for this type of plant."
        return plant_advice


# Run the functions and print the results:
print(advice_based_on_season(season))
print(advice_based_on_plant_type(plant_type))

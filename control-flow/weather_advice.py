# Get user input for weather conditions
weather = input("What is the current weather? (sunny, rainy, cold): ")

# Provide clothing recommendations based on weather conditions
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
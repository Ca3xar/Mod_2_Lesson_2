attendees = int(input("Enter number of attendees:"))
venue = "large hall" if (attendees > 100) else ("conference room")
extras = input("do you want extras? yes or no")
additions = "projector" if (venue == "large hall") else ("audio system")
food = input("Vegetarian or Not")
catering = "Veggie Delight Caterers" if (food == "Vegetarian") else ("Gourmet Meals Caterers")

print(venue,catering,additions)
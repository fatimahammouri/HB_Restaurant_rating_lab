"""Restaurant rating lister."""
def Restaurant_scoring(file_name):
    opened_file = open(file_name)
    rating_dict = {}

    for line in opened_file:
        line = line.rstrip("\n")
        data = line.split(":")
        #print(data)
        rating_dict[data[0]] = data[1]
        # print(rating_dict)   

    user_restaurant_name = input("What is the restaurant name? > ")
    user_restaurant_score = input("What is the restaurant score? > ")

    while int(user_restaurant_score) > 5 or int(user_restaurant_score) < 1:
        user_restaurant_score = input("Score must be between 1 and 5. What is the restaurant score? > ")
        
    rating_dict[user_restaurant_name.title()] = user_restaurant_score
    
    restaurants = rating_dict.items()
    restaurants = sorted(restaurants)
    # print(restaurants)
    
    for ratings_set in restaurants: 
        print(f"{ratings_set[0]} is rated at {ratings_set[1]}.")
      
 

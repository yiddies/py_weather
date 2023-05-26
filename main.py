from functions import get_current_weather, get_location, get_future_weather, print_current_weather, print_future_weather

while True:
    print('What would you like to do? (Check weather with "Check <city>", Check future weather with "Check future <city>", exit with "Exit")')
    user_action = input("")
    user_action = user_action.strip().lower()
    
    if user_action.startswith('check'):
        if 'future' in user_action:
            command, city = user_action.split('future', 1)
            forecast_days = 7
        else:
            command, city = user_action.split(' ', 1)
            forecast_days = 1

        location = get_location(city)
        if location is None:
            continue

        if forecast_days == 1:
            data = get_current_weather(location)
            print_current_weather(location, data)
        else:
            data = get_future_weather(location, forecast_days)
            print_future_weather(location, data, forecast_days)

    elif user_action.startswith('exit'):
        break
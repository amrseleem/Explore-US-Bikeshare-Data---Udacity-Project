import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city= input("Which city would you like to explore? chicago, new york city, washington?").lower()
        if city not in ("chicago", "new york city", "washington"):
            print("Sorry, not found. Please insert a valid input!")
            continue
        else:
            break
                                     
    # TO DO: get user input for month (all, january, february, ... , june)
  
    while True:
        month= input ("Which month would you like to filter? january, february, march, april, may, june, or 'all'?").lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry, not found. Please insert a valid input!")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input ("Are you looking for a particular day?, if so, please type which one: monday,....,saturday, sunday, or 'all'").lower()
        if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"): 
            print("Sorry, not found. Please insert a valid input!")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # first of all we should load the data
    df = pd.read_csv(CITY_DATA[city])

    # at this stage,if we looked at the data, we find the data frame is not ready. The month and weekdays are in the start time, so we need to get it out and filter. 
    # then, we should establish the new data frame and filter it by month and day 

    #we should extract the month and weekdays from start time but first change the starttime to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["weekday"] = df["Start Time"].dt.weekday_name
    # so far we craeted the columns, and now we are filtering by month and day
    if month != 'all':
        month_list = ["january", "february", "march", "april", "may", "june"]  
        month = month_list.index(month) + 1
        df = df[df["month"] == month]
    #so far, we have created the month list and filtered for momths, it is now time for filtering days              
    if day != 'all':
        df = df[df["weekday"] == day.title()]        
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month is:", most_common_month)
                    
    # TO DO: display the most common day of week
    most_common_day = df["weekday"].mode()[0]
    print("The most common day of week is:", most_common_day)                
                  

    # TO DO: display the most common start hour
    df["hour"]= df["Start Time"].dt.hour
    most_common_hour = df["hour"].mode()[0]
    print("The most common hour of day is:", most_common_hour)               
                   
                   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is:", start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].value_counts().idxmax()
    print("The most commonly used end station is:", end_station)               

    # TO DO: display most frequent combination of start station and end station trip
    
    df["combination_station"] = df["Start Station"] + " "+df["End Station"]
    print("The most frequent combination of start station and end station trip is:", df["combination_station"].mode()[0])
                    
                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types =df["User Type"].value_counts()
    print("The numer of user types are:", user_types)

    # TO DO: Display counts of gender
                   
    if "Gender" in df.columns:
        gender_counts =  df["Gender"].value_counts()
        print("The number of gender is:", gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:    
        earliest_year = df["Birth Year"].min() 
        print("The earliest yeare is:", earliest_year)
    
        most_recent_year = df["Birth Year"].max()
        print("The most recent year is:", most_recent_year)
    
        most_common_yearofbirth = df["Birth Year"].value_counts().idxmax()
        print("The most common year of birth is:", most_common_yearofbirth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #To display the raw data, I have done it with the help of: https://stackoverflow.com/questions/37512079/python-pandas-why-does-df-iloc-1-values-for-my-training-data-select-till
def display_raw_data(df):
    """
    Displays the raw data, after asking the user if wishes to see some raw data. 
    Then, we show the user 10 rows.
    """    
    raw_data = input("Do you want to display some raw data? Please yes or no?").lower()
    x=1 
    while True:
        if raw_data == "yes":
           print(df.iloc[x : x+10])
           x += 10
           raw_data = input("Do you want to see more raw data? yes or no?").lower()
        
        else:
           break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs (would like to see data for Chiacago, New York, Washington? if so. enter city name)
    city = input("Would like to see data for Chicago, New York City, Washington? \nif yes, enter city name: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Invalid Input!")
        city = input("Entre city name: ").lower()
    print ("The city is {}.".format(city))
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("which month? January, February, March, April, May, June or all? ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Invalid Input!")
        month = input("Entre month name or all: ").lower()
    print ("The month is {}.".format(month))
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day? sunday, monday, tuesday, wednesday, thursday, friday, saturday or all? ").lower()
    while day not in ['sunday', 'monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday','all']:
        print("Invalid Input!")
        day = input("Entre day name or all: ").lower()
    print ("The day is {}.".format(day))
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
# load data file into a dataframe
    #filename = 'chicago.csv'
    #df = pd.read_csv(filename)
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]
    return df
    #return df.head()
     
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]

    print('Most Popular Start day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']  + " to " + df['End Station']
    popular_trip = df['trip'].mode()[0]

    print('Most popular_trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()

    print('total_travel_time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('mean_travel_time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('gender:', gender)
    else:
        print(" Gender Information is not available in this city")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('earliest_birth_year:', earliest_birth_year)
    else:
        print(" Birth Information is not available in this city")
    if 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].max()
        print('most_recent_birth_year:', most_recent_birth_year)
    else:
        print(" Birth Information is not available in this city")
    if 'Birth Year' in df.columns:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('most_common_birth_year:', most_common_birth_year)
    else:
        print(" Birth Information is not available in this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    print('\nDisplaying 5 random rows of the data upon request...\n')
    df = pd.read_csv(CITY_DATA[city])
    start_time = time.time()
    display = input("Would like to see random data for your city? \n Enter yes or no: ").lower()
    while display.lower() == 'yes':
        print(df.sample(axis=0, n=5))
        display = input("Would like to see more random data for your city? Enter yes or no: ").lower()
    print ("Ending randon data display") 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
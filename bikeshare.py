import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ["chicago","new york city", "washington"]
    while True:
        city = str(input('Would you like to see data for chicago, new york city, or washington? Enter city name: \n'))
        if city.lower() not in city_list:
            print('Please, enter a valid city name')
            continue
        else:
            print('You will see data for {}'.format(city))
            break

def get_month():
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = str(input('Would you like to filter the data by month? Enter: january, february, march, april, may, june for the month you want to filter by or all for not filter.\n'))
        if month.lower() not in month_list:
            print('Enter a valid month name')
            continue
        else:
            print('You will filter data by {}'.format(month))
            break

def get_day():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = str(input('Would you like to filter the data by day of the week? Choose: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all if apply to all ?\n'))
        if day.lower() not in day_list:
            print('Enter a valid day of the week name')
            continue
        else:
            print('You will filter data by {}'.format(day))
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and the End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #TO DO: extract hour from Start Time to create new columns
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
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}: '.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}: '.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is {}: '.format(most_common_hour))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {}: '.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is {}: '.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = 'from' + df['Start Station'] + 'to' + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print('The most common trip is {}: '.format(most_common_trip))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {}: '.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is {}: '.format(mean_travel_time))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The number of user type is {}: '.format(user_types))

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Number of Gender is {}: '.format(gender_count))
    except KeyError:
        print('Number of Gender is not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is {}: '.format(earliest_birth_year))
    except KeyError:
        print('Earliest Year of Birth  is not available.')

    try:
        recent_birth_year = df['Birth Year'].max()
        print('The recent year of birth is {}: '.format(recent_birth_year))
    except KeyError:
        print('Recent Year of Birth is not available.')

    try:
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}: '.format(common_birth_year))
    except KeyError:
        print('Most Common Year of Birth is not available.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    count = 0
    while True:
        answer = str(input('Would you like to see 5 lines of raw data? Enter yes or no: '))
        # Check if response is yes, print the raw data and increment count by 5
        if answer.lower() == 'yes':
            print(df.iloc[count: count + 5])
            count += 5
        # otherwise break
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #city = get_city()
        #month = get_month()
        #day = get_day()
        #df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

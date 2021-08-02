import pandas as pd
from collections import Counter

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    
    ## How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()
    
    ## What is the average age of men?
    average_age_men = round(
        df.age[df.sex == 'Male'].mean(),1
    )
    
    ## What is the percentage of people who have a Bachelor's degree?
    # constructs a dictionary of each type of education listed and ists number of occurances
    X = Counter(df['education'])
    
    percentage_bachelors = round(
        X['Bachelors']/sum(X.values())*100,1
    )
    
    ## What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    ## What percentage of people without advanced education make more than 50K?
    # advanced education
    A = df[
        (df['education'] == 'Bachelors') | 
        (df['education'] == 'Masters')   | 
        (df['education'] == 'Doctorate')
    ]
    # no advanced education
    B = df[
        (df['education'] != 'Bachelors') & 
        (df['education'] != 'Masters')   & 
        (df['education'] != 'Doctorate')
    ]
    
    higher_education_rich = round(
        len(A[A['salary'] == '>50K'])/len(A)*100,1
    )
    lower_education_rich = round(
        len(B[B['salary'] == '>50K'])/len(B)*100,1
        )
    
    ## What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    ## What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    X = df[df['hours-per-week'] == min_work_hours].salary.value_counts()
    
    rich_percentage = (X[1]/X.sum())*100
    
    ## What country has the highest percentage of people that earn >50K?
    X = df[df['salary'] == '>50K']
    #counts per country where rich
    A = X['native-country'].value_counts()
    #Count per country
    B = df['native-country'].value_counts()
    
    highest_earning_country = (A/B).idxmax()
    highest_earning_country_percentage = round(
        (A/B).max()*100,1
    )
    
    ## Identify the most popular occupation for those who earn >50K in India.
        #rich indians
    X= df[
        (df['native-country'] == 'India') & 
        (df['salary'] == '>50K')
    ]
    
    top_IN_occupation = X.occupation.value_counts().idxmax()
    
    print("Number of each race:\n", race_count) 
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }




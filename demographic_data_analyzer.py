import pandas as pd
def data_preprocessing(data):
    # removing the duplicated values 
    # new_df = data[data.duplicated() != True]
    
    # fixing columns name ( replace '-' with '_')
    data.columns = [column.replace('-', '_') for column in data.columns]
    
    # returning the new data_frame
    return data

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = data_preprocessing(pd.read_csv('adult.data.csv'))
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex == 'Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    num_ppl_w_ba = df.query('education == "Bachelors"').shape[0]
    percentage_bachelors = round(num_ppl_w_ba/df.shape[0] *100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # with adv edu
    higher_education = df.query('education == "Bachelors" or education == "Masters" or education == "Doctorate"')
    num_adv_eppl_make_over_50k = higher_education.query('salary == ">50K"').shape[0]
    
    # without adv edu
    lower_education = df.query('education != "Bachelors" and education != "Masters" and education != "Doctorate"')
    num_none_adv_eppl_make_over_50k = lower_education.query('salary == ">50K"').shape[0]
    
    # percentage with salary >50K
    higher_education_rich = round((num_adv_eppl_make_over_50k / higher_education.shape[0]) *100, 1)
    lower_education_rich = round((num_none_adv_eppl_make_over_50k / lower_education.shape[0]) *100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.hours_per_week.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.query('hours_per_week == 1').shape[0]

    rich_percentage = round((df.query('hours_per_week == 1').query('salary == ">50K"').shape[0]/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df.query('salary == ">50K"').native_country.value_counts()/\
                               df.native_country.value_counts()).sort_values(ascending=False).index[0]
    
    highest_earning_country_percentage = round((df.query('salary == ">50K"').native_country.value_counts()/\
                                          df.native_country.value_counts()).sort_values(ascending=False)[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    ppl_in_india =df.query('native_country == "India"')
    top_earning_ppl_IN = ppl_in_india.query('salary == ">50K"')
    top_IN_occupation =top_earning_ppl_IN.occupation.value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race: \n", race_count, sep="") 
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

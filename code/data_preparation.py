import pandas as pd
import numpy as np



def clean_rt(rt_movie_info):
    """
    
    Takes in rt_movie_info and returns a cleaned dataframe.
    
    """
    rt_movie_info.dropna(subset = ['box_office'], inplace = True)
    
    for col in ['box_office']:
        rt_movie_info[col] = rt_movie_info[col].str.replace(r'\D', '')
        rt_movie_info[col] = rt_movie_info[col].astype('int64')
    
    return rt_movie_info



def top_10pct_rt_directors(rt_movie_info):
    """
    
    Takes in a cleaned rt_movie_info and returns a series of the top 10% grossing movie directors. 
    
    """
    top_10pct_directors = rt_movie_info.groupby(['director'])['box_office'].mean().sort_values(ascending = False).head(27)
    
    return top_10pct_directors




def create_kaggle_profit_column(kaggle_movies):
    """
    
    Takes kaggle_movies df and returns same df with added 'profit' column.
    
    """
    
    kaggle_movies['profit'] = kaggle_movies['gross'] - kaggle_movies['budget']
    
    return kaggle_movies



def kaggle_studio_vs_profit(dataframe):
    
    """
    
    Takes kaggle_movies df and groups 'company' column by 'profit' in descending order,
    returning the top 20 most profitable studios, on average.
    
    """

    kag_studio_vs_profit = dataframe.groupby(['company'])['profit'].mean().sort_values(ascending = False).head(20)
    
    return kag_studio_vs_profit



def clean_kaggle_ratings(dataframe):

    """
    
    Takes kaggle_movies df and returns cleaned 'rating' column.
    
    """

    dataframe['rating'] = dataframe['rating'].map(lambda x: 'NOT RATED' if x == 'Not specified' else x)
    dataframe['rating'] = dataframe['rating'].map(lambda x: 'R' if x == 'NC-17' else x)

    for rating in ['B15', 'TV-MA', 'TV-PG', 'TV-14', 'B']:
        dataframe.drop(dataframe[dataframe['rating'] == rating].index, inplace = True)

    return dataframe



def create_kaggle_ratings_dfs_for_subplots(dataframe):
    """
    
    Takes kaggle_movies and returns six dfs, one for each rating.
    
    """
    ratings_list = ['R', 'PG-13', 'PG', 'NOT RATED','G','UNRATED']
    dfs_list = []
    
    for rating in range(len(ratings_list)):
        df = dataframe[dataframe['rating'] == ratings_list[rating]]
        dfs_list.append(df)
    
    return dfs_list
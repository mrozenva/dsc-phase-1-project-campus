def plot_top_10pct_rt_directors(top_10pct_directors):
    """
    
    Takes in output of top_10pct_rt_directors and displays the series as a barplot.
    
    """
    plt.figure(figsize = (15,6))
    plt.title('Top 10% Average Grossing Movie Directors (Rotten Tomatoes)')
    directors_plot = sns.barplot(top_10pct_directors.index, top_10pct_directors.values)
    directors_plot.set_xticklabels(directors_plot.get_xticklabels(), rotation = 80);
    plt.xlabel('Movie Directors')
    plt.ylabel('Average Gross Return ($10M) (Box Office)')
    return plt.show()



def kaggle_studio_vs_profit_barplot(kaggle_studio_vs_profit):
    
    """
    
    Takes output of kaggle_studio_vs_profit and returns this output in the form of a barplot. 
    
    """

    plt.figure(figsize = (20,6))
    plt.title('Top 20 Most Profitable Movie Studios')
    studios_plot = sns.barplot(x = kaggle_studio_vs_profit.index,
                               y = kaggle_studio_vs_profit.values,
                               palette = 'Blues_r')
    studios_plot.set_xticklabels(studios_plot.get_xticklabels(), rotation = 70);
    plt.xlabel('Movie Studios')
    plt.ylabel('Average Profit ($10M)')
    return plt.show()



def rating_vs_num_movies_barplot(dataframe):
    """
    
    Takes kaggle_movies df and creates a barplot with 'rating' column on x axis
    and number of movies for each rating on y axis.
    
    """

    plt.title('MPAA Rating vs. Number of Movies')
    plt.xlabel('MPAA Rating')
    plt.ylabel('Number of Movies')
    rating_count_barplot = sns.barplot(dataframe['rating'].value_counts().index, 
                                       dataframe['rating'].value_counts().values, 
                                       palette = 'mako')
    return plt.show()
    
  
    
def rating_vs_average_profit_barplot(dataframe):

    """
    
    Takes kaggle_movies df and creates a barplot with rating on the x axis 
    and average profit in units of $10M on the y axis.
    
    """
    plt.title('MPAA Rating vs. Average Profit ($10M)')
    rating_vs_mean_profit_barplot = sns.barplot(dataframe['rating'], 
                                                dataframe['profit'],  
                                                palette = 'mako', 
                                                order = ['R', 'PG-13', 'PG', 'NOT RATED','G','UNRATED'])
    plt.xlabel('MPAA Rating')
    plt.ylabel('Average Profit ($10M)')
    return plt.show()


def genre_vs_profit_barplot(dataframe):
    plt.title('Movie Genre vs Profit')
    chart = sns.barplot('genre', 
                        'profit', 
                        data = dataframe)
    chart.set_xticklabels(chart.get_xticklabels(), rotation = 60)
    chart.set(xlabel='Movie Genre', ylabel='Profit ($10M)');
    return plt.show()



def ratings_subplots(dfs_list):
    """
    Hardcoded subplots for each of the six MPAA movie ratings.
    """

    
    
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(ncols=3, 
                                              nrows = 2,  
                                              figsize = (18,10))
    
    axes_tuple = ((ax1, ax2, ax3), (ax4, ax5, ax6))
    
    fig.suptitle('Profit vs. Runtime for each MPAA Rating')
#     for a in range(len(axes_tuple)):
#         for axes in range(len(axes_tuple[a])):
#             axes_tuple[a][axes].set_xlabel('Runtime (Minutes)')
#             axes_tuple[a][axes].set_ylabel('Profit ($10M)')
            
    fig.suptitle('Profit vs. Runtime for each MPAA Rating')

    sns.regplot(x=dfs_list[0]['runtime'], y=dfs_list[0]['profit'], ax=ax1, color = 'black')
    sns.regplot(x=dfs_list[1]['runtime'], y=dfs_list[1]['profit'], ax=ax2, color = 'darkslateblue')
    sns.regplot(x=dfs_list[2]['runtime'], y=dfs_list[2]['profit'], ax=ax3, color = 'steelblue')
    sns.regplot(x=dfs_list[3]['runtime'], y=dfs_list[3]['profit'], ax=ax4, color = 'teal')
    sns.regplot(x=dfs_list[4]['runtime'], y=dfs_list[4]['profit'], ax=ax5, color = 'c')
    sns.regplot(x=dfs_list[5]['runtime'], y=dfs_list[5]['profit'], ax=ax6, color = 'palegreen')

    for a in range(len(axes_tuple)):
        for axes in range(len(axes_tuple[a])):
            axes_tuple[a][axes].set_xlabel('Runtime (Minutes)')
            axes_tuple[a][axes].set_ylabel('Profit ($10M)')
    
    ax1.set_title('R')
    ax2.set_title('PG-13')
    ax3.set_title('PG')
    ax4.set_title('NOT RATED')
    ax5.set_title('G')
    ax6.set_title('UNRATED') 
    
    return plt.show()
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter


def fetch_stats(selected_user , df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    #extracting the number of messages
    num_messages = df.shape[0]
    words = []
    for messages in df['message']:
        words.extend(messages.split())


    #extracting the number of media files shared
    num_media = df[df['message']=='<Media omitted>\n'].shape[0]

    #extracting all the links using the library urlextract
    links = []
    extractor = URLExtract()
    for message in df['message']:
        links.extend(extractor.find_urls(message))


    return num_messages, len(words) , num_media , len(links)

def busiest_users(df):
    top_10_busiest = df['user'].value_counts().head(10)
    df = round((df['user'].value_counts() / df['user'].shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return top_10_busiest , df



def monthly_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap


def create_wordcloud(selected_user, df):
    f = open('stopWordsHinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    f = open('stopWordsHinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def sentiment_analysis(selected_user , df , ddf):
    z = open('stopWordsHinglish.txt', 'r')
    stop_words = z.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # sum and no_points for the overall sentiment score that will be calculated later
    sum = 0.00
    no_points = 0

    # arr will store the list of sentiment scores for each month and mon will store the name of that month
    arr = []
    mon = []

    # curr_month for checking for the change in the month , flag to initialize the value of month for the first time
    curr_month = ""
    flag = True

    # message_score and no_message_words are the monthly counterparts of sum and no_points
    message_score = 0.00
    no_message_words = 0

    # traversing through all the messages in the dataframe temp
    for date in temp['date']:

        message = temp.loc[temp['date'] == date, 'message'].values[0]
        # initializing curr_month for the first time
        if flag:
            curr_month = temp.loc[temp['date'] == date, 'month'].values[0]
            flag = False

        # traversing throught each word in the present message after converting it to lower case
        for word in message.lower().split():

            # checking if the word present in the list of stop_words from the data set
            if word not in stop_words:

                # checking if the word is present in the ddf dataframe to extract it's sentiment score
                if (ddf['word'].eq(word)).any():

                    # adding the score and incrementing the number of sentiment scores taken to average them out later below
                    message_score += float(ddf.loc[ddf['word'] == word, 'Spoints'].values[0])
                    no_message_words = no_message_words + 1

                    # counterparts for the overall sentiment score calculation
                    sum += float(ddf.loc[ddf['word'] == word, 'Spoints'].values[0])
                    no_points = no_points + 1

                else:
                    # if the sentiment score of the present word is not defined , then ,
                    # it is considered to be neutral word with 0.5 as sentiment score
                    sum += 0.50
                    message_score += 0.50
                    no_message_words = no_message_words + 1
                    no_points = no_points + 1

        # if the month changes  , we can append the sentiment score of the last month to the list ,
        # and , initialize the values back to zero
        if curr_month != temp.loc[temp['date'] == date, 'month'].values[0] and no_message_words != 0:
            mon.append(curr_month)
            arr.append(message_score / no_message_words)

            curr_month = temp.loc[temp['date'] == date, 'month'].values[0]
            message_score = 0.00
            no_message_words = 0

    # in the process we will miss the values for the last month , thus , checking and adding to the list
    if message_score != 0:
        mon.append(curr_month)
        arr.append(message_score / no_message_words)

    return sum/no_points , mon , arr


def top_scorers(df , ddf):
    z = open('stopWordsHinglish.txt', 'r')
    stop_words = z.read()

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    unique_user = []
    Senti_score = []
    for each_user in temp['user'].unique().tolist():
        prac = temp[temp['user'] == each_user]
        sum = 0.00
        no_points = 0

        for message in prac['message']:

            # traversing throught each word in the present message after converting it to lower case
            for word in message.lower().split():

                # checking if the word present in the list of stop_words from the data set
                if word not in stop_words:

                    # checking if the word is present in the ddf dataframe to extract it's sentiment score
                    if (ddf['word'].eq(word)).any():

                        # counterparts for the overall sentiment score calculation
                        sum += float(ddf.loc[ddf['word'] == word, 'Spoints'].values[0])
                        no_points = no_points + 1

                    else:
                        # if the sentiment score of the present word is not defined , then ,
                        # it is considered to be neutral word with 0.5 as sentiment score
                        sum += 0.50
                        no_points = no_points + 1
        unique_user.append(each_user)
        if no_points != 0:
            Senti_score.append(sum / no_points)
        else:
            Senti_score.append(0.50)

    new_df = pd.DataFrame({'user_name': unique_user, 'Senti_score': Senti_score})
    new_df = new_df.sort_values(by=['Senti_score'], ascending=False).head(5)

    return new_df['user_name'].tolist() , new_df['Senti_score'].tolist()

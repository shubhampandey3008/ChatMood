import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import re
import pandas as pd

g = open("sentiment_score.txt" , "r" , encoding = 'utf-8')

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    #preprocessing the dataframe with the sentiment scores
    data_set = g.read()
    ddf = preprocessor.preprocess_second(data_set)

    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")
    selected_user = st.sidebar.selectbox(" Do analysis with respect to : ", user_list)

    if st.sidebar.button("Show analysis"):

        num_messages , num_words , num_media , num_links = helper.fetch_stats(selected_user , df)

        col1 , col2 , col3 , col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total words")
            st.title(num_words)

        with col3:
            st.header("Total media")
            st.title(num_media)

        with col4:
            st.header("Total links")
            st.title(num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # finding the busiest users in the group
        if selected_user == 'overall' :
            st.title('Most Busy Users')
            x , new_df = helper.busiest_users(df)
            name = x.index
            count = x.values
            fig , ax = plt.subplots()

            col1 , col2 , col3= st.columns(3)

            with col1:
                ax.bar(name , count )
                plt.xlabel("Names")
                plt.ylabel("Message count")
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')

        st.title('Most commmon words')
        st.pyplot(fig)

        #sentiment analysis
        st.title("Sentiment Analysis")
        val , dx , dy = helper.sentiment_analysis(selected_user , df , ddf)
        fig,ax = plt.subplots()
        ax.plot(dx, dy ,color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.header("Sentiment Score")
        st.title(val)

        #Top 5 positive users
        if selected_user == 'overall':
            st.title("Top scorers")
            dx, dy = helper.top_scorers(df , ddf)
            fig, ax = plt.subplots()
            ax.bar(dx, dy, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)





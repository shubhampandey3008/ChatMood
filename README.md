# ChatMood :speech_balloon: :bar_chart:

ChatMood is an innovative web application that not only analyzes and visualizes WhatsApp chat data, but also delves into the nuances of conversation sentiments. It leverages cutting-edge Natural Language Processing (NLP) techniques to make sense of both English and 'Hinglish' (a hybrid of Hindi and English) conversations. 

Powered by NLP, ChatMood transforms the raw chat data into meaningful insights. It begins by tokenizing the sentences into individual words, then applies lemmatization to reduce words to their base or root form, thereby ensuring that different forms of the same word are analyzed together. It also removes 'stop words' - common words like 'is', 'at', 'which', and 'on' that usually carry little meaningful information, to focus on the meaningful parts of the conversation.

The standout feature of ChatMood is its unique sentiment analysis. This app expertly handles 'Hinglish' conversations. It uses a special lexicon file where individual 'Hinglish' words are manually scored from 0 to 1 based on the emotions they represent. By reading and applying these scores, ChatMood effectively captures the sentiment of bilingual conversations, showcasing its versatility and inclusivity.

![Screenshot1]https://drive.google.com/file/d/197Y9I4xMww9nnDflvgBZppT-2xKbYQ8f/view?usp=sharing
![Screenshot2](https://drive.google.com/file/d/1p_TbrJCuaoDpAY3HSHFZAd1cf-QDsKV5/view?usp=sharing)
![Screenshot3](https://drive.google.com/file/d/1koRup_jBmKWY_PnNXMQ_nbrM66W8_G_f/view?usp=sharing)
![Screenshot4](https://drive.google.com/file/d/1v1RgF1Kark3p-S-oaZLw38pATuzQ8I9F/view?usp=sharing)
![Screenshot5](https://drive.google.com/file/d/143NREr9oNcsewjNRCBwAv0nUOwXLwwpm/view?usp=sharing)

## :star: Features

ChatMood offers a wide array of analytics and visualizations, including:

- **Sentiment Score**: This is a quantification of the overall sentiment of the group chat, ranging from 0 (most negative) to 1 (most positive). This score reflects the mood of the conversation, giving you a sense of the tone and vibe in the group.
- **Top Sentiment Scorers**: A bar graph showcasing the users with the highest sentiment scores, ranking them based on their positivity. This reveals the most positive contributors in the group.
- **Basic Chat Statistics**: Including total messages, total words, total media, and total links. This gives you a quick rundown of the chat activity.
- **Temporal Analysis**: Graphs of messages per month and average messages per day, providing a temporal view of chat activity.
- **Activity Analysis**: Mapping the number of messages per weekday and the busiest chat days. This tells you when the group is most active.
- **User Analysis**: A bar graph of the most active users. This indicates who are the major contributors in the group.
- **Word Cloud**: A visualization of the most frequently used words. This can highlight common topics or themes in the chat.


## :wrench: Installation 

Follow these steps to get ChatMood up and running on your local machine:

This guide assumes you have Python 3.8, pip, and git installed on your machine. If you have a different version of Python, consider using a virtual environment or Docker to avoid any conflicts.

```bash
# Clone the Repository
git clone https://github.com/shubhampandey3008/WhatsappChatSentimentAnalyzer.git

# Navigate to the Cloned Directory
cd WhatsappChatSentimentAnalyzer

# Install Required Packages
pip install -r requirements.txt

# Run the Application
streamlit run app.py
```

## :gear: Usage

Once ChatMood is up and running on your local machine, the next step is to export your WhatsApp chat:

1. **Exporting WhatsApp Chat**: WhatsApp allows you to export your individual or group chats to a text file. This can be done directly from the WhatsApp app. It's important to note that the **date and time should be in the 24-hour format**.

2. **Uploading the Chat File**: Navigate to the ChatMood application on your browser. Here, you'll find an option to upload the exported chat file. 

3. **Choosing the User**: After uploading, if it is a group chat, you'll need to select the specific user you want to analyze. You can also choose 'Overall' to analyze the entire group's chat data.

If you've uploaded an individual chat, ChatMood will automatically start the analysis, as there's only one user to analyze.

Through ChatMood, you can dive into various metrics, trends, and sentimental analyses of your WhatsApp conversations, both at an individual and group level.



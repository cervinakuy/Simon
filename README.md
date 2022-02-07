# Simon - Discord Q&A Help Bot Template
Tired of needing to answer the same questions over and over? As the owner of a large customer support discord server, I was too. Simon is a simple Discord bot template written in Python to help assist the yourself, moderators, and your users! 

In my own experience, successful configuration of Simon resulted in a **87% drop** in daily message count in public channels, with
most users receiving immediate help via Simon's help in DM as soon as they joined.

## Features
* Automatically sends responses to common questions in specific channels (or DM)
* DM Welcome join message
* Custom activity status ("Playing DM me your questions!")
* Require user text attachments to use paste websites \
  (To protect users from potentially malicious content)

## Simon in Action
#### Answering common queries / questions
![](https://i.imgur.com/NnDJLib.png)

#### DM welcome message upon join
![](https://i.imgur.com/Lx0CF4x.png)

#### Custom activity status
![](https://i.imgur.com/NQ4NAmR.png)

## Usage

#### Automatically answer common queries / questions
```
# add_query(hot_words, minimum_hot_words_count, automated_response]
#   hot_words (list): a list of words to detect for, order does not matter
#   minimum_hot_words_count (int): a minimum number of hot words in a message needed
#                            for a specific automated response
#   automated_response (str): The automated response to send from the bot
query_manager.add_query(["readme", "github"], 2, "Simon's README can be found at https://github.com")
```


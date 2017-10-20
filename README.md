# Gfycat_Bot

Reddit users often share the incorrect link when sharing GIFs they have uploaded to https://www.gfycat.com. This common mistake is due to the fact that once the gif is uploaded, Gfycat redirects users to the GIFs homepage which contains a lot of pre loaded elements that are not only unnecessary (such as related uploads) to the GIF but also increases the time taken for the page to load. This bot truncates the bloated link to a direct URL to the the GIF with playback controls in a larger size. This makes the GIF load faster as well as fixes the problem of the link not opening that users of some reddit mobile apps faced. The direct video is also of higher quality.

My original bot was [/u/gfy_cat_fixer_bot](https://www.reddit.com/user/gfy_cat_fixer_bot) which was later merged with another bot to create [/u/Gfycat_Details_Fixer](https://www.reddit.com/user/Gfycat_Details_Fixer/?sort=top). 

This repo also consists of a userscript written in JavaScript that can be used with popular extensions such as GreaseMonkey or TamperMonkey that provides the same functionality.

This bot makes use of [PRAW](https://praw.readthedocs.io/en/latest/).

![Top 10 most appreciated bots on Reddit (Ranked using the lower bound of Wilson score confidence interval for a Bernoulli parameter)](http://i.imgur.com/MLxzJus.png)  

[Source for ranked bots](https://goodbot-badbot.herokuapp.com/)

Example of a sample bloated Gfycat GIF
![A](http://i.imgur.com/SASyqnN.png)

Example of a direct Gfycat GIF
![B](http://i.imgur.com/RnWGN5h.png)

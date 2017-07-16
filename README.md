# Gfycat_Bot

Reddit users often share the incorrect link when sharing gifs they have uploaded to https://www.gfycat.com. This common mistake is due to the fact that once the gif is uploaded, Gfycat redirects users to the gifs homepage which contains a lot of pre loaded elements that are not only unnecessary (such as related uploads) to the gif but also increases the time taken for the page to load. This bot truncates the bloated link to a direct URL to the the gif with playback controls in a larger size. This makes the gif load faster as well as fixes the problem of the link not opening that users of some reddit mobile apps faced.

My original bot was [/u/gfy_cat_fixer_bot](https://www.reddit.com/user/gfy_cat_fixer_bot) which was later merged with another bot to create [/u/Gfycat_Details_Fixer](https://www.reddit.com/user/Gfycat_Details_Fixer/). [Source for merged bot](https://github.com/ImJustToNy/GfycatDetailsConvert) *credit to @ImJustToNy*

This bot makes use of [PRAW](https://praw.readthedocs.io/en/latest/).

example of bloated gfycat url
![A](http://i.imgur.com/SASyqnN.png)

example of direct url to gif
![B](http://i.imgur.com/RnWGN5h.png)

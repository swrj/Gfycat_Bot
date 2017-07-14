# Gfycat_Bot
Reddit bot that checks /new at specified time intervals for Gfycat submissions that are incorrectly linked an replies to the submission with a fixed URL.

Reddit users often share the incorrect link when sharing gifs they have uploaded from https://www.gfycat.com. This common mistake is due to the fact that once the gif is uploaded, Gfycat redirects users to the gifs homepage which contains a lot of elements that are unnecessary to the gif. These elements (at the time of writing) included 6 related gifs which are loaded and looped on screen as well as other information irrelevant to the viewing of the gif. This bot truncates the bloated link to a direct URL that consists of nothing but the gif, in a larger size with playback controls. This not only reduces the bandwidth used, but also results in faster playback and the enabling of useful playback controls. 

This bot makes use of PRAW.

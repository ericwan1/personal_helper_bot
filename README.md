# personal_reddit_helper

So I noticed that I've been spending an inordinate amount of time lately on social media. Luckily, my iPhone has a built in widget that tells me how much time I've spent on each app. After realizing I spent more than two hours a day on the reddit app (and more on my laptop) I made the decision to delete the app. However, I still needed my daily fix of reddit. Thus, I coded this short script. When run, it grabs a certain number of hot posts from a subreddit(s) of your choosing and emails them to you. The email also contents links to the discussion and post. I've been using this script to help limit the amount of time I spend on social media, and thankfully for me, I've been able to spend only about an 30 minutes a day on reddit now. 

### Using the script

You will have to enter your own information for the reddit client and emails (can't give that out!). Your own reddit `client_id` and `client_secret` can be found on https://www.reddit.com/prefs/apps/. 

Feel free to set your own subreddits, post count, etc. 

### Further thoughts

This was a really interesting project that I worked on over two days. It was the first time that I got to really read, understand, and utilize API to build something, which was cool. I think for future development that I would like to: 

1. Improve upon the output format of the subreddits and links. Currently for my personal use it is fine, but I imagine that others may want a more aesthetically pleasing email. 

2. Work on security. Figuring out a way to ensure that important email information, passwords, reddit login info, etc. will not have to be typed into the script. 

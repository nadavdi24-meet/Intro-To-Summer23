def create_youtube_video(title , description):
	youtube_video = {"title" : title , "description" : description , "likes" : 0 , "dislikes" : 0 , "comments" : "no comments"}
	return youtube_video

def like(video):
	if "likes" in video:
		video["likes"] += 1

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] += 1

def add_comments(video , username , comment_text):
	video["comments"] = {username : comment_text}

youtube_video = create_youtube_video("how i made a billion dollars as a 3 year old" , "how to be rich as a 3 year old")

for i in range(495):
	like(youtube_video)

print(youtube_video)


from facebook_scraper import get_posts
import pickle


#group_id = 'gamificationForEducation' #Gamification For Education
#group_id='gamefication' #Gamification
group_id='learningwithgames'#Game-based Learning, Gamification, and Games in Education
group_name = 'learningwithgames1_100000'

all_post = []

for post in get_posts(group=group_id, pages=100000):
	all_post.append(post)

pickle.dump(all_post, open('all_post_{}'.format(group_name), 'wb'))
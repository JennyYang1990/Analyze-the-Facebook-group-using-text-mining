import pickle
import numpy as np
import datetime as dt

post_file_name_list = ['all_post_gamification2_10000','all_post_gamification3_100000']
save_file_name = 'gamification_merged1'
def merge_post(post_file_name_list):
	post_dict = {}
	for post_file in post_file_name_list:
		posts = pickle.load(open(post_file, 'rb'))
		# print(len(posts))
		for p in posts:
			if p['post_id'] not in post_dict:
				post_dict[p['post_id']] = p
	return post_dict
all_post = merge_post(post_file_name_list)
pickle.dump(all_post, open(save_file_name, 'wb'))

def user_post_stat(posts):
	user_post_dict = {}
	for post_id in posts:
		user = posts[post_id]['user_id']
		if user not in user_post_dict:
			user_post_dict[user] = {'count':1, 'post_id':[post_id]}
		else:
			user_post_dict[user]['count'] += 1
			(user_post_dict[user]['post_id']).append(post_id)
	return user_post_dict
stat = user_post_stat(all_post)
def user_post_ranking(stat):
	user_id = []
	user_count = []
	for u in stat:
		user_id.append(u)
		user_count.append(stat[u]['count'])
	ranks = np.argsort(user_count)
	ranked_user_id = [user_id[i] for i in ranks[::-1]]
	ranked_user_count = [user_count[i] for i in ranks[::-1]]
	return ranked_user_id, ranked_user_count
ranked_user_id, ranked_user_count = user_post_ranking(stat)
stat[ranked_user_id[0]]
stat[ranked_user_id[14]]['count']


def likes_post_stat(posts):
	post_ids = []
	post_like = []
	for post_id in posts:
		post_ids.append(post_id)
		post_like.append(posts[post_id]['likes'])
	ranks = np.argsort(post_like)
	ranked_post_id = [post_ids[i] for i in ranks[::-1]]
	ranked_post_like = [post_like[i] for i in ranks[::-1]]
	return ranked_post_id, ranked_post_like
ranked_post_id_like, ranked_post_like = likes_post_stat(all_post)
all_post[ranked_post_id_like[9]]

def comments_post_stat(posts):
	post_ids = []
	post_like = []
	for post_id in posts:
		post_ids.append(post_id)
		post_like.append(posts[post_id]['comments'])
	ranks = np.argsort(post_like)
	ranked_post_id = [post_ids[i] for i in ranks[::-1]]
	ranked_post_like = [post_like[i] for i in ranks[::-1]]
	return ranked_post_id, ranked_post_like
ranked_post_id_comment, ranked_post_comment = comments_post_stat(all_post)
all_post[ranked_post_id_comment[9]]

def find_earliest_latest_time(merge_post_file_name):
	posts = pickle.load(open(merge_post_file_name, 'rb'))
	earlist_dt = dt.datetime(3000,1,1,12,0,1)
	latest_dt = dt.datetime(1900,1,1,12,0,1)
	for pid in posts:
		current_dt = posts[pid]['time']
		if earlist_dt > current_dt:
			earlist_dt = current_dt
		if latest_dt < current_dt:
			latest_dt = current_dt
	return earlist_dt, latest_dt
earlist, latest = find_earliest_latest_time('gamificationforeducation_merged')

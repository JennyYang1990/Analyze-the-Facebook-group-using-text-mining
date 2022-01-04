import lda_utils as utils
import pickle
import numpy as np

file_name = 'gamification_merged1'
dat = pickle.load(open(file_name, 'rb'))

all_text = []
for pid in dat:
	all_text.append(dat[pid]['text'])

common_dictionary, common_corpus = utils.process_data(all_text)

topics, lda = utils.run_lda(common_corpus, common_dictionary, topic_num=15, display_num=15)

utils.save_topics(topics, topic_path=file_name+'_topics.pkl')

hash_tags = []
hash_tag_index = []
for i in common_dictionary:
	if common_dictionary[i][0] == '#':
		hash_tags.append(common_dictionary[i])
		hash_tag_index.append(i)
hash_index_to_tag = {x:y for x,y in zip(hash_tag_index, hash_tags)}
hash_tag_to_index = {x:y for x,y in zip(hash_tags, hash_tag_index)}


hash_tag_stat = {i:0 for i in hash_tags}
hash_tag_rev_index = {i:[] for i in hash_tags}
post_hash_tags = []
for i,pst in enumerate(common_corpus):
	hash_tag_pst = []
	for tp in pst:
		if tp[0] in hash_index_to_tag:
			hash_tag_stat[hash_index_to_tag[tp[0]]] += tp[1]
			(hash_tag_rev_index[hash_index_to_tag[tp[0]]]).append(i)
			hash_tag_pst.append(hash_index_to_tag[tp[0]])
	post_hash_tags.append(hash_tag_pst)
hash_tag_freq = [i for i in hash_tag_stat.values()]
rank_freq_hash_tag = [hash_tags[i] for i in np.argsort(hash_tag_freq)][::-1]
rank_freq_hash_tag_freq = [hash_tag_stat[hash_tags[i]] for i in np.argsort(hash_tag_freq)][::-1]
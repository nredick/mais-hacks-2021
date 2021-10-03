import tensorflow as tf
import random
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


#seed_text = "dream cloud cheese"
saved_model_path = 'model/'
loaded_model = tf.keras.models.load_model(saved_model_path)
tokenizer = pickle.load(open('model/tokenizer.pkl','rb'))
max_sequence_len=50

def line_breaker(s):
	""" breaks string s into lines mostly randomly"""
	s = s.split()
	l=len(s) # len of string
	output=""
	while l>0:
		x=random.randint(1,int(l/2)+1)
		tmp = s[:x]
		output += ' '.join(tmp) + "\n"
		s=s[x:]
		l -= x
	# line breaking between repeated words
	split = output.split(' ')
	final = ""
	for i in range(len(split)-1):
		if split[i]==split[i+1]:
			final += split[i] + '\n'
		else: 
			final += split[i] + ' '
	if split[-2]==split[-1]:
		final += "\n"+split[-1]
	else:
		final +=split[-1]
	final_output = final[0].upper()+final[1:]
	return final_output  

def pred_poem(seed_text, next_words=30, incl_title=True,):
	og_seed = seed_text
	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([seed_text])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
		predicted = np.argmax(loaded_model.predict(token_list), axis=-1)
		output_word = ""
		for word, index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		seed_text += " " + output_word
	if not incl_title:
		seed_text = seed_text[len(og_seed)+1:]
	return line_breaker(seed_text)

#print(pred_poem('green leaf tree'))
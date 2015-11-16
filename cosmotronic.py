import sys
import math as m
import random
import string
import time
import os
import subprocess

def parser(input_file):
	exclude = set(string.punctuation)
	read_string = input_file.read()
	read_string = string.replace(read_string, '|', ' ')
	read_string = ''.join(c for c in read_string if c not in exclude)

	chain = {'':[]}

	prev = ''

	for word in read_string.split():
		chain[prev].append(word)
		if word not in chain:
			chain[word] = []
		prev = word

	for val in chain:
		if chain[val] == []:
			chain[val].append('')

	return chain

def generate(word, chain, t):
	next_word = random.choice(chain[word])
	line = ' ' * int(30 * (m.sin(m.radians(t)) + 1)) + next_word
	return (next_word, line)

def main():
	if len(sys.argv) != 2:
		print "Usage: 'python cosmotronic.py [input-file]'"
		exit()

	with open(sys.argv[1], 'r') as input_file:
		chain = parser(input_file)
		word = ''
		t = 0
		while True:
			generated = generate(word, chain, t)
			word = generated[0]
			print generated[1]
			t += 10
			if sys.platform.startswith('darwin'):
				p = subprocess.Popen(["say", "'" + word + "'"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
				#os.system("say '" + word + "'")
			elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
				p = subprocess.Popen(["cscript", "say.vbs", "'" + word + "'"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
				#os.system('cscript say.vbs "' + word + '"')
			time.sleep(.3 * len(word))

if __name__ == "__main__":
	main()
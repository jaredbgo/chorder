
import numpy as np

def key_finder(note, scale='major'):
	notes = ['A', 'A#/Bb', 'B/Cb', 'C', 'C#/Db', 'D', 'D#/Eb', 'E/Fb', 'F', 'F#/Gb', 'G', 'G#/Ab']
	valid_notes = []
	for each in notes:
		if '/' in each:
			valid_notes += each.split('/')
		else:
			valid_notes.append(each)

	major_interval = np.cumsum([0, 2, 2, 1, 2, 2, 2, 1])
	minor_interval = np.cumsum([0, 2, 1, 2, 2, 1, 2, 2])
	scale_list = ['major', 'minor']

	major_chord_types = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished']
	minor_chord_types= ['minor', 'dimished', 'major', 'minor', 'minor', 'major', 'major']


	if len(note) > 2:
		raise Exception('Note must be at most 2 characters')

	elif note not in valid_notes:
		raise Exception('Note must be in {}'.format(valid_notes))

	if note in notes:
		idx = notes.index(note)

	else:
		for i, each in enumerate(notes):
			if note in each.split('/'):
				idx = i

				break

	
	notenames = []
	if scale.lower() == 'major':

		currnote = (idx + major_interval)%len(notes)

		for each in currnote:
			notenames.append(notes[each])

		return {"Chords of " + note + " " + scale.lower(): [s1 + ' ' + s2 for s1, s2 in zip(notenames, major_chord_types)]}

	elif scale.lower() == 'minor':

		currnote = (idx + minor_interval)%len(notes)

		for each in currnote:
			notenames.append(notes[each])

		return {"Chords of " + note + " " + scale.lower():[s1 + ' ' + s2 for s1, s2 in zip(notenames, minor_chord_types)]}
	else:
		raise Exception('Scale must be one of {}'.format(scale_list))

def main():

	keep_going = True
	print("")
	print("Welcome to Chorder!")
	print("")


	while keep_going:

		key = input("Enter the root: ")

		scale = input("Enter the scale: ")

		chords = key_finder(key, scale=scale)

		scale_name = list(chords.keys())[0]

		scale = chords[scale_name]

		print('')
		print('---------------------------')
		print('**********CHORDER**********')
		print('---------------------------')
		print('')

		print(scale_name + ':')
		print('')

		for each in scale:
			print(each)
		print('')

		again = input("Would you like another key? Enter yes or no: ")
		again = again.lower()
		while again not in ['yes', 'no']:
			print("I'm sorry, response must be in {}".format(['yes', 'no']))
			print('')
			again = input("Would you like another key? Enter yes or no: ")
			again = again.lower()

		if again == 'yes':
			keep_going = True
			print('')
			print ("OK, let's do it again!")
			print('')
		else:
			keep_going = False
			print('')
			print ("Thanks for using Chorder!")
			print('')

if __name__ == '__main__':
	main()

# Import important libraries

import os 
import gc
from pprint import pprint 

# Get CWD
cwd = os.getcwd()

# Get the data from the user. It's all strings, so just prompt them.
id = input('Enter poll ID\n')
round = input('Enter the round this question is for from among the following: first, second, third\n')
questionText = input('Enter Question Text. This is likely what you will have TTS read as well.\n')
shortQuestionText = input('Enter Short Question Text (What it shows over the doors during gameplay)\n')
# Yes I can do this in an array but I don't feel like looking up python array stuff right now. You do it, Mr. Fancy-Pants Bigshot Python Dev.
firstChoice = input('Enter first poll choice.\n')
secondChoice = input('Enter second poll choice.\n')
thirdChoice = input('Enter third poll choice.\n')
fourthChoice = input('Enter fourth poll choice.\n')
fifthChoice = input('Enter fifth poll choice.\n')
sixthChoice = input('Enter sixth poll choice.\n')
seventhChoice = input('Enter seventh poll choice.\n')
eighthChoice = input('Enter eighth poll choice.\n')

# Create a data.jet file using a stock one as base. The folder will be made off of the poll id.
try:
	os.makedirs(cwd+'/'+id)
except OSError:
	pass
newDataJetFile = open(cwd+'/'+id+'/data.jet', "w")
newDataJetFile.write('{\n "fields": [\n  {\n   "t": "B",\n   "v": "false",\n   "n": "HasIntroAudio"\n  },\n   ')
newDataJetFile.write('{\n  "t": "A",\n   "v": "intro",\n   "n": "IntroAudio"\n  },\n   ')
newDataJetFile.write('{\n  "t": "B",\n   "v": "true",\n   "n": "HasQuestionAudio"\n  },\n   ')
newDataJetFile.write('{\n  "t": "A",\n   "v": "question",\n   "n": "QuestionAudio",\n   "s": ""\n  },\n   ')
newDataJetFile.write('{\n  "t": "B",\n   "v": "false",\n   "n": "HasOutroAudio"\n  },\n   ')
newDataJetFile.write('{\n  "t": "A",\n   "v": "outro",\n   "n": "OutroAudio"\n  }\n ]\n}')
newDataJetFile.close()


# Now create or open and append the Poll Mine content file
newPollMineContent = open(cwd+'/content.jet', "a")

# Write to it the stuff to copy out later
newPollMineContent.write('\n  {\n   "category": "",\n   "choices": [\n')
newPollMineContent.write('    "'+firstChoice+'",\n')
newPollMineContent.write('    "'+secondChoice+'",\n')
newPollMineContent.write('    "'+thirdChoice+'",\n')
newPollMineContent.write('    "'+fourthChoice+'",\n')
newPollMineContent.write('    "'+fifthChoice+'",\n')
newPollMineContent.write('    "'+sixthChoice+'",\n')
newPollMineContent.write('    "'+seventhChoice+'",\n')
newPollMineContent.write('    "'+eighthChoice+'"\n   ],\n')
newPollMineContent.write('   "id": "'+id+'",\n   "intro": null,\n   "isValid": "",\n   "outro": null,\n')
newPollMineContent.write('   "question": "'+questionText+'",\n')
newPollMineContent.write('   "questionShort": "'+shortQuestionText+'",\n')
newPollMineContent.write('   "round": "'+round+'",\n   "us": false,\n   "x": false\n  },')
newPollMineContent.close()

# And collect garbage, juuuuuuuuust in case.
gc.collect()
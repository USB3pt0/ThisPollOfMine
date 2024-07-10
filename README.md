# ThisPollOfMine
A python script to make modding Poll Mine for The Jackbox Party Pack 8 easier.

I hacked together these scripts as I had been modding Nonsensory and Poll Mine by hand, but the files of both having another folder with data the game uses became tedious and I was making mistakes.  More than I did writing these scripts, anyway.  These instructions assume a basic knowledge of scripting/coding logic, primarily because you have to copy and paste the entries to the .jet files yourself, and you don't want to muck up the formatting for {} brackets, or extra commas, and soforth.

# PREREQUISITES
You need Python 3 installed.  The script will make subfolders the game requires.  You also need to know where your Poll Mine folder is; it will be in [JPP8 install directory]/games/SurveyBomb. The files you need to edit are in content, as are the folders you need to put the folders these scripts generate.

# INSTRUCTIONS
1. Run the script by double clicking it or from command line, if you prefer.
2. First you will be prompted for a Poll ID. The game starts in the 70000s but I believe it's arbitrary...I started with 00001 myself.
3. Next is the round.  The ONLY options are (first, second, third) for round 1, 2, and 3 respectively.  If you don't know the differences between rounds I'll list them below.
4. Next you'll be asked for questionText. This is the poll itself, what Laverne (usually) reads out loud before you rank your choices.
5. Next is shortQuestionText, which is what's above the doors during the game while you're choosing as a team.
6. Lastly there'll be 8 choices, that you must have an entry for each in.
7. Once you entered the last choice, the window will close and generate a folder for the poll ID as well as a content.jet.  Generate a question.ogg, either a silent audio file, a placeholder file, cut Laverne's voice into something for it, use TTS/ML voices...whatever. Needs to be there or the game will softlock.
8. Copy the generated folder(s) to [Poll Mine folder]/SurveyBombQuestions, and copy the content from content.jet to SurveyBombQuestions.jet. You can delete whatever out of there if you wish, or make an empty file using them as a structure and back them up like I do.
9. Run Poll Mine. It should now select from the polls you added.

# NOTES
Make sure you have 8 answers for EVERY poll.
Make sure you have at least one poll for EVERY round.
Want to make it personal? You can change the poll choices in the .jet to a single entry (or look at the stock files for more options with) called "{{PLAYERS}}".  This will fill out whatever empty spaces with randomly selected player names.  
There are some fields I don't touch that the main .jet occasionally uses.  One such one is you can put a few conditions in the isValid field, such as numPlayers >= 6 to make the prompt only appear when the number of players matches.


# FUTURE PLANS AND TO-DO
I want to make this an application for easier editing.  Also, I want to mod the script so it doesn't make a generic data.jet for everything, just so I can add subtitles for the question.ogg audio... though it seems pointless to have subtitles if the question's right there on screen...
In the data.jet for each question are also introAudio and outroAudio fields. If you look at the stock stuff you may find what you need to set these if you wish. It merely plays another .ogg before and/or after question.ogg, typically Laverne would have a joke related to the prompt for it. You'll have to edit the data.jet AND the SurveyBombQuestions.jet file for that, though.

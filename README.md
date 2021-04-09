
**RAJASRI KOLLI**


In this Project all the sensitive information from the text files  are redacted based on given input flags and commands.



*Info to be redacted*: The redacted flags generally are names, genders, dates, concept and phones.

For the names : nltk and nltk.ne_chunk() are used to identify named entities with labels named "PERSON".


For the dates : the regular expression for identifies the terms/dates of format 'dd/mm/yyyy'

For the Phones : regular expressions are used to identify them finding the following formats of phone numbers such as 'ddd./-ddd./-dddd'

For the genders :  a list of possible genders include =['he','she','him','her','his','hers','male','female','man','woman','men','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']

if  taken any file which has any of the above gender form , it replaces the word.

For the concept : this function identifies synonyms of given concept word with the help of importing wordnet from nltk.corpus

-- All the sensitive information is replaced with ' ^ ' times the length of item to be redacted.


OUTPUT : For the output all the redacted content into file and converting into pdf files.

os.system("enscript {0} -o - | ps2pdf - {1}/{2}".format(f_name,loc,fi_name))

FLAG RECOGNITON

For the flag recognition I have used the sys.argv() function to access the input flags and storing them in their respective lists.

After the intial flag recognition each list has the repective filenames or flags or texts or commands stored in them.

for example:

input_label='--input' flags=["--names","--dates","--places","--phones","--genders","--addresses"] concept_label='--concept' output_label='--output' #stats_label=["stderr","stdout"] not_concept=["--input","--names","--dates","--places","--phones","--genders","--addresses","--output","--stats"] count=0 input_commands=[] flags_commands=[] concepts_commands=[] output_commands='' stats_commands=[]

PROJECT-1 IN CLASS PHASE 2

In this phase, Unredactor.py has been added to the project. The Unredactor takes the redacted document and it will give the top three most likely candidates to be filled in the redacted location.

For Discovering the best names I have trained a model to predict the missing words using the Large Movie Review Data Set. This data set contains movie reviews from IMDB.

Creating the unredactor involved 4 basic tasks:
TASK 1: TRAINIG THE MODEL with Train data seperated from the data set Downloaded

The data set has the structure: aclimb --->test,train,readme,imdb.vocab test-----> neg,pos,urls_neg.txt,urls_pos.txt train----->neg,pos,urls_neg.txt,urls_pos.txt pos----->Collection of txt files neg------>Collection of txt files

Due to large Data Set I have choosen Pos folder of train for training the data and tested on the Pos folder of test for testing the data.

#training Data Phase trainData=doextraction(sys.argv[-1])

The doextraction function of unredactor.py takes the location of the folder containing training data such as "train/pos/*.txt". The doextraction function reads one file by one file and for each file identifies the enitities that are found to be labelled PERSON in accord to ne_chunk(pos_tag(word_tokenize(x))) tree generated.

Stores these entities enities in a list.

FEATURE GENERATION

We have considered 4 features:

feature1: Number of the words that are found to be redacted in a file(repetetive allowed) feature2: Number of Spaces found in particular redacted word feature3: Number of Characters in particular redacted word except spaces feature4: Word Count of the file

For Eg: "Vishnu studies CS in OU. Vishnu has most of his friends from India."

Feature Vector for Vishnu would be [2,0,6,13] I have also created alist such that it has info related to the person and corresponding feature vector.

For Eg:[["Bromwell",[2,0,8,136]],["Natella",[2,0,7,136]]]

The trained data phase returns the above kind of list and also the count of files that it has been trained upon.

TASK 2: REDACTING THE PERSON NAMES OF THE TEST DATA FILES

the doextract function takes the test data set location as input. The files in the test data are opened one by one in read mode and the list of the words with label=PERSON are identified and stored in a list. Then the test files are again opened in the write mode and the words resembling the list items obtained above are redacted with "*" for each character in the word.

TASK 3: Predicting the Names of the redacted files in the test

The doPredict function takes the Test data files location and trained data feature list as input and in return predicts the top three most likely word for the each redacted field in the test folder.

Initially we generate feature vector for the redacted words and compare them to the trained data feature list items one by one using the Cosine simmilarity measure. The most likely words are the ones that have high measures obtained.

for Eg: The top three most likely word for the 1 redacted word in file are: [['Steven Caseman', 0.99999999999999989], ['Amanda Tapping', 0.99999999999999989], ['Morgan Freeman', 0.99999988069260182]] similary the above sort of thing is done for all redacted fields in the file.

EXECUTABLE METHOD: try ro execute by typing-- python3 unredactor.py "train/pos/*.txt"

AS Whole Train files is includes it literally takes 20+ min to execute, for faster execution you can try -- python3 unredactor.py "data/*.txt" which has 27 files in total

TESTS:

I have written seven test files testing the main features of the files.

OUTPUT(PACKAGING and making the project locally testable )

vishnu@vishnu-Inspiron-5537:~/Desktop$ python3 unredactor.py "train/pos/*.txt" The top three most likely word for the 1 redacted word in file are: [['Steven Caseman', 0.99999999999999989], ['Amanda Tapping', 0.99999999999999989], ['Morgan Freeman', 0.99999988069260182]]

The top three most likely word for the 2 redacted word in file are: [['Shikhar', 0.99999999999999989], ['Eleanor', 0.99999995540398112], ['Jackson', 0.99999995540398112]]

The top three most likely word for the 3 redacted word in file are: [['Adam Sandler', 0.99999990975777853], ['Chris Farley', 0.99999965152274484], ['Parker Posey', 0.99999963471787467]]

The top three most likely word for the 4 redacted word in file are: [['Akshay Khanna', 0.99999989822920354], ['Maria Bandaur', 0.99999989580625992], ['Dandy Warhols', 0.9999995976365984]]

The top three most likely word for the 5 redacted word in file are: [['Penny Opera', 1.0], ['Lotte Lenya', 1.0], ['Guy Ritchie', 1.0]]

REQUIRED:

DEPENDENCIES: NLTK-pip3 install nltk for installing nltk

VERSION: PYTHON VERSION 3.6 preferred ,any version above PY(3.0) have to work.

REFERENCES: LARGE IMDB MOVIE DATA SET- http://ai.stanford.edu/%7Eamaas/data/sentiment/ ENTITY SEARCH- https://developers.google.com/apis-explorer/#p/kgsearch/v1/kgsearch.entities.search?indent=true&query=ashton+&types=Person&_h=5& KNOWLEDEGE GRAPH SEARCH API- https://developers.google.com/knowledge-graph/#typical_use_cases Sorting List using Itemgetter- http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

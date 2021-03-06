# Academic-Writing-Expert

Developed a web-based academic writing system that assisted international researchers to easily write a paper in English with real-time suggestions of grammar patterns, collocations and spell checkers<br><br>
**Skills: Python, Hadoop MapReduce, Flask, JavaScript, AJAX, HTTP requests handling, Bootstrap, CSS, HTML, spaCy, Natural Language Processing, Big Data Processing, Web Development**<br>
- Built a large scale of corpus by tokenizing 20,000,000 sentences, extracting and filtering patterns from CiteSeerX with Hadoop MapReduce and identifying valid collocations based on 930 high frequency academic keywords<br>
- Created an interactive user interface by real-time parsing user input, making HTTP requests to communicate with backed corpus and displaying extracted linguistic information on demand with higher precision<br>

### Demo Video
<a href="https://www.youtube.com/watch?v=62C2kA_UyeA&feature=youtu.be" target="_blank"><img src="./imgs/cover.png"  width="720" height="540" border="10"/></a>
<br>

### Features
##### Interactive User Interface
Users can compose their academic writing in the text box. Suggestions of grammar patterns and collocations will show in a pop-up menu below <br>
<img src="./imgs/interface.png" width="700px" />
<br>

##### Real-Time Suggestions based on input text
A pop-up menu shows next-step writing suggestions based on user's current input text. The left column are suggestions for grammar patterns, sorted from patterns with high to low frequencies in corpus. The right column is the corresponding collocations for the grammar pattern. Users can click on the collocation to autocomplete the collocation in their text.
<img src="./imgs/interactive.png" width="700px" />
<br>

##### Sentence Example
Academic Writing Expert also provides users with sentence examples to show users how to use the grammar patterns well. All you need to do is just click on the "show example" button
<p align="left">
<img src="./imgs/example.png" width="700px" />
</p>
<br>

##### Spell Checker
Our system also inclues a spell checker to automatically detect if user's input text has any typo and offer three possible corrections
<img src="./imgs/spell.png" width="700px" />
<br>

### Processing Structure
<img src="./imgs/structure.png"  />
<br>

### Experiment
##### 1. Grammar Patterns and Collocations filtering and extracting
a. Lemmatized, find POS(Part-of-peech) for the sentences from CiteSeerX, and tokenize them using Genia Tagger <br>
b. Convert those tokenized sentences into N-gram, and further convert them into "elements" <br>
c. Extract possible grammar patterns based on existing grammars <br>
<img src="./imgs/grammar.png"  />
<br>
d. Filter the valid grammar patterns based on statistical analysis <br>
e. Use the N-grams and the valid grammar patterns to find possible collocations<br>
f. Filter the valid collocations based on statistical analysis<br>
g. Store the valid grammar patterns and their corresponding valid collocations to our corpus<br>
<img src="./imgs/collocations.png"  />
<br>
##### 2. Spell Checker
a. Training data is from CiteSeer papers <br>
b. Use Noisy-Channel model and do some permutation for vocabularies including insert, delete, replace and transpose<br>
c. Combine the result from step b with often-confused-words list from alphaDictionary to compute some candidates<br>
d. Calculate the most possible correct word as suggestion of spell checker with Maximum Likehood Estimation<br>
<img src="./imgs/spellchecker.png"  />
<br>

 

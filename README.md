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



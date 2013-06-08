SCIENCE HACK DAY, Nairobi - 2013: MACHINE LEARNING FOR PHYSICS
===============================================================

A project based on ideas of Machine Learning _(M.L)_ : We need to train computers to accurately recognize sentences in either Swahili or English out of reading entries from Wikipedia from both languages. We will then use similar rules and techniques to detect the presence of particular sub-atomic particles inside Physics data collected by collaborators at the Compact Muon Solenoid (C.M.S) experiment at CERN.


scikit-learn example and our experiements at Siena. 
======================================================= 

  It's great to see you've already started looking at the scikit-learn tools! That will probably really help things this weekend. 

  Here at Siena, I've started to look into this stuff as well with a student of mine, Jess Muenkel (cc'ed on this email). I've wanted to look at these python tools for some time, so this is a great excuse for me to dedicate this time!  :)

   I've attached the very first example that Jess and I wrote. All of this is based on the scikit examples. For now, we've chosen to focus on the Decision Tree (DT) algorithm, as I think it's supposed to be relatively easy to use. I should point out, we've not spent any time trying to actually learn what the algorithm does (yet) we've only got it to work. 

http://scikit-learn.org/stable/

http://scikit-learn.org/stable/modules/tree.html

   The example (reasonably commented) walks through the standard procedure for ML (Machine Learning):

  * Choose an algorithm.

  * Give it two (or more) datasets from different populations. These are called TRAINING samples. 

   * Train the algorithm. 

   * Give it another sample of *different* data where you know the answers and see how well the algorithm predicts the dataset. This is called the TESTING sample. 

   If you have scikits and matplotlib installed, you should be able to run this. In fact, I urge you to test it out and hand it out to others as a ``hello world" type example. 

   Once Jess and I had this running, I had Jess pull about 400 sentences (randomly) from the Swahili and English versions of Wikipedia. We then split each of these in half: 200 sentences for training and 200 for testing. 

    Jess then wrote a python program to count the frequency of certain letters in *each sentence*. She created files that have one line per sentence on which is the percentage a letter appears *in that one sentence*. She has one set of files for Swahili and one set for English. So the first few lines look something like this:

0.131868 0.087912 0.098901 0.076923 0.065934
0.153061 0.091837 0.051020 0.081633 0.091837
0.157895 0.073684 0.105263 0.042105 0.115789
0.170213 0.056738 0.127660 0.049645 0.042553
0.212121 0.050505 0.121212 0.020202 0.060606
0.240000 0.053333 0.106667 0.040000 0.066667

   I won't tell you what letters we've chosen (that's for the Hack Day! :)), but with just a few we can tell you whether or not a sentence is in Swahili or English with about 97% accuracy! *Just* from single letter counts! We were quite surprised and impressed with the algorithm!

   We stayed away from letters that might not appear in both languages like ``q". 

   Anyways, this is very analagous to what high-energy particle physicists do with our data. We measure some quantities (letters) in our detector and for each proton-proton collision (sentence) we look for some combination of those measured quantities (frequency of letters, for example) that can help us decide whether or not an event produced a W boson or top-quark (Swahili or English). I think this might be an interesting roadmap for how to approach this type of project for the Hack Day. 

   As always, it's *you guys* that are running the event. I'm only here to help and provide data and ideas. So feel free to come up with your own approach....this is only one suggestion. 

   Tomorrow, Jess and I will prepare some CMS data for you to play with. But even just trying out the language stuff will be challenging. I *think* if you write your code generally to read in data like the above sample, it will be interchangeable between the language and CMS example. At least I think so.  :)    We'll see how it all works out!

* For the hackday itself (or just before?)
========================================= 
Once you understand the code, I would recommend this:

* Grab a few hundred sentences in Swahili and English and put them into separate text files. 
* Write some code to count up the number of times a particular letter appears in each sentence. Maybe start with ``a" and ``e".
* Write to a file the fractional amount that letter appears. For instance, if there are 5 ``e"s in a 100 letter sentence, you would write out 0.05. Write these out as columns. 
* Modify this example to read in those files and put them into the ``X" array. 

   Of course, this can all be done at the Hack Day, but you can help others if you already have some starter code. 

   Also, think about if there's anyway to post these exercises (and the work that the other hackers do) online for others to learn from. Maybe some nice webpage of the work or even making one of Github's pages? I've never done that but maybe one of the other hackers has experience? Just a thought. 

* Notes on the screen-shot attached (Check inside the folder named ``resources") 
=================================================================================
 Also, your screen shots look exactly like what we get. Those ``datasets" are completely arbitrary. You can imagine that they might represent frequency of letters, or energy of particles, or heights of people, but the point is that with the naked eye we can see that there are two distinct populations of whatever they are. It's a 3D dataset (every entry in a dataset is defined by three numbers) so I plotted each 2D relationship: x vs y, x vs z, y vs z. Just to try to give some sense of how different they are.  

-- 
-- 
----------------------------
Matt Bellis
Siena College
mbellis@siena.edu
http://www.mattbellis.com
----------------------------

" 


More links: 
____________ 
* SciKit Learn: http://scikit-learn.org/stable/

* Decision trees using SciKit Learn: http://scikit-learn.org/stable/modules/tree.html 

* C.M.S (Compact muon solenoid's) experiment's event viewer: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookFireworks 

* Genism, for collecting a bag of words from Wikipedia dumps: http://radimrehurek.com/gensim/index.html

* Science hack day, Nairobi - 2013: Ideas Wiki => http://shdnairobi.pbworks.com/w/page/66494507/SHD%20Nairobi%202013%2C%20Hack%20ideas 


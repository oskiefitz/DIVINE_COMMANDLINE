## BASICALLY:
In this folder there are two examples of extracted verse data and parsing data. 

## VERSE DATA

The verses data looks like this, extracted from Biblehub.com to .txt files: 
e.g. Genesis 1:1 - look from right to left, it's Hebrew text  


בְּרֵאשִׁ֖ית\
בָּרָ֣א\
אֱלֹהִ֑ים\
אֵ֥ת\
הַשָּׁמַ֖יִם\
וְאֵ֥ת\
הָאָֽרֶץ׃

\\\\

Each word from the verse is printed in a list, the list is in order. So this verse reads:  

//     [   1 בְּרֵאשִׁ֖ית  2 בָּרָ֣א  3 אֱלֹהִ֑ים 4 אֵ֥ת 5 הַשָּׁמַ֖יִם 6 וְאֵ֥ת  7 הָאָֽרֶץ׃]  //  

/There are about 6000 verses , each filing path for this verse would be ~/Bible/Genesis/Chapter_1/Genesis_Chapter_1_Verse_1.txt ;
so - ~/Bible/[BOOK NAME]/Chapter_[CHAPTER NUMBER]_Verse_[VERSE NUMBER].txt

\\\\\

## PARSING DATA

Parsing data looks like this:
e.g. Genesis 1:1 :

Prep-b &#124; N-fs: Preposition-b :: Noun - feminine singular\
V-Qal-Perf-3ms: Verb - Qal - Perfect - third person masculine singular\
N-mp: Noun - masculine plural\
DirObjM: Direct object marker\
Art &#124; N-mp: Article :: Noun - masculine plural\
Conj-w &#124; DirObjM: Conjunctive waw :: Direct object marker\
Art &#124; N-fs: Article :: Noun - feminine singular  



Each line is asigned to each word of the verse data file - notice how there are 7 lines.
There is data for each verse, the naming convention is:
\
~/Bible_with_Parsing/Genesis/Genesis_Chapter_1_Verse_1_PARSED.txt 
so = ~/Bible_with_Parsing/[BOOK NAME]/[BOOK NAME]_Chapter_[CHAPTER NUMBER]_Verse_[VERSE NUMBER].txt

Notice here in this path there's no Chapter folder in the path -- I forgot to add that on the initial script but I cba to do it again because there's like 6000 files. 
\
## TO DO

בְּרֵאשִׁ֖ית (P) בָּרָ֣א (P) אֱלֹהִ֑ים (P) אֵ֥ת (P) הַשָּׁמַ֖יִם (P) וְאֵ֥ת (P) הָאָֽרֶץ (P)׃
  
  
  Create sentences from the list, then insert the parsing data to its asigned word. Like this above, where P is what is written on the PARSED file, i.e. for the first word from the right, P is "Prep-b &#124; N-fs: Preposition-b :: Noun - feminine singular" 
It's tricky because it's right aligned, make sure you're UTF-8 , also consider U+200F RIGHT-TO-LEFT MARK (&rlm;). In UTF-8 it is E2 80 AF : I'm struggling to make it work atm..

First thing to do is to make a script that prints the parsing info next to its asigned word, then after that, to make a script that does it for all 6000 verses using their file paths.





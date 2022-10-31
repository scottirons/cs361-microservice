# cs361-microservice

Communication Contract:

1. Requesting information:
- My microservice will work by reading a text file containing a language name. To request a URL to more information on the language, please write the language name to the text file. Capitalization doesn't matter, but it should be all on one line without extra spaces.

2. Receiving information:
- As it currently stands, my program will share both a short piece of text and a URL (or multiple URLs) that will link to Glottolog, a website with information about the world's languages.
- The three different types of received information will be:
  a) If the language has a unique page on Glottolog, a short message and one URL
  b) If the language does not have a unique page, a short message and multiple URLs
  c) If the language is not on Glottolog at all, a short message saying such.
  
For example, writing the following to the text file as a request:

Spanish

Will return the following response:

Click here to learn more about Spanish: https://glottolog.org/resource/languoid/id/stan1288

<img width="1154" alt="CS361 ironss microservice sequence diagram" src="https://user-images.githubusercontent.com/87613441/199059090-26eec33a-60ae-4e49-bedc-b99750b2423e.png">

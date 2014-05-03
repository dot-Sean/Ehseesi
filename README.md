**[For Elliot: the Project's final Google Doc](https://docs.google.com/document/d/1QzRitdP4-GWRlYfw9CxIi4BzgubfXXRwGcuYEMM-7ag/edit)**

**PURPOSE:**

Although it may look like the name of a magical Westerosi dragon princess, Ehseesi is actually a specialized search engine! Pronounced “ay see see”, Ehseesi  aims to help fans of sports and TV shows find their live-streaming content. Inspired by occasional difficulty in finding where to watch Tar Heel basketball games, we hope to create a search utility that locates TV listings and online streams for all available games. It was originally planned as a search engine solely for ACC college sports, hence the odd name.

**SCOPE:**

A search engine? Sounds complicated. For the purpose of this class (Information Science 560), though, we’ll try to keep this ambitious sounding project simple. We will eliminate the need for natural language processing by letting Twitter handle our search queries. 

Ehseesi will take advantage of Twitter’s public API to find real-time links to livestreaming content. To form queries, It will accept user input and append “live stream” to the end of it. It will use this query to search for the top Tweets containing it. It will then parse the tweets retrieved to extract links, which it feeds back to the user (with a disclaimer that links are not guaranteed to be legal or safe).

**PLAN FOR DISPERSAL AND REUSE:**

Our Github repo is freely available under the MIT license. Anybody can use our code as long as they attribute it to us. Our program, if successful, will prove useful to anybody looking for live-streaming content. In the long-term, the program could become not only useful but reliable, filtering out spammy links and implementing links from more reliable sources than Twitter. Google is surprisingly bad at finding such media. Twitter functions surprisingly well as a real-time search engine and is more tolerant of illegal content (which many people are looking for). By focusing narrowly on a specific kind of media, Ehseesi has the potential to differentiate itself from existing search options. There are legal and illegal sources from which stream lists can be compiled. Ehseesi ideally would bring the two types together in a single place.

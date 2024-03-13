# Practical Task 2 of Task 20 - NLP - Semantic Similarity using movies.txt

# This programme creates a function to return the movie a user would watch, if 
# they have watched 'Planet Hulk'. The function takes the description of 
# 'Planet Hulk' and returns the movie title of most similar movie

# Pseudo code: Create dictionary with movies.txt. 
# Create separate lists with movie titles and movie descriptions.
# Define function with Planet Hulk description as arguement. 
# Tokenize Planet Hulk description and use for-loop to
# iterate through movie descriptions. Store similarity values in a list.
# Find the maximum similarity value and retrieve corresponding index from the 
# descriptions list. Use the same index to retrieve movie title from the 
# movies list. Store retrieved movie title and max similarity value in a tuple
# and return the variable. Call the function and print the returned value 
# using f-string.

# import spaCy and language model
import spacy
nlp = spacy.load('en_core_web_lg')

planethulk_desc = "Will he save their world or destroy it? When the Hulk \
becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle \
and launch him into space to a planet where the Hulk can live in peace. \
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery \
and trained as a gladiator."

# Dictionary with movie titles as keys and descriptions as values
movies_desc = {
"Movie A" : "When Hiccup discovers Toothless isn't the only Night Fury, he \
must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant \
named Grimmel finds it first.",
"Movie B" : "After the death of Superman, several new people present themselves \
as possible successors.",
"Movie C" : "A darkness swirls at the center of a world-renowned dance company,\
one that will engulf the artistic director, an ambitious young dancer, and a \
grieving psychotherapist. Some will succumb to the nightmare. Others will \
finally wake up.",
"Movie D" : "A humorous take on Sir Arthur Conan Doyle's classic mysteries \
featuring Sherlock Holmes and Doctor Watson.",
"Movie E" : "A 16-year-old girl and her extended family are left reeling after \
her calculating grandmother unveils an array of secrets on her deathbed.",
"Movie F" : "In the last moments of World War II, a young German soldier \
fighting for survival finds a Nazi captain's uniform. Impersonating an officer,\
the man quickly takes on the monstrous identity of the perpetrators he is \
trying to escape from.",
"Movie G" : "The world at an end, a dying mother sends her young son on a \
quest to find the place that grants wishes.",
"Movie H" : "A musician helps a young singer and actress find fame, even as \
age and alcoholism send his own career into a downward spiral.",
"Movie I" : "Corporate analyst and single mom, Jen, tackles Christmas with \
a business-like approach until her uncle arrives with a handsome stranger in tow.",
"Movie J" : "Adapted from the bestselling novel by Madeleine St John, Ladies \
in Black is an alluring and tender-hearted comedy drama about the lives of a \
group of department store employees in 1959 Sydney."
}

# create a list with the movie descriptions
movies_desclist = list(movies_desc.values())

# create a list with the movie titles
movie_list = list(movies_desc.keys()) 

# initialize variable to hold maximum similarity value
movie_simi = 0.0

# define function that takes movie description as argument
def best_matchmovie(movie_desc):
    
    # tokenize Planet Hulk description
    movie_doc = nlp(movie_desc)
    
    # create empty list to store similarity values
    similarity_list = []
    
    # iterate through list with movie descriptions to check similarity 
    # with Planet Hulk desciption, and append to similarity_list
    for movie_similarity in movies_desclist:
        similarity_check = nlp(movie_similarity).similarity(movie_doc)
        similarity_list.append(similarity_check)

    # store the maximum similarity value into variable movie_sim    
    movie_sim = max(similarity_list)
    
    # for-loop to iterate through list of similarity scores to get index
    # of maximum similarity value 
    count = 0
    for i in similarity_list:
        # when similarity score is max value, store that index in 
        # variable 'max_index'
        if i == movie_sim:
            max_index = count
        count = count + 1
    
    # store the movie name with max_index and the maximum similarity 
    # score as a tuple in variable 'best_moviematch'
    best_moviematch = (movie_list[max_index], movie_sim)

    return(best_moviematch)

# call the function by passing Planet Hulk description as arguement
best_match = best_matchmovie(planethulk_desc)

# print the best match movie using f-string
print(f"\n The title of the movie that is most similar to Planet Hulk \
is: {best_match[0]} with similarity score of {best_match[1]}.\n")

# movie-recommender-system
ML based movie recommender system trained for 5000 different movies and recommendation through vector calculation. The movies are recommended based on the vectors and the cosine distance and the top 5 nearest movies (precisely the vectors) calculated through the cosine distance are then recommended based on that and the movie name and it's posters are then fetched through the TMDB api. You might have to fetch a completely new API key for it to work and display correct poster images on your system. 

Then after fetching the code you will have to modify a line of the code where it asks for the API key for the URL to work properly.

The app.py is the main file with an UI that can be run on a localhost server. Just download and run on any Virtual Environment like using PyCharm.

The data file that was used can found on the tmdb website or you can get it from the archive.zip file and extract it in your own system.
Moreover first run all the codes of movie-recommender-system.ipynb file and then you will make at the end few (.pkl) files which you will have to copy in the venv environment project folder.
Then you can run the entire file named app.py which will open a link in your web browser in your localhost server. 

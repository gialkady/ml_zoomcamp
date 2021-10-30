Description of the problem
-----------------------------


When i started to read the dataset, i had an error " 'utf-8' codec can't decode byte 0xd2 in position 7431: invalid continuation byte". I googled it and i found that it is "Unicode Decode Error". I solved by adding the encoding as follows:

df = pd.read_csv('https://raw.githubusercontent.com/gialkady/ml_zoomcamp/Homeworks/Midterm%20Project/Data/NetflixOriginals.csv', encoding='latin-1') 


I'll explore top rated movies and look for insights that could help a film production company understand what genre of film gets more rating.


Trends
Although this is a personal project,but if a film investor or a film production company needed go produce a movie and was concerened about what genre would attract more ratings which most times attract viewership ( more room for analysis), it would be easy to advice such a client to focus on the documentary genre. Because the data has proven that this genre records more ratings than every other genre. It is also important to noe that further analysis can still be carried out on what kind of documentary rakes in more ratings.

Limitations
There could be several limitations to this analysis, such as:

More data could be collected.
High ratings may not translate to high revenues.

Instructions on how to run the project
----------------------------------------

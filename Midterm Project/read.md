Description of the problem
-----------------------------
The problem is Predicting the ratings of Netflix movies based on several features including runtime, genre, langauge, year, week day and month. This can be useful in providing a service for film investor or a film production company needed go produce a movie and was concerened about what genre would attract more ratings which most times attract viewership ( more room for analysis), it would be easy to advice such a client to focus on the documentary genre. Because the data has proven that this genre records more ratings than every other genre. It is also important to noe that further analysis can still be carried out on what kind of documentary rakes in more ratings.
Also through EDA, I explored the top rated movies and looked for insights that could help a film production company understand what genre of film gets more rating.

Models used
---------------

I used three tree-based regression models to select the best model for the prediction process:

- ✅ Linear Regression
- ✅ RandomForest
- ✅ XGBoost

Finally, XGBOOST model wins with RMSE of 0.8720874293273928

Instructions on how to run the project
----------------------------------------

The project is not complicated so it follows the same procedures we learned in the course. 

Problems i faced 
--------------------

- When i started to read the dataset, i had an error " 'utf-8' codec can't decode byte 0xd2 in position 7431: invalid continuation byte". I googled it and i found that it is "Unicode Decode Error". I solved by adding the encoding as follows:

  df = pd.read_csv('https://raw.githubusercontent.com/gialkady/ml_zoomcamp/Homeworks/Midterm%20Project/Data/NetflixOriginals.csv', encoding='latin-1') 

- typeerror: ('expecting data to be a dmatrix object, got: ', <class 'numpy.ndarray'>) , this error appears when i loaded the xgboost model.

Limitations
---------------------

- Dataset is small so more data should be collected.
- High ratings may not translate to high revenues.




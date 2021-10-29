
When i started to read the dataset, i had an error " 'utf-8' codec can't decode byte 0xd2 in position 7431: invalid continuation byte". I googled it and i found that it is "Unicode Decode Error". I solved by adding the encoding as follows:
df = pd.read_csv('https://raw.githubusercontent.com/gialkady/ml_zoomcamp/Homeworks/Midterm%20Project/Data/NetflixOriginals.csv', encoding='latin-1') 

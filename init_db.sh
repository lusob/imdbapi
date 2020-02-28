#/bin/bash
wget -c https://datasets.imdbws.com/title.basics.tsv.gz https://datasets.imdbws.com/title.crew.tsv.gz https://datasets.imdbws.com/title.ratings.tsv.gz
gunzip -f title.basics.tsv.gz title.crew.tsv.gz title.ratings.tsv.gz 
echo "Importing dataset to sqlite..."; echo -e ".mode tabs\n.import title.basics.tsv imdb_title_basics\n.import title.crew.tsv imdb_title_crew\n.import title.ratings.tsv imdb_title_ratings" | sqlite3 ./instance/app.db 2> /dev/null; echo "Importation done!"

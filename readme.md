stocks.json contains all the stocks KNOW TO MAN!!!!  
use the http://127.0.0.1:8000/api/stockwatch/realdata/ endpoint to upload ALL STOCKS traded in usd into the db  
WARNING: this will take a while and may fail on slower computers(http default timeout is 100 seconds)  


to get this app running on your local machine:  
1. clone the repo  
2. cd into the repo  
3. set up a virtual environment  
4. run $pip install -r requirements.txt  
5. cd into ./server  
6. run python manage.py makemigrations  
7. run python manage.py migrate  
8. create a superuser with python manage.py createsuperuser  
9. run python manage.py runserver  
10. get a working finnhub api key and add it to a .env file  

11. on a second terminal cd into ./frontend  
12. run $yarn  
13. run $yarn start  

14. log into the superuser at http://localhost:3000/login  
15. go to the enpoints at http://localhost:3000/api/stockwatch/realdata/  
this will take a while to load all the stocks into the db  
(if it fails buy a better computer lol)  

you will be able to access user endpoints(for not) but to use any functions you must be logged in  

must use your own finnhub api key in the .env file in the server folder  

if you would like to use the app with just a few stocks you can go to http://  localhost:3000/api/stockwatch/tempdata  
it will only add apple, microsoft, amazon, google, tesla and netflix to the db  
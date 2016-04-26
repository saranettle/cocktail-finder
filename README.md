#Cocktail Finder

Hello, and welcome to my Github repo for my first Flask Application that uses a MySQL database. If you are learning Flask, please feel free to check out the files used to create this app.

The data that supplies that database comes from my cocktail web scraper. To learn more about it, visit my Github repo here:

https://github.com/saranettle/wikipedia-cocktail-scraper

The goal of this webapp is to create a list of different cocktails and dynamically generate pages that would give the ingredients for each drink. The idea of this application comes from the fact that I love cocktails, but I don't know very much about them. With this app, users can find drinks based on primary alcohol. In a way, it's like a virtual recipe book!

I used an SQL database to hold the cocktail information, and the flask application dynamically generates the page based on the database. For example, each drink's square is based on the primary alcohol. The class of each square is dynamically generated from the database, and then the css file gives each class a different color. With the database, we have greater ease with sorting the data. The menu allows a user to easily see drinks that use a particular alcohol as the primary ingredient.

Please note that the file you see here is used to deploy on Python Anywhere, so if you download this onto your computer it will not work. In the future I will add some more files for those who would like to use this application on their own server/database.

Use the app here:

http://snettle.pythonanywhere.com/

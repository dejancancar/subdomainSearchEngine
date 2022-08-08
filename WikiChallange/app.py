from flask import Flask
import wikipedia

app = Flask(__name__)

#for testing on local
app.config["SERVER_NAME"] = "localhost:5000"

#welcome page
@app.route('/')
def home():
   return '<h1>Welcome!</h1><p>Please enter a subdomain name to search for the relative page on wikipedia! Example: dogs.wiki-search.com</p>'

#dynamic subdomain 
@app.route('/', subdomain="<sdname>")
def search_home(sdname):
    #empty array to store result
    urls = []
    try:
        #append url to array if no exceptions are thrown
        page = wikipedia.page(sdname).url
        urls.append(page)
    except wikipedia.exceptions.DisambiguationError as e:
        #catch exceptions and iterate through them
        for link in e.options:
            try:
                #add url to the result array and pass on any new exceptions
                urls.append(wikipedia.page(link).url)
            except wikipedia.exceptions.DisambiguationError:
                pass
    return {"links" : urls}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
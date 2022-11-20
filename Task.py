from fastapi import FastAPI

app = FastAPI()
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
Voetbal = [
    {'id': 0,
     'Ploeg': 'Anderlecht',
     'Punten' :20,
     'Landskampioen' : 30,
     'Opgericht': 1908,
    {'id': 1,
     'Ploeg': 'Club Brugge',
     'Punten': 33,
     'Landskampioen':18,
     'Opgericht': 1995,
    {'id': 2,
     'Ploeg': 'KRC Genk',
     'Punten':46,
     'Landskampioen': 4,
     'Opgericht':1988,
     {'id': 3,
     'Ploeg': 'Antwerp',
     'Punten':35,
     'Landskampioen': 4,
     'Opgericht':1880,}
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(voetbal)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for ploeg in Voetbal:
        if ploeg['id']== id:
            results.append(ploeg)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()


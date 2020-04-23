from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, FOAF, RDFS, OWL
import pandas as pd

g = Graph()
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Load the CSV data as a pandas Dataframe.
csv_data = pd.read_csv("task1.csv")

# Here I deal with spaces (" ") in the data. I replace them with "_" so that URI's become valid.
csv_data = csv_data.replace(to_replace=" ", value="_", regex=True)

# Here I mark all missing/empty data as "unknown". This makes it easy to delete triples containing this later.
csv_data = csv_data.fillna("unknown")

# Loop through the CSV data, and then make RDF triples.
for index, row in csv_data.iterrows():
    # The names of the people act as subjects.
    subject = row['Name']
    # Create triples: e.g. "Cade_Tracey - age - 27"
    g.add((URIRef(ex + subject), URIRef(ex + "age"), Literal(row["Age"])))
    g.add((URIRef(ex + subject), URIRef(ex + "married"), URIRef(ex + row["Spouse"])))
    g.add((URIRef(ex + subject), URIRef(ex + "country"), URIRef(ex + row["Country"])))

    # If We want can add additional RDF/RDFS/OWL information e.g
    g.add((URIRef(ex + subject), RDF.type, FOAF.Person))

# I remove triples that I marked as unknown earlier.
g.remove((None, None, URIRef("http://example.org/unknown")))

# Clean printing of the graph.
print(g.serialize(format="turtle").decode())
from flask import Flask, request, jsonify, render_template
from rdflib import Graph
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# โหลดไฟล์ OWL
g = Graph()
g.parse("mytourism.owl", format="xml")

def search_ontology(keyword, lang="th"):
    query = f"""
    PREFIX tourism: <http://www.my_ontology.edu/mytourism#>
    SELECT ?subject ?name 
           (GROUP_CONCAT(DISTINCT ?motto; separator=", ") AS ?mottos) 
           (GROUP_CONCAT(DISTINCT ?flower; separator=", ") AS ?flowers) 
           (GROUP_CONCAT(DISTINCT ?tree; separator=", ") AS ?trees) 
           (GROUP_CONCAT(DISTINCT ?seal; separator=", ") AS ?seals) 
           (GROUP_CONCAT(DISTINCT ?traditionalName; separator=", ") AS ?traditionalNames) 
           ?latitude ?longitude
    WHERE {{
        ?subject tourism:hasNameOfProvince ?name .
        ?subject tourism:hasMotto ?motto .
        ?subject tourism:hasFlower ?flower .
        ?subject tourism:hasTree ?tree .
        ?subject tourism:hasSeal ?seal .
        ?subject tourism:hasTraditionalNameOfProvince ?traditionalName .
        ?subject tourism:hasLatitudeOfProvince ?latitude .
        ?subject tourism:hasLongitudeOfProvince ?longitude .
        FILTER (CONTAINS(LCASE(STR(?name)), LCASE("{keyword}")) 
            && LANG(?name) = "{lang}"
            && LANG(?motto) = "{lang}" 
            && LANG(?flower) = "{lang}"
            && LANG(?tree) = "{lang}"
            && LANG(?traditionalName) = "{lang}"
            && LANG(?seal) = "{lang}")
    }}
    GROUP BY ?subject ?name ?latitude ?longitude
    LIMIT 10
    """
    
    results = g.query(query)
    return [{
        "id": str(row.subject),
        "label": str(row.name),
        "mottos": str(row.mottos).split(", ") if row.mottos else [],
        "flowers": str(row.flowers).split(", ") if row.flowers else [],
        "trees": str(row.trees).split(", ") if row.trees else [],
        "seals": str(row.seals).split(", ") if row.seals else [],
        "traditionalNames": str(row.traditionalNames).split(", ") if row.traditionalNames else [],
        "latitude": str(row.latitude),
        "longitude": str(row.longitude),
    } for row in results]

@app.route("/")
def index():
    return render_template("index.html")  # ให้ Flask แสดงหน้าเว็บ

@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("q", "")
    lang = request.args.get("lang", "th")  # รับพารามิเตอร์ภาษา
    if not keyword:
        return jsonify([])
    
    results = search_ontology(keyword, lang)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
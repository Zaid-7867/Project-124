from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "id":1,
        "name":"Raju",
        "contact":"9987644456",
        "done":False
    },
    {
        "id":2,
        "name":"Rahul",
        "contact":"9876543222",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400)
    task={
        "id":tasks[-1]['id']+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "task":"added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

@app.route("/")
def helloWorld():
    return "Hello World"

if __name__ =="__main__":
    app.run(debug=True)
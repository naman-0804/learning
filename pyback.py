from flask import Flask, jsonify
import requests
app=Flask(__name__)
@app.route("/")
def home():
    return "Home"
@app.route("/getdata",methods=['GET'])
def getData():
    try:
        response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/postdata",methods=['POST'])
def postData():
    try:
        print("POST /postdata HIT")
        payLoad={"title":"foo","userId":1}
        response=requests.post("https://dummyjson.com/posts/add",json=payLoad)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/deletedata",methods=['DELETE'] )
def deleteData():
    try:
        print("DELETE /deletedata HIT")
        response=requests.delete("https://dummyjson.com/posts/1")
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/updatedata",methods=['PUT'] )
def updateData():
    try:
        print("PUT /updatedata HIT")
        payLoad={"title":"updated title"}
        response=requests.put("https://dummyjson.com/posts/1",json=payLoad)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=='__main__':
    app.run(debug=True)
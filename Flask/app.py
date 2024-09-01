from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

import pickle
model = pickle.load(open(r'C:/Users/zains/Flask/fdemand.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("homepage.html")

@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        p = request.form["hp"]
        if(p=='y'):
            p=1
        if(p=='n'):
            p=0
        q = request.form["pr"]
        if(q=='y'):
            q=1
        if(q=='n'):
            q=0
        r = request.form["op"]
        s = request.form["cu"]
        if(s=='0'):
            s=0
        if(s=='1'):
            s=1
        if(s=='2'):
            s=2
        if(s=='3'):
            s=3
        t = request.form["ccode"]
        u = request.form["rcode"]
        v = request.form["cat"]
        if(v=='Beverages'):
            v=0
        if(v=='Biryani'):
            v=1
        if(v=='Dessert'):
            v=2
        if(v=='Extras'):
            v=3
        if(v=='Fish'):
            v=4
        if(v=='Other Snacks'):
            v=5
        if(v=='Pasta'):
            v=6
        if(v=='Pizza'):
            v=7
        if(v=='Rice Bowl'):
            v=8
        if(v=='Salad'):
            v=9
        if(v=='Sandwich'):
            v=10
        if(v=='Seafood'):
            v=11
        if(v=='Soup'):
            v=12
        if(v=='Starters'):
            v=13
        
        w = [[int(t),int(u),float(r),int(v),int(s),int(q),int(p)]]
        output = model.predict(w)
        print(output)
        
        return render_template("index.html",y="The predicted number of orders is "+str(output[0]))
        #print(p)
        return render_template("index.html",y=p)

# @app.route('/user')
# def User():
#     return 'Hello user!!'
if __name__ == "__main__":
    app.run(debug=True)

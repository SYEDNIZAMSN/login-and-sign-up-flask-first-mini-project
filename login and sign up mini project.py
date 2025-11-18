from flask import Flask,Response,request,url_for,redirect,session
app=Flask(__name__)
app.secret_key="supersecret"
@app.route("/",methods=["GET","POST"])
def index():
   if request.method == "POST":
       log = request.form.get("log")
       session["log"] = log
       return redirect(url_for("auth"))
   return f'''
    <form method="POST">
    <h2>Nizam website</h2>
    <label for ="101">
    <input type="radio" name="log" id="101" value="login">login
    </label>
    <label for ="102">
    <input type="radio" name="log" id="102" value="signup">sign up
    </label>
    <input type="submit" name="submit">
    </form>
'''
@app.route("/auth",methods=["GET","POST"])
def auth():
    log = session.get("log")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if log=='login':
           if username =="Nizam" and password =="Nahida":
               session["username"] ="Nizam"
               return redirect(url_for("welcome"))
           else:
               return Response("Invalid username and/or password",)
        else:
            if username != "Nizam" and password != "Nahida":
                session["username"] = username
                return redirect(url_for("welcome"))
            else:
                return Response("user already exists", 401)

    return f'''
     <form method="POST">
     <h3>{log.capitalize()} form</h3>
     username <input type="text" name="username" placeholder="username"><br><br>
     password <input type="password" name="password" placeholder="password"><br><br>
     <input type="submit" name="{log.capitalize()}">
'''

@app.route("/welcome")
def welcome():
    if "username" in session:
     message=' '
     if session["log"] == "signup":
         message="sign up successfully"
     return f'''
      Wellcome {session["username"]}! <br> 
      <p>{message}</p>
      <br>
      <a href="{url_for('logout')}">Logout</a>
'''
    return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))


if __name__=="__main__":
    app.run(debug=True,port= 5002)
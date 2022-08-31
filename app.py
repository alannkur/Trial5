from flask import Flask,redirect,render_template,request,flash,Markup,session

app = Flask(__name__)
app.secret_key="srtyjhnbvgh"
logged=False


@app.route('/')
def home():
    return render_template("Home.html")

@app.route("/login")
def login():
    if 'userName' not in session:
        return render_template('Login.html')
    return redirect('/user')

@app.route("/user")
def user():
    if 'userName' in session:
        return render_template("Main.html")
    return redirect('/login')

@app.route('/authenticateUser',methods=['POST','GET'])
def authenticateUser():
    if request.method=='POST':
        if request.form['userName']=="itachi" or request.form['userName']=="Itachi" and request.form["password"]=="Sasuke" or request.form["password"]=="sasuke" :
            session['userName'] = request.form['userName']
            return redirect('/user')
        flash(Markup("<div class='alert alert-danger' role='alert'>Invalid Answer</div>"))
        #flash(Markup('<div class="alert alert-danger alert-dismissible fade show" role="alert">Invalid username/password <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('userName',None)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
'''
 <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
                  <div class="carousel-item active">
                      <img class="d-block w-100" src="{{ url_for('static',filename='images/948905.jpg') }}" alt="First slide">
                  </div>
                  <div class="carousel-item">
                      <img class="d-block w-100" src="{{ url_for('static',filename='images/612520.png') }}" alt="Second slide">
                  </div>
                  <div class="carousel-item">
                      <img class="d-block w-100" src="..." alt="Third slide">
                  </div>
              </div>
              <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only">Next</span>
              </a>
          </div>
'''

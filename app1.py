from flask import Flask,redirect,render_template,request,url_for
app=Flask(__name__)
books=[]
@app.route('/')
def index():
    return render_template('index1.html',books=books)
@app.route('/add_book',methods=['GET','POST'])
def add_book():
    if request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        books.append({'title':title,'author':author})
        return redirect(url_for('index'))
    return render_template('add_book.html')
if __name__=='__main__':
    app.run(debug=True)
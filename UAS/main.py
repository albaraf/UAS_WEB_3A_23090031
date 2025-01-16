from flask import Flask, render_template, request, redirect, url_for, flash
from DB_Operations import fetch_all_items, insert_item, fetch_item_by_id, update_item, delete_item

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    items = fetch_all_items()
    return render_template('index.html', items=items)

@app.route('/produk')
def produk():
    items = fetch_all_items()
    return render_template('produk.html', items=items)

@app.route('/add_item', methods=["POST" , "GET"])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        #insert item to db
        insert_item(name,description)
        flash('Item Added Successfully!')
        return redirect(url_for('produk'))
    return render_template('add.html')

@app.route('/edit/<id>', methods = ["GET","POST"])
def edit_item(id):
    item = fetch_item_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        #update item
        update_item(id,name,description)
        flash('Item Updated Successfully!')
        return redirect(url_for('produk'))
    return render_template('edit.html', item=item)

@app.route('/delete/<id>', methods = ["GET","POST"])
def delete_item_route(id):
    delete_item(id)
    flash('Item Deleted Successfully!')
    return redirect(url_for('produk'))

if __name__ == '__main__':
    app.run(debug=True)
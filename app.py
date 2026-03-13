from flask import Flask, render_template, request, redirect, url_for
from models import Business # Importing your OOP class

app = Flask(__name__)

# This list will act as our STACK (Requirement)
business_stack = []

@app.route('/')
def home():
    # We pass the stack to the HTML. 
    # To show 'Recently Added', we reverse it: [::-1]
    recent_businesses = business_stack[::-1]
    return render_template('index.html', businesses=recent_businesses)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        
        # Requirement: Instantiate the Class (OOP)
        new_biz = Business(name, category)
        
        # Requirement: Implement Stack (LIFO) behavior
        business_stack.insert(0, new_biz)
        
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
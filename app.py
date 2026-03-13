from flask import Flask, render_template, request, redirect, url_for, flash
from models import Business

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

# This is our Stack (LIFO) to store businesses
business_stack = []
# Home route to display all businesses in the stack
# @app.route('/')
def home():
    return render_template('index.html', businesses=business_stack)
# Route to handle adding new businesses (POST) or showing the form (GET)
@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        # Logic to extract data and update the LIFO stack
        # 1. Grab data from the form
        name = request.form.get('name')
        category = request.form.get('category')
        
        # 2. Create the business object (OOP)
        new_biz = Business(name, category)
        
        # 3. Add to the top of our stack (LIFO behavior)
        business_stack.insert(0, new_biz)
        
        # 4. Show a success message
        flash(f"Success! {name} has been added to the directory.")
        
        return redirect(url_for('home'))
    
    # If it's a GET request, just show the form
    return render_template('add.html')
@app.route('/clear', methods=['POST'])
def clear_stack():
    business_stack.clear()
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    """Render the main page of the Mutabrine website."""
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """Handle the contact form submission."""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Simple validation
        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # In a real application, you would:
        # 1. Store this in a database
        # 2. Send an email notification
        # 3. Handle more robust validation
        
        # Log form submission for debugging
        app.logger.info(f"Form submission received from {name} ({email})")
        
        # Success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('index') + '#contact')
    
    except Exception as e:
        app.logger.error(f"Error processing form: {str(e)}")
        flash('An error occurred while processing your request. Please try again later.', 'error')
        return redirect(url_for('index') + '#contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

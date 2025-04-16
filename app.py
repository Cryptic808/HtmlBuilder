import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for, abort

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Dictionary of service details
SERVICES = {
    'construction': {
        'title': 'Construction Services',
        'description': 'Expert residential and commercial construction with a focus on quality and timeliness.',
        'image': 'construction.jpg',
        'features': [
            'Custom residential builds',
            'Commercial construction',
            'Renovations and remodeling',
            'Project management services',
            'Architectural consultation'
        ]
    },
    'branding': {
        'title': 'Branding & Design',
        'description': 'Creative branding solutions to establish and enhance your business identity.',
        'image': 'branding.jpg',
        'features': [
            'Logo design',
            'Brand identity packages',
            'Marketing materials',
            'Corporate style guides',
            'Rebranding services'
        ]
    },
    'tshirt-printing': {
        'title': 'T-Shirt Printing',
        'description': 'High-quality custom t-shirt printing for events, businesses, and promotional needs.',
        'image': 'tshirts.jpg',
        'features': [
            'Screen printing',
            'Digital printing',
            'Custom designs',
            'Bulk orders',
            'Quick turnaround options'
        ]
    },
    '3d-signage': {
        'title': '3D Signage',
        'description': 'Eye-catching dimensional signage that makes your business stand out.',
        'image': 'signage.jpg',
        'features': [
            'Custom 3D letters and logos',
            'Illuminated signage',
            'Architectural signage',
            'Reception area branding',
            'Exterior building signs'
        ]
    },
    'printing': {
        'title': 'Photocopying & Printing',
        'description': 'Professional printing and copying services for all your document needs.',
        'image': 'printing.jpg',
        'features': [
            'High-volume photocopying',
            'Color and black & white printing',
            'Document binding',
            'Lamination services',
            'Digital file preparation'
        ]
    },
    'metal-fabrication': {
        'title': 'Metal Fabrication',
        'description': 'Custom metal fabrication services for construction, signage, and architectural elements.',
        'image': 'fabrication.jpg',
        'features': [
            'Steel fabrication',
            'Aluminum works',
            'Welding services',
            'Custom metalwork',
            'Architectural metal elements'
        ]
    },
    'large-format': {
        'title': 'Large Format Printing',
        'description': 'High-impact large format prints for advertising, events, and displays.',
        'image': 'large-format.jpg',
        'features': [
            'Banners and flags',
            'Posters and billboards',
            'Exhibition graphics',
            'Vehicle wraps',
            'Window graphics'
        ]
    },
    'office-branding': {
        'title': 'Office Branding',
        'description': 'Transform your workspace with professional office branding and environmental graphics.',
        'image': 'office.jpg',
        'features': [
            'Wall graphics and murals',
            'Office signage',
            'Reception branding',
            'Wayfinding systems',
            'Corporate environments'
        ]
    },
    'it-services': {
        'title': 'IT Services',
        'description': 'Professional IT services and solutions to support your business technology needs.',
        'image': 'it-services.jpg',
        'features': [
            'Network setup and maintenance',
            'Cybersecurity solutions',
            'Cloud computing services',
            'Software development',
            'IT consulting and support'
        ]
    }
}

@app.route('/')
def index():
    """Render the main page of the Mutabtrine Investments Ltd website."""
    return render_template('index.html')

@app.route('/services/<service_name>')
def service_detail(service_name):
    """Render the service detail page."""
    if service_name not in SERVICES:
        abort(404)
    
    service = SERVICES[service_name]
    return render_template('service.html', service=service, service_name=service_name, services=SERVICES)

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
        flash('Thank you for your inquiry! Our team will contact you within 24 hours.', 'success')
        return redirect(url_for('index') + '#contact')
    
    except Exception as e:
        app.logger.error(f"Error processing form: {str(e)}")
        flash('An error occurred while processing your request. Please try again later.', 'error')
        return redirect(url_for('index') + '#contact')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

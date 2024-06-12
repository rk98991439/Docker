from flask import Flask, request, render_template_string, make_response
import qrcode
import io
import base64

app = Flask(__name__)

# HTML template for rendering the form and QR code
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>
</head>
<body>
    <h1>QR Code Generator</h1>
    <form method="post" action="/">
        <label for="value">Enter Text or URL:</label>
        <input type="text" id="value" name="value" required>
        <button type="submit">Generate QR Code</button>
    </form>
    {% if qr_code %}
    <h2>Generated QR Code:</h2>
    <img src="data:image/png;base64,{{ qr_code }}">
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def generate_qr():
    qr_code = None
    if request.method == 'POST':
        value = request.form.get('value')
        
        if value:
            # Generate the QR code
            img = qrcode.make(value)
            
            # Save the QR code to a buffer
            buffer = io.BytesIO()
            img.save(buffer)
            buffer.seek(0)
            
            # Encode the image to base64
            qr_code = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Render the HTML template with the QR code
    return render_template_string(HTML_TEMPLATE, qr_code=qr_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


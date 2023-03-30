from flask import Flask, request, render_template
from jinja2 import Environment, FileSystemLoader
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    pdf_file = request.files['pdf-file']
    pdf_reader = PyPDF2.PdfReader(pdf_file)    
    page = pdf_reader.pages[0]
    text = page.extract_text()
    name = email = phone = None
    lines = text.split('\n')
    for i in range(0,len(lines)):
          val = lines[i].replace(" ", "")
          if 'Name' in val:
               
               name = val.replace("Name:", "")
          if 'email' in val:
               email = lines[i+1].replace("email", "")
          if 'phone' in val:
               phone = val.replace("phone:", "")
    return render_template('result.html', name=name, email=email, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
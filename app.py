from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
# pass text(which is query) to search function    

    your_list = result('text')
# get result list from search function when the received flag is on
    if received == 1
#print lists on results.html
        return render_template('results.html', your_list = your_list)
    else
#guide to 404 not found page
        return render_template('page_not_found.html')


if __name__=='__main__':
    app.run(debug=True)
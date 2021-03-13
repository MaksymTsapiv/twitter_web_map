from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from os import getcwd, path
from twitter_web_map import main

app = Flask(__name__)
REFRESH_ICON = '<a href=""><i class="fa fa-refresh" style="font-size:36px; position: fixed; right: auto; z-index: 100000; margin-left: 95%; margin-top: 2%"></i></a>'


@app.route('/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('input.html')
    if request.method == 'POST':
        form_data = request.form
        main(form_data.get("username"))
        # update("D:\\PythonProjects\\lab_3\\Task_3\\templates\\index.html")
        update(path.join("templates", "index.html"))
        return render_template('index.html')





def update(filename):
    with open(filename, encoding='utf8') as fp:
        soup = BeautifulSoup(fp, "html.parser")
    extraSoup = BeautifulSoup(REFRESH_ICON)
    tag = soup.find("body")
    tag.insert(1, extraSoup)
    with open(filename, "w", encoding='utf8') as fp:
        fp.write(soup.prettify())

if __name__ == '__main__':
    app.run(debug=True)
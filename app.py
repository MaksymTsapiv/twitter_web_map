from flask import Flask, render_template, request, render_template_string
from bs4 import BeautifulSoup
from twitter_web_map import main

app = Flask(__name__)
REFRESH_ICON = '<a href=""><i class="fa fa-refresh" style="font-size:36px; position: fixed; right: auto; z-index: 100000; margin-left: 95%; margin-top: 2%"></i></a>'


@app.route('/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('input.html')
    if request.method == 'POST':
        form_data = request.form
        map_page = main(form_data.get("username"))
        map_template = update(map_page)
        return render_template_string(map_template)


def update(file):

    soup = BeautifulSoup(file, "html.parser")
    extraSoup = BeautifulSoup(REFRESH_ICON)
    tag = soup.find("body")
    tag.insert(1, extraSoup)
    return soup.prettify()


if __name__ == '__main__':
    app.run()

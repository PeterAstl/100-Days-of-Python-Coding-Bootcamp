from flask import Flask

app = Flask(__name__)



@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return ('<h1 style = "text-align: cemter"> Hello, World!</h1>'
            '<p>This is an example HTML page</p>'
            '<img src = "https://gifuu.agency/wp-content/uploads/2020/12/GIFuu-Agentur-GIF-Marketing-Maskottchen-Olaf.gif" width=400>'
            '<u><em><b>Bye</b></em></u>')

@app.route("/username/<name>")
def hello_user(name):
    return f"Hello, {name}!"



if __name__ == '__main__':
    app.run(debug=True)


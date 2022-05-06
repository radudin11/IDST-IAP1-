from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://cdn-prd.content.metamorphosis.com/wp-content/uploads/sites/6/2021/10/paula-poundstone-funny-cat-quote.jpg",
    "https://trendfool.com/wp-content/uploads/2022/01/1641122243_maxresdefault-768x432.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUxVg-8ss7avs4R8uZfAdJDzR1bvuQiuZzgA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRet8QmxsYd1myXC5jCa8Xt-WHPIBAnDEftow&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8DBJQ2C_stTO3upANwx65F8UiDlltHYcrrQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3clEm_PGjSNoaLpn9tj1JAFDQH7ugxakh7Q&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0j2lMbKAWfkFRcbK0VYPdkePvNGSh-qwEpA&usqp=CAU"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
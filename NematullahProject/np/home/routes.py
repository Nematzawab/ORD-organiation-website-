from flask import Blueprint, render_template, url_for
from np import Publications, Regions

home_b = Blueprint("home", __name__)


@home_b.route("/")
@home_b.route("/home")
def home():
    data = Publications.query.limit(4).all()
    data2 = Regions.query.all()
    return render_template("home/home.html", title="Home", data=data, data2=data2)


def increase(c):
    c += 1
    return c

@home_b.route("/regions/<int:rid>")
def regions(rid):
    data = Regions.query.get(rid)
    x = 1
    data2 = []
    for i in data.regions.split(','):
        data2.append((x, i))
        x += 1
    return render_template("home/regions.html", title=f"Regions {data.name}",
                           data=data, data2=data2)




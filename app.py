from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [
  {
    "name": "Python",
    "commits": "3000",
    "uneven": "Popular for data science"
  },
  {
    "name": "JavaScript",
    "commits": "4200",
    "uneven": "Used for web development"
  },
  {
    "name": "SQL",
    "commits": "1500",
    "uneven": "Great for databases"
  }
]

# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "name",
    "title": "Language",
    "sortable": True,
  },
  {
    "field": "commits",
    "title": "GitHub Commits",
    "sortable": True,
  },
  {
    "field": "uneven",
    "title": "Description",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
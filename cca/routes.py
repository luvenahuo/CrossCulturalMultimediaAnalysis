from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify
from cca import app, db
from cca.models import Commits, Images, Affinity, Tags
import json

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template("home.html")

@app.route('/selectevent', methods = ['GET', 'POST'])
def selectevent():
  if request.method == "POST":
    event = request.form['events']
    return redirect("/index")
  return redirect("/index")

@app.route('/index', methods=['GET'])
def index():
    date_format = '%Y-%m-%d %H:%M:%S'
    commits = Commits.query.order_by(Commits.video_date).all()
    d = [c.video_date.strftime("%Y-%m-%d") for c in commits]

    title = 'CCA'
    dates = {'min':d[0], 'max':d[-1]}

    commit_data = [{"name": "United States", "data":[]}, 
         #{"name": "Common", "data":[]}, 
         {"name": "China", "data":[]}]

    commits = db.session.query(Commits, Affinity).outerjoin(Affinity, Affinity.id == Commits.affinity_id).all()

    for c in commits:
        if c[1].name == 'United States':
            tags = Tags.query.filter_by(commit_id = c[0].id).all()
            data = {
                "date": c[0].video_date.strftime(date_format),
                "details":{
                    "name": c[0].index, "message": c[0].message,
                    "tags": [t.tag for t in tags]
                }}
            commit_data[0]["data"].append(data)

            # common = c.Commits.get_common().all()
            # for a in common:
            #     print(a.id, a.common.all()[0].id)
            #     commit_data[1]["data"].append({
            #         "date": a.common.all()[0].video_date.strftime(date_format),
            #         "details":{
            #             "isCommon": 1, 
            #             "name": a.common.all()[0].index,
            #             "common": a.index,
            #             "message": {
            #                 "US": a.common.all()[0].message,
            #                 "China": a.message
            #             }
            #         }
            #     })

        elif c[1].name == 'China':
            commit_data[1]["data"].append({
                "date": c[0].video_date.strftime("%Y-%m-%d %H:%M:%S"),
                "details":{
                    "name": c[0].index, "message": c[0].message, 
                }})
    #print(commit_data)
    return render_template('index.html', title=title, dates=dates, commits=commit_data)

@app.route('/img/<i>', methods=['POST'])
def img(i):
    commit = Commits.query.filter_by(index = i).first()
    imgs = Images.query.filter_by(commit_id = commit.id).all()
    paths = [i.path for i in imgs]

    return jsonify(paths)
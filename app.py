from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from helper import generate_roadmap, analyse

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/essayRoadmaps', methods=['GET', 'POST'])
def essay_roadmaps():
    if request.method == 'POST':
        topic = request.form['topic']
        if not topic:
            flash("Please provide a topic", "error")
            return redirect(url_for('essay_roadmaps'))
        roadmap = generate_roadmap(topic)
        if os.path.exists('roadmaps.json'):
            with open('roadmaps.json', 'r') as file:
                roadmaps = json.load(file)
        else:
            roadmaps = []
        roadmaps.append({"topic":topic, "roadmap": roadmap})
        with open('roadmaps.json', 'w') as file:
            json.dump(roadmaps, file)
        return redirect(url_for('essay_roadmaps'))

    if os.path.exists('roadmaps.json'):
        with open('roadmaps.json', 'r') as file:
            roadmaps = json.load(file)
    else:
        roadmaps = []
    return render_template('essayRoadmaps.html', roadmaps=roadmaps)

@app.route('/viewRoadmap/<topic>')
def view_roadmap(topic):
    if os.path.exists('roadmaps.json'):
        with open('roadmaps.json', 'r') as file:
            roadmaps = json.load(file)
        roadmap = [rm["roadmap"] for rm in roadmaps if (rm['topic'] == topic)][0]
    else:
        roadmap = None

    return render_template('viewRoadmap.html', topic=topic, roadmap=roadmap)


@app.route('/analyseEssay', methods=['GET', 'POST'])
def analyse_essay():
    if request.method == 'POST':
        essay = request.form['essay']
        analysis_result = analyse(essay)
        return render_template('analyseEssay.html', result=analysis_result)
    return render_template('analyseEssay.html')

if __name__ == '__main__':
    app.run(debug=True)

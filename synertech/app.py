from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.synertech

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/comment', methods=['POST'])
def write_comment():
    subject_receive = request.form['subject_give']
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']

    doc = {
        'subject': subject_receive,
        'title': title_receive,
        'comment': comment_receive
    }
    db.users.insert_one(doc)

    return jsonify({'msg': '저장이 되었습니다.!'})


@app.route('/comment', methods=['GET'])
def read_comments():
    comments = list(db.users.find({}, {'_id': False}))
    return jsonify({'all_comments': comments})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
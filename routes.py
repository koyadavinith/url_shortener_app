from url import app,db
from flask import render_template,url_for,redirect, request
from url.models import urls
from validators import url

@app.route('/<short_url>')
def redirect_to_url(short_url):
    link = urls.query.filter_by(short_url = short_url.split('/')[-1]).first_or_404()
    return redirect(link.orginal_url)


@app.route('/')
@app.route('/home',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        orginal_url = request.form.get('orginal_url')
        if not url(orginal_url):
            return render_template('index.html', error_message='Please enter a valid URL.')
        url1 = urls(orginal_url = orginal_url)
        db.session.add(url1)
        db.session.commit()
        short_url = url1.short_url
        whole_url = url_for('redirect_to_url', short_url=short_url,_external = True)
        return render_template('index.html', orginal_url = orginal_url,whole_url = whole_url)
    else:
        return render_template('index.html')

@app.route('/history')
def history():
    links = urls.query.all()
    return render_template('history.html',links = links)


    



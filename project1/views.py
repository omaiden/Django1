from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
import datetime
import MySQLdb

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	#t = Template("<html><body>It is now {{current_date}}.</body></html>")
	html = render_to_response('current_datetime.html', {'current_date': now})#t.render(Context({'current_date': now}))
	#html = t.render({'current_date': now})
	return HttpResponse(html)
	
def hours_ahead(request, offset):
	#offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def book_list(request):
	db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
	cursor = db.cursor()
	cursor.execute('SELECT name FROM books ORDER BY name')
	names = [row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html', {'names': names})
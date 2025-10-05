from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		'title': 'Home',
		'features': [
			'Django',
			'Templates',
			'Static Files'
		]
	}
	return render(request, 'home.html', context)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

announcements = [
    {'id': 1, 'title': 'New Website','content': 'We are excited to announce the launch of our new Announcement Website!'},
    {'id': 2, 'title': 'Maintenance of Our Website', 'content': 'Our website maintenance schedule has been confirmed. Please be advised that the site will undergo scheduled maintenance this Saturday'},
    {'id': 3, 'title': 'Event', 'content': 'These events include workshops, student-led discussions, and online webinars designed to provide'},
]

def announcement_list(request):
	return render(request, 'announcement_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a["id"] == id), None)
    return render(request, 'announcement_detail.html', {'announcement': announcement})
from django.shortcuts import render
from finalproject import settings
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def login(req):
	return render(req,'myapp/eegstart.html')
def choose(req):
	if req.method=="POST":
		#try:
		file=req.FILES['filewav']
		
		path='static/filewav'
		import mne
		data=mne.io.read_raw_edf(path,preload=True)
		fig = Figure()
		canvas = FigureCanvas(fig)
		ax = fig.add_subplot(111)
		data.plot(duration=5)
		response=django.http.HttpResponse(content_type='image/png')
		canvas.print_png(response)
		return response
		

		    
		
	return render(req,'myapp/choose.html')

def mplimage(request):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data.plot(duration=5)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


# Create your views here.

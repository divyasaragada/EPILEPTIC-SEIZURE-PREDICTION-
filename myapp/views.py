from django.shortcuts import render,HttpResponse
from finalproject import settings
import matplotlib.pyplot as plt
import matplotlib
from .utils import get_plot


def login(req):
	return render(req,'myapp/mylogin.html')
def start(req):
	return render(req,'myapp/eegstart.html')
def choose(req):
	if req.method=="POST":
		#try:
		file=req.FILES['filewav']
		with open('myapp/static/upload/'+'myfile', 'wb+') as destination:
			for chunk in file.chunks():
				destination.write(chunk)  
		
		import mne
		data=mne.io.read_raw_edf(file.temporary_file_path(),preload=True)
		#data=mne.io.read_raw_edf('myapp/static/upload/myfile',preload=True)
		#data.plot(duration=50)
		#plt.savefig('myapp/static/upload/foo.png')

		chart=get_plot(data)
		return render(req,'myapp/choose.html',{'chart':chart,'data1':data})

		
	return render(req,'myapp/choose.html')




# Create your views here.

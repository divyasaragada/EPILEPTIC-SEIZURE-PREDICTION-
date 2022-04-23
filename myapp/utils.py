import matplotlib.pyplot as plt
import base64
from io import BytesIO
import mne
def get_graph():
	buffer=BytesIO()
	plt.savefig(buffer,format='png')
	buffer.seek(0)
	image_png=buffer.getvalue()
	graph=base64.b64encode(image_png)
	graph=graph.decode('utf-8')
	buffer.close()
	return graph
def read(file):
	#data=mne.io.read_raw_edf('C:/Users/DIVYA/DESKTOP/MAJOR PROJECT/finalproject/'+file.name,preload=True)
	import mne
	data=mne.io.read_raw_edf(file.name,preload=True)
	return data


def get_plot(data):
	
	#data=mne.io.read_raw_edf('C:\\Users\\DIVYA\\Desktop\\MAJOR PROJECT\\FINALDATASET\\chb03_01.edf',preload=True)
	#data.plot(duration=50)
	#or
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=5)
	#plt.switch_backend('AGG')
	#plt.title('sales of items')
	#plt.plot(x,y)
	# plt.xticks(rotation=45)
	# plt.xlabel('item')
	# plt.ylabel('price')
	# plt.tight_layout()
	graph=get_graph()
	return graph

def get_beta_plot(data):
	low_freq, high_freq = 12.0, 30.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph

def get_alpha_plot(data):
	low_freq, high_freq = 8.0, 12.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph

def get_theta_plot(data):
	low_freq, high_freq = 4.0, 8.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23,scalings={"eeg":75e-6}, title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph


def get_delta_plot(data):
	low_freq, high_freq = 0.5, 4.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph






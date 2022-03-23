import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
	buffer=BytesIO()
	plt.savefig(buffer,format='png')
	buffer.seek(0)
	image_png=buffer.getvalue()
	graph=base64.b64encode(image_png)
	graph=graph.decode('utf-8')
	buffer.close()
	return graph

def get_plot(data):
	import mne
	#data=mne.io.read_raw_edf('C:\\Users\\DIVYA\\Desktop\\MAJOR PROJECT\\FINALDATASET\\chb03_01.edf',preload=True)
	data.plot(duration=50)
	
	#plt.switch_backend('AGG')
	#plt.title('sales of items')
	#plt.plot(x,y)
	# plt.xticks(rotation=45)
	# plt.xlabel('item')
	# plt.ylabel('price')
	# plt.tight_layout()
	graph=get_graph()
	return graph
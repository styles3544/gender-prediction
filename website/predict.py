from flask import Blueprint, render_template, request, url_for
from fastai.vision.widgets import *
from fastbook import *
import pathlib


predict = Blueprint('predict', __name__)

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def predict_label(im_path):
	learn_inf = load_learner('website\static\export.pkl')
	p,_,probs = learn_inf.predict(im_path)
	print(str(p), probs[1].item())
	return (str(p), probs)

@predict.route('/predict/', methods = ['GET', 'POST'])
def prediction():
	if request.method == 'POST':
		img = request.files['file']

		img_path = "website/static/images/" + img.filename	
		# img.save(img_path)
		img.save(f'website/static/images/{img.filename}')

		prdct = predict_label(img_path)
		boy = round(prdct[1][0].item(), 3)
		girl = round(prdct[1][1].item(), 3)
		return render_template("predict.html", p=prdct[0], filename = img.filename, prob1= boy, prob2=girl )
	
	else:
		return render_template("predict.html")


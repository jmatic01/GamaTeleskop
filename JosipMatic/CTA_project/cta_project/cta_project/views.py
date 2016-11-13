import datetime
from pyramid.response import Response
from pyramid.response import FileResponse
from paste.httpserver import serve
import json
import csv
from bson.json_util import dumps
def my_view(request):
    request.db.authenticate('bartolovic','bartolovic')
    return {'project':'cta_project'}
def csvview(request):
	response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
	return response
def wea_ws(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gust(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_see(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dust(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzd(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttemp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttopright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerr(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1t(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globr(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtw(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_ac(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrob(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crate(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rack(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devaz(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzd(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcx(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_stars(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_bright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloud(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skyt(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psf(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfn(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_size(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_b(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_l(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_ped(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_ped(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gusty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dusty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottlefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerry(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1ty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2ty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globry(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astroby(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_cratey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_racky(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skyty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfny(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_by(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_ly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response



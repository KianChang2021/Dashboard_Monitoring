from logging import debug
from posixpath import basename
#from urllib import request
from flask import Flask,jsonify,request
from flask_cors import CORS
from waitress import serve
import Connect_Monitoring_DB,send_gmail,logger
from datetime import datetime,date
import time,json,calendar
app = Flask(__name__)
CORS(app)

@app.route('/ma_data', methods=['POST'])
def ma_status():
    try:
        serial_number = request.json['serial_number']
        ip = request.json['ip']
        branch = request.json['branch']
        Connect_Monitoring_DB.add_Result_MA_Live([str(serial_number),ip],str(branch))
        response_data = [{'Status':'Success'}]
    except Exception as ex:
        response_data = [{'Status':'Fail'}] 
        data = "Error MA_data API : "+ str(ex)
        logger.api_server_log(data)

    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/hd_data', methods=['POST'])
def hd_data():
    try:
        serial_number = request.json['serial_number']
        timestamp = request.json['timestamp']
        branch = request.json['branch']
        Connect_Monitoring_DB.add_live_data_monitoring([serial_number,timestamp],branch)
        response_data = [{'Status':'Success'}]
        
    except Exception as ex:
        response_data = [{'Status':'Fail'}] 
        data = "Error HD_data API : "+ str(ex)
        logger.api_server_log(data)
    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


@app.route('/network', methods=['POST'])
def network():
    try:
        new_data = request.json['branch']
        Connect_Monitoring_DB.add_network_status(str(new_data))
        response_data = [{'Status':'Success'}]
    except Exception as ex:
        response_data = [{'Status':'Fail'}] 
        data = "Error Network API : "+ str(ex)
        logger.api_server_log(data)

    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/MA_Status/', methods=['GET'])
def Ma_live_Result():
    
    nas_data =""
    response_data = []
    Branch = Connect_Monitoring_DB.get_branch()
    try:
        for y in Branch:
            data_list = []
            data_list_1 = []
            now = datetime.now()
            # Get Internet Check
            Nas = Connect_Monitoring_DB.get_network_status(y.branch_name)
            if Nas != []:
                dt_object = datetime.fromtimestamp(int(Nas[0].createdtime))
                new_data = now-dt_object
                days, hours, minutes = new_data.days, new_data.seconds // 3600, new_data.seconds // 60 % 60
                curr_date = date.today()
                if str(calendar.day_name[curr_date.weekday()]) != "Sunday" and now.hour <= 23 and now.hour >= 6:
                    if now.hour == 6 and now.minute <= 15:
                        if days == 0 and hours >= 0 and minutes >=8:
                            nas_data = 'fail'
                            send_gmail.send_mail_internet(str(y.branch_name))
                        else:
                            nas_data = 'pass'
                    else:
                        nas_data = 'pass'
                else:
                    nas_data = 'pass'
            else:
                nas_data = 'fail'
                send_gmail.send_mail_internet(str(y.branch_name))
            #End Get Internet Check
            
            # Get Ma Status Check
            data = Connect_Monitoring_DB.get_Ma_Status(y.branch_name)
            for x in data:
                dt_object = datetime.fromtimestamp(int(x[1]))
                new_data = now-dt_object
                days, hours, minutes = new_data.days, new_data.seconds // 3600, new_data.seconds // 60 % 60
                if days == 0:
                    if hours == 0:
                        if minutes<=30:
                            data_list.append(x[0])
            # End Get Ma Status Check

            # Get Live Data status
            data_1 = Connect_Monitoring_DB.get_live_data_status(y.branch_name)
            for x in data_1:
                dt_object = datetime.fromtimestamp(int(x[1]))
                new_data = now-dt_object
                days, hours, minutes = new_data.days, new_data.seconds // 3600, new_data.seconds // 60 % 60
                if days == 0:
                    if hours == 0:
                        if minutes <=30:
                            data_list_1.append(x[0])
            # End Get Live Data status

            response_data += [{'Branch':y.branch_name,'MA':data_list,'Live_Data':data_list_1,'Network':nas_data}]
        response = jsonify(response_data)
    except Exception as e:
        Error = "Error : " + str(e)
        response = jsonify({'result': Error})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8085)
    #app.run(host="0.0.0.0", port=8085,debug=True)
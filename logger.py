import datetime,logging
now = datetime.datetime.now()
now_1 = now.strftime("%d_%m_%Y")

def api_server_log(data):
    name = "./logs/"+now_1 +"_API.log"
    logging.basicConfig(filename=name, format='%(asctime)s %(message)s', filemode='a')
    logger=logging.getLogger('/logs')  
    try:
        logger.error(str(data))
    except Exception as ex:
        data = "Error occurs in ma_log" +str(ex)
        logger.error(str(data))

def main_log(data):
    name = "./logs/"+now_1 +"_Monitoring.log"
    logging.basicConfig(filename=name, format='%(asctime)s %(message)s', filemode='a')
    logger=logging.getLogger('/logs')  
    try:
        logger.error(str(data))
    except Exception as ex:
        data = "Error occurs in ma_log" +str(ex)
        logger.error(str(data))

def ma_log(data):
    name = "./logs_MA/"+now_1 +"_Monitoring.log"
    logging.basicConfig(filename=name, format='%(asctime)s %(message)s', filemode='a')
    logger=logging.getLogger('/logs_MA')  
    try:
        test = "test1"
        logger.error(str(data))
    except Exception as ex:
        data = "Error occurs in ma_log" +str(ex)
        logger.error(str(data))


if __name__ == "__main__":
    a="test"
    ma_log(a)
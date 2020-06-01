import time
import sys
import iothub_client
import os
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult, IoTHubError
import numpy as np

CONNECTION_STRING = "HostName=your_hostname;DeviceId=device1;SharedAccessKey=access_key"
PROTOCOL = IoTHubTransportProvider.HTTP 


PATHTOFILE = "/home/pi/day5_iot_azure/azure-iot-sdk-python/device/samples/test.txt"
FILENAME = "test.txt"
path = "/home/pi/day5_iot_azure/azure-iot-sdk-python/device/samples/files"

def blob_upload_conf_callback(result, user_context):
    if str(result) == 'OK':
        print ( "...file uploaded successfully." )
    else:
        print ( "...file upload callback returned: " + str(result) )

def iothub_file_upload_sample_run():
    try:
        print ( "IoT Hub file upload sample, press Ctrl-C to exit" )
        client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
#        for i in np.arange(0,4):
 #           print(i)
        for r,d,f in os.walk(path):
           for file in f:
               print(os.path.join(r,file))
	       PATHTOFILE =os.path.join(r,file)
	       FILENAME=os.path.basename(file)
               f = open(PATHTOFILE, "r")
	       content = f.read()

				# Please note that because of the way the C SDK wrapper is written, file upload is limited to text files.
				# The last parameter of this method call is user_context.
				# it will be passed to the blob_upload_conf_callback so that calls and callbacks can be matched together
				# in case there are multiple simultaneous uploads
	       client.upload_blob_async(FILENAME, content, len(content), blob_upload_conf_callback, 0)

	       print ( "" )
	       print ( "File upload initiated..." )

#	       while True:
#	           time.sleep(30)

    except IoTHubError as iothub_error:
        print ( "Unexpected error %s from IoTHub" % iothub_error )
        return
    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )
    except:
        print ( "generic error" )

if __name__ == '__main__':
    print ( "Simulating a file upload using the Azure IoT Hub Device SDK for Python" )
    print ( "    Protocol %s" % PROTOCOL )
    print ( "    Connection string=%s" % CONNECTION_STRING )

    iothub_file_upload_sample_run()

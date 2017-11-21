# coding=utf-8

import time
import random

from bfgateway_pb2 import *
from bfkv_pb2 import *
from google.protobuf.any_pb2 import *

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_PING_TYPE = BfPingData().DESCRIPTOR

def getClientId(context):
    clientId = ""
    mt =  context.invocation_metadata()
    for it in mt:
        #print "metadata: %s:%s" % (it[0],it[1])
        if it[0] == "clientid":
            clientId = it[1]
            break
    return clientId

class KvService(BetaBfKvServiceServicer):
    def __init__(self):
        print "init KvService"
        
    def Ping(self, request, context):
        print "===Ping===clientid=(%s)"%getClientId(context)
        print request
        
        resp = BfPingData(message=request.message)
        return resp
        
    def PingStreamCS(self, request_iterator, context):
        print "===PingStreamCS===clientid=(%s)"%getClientId(context)
        resp_data = BfPingData(message="pong")
        resp = Any()
        resp.Pack(resp_data)
        for req in request_iterator:
            if req.Is(_PING_TYPE):
                req_data = BfPingData()
                req.Unpack(req_data)
                print req_data
            yield resp

    def PingStreamC(self, request_iterator, context):
        print "===PingStreamC===clientid=(%s)"%getClientId(context)
        for req in request_iterator:
            if req.Is(_PING_TYPE):
                req_data = BfPingData()
                req.Unpack(req_data)
                print req_data
                
        resp_data = BfPingData(message="pong")
        resp = Any()
        resp.Pack(resp_data)
        return  resp
    
    def PingStreamS(self, request, context):
        print "===PingStreamS===clientid=(%s)"%getClientId(context)
        req = request
        if req.Is(_PING_TYPE):
            req_data = BfPingData()
            req.Unpack(req_data)
            print req_data

        resp_data = BfPingData(message="pong")
        resp = Any()
        resp.Pack(resp_data)
        for i in range(1,10):
            print i
            yield resp
            time.sleep(random.uniform(0.5, 1))
    
    def SetKv(self, request, context):
        pass

    def GetKv(self, request, context):
        pass
            
def run():
    kvservice = beta_create_BfKvService_server(KvService())
    kvservice.add_insecure_port('[::]:50059')
    kvservice.start()
    print "start kvservice"
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print "stop kvservice"
        kvservice.stop(0)

if __name__ == '__main__':
    run()

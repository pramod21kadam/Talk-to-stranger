from flask import request
from flask.views import MethodView
from .base import *
from service.reportbotServ import ReportBotServ

class ReportBotCtrl(MethodView):
    def post(self):
        try:
            data = getData(request)
            if True:
                boolean, msg = ReportBotServ().report(data)
                if boolean:
                    return successRes("Done"), 200
                else:
                    return failureRes(f"{msg}"), 500
            return failureRes("Invalid"), 422
        except Exception as error:
            return failureRes(f"{error}"), 500
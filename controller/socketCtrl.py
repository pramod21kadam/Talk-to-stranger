from packages.packages import *
from service._init_ import *
class SchoolClassServ(MethodView):
    def get(self):
        print("get")
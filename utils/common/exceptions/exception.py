from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status

"""
from utils.common.exceptions import exception
raise exception.myException400({
                "success": False,
                "msg": "邮箱验证码不能为空",
                "results": "",
            })
"""

def custom_exception_handler(exc,context):

    response = exception_handler(exc,context) #获取本来应该返回的exception的response
    if response is not None:
        #response.data['status_code'] = response.status_code  #可添加status_code
        try:
            response.data["success"] = False
            detail_data = response.data.get("detail",None)
            if detail_data: # 如果有detail字段, 将detail换成msg
                response.data["msg"] = response.data['detail']
                del response.data['detail']
            else:
                pass
        except:
            pass

    return response

class myException401(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
class myException400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
class myException403(APIException):
    status_code = status.HTTP_403_FORBIDDEN
class myException404(APIException):
    status_code = status.HTTP_404_NOT_FOUND
class myException500(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
class myException412(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
class myException415(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
class myException422(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

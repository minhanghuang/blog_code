from jsonschema import validate,exceptions
from utils.common.exceptions import exception

class MyJsonSchema(object):

    def __init__(self):
        self.json_schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": "TestInfo",
            "description": "some information about test",
            "type": "object",
            "properties": {},
            "required": [],
        }

    def init(self,instance=None, schema=None):

        self.clear_jsonschema()  # 清空数据
        self.create_schema(schema)  # 拼接schema
        self.check_field(instance=instance,schema=schema)

    def check_field(self,instance=None, schema=None):
        if instance.keys() != schema.keys():
            raise exception.myException400({
                "success": False,
                "msg": "参数不符合要求,需要:[{}],获取的:[{}]".format(schema.keys(),instance.keys())
            })

    def create_schema(self,schema):
        """
        拼接json_schema数据
        :param schema: 字段
        :return: None
        """
        for i,j in schema.items():
            dict_filed = {
                "description": "{} of test".format(i),
                "type": "{}".format(j)
            }
            self.json_schema["properties"][i] = dict_filed
            self.json_schema["required"].append(i)

        return None

    def check_json(self, instance=None, schema=None):
        """
        校验Json数据
        :param instance: 被校验数据
        :param schema: json格式模板 -> dict
        :return: None
        """

        self.init(instance=instance,schema=schema)

        try:
            validate(instance=instance, schema=self.json_schema)
        except exceptions.SchemaError as e: # schema模式无效
            raise exception.myException400({
                "success": False,
                "msg": "{}".format(e.message)
            })
        except exceptions.ValidationError as e: # JSON数据实例无效
            raise exception.myException400({
                "success": False,
                "msg": "{}:{}".format(e.relative_path.pop(),e.message)
            })
        except:
            raise exception.myException400({
                "success": False,
                "msg": "Json校验异常"
            })

        return None

    def clear_jsonschema(self):
        """
        清空实例对象 schema 因为实例化对应只有一个,往里面加数据时,会重复
        :return: None
        """
        self.json_schema["properties"] = {}
        self.json_schema["required"] = []

        return None

jsonschema_obj = MyJsonSchema()
# jsonschema_obj.check_json({"name": "0","age": "0"}, {"name":"strings","age":"string"})



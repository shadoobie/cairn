import json


class TestUtilities:

    def load_json_file(self, schema_file):
        schema = None
        try:
            schema = json.load(schema_file)
        except ValueError:
            print("ValueError thrown when trying to load json schema.")
        except AttributeError:
            print("AttributeError when trying to load json schema.")
        except:
            print("something else went wrong when trying to load json schema.")

        return schema


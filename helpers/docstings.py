class HeaderDocString:
    _token_template = {
        "token": {
            "in": "header",
            "name": "Authorization",
            "required": True,
            "description": "",
            "schema": {"type": "string"},
        }
    }

    @classmethod
    def get_token_doc(cls, description: str, required: bool = True) -> dict:
        doc = cls._token_template.copy()
        doc["token"]["description"] = description
        doc["token"]["required"] = required
        return doc

    @classmethod
    def get_bearer_doc(cls):
        return cls.get_token_doc("Provide bearer token")

    @classmethod
    def get_basic_doc(cls):
        return cls.get_token_doc("Provide basic authorization in base64 format")


class KwargsDoc:
    pass

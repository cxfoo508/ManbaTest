# 请填写：默认值const，必填项required，字段长度，最大值最小值，list长度。---这一行字不能删除
{
    "title": "data info",
    "type": "object",
    "properties": {
        "msg_body": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "maximum": 0,
                            "minimum": 0,
                            "ENUM": [
                                "枚举1", "枚举2"
                            ],
                            "CONST": "默认"
                        }
                    },
                    "REQUIRED": {
                    }
                }
            },
            "REQUIRED": {
            }
        },
        "extra": {
            "type": "string",
            "minLength": 3,
            "maxLength": 30,
            "ENUM": [
                1, 2
            ],
            "CONST": "7"
        },
        "msg_list": {
            "type": "array",
            "items": [
                {
                    "type": "string",
                    "minLength": 3,
                    "maxLength": 30,
                    "ENUM": [
                        5, 6
                    ],
                    "CONST": "7"
                }
            ],
            "minItems": 0,
            "maxItems": 0
        }
    },
    "REQUIRED": {
    }
}

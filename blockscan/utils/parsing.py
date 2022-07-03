class ResponseParser:
    @staticmethod
    def parse(response: dict):
        result = response["result"]
        if "jsonrpc" in response.keys():
            status = True
            message = response["id"]
        else:
            status = bool(int(response["status"]))
            message = response["message"]
        assert status, f"{result} -- {message}"
        return result

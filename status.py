import sys
import os
import shotstack_sdk as shotstack
from shotstack_sdk.api import edit_api
if __name__ == "__main__":
    host = "https://api.shotstack.io/stage"
    configuration = shotstack.Configuration(host = host)
    configuration.api_key['DeveloperKey'] = os.getenv("SHOTSTACK_KEY")
    with shotstack.ApiClient(configuration) as api_client:
        api_instance = edit_api.EditApi(api_client)
        api_response = api_instance.get_render(sys.argv[1], data=False, merged=True)
        status = api_response['response']['status']
        print(f"Status: {status}")
        if status == "done":
            url = api_response['response']['url']
            print(f">> Asset URL: {url}")
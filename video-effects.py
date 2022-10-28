import shotstack_sdk as shotstack
import os
import sys

from shotstack_sdk.api import edit_api
from shotstack_sdk.model.clip import Clip
from shotstack_sdk.model.track import Track
from shotstack_sdk.model.timeline import Timeline
from shotstack_sdk.model.output import Output
from shotstack_sdk.model.edit import Edit
from shotstack_sdk.model.video_asset import VideoAsset
from shotstack_sdk.model.transition import Transition
from shotstack_sdk.model.soundtrack import Soundtrack

if __name__ == "__main__":
    host = "https://api.shotstack.io/v1"

    configuration = shotstack.Configuration(host = host)

    configuration.api_key['DeveloperKey'] = os.getenv("SHOTSTACK_PROD_KEY")
    
    with shotstack.ApiClient(configuration) as api_client:
        api_instance = edit_api.EditApi(api_client)

        video_urls = ['https://cdn.shotstack.io/au/v1/62hne3bb81/a7508c53-aaa7-4d16-9c8b-795b8042de3b.mp4',
                    'https://cdn.shotstack.io/au/v1/62hne3bb81/5e75c6e0-3c5c-408c-bcaf-04c27fa9aa9b.mp4',
                    'https://cdn.shotstack.io/au/v1/62hne3bb81/fcb16166-8ec1-4a19-ac65-dd850f173726.mp4'
        ]
        
        soundtrack = Soundtrack(
            src    = 'https://cdn.pixabay.com/audio/2022/03/23/audio_07b2a04be3.mp3',
            effect = 'fadeInFadeOut',
            volume = 1.0
        )
        
        transition = Transition(
            _in = 'fade',
            out = 'fade'
        )
        
        clips = []
        start = 0.0
        length = 5.0

        for video in video_urls:
            video_asset = VideoAsset(src = video)

            clip = Clip(
                asset = video_asset,
                start = start,
                length = length,
                transition = transition,
                effect = 'zoomIn'
            )

            start = start + length
            clips.append(clip)

        track = Track(clips = clips)

        timeline = Timeline(
            background = "#000000",
            soundtrack = soundtrack,
            tracks = [track]
        )

        output = Output(
            format = "mp4",
            resolution  = "hd"
        )

        edit = Edit(
            timeline = timeline,
            output = output
        )

        try:
            api_response = api_instance.post_render(edit)

            message = api_response['response']['message']
            id = api_response['response']['id']
        
            print(f"{message}\n")
            print(f">> render id: {id}")
        except Exception as e:
            print(f"Unable to resolve API call: {e}")
# Trim and merge videos using Python

This repository is the code for [Python trim and merge videos](https://shotstack.io/learn/python-trim-merge-videos/?utm_source=github&utm_campaign=sample_repos) tutorial using the [Shotstack API](https://shotstack.io/product/video-editing-api/?utm_campaign=sample_repos).


### What is Shotstack API?

Shotstack API is a cloud based video editing API that enables you to render multiple videos concurrently. Visit the [Python SDK](https://shotstack.io/docs/guide/sdks). [Sign up](https://dashboard.shotstack.io/register?utm_campaign=sample_repos) for a free developer account to get your API keys. 

### Why use Shotstack API?

Rendering videos is a resource consuming process. It may take several minutes to render one video depending on the
complexity. Shotstack enables to concurrently render multiple videos in the powerful cloud infrastructure. This reduces rendering time and fastens the process. Visit our [Docs](https://shotstack.io/docs/guide/getting-started/core-concepts/?utm_source=github&utm_campaign=sample_repos) to learn more.

Checkout other Python demo examples in this [Github repo](https://github.com/shotstack/python-demos).

### Configuration

#### Installation

Clone this repository with following command

```bash
git clone https://github.com/shotstack-samples/trim-merge-videos-python.git
```

Go inside the project directory

```bash
cd trim-merge-videos-python
```

Install the required dependencies including the [Shotstack Python SDK](https://pypi.org/project/shotstack-sdk/0.2.1/)

```bash
pip install -r requirements.txt
```
You may need to use `pip3` instead of `pip` depending on your configuration

#### Set your API key

This program uses the **staging** endpoint by default so use your provided **staging** key:

```bash
export SHOTSTACK_KEY=your_key_here
```

Windows users (Command Prompt):

```bash
set SHOTSTACK_KEY=your_key_here
```

Replace `your_key_here` with your provided sandbox API key which is free for testing and development.

### Running the scripts

There are three Python scripts in this repository. First is the `trim-videos.py` that trims a video. Second is the `merge-videos.py` file that merges two videos. Third is the `video-effects.py` file that adds transitions, motion effects, and a background music to the videos.

### Checking render status

To check the render status, run the `**status.py**` file in the command line.

```bash
python status.py {renderId}
```
Replace `{renderId}` with the ID returned from the **watermark.py** or **watermark-list.py** script. Re-run the
status.py script every 4-5 seconds until the status is **done** and a URL is returned. If something goes wrong the
status will show as **failed**.

If everything ran successfully you should now have the URL of the final video, just like the one at the start of the
tutorial.

### Accessing rendered media files via dashboard

To access your rendered files, sign into your Shotstack account. Inside the dashboard, you can find all rendered media under the **Renders** tab.

![Alt Text](https://i.postimg.cc/8cCHTZ8V/2022-09-21-11-15-52-Shotstack-Dashboard.png)


### Edit and automate video production using Python

This is just a basic example. You can do way more with Shotstack Python SDK like: 
- Beautify videos by adding effects, transitions, overlays, titles
- Automate media editing and production
- Automatically generat personalized media with code
- Convert media files i.e. gif, mp3, mp4, jpg, bmp, and png
- Generate and add SRT files to multiple videos concurrently
- Use AI to generate media assets to produce videos and more

See our other [tutorial articles](https://shotstack.io/learn/?utm_campaign=sample_repos) to learn programmatic media
using Python. 
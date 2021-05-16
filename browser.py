from ffmpeg_screen_recorder import Screen_recorder
import argparse
import os
import sys
from selenium import webdriver
import time


def parse_args():
    argument_parser = argparse.ArgumentParser(description='The browser code.')
    argument_parser.add_argument('--server_number', type=int, required=True, help='')
    argument_parser.add_argument('--resolution', type=str, required=True, help='')
    return argument_parser.parse_args()


def main():
    args = parse_args()
    screen_recorder = None
    e = None
    try:
        chrome_driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        driver.maximize_window()
        video_path = os.path.join(os.path.dirname(__file__), 'record.mp4')
        screen_recorder = Screen_recorder(args.resolution, args.server_number, video_path)
        screen_recorder.start()
        driver.get('https://www.google.com/')
        time.sleep(5)
        driver.close()
        screen_recorder.stop()
    except Exception as exception:
        e = exception
    if e :
        sys.exit(f'{e}')


if __name__ == '__main__':
    main()

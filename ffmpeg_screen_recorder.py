import subprocess


class Screen_recorder:
    def __init__(self, resolution: str, input_screen: int, output_filename = 'Recording.mp4'):
        self.__resolution = resolution
        self.__input_screen = input_screen
        self.__output_filename = output_filename
        self.__recording_process = subprocess.Popen

    def start(self):
        '''records in mp4
        '''
        command = f'ffmpeg -f x11grab -video_size {self.__resolution} -i :{self.__input_screen} -codec:v libx264 -r 12 -y "{self.__output_filename}"'
        self.__recording_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
    def stop(self):
        self.__recording_process.communicate(b"q")
        self.__recording_process.kill()

from Katna.video import Video
import os

# For windows, the below if condition is must.
if __name__ == "__main__":

     # set the autoflip build and model path directory based on your installation
     # usually autoflip build is located here : /mediapipe/repo/bazel-build/mediapipe/examples/desktop/autoflip
     # usually mediapipe model is located here : /mediapipe/repo/mediapipe/models
     autoflip_build_path = "/absolute/path/to/autoflip/build/folder
     autoflip_model_path = "/absolute/path/to/autoflip/model/folder

     # desired aspect ratio (e.g potrait mode - 9:16)
     aspect_ratio = 9:16

     # input video file path
     file_path = os.path.join(".", "tests", "data", "pos_video.mp4")

     # output file to save resized video
     abs_file_path_output = os.path.join(".", "tests", "data", "pos_video_resize.mp4")

     #instantiate the video class
     vd = Video(autoflip_build_path, autoflip_model_path)

     print(f"Input video file path = {file_path}")

     vd.resize_video(file_path = file_path, abs_file_path_output = abs_file_path_output, aspect_ratio = aspect_ratio)

     print(f"output resized video file path = {abs_file_path_output}")

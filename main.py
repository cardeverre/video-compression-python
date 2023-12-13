from moviepy.editor import VideoFileClip
import sys
import os

def compress_video(input_video_path, compression_percent, output_video_path=None):
    """
    Compresses a video file (MOV or MP4) to a specified compression percentage while retaining audio.
    Uses the moviepy library.

    :param input_video_path: Path to the input video file.
    :param compression_percent: The percentage to compress the video (0-100).
    :param output_video_path: Path for the output compressed video file. If None, appends '_compressed' to the input file name.
    :return: None
    """

    # Ensure the compression percentage is valid
    if not 0 <= compression_percent <= 100:
        raise ValueError("Compression percentage must be between 0 and 100.")

    # Check if input file is either MOV or MP4
    if not input_video_path.lower().endswith(('.mov', '.mp4')):
        raise ValueError("Input file must be a .mov or .mp4 file.")

    # Derive output video path if not provided
    if output_video_path is None:
        base_name = os.path.splitext(input_video_path)[0]
        output_video_path = f"{base_name}_compressed.mp4"

    # Load the video file
    clip = VideoFileClip(input_video_path)

    # Calculate new resolution
    new_resolution = (int(clip.size[0] * compression_percent / 100), 
                      int(clip.size[1] * compression_percent / 100))

    # Resize the clip and write to a file
    clip_resized = clip.resize(new_resolution)
    clip_resized.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

    print(f"Video compressed and saved as {output_video_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compress_video.py <path_to_video> <compression_percentage>")
        sys.exit(1)

    video_path = sys.argv[1]
    compression = int(sys.argv[2])

    compress_video(video_path, compression)

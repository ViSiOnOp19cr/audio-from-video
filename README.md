# Video to Audio Converter

This is a simple Python script that extracts audio from a video file using the MoviePy library.

## Prerequisites

- Python 3.x
- MoviePy library (install using `pip install moviepy`)

## Usage

1. Clone the repository:
2. Run the script:
 Select a video file using the file dialog that appears.

4. The script will extract the audio from the selected video and save it as a `.mp3` file named `demo.mp3` in the current directory.

## Code Explanation

- `import moviepy.editor`: This imports the MoviePy library, which is used for video editing tasks.
- `from tkinter.filedialog import *`: This imports file dialog functionality from the tkinter library, allowing the user to select a file interactively.
- `vid = askopenfile()`: This opens a file dialog for the user to select a video file.
- `video=moviepy.editor.VideoFileClip("file location")`: This loads the selected video file using MoviePy.
- `aud = video.audio`: This extracts the audio from the video file.
- `aud.write_audiofile("demo.mp3")`: This writes the audio to an MP3 file named `demo.mp3`.

## Contribution

Contributions are welcome! Feel free to open issues or pull requests for any improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# VidMake

VidMake is a simple, script-based video maker. You describe your video in a `.VidMake` file (JSON), then render it from the command line.

This first version focuses on **text over solid-color backgrounds** with basic timing and positioning.

## Features

- JSON-based `.VidMake` files
- Set resolution, FPS, codecs, and background color
- Add multiple text events with:
  - start/end timestamps
  - position (x/y)
  - font size
  - color
- Renders to MP4 using `moviepy` + `ffmpeg`

## Example `.VidMake` file

```json
{
  "resolution": [1280, 720],
  "fps": 30,
  "duration": 8,
  "background_color": "#20232A",
  "video_codec": "libx264",
  "audio_codec": "aac",
  "texts": [
    {
      "text": "VidMake Demo",
      "start": 0,
      "end": 3,
      "x": "center",
      "y": "center",
      "fontsize": 64,
      "color": "#61DAFB"
    },
    {
      "text": "Script-based video generation",
      "start": 3,
      "end": 6,
      "x": "center",
      "y": 450,
      "fontsize": 40,
      "color": "#FFFFFF"
    },
    {
      "text": "Powered by VidMake",
      "start": 6,
      "end": 8,
      "x": "center",
      "y": "center",
      "fontsize": 48,
      "color": "#FFFFFF"
    }
  ]
}
```

Save this as `example.VidMake` and render it with:

```bash
python vidmake.py example.VidMake out.mp4
```

## Usage

1. Install dependencies:

```bash
cd VidMake
pip install -r requirements.txt
```

You need `ffmpeg` installed on your system (e.g. `sudo apt install ffmpeg`).

2. Render a video:

```bash
python vidmake.py path/to/file.VidMake output.mp4
```

## Roadmap

Planned extensions (future versions):

- More shapes and layers (images, gradients, shapes)
- Audio tracks and basic music/sfx timing
- CLI helper: `vidmake render example.VidMake`
- Validation + schema for `.VidMake` files
- GUI/web editor for VidMake scripts

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.

See the [LICENSE](LICENSE) file for full details.

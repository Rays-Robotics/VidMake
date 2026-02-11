#!/usr/bin/env python3
"""VidMake: simple script-based video generator.

Takes a .VidMake JSON file describing:
- video resolution + fps
- background color
- text overlays with timestamps, positions, sizes, and colors

Usage:
  python vidmake.py example.VidMake output.mp4

Requires:
  - Python 3.9+
  - moviepy (pip install moviepy)

This is a minimal first version focused on text + solid background.
"""

import json
import sys
from pathlib import Path

from moviepy.editor import ColorClip, TextClip, CompositeVideoClip


def load_spec(path: Path) -> dict:
  with path.open("r", encoding="utf-8") as f:
    return json.load(f)


def hex_to_rgb(hex_color: str):
  hex_color = hex_color.lstrip("#")
  if len(hex_color) != 6:
    raise ValueError(f"Invalid hex color: {hex_color}")
  return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def build_video(spec: dict, output_path: Path):
  width, height = spec.get("resolution", [1280, 720])
  fps = spec.get("fps", 30)
  duration = spec.get("duration", 10)
  bg_color = hex_to_rgb(spec.get("background_color", "#000000"))

  base = ColorClip(size=(width, height), color=bg_color, duration=duration)

  text_events = spec.get("texts", [])
  layers = [base]

  for ev in text_events:
    text = ev["text"]
    start = float(ev.get("start", 0))
    end = float(ev.get("end", duration))
    color = ev.get("color", "#FFFFFF")
    fontsize = int(ev.get("fontsize", 48))
    x = ev.get("x", "center")
    y = ev.get("y", "center")

    txt_clip = (
      TextClip(text, fontsize=fontsize, color=color)
      .set_start(start)
      .set_end(end)
      .set_position((x, y))
    )
    layers.append(txt_clip)

  final = CompositeVideoClip(layers)

  codec = spec.get("video_codec", "libx264")
  audio_codec = spec.get("audio_codec", "aac")

  final.write_videofile(
    str(output_path),
    fps=fps,
    codec=codec,
    audio_codec=audio_codec,
    audio=False,
  )


def main(argv):
  if len(argv) < 3:
    print("Usage: vidmake.py input.VidMake output.mp4")
    sys.exit(1)

  input_path = Path(argv[1])
  output_path = Path(argv[2])

  if not input_path.exists():
    print(f"Input file not found: {input_path}")
    sys.exit(1)

  spec = load_spec(input_path)
  build_video(spec, output_path)


if __name__ == "__main__":
  main(sys.argv)

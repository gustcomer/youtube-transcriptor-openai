import os
import sys
import subprocess


def transcribe_audio(audio_file, model_name="medium"):
  subprocess.run(
    [
      "whisper",
      "--language", "pt",
      "--word_timestamps", "True",
      "--model", model_name,
      audio_file
    ]
  )


if __name__ == "__main__":
  af = sys.argv[1]
  print(af)
  transcribe_audio(af)
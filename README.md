# video-concat
literally just something SUUUUPER basic to concat a bunch of video files for work
I didn't even plan on building in error handling but here we are


This documentation is, again, super basic. I need to work on this but I'm the only maintainer rn so meh


## Dependencies
[FFMPEG](https://ffmpeg.org/download.html)

easygui

No dependencies required for compiled version

## Changelog
| Version | Date | Released By | Description |
|---|---|---|---|
| v0.1 | 04.11.22 | trixiewasanegg | Initial Release |
| v0.2 | 15.11.22 | trixiewasanegg | Implemented logging for debug & loop to repeat files |
| v0.3 | 03.01.22 | trixiewasanegg | Moved away from MoviePy and directly engaging with ffmpeg |
| v0.31 | 18.02.22 | trixiewasanegg | Bug fix for files with capitalised extensions, removed bodge.py, removed herobrine |

## To Do
Extend valid format range \
Auto detect FPS (still allow for override) \
Batch processing 
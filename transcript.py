import re
import sys
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url: str) -> str:
    """Extract the 11-character video ID from common YouTube URL formats."""
    parsed_url = urlparse(url)

    # https://youtu.be/VIDEO_ID
    if parsed_url.hostname in {"youtu.be", "www.youtu.be"}:
        video_id = parsed_url.path.lstrip("/").split("/")[0]

    # https://youtube.com/watch?v=VIDEO_ID
    elif parsed_url.hostname in {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
    }:
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v", [""])[0]

        else:
            video_id = ""

    else:
        video_id = ""

    if not re.fullmatch(r"[\w-]{11}", video_id):
        raise ValueError("Invalid or unsupported YouTube URL.")

    return video_id


def get_transcript(url: str) -> str:
    """Fetch a YouTube transcript and return it as plain text."""
    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=["en"])

    return "\n".join(snippet.text.strip() for snippet in transcript)
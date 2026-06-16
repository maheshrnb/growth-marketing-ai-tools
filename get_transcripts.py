from youtube_transcript_api import YouTubeTranscriptApi
videos = {
    "cyrus_shepard_ai_seo": "https://www.youtube.com/watch?v=7P7-lVsUfaA",
    "kyle_roof_ai_content": "https://www.youtube.com/watch?v=oKQB5-IXHZU",
    "bernard_huang_clearscope": "https://www.youtube.com/watch?v=MYE6T_gd7H0",
    "aleyda_solis_ai_seo": "https://www.youtube.com/watch?v=3BXsHCqGHBg",
}

for name, url in videos.items():
    video_id = url.split("v=")[1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t["text"] for t in transcript])
        filename = f"research/youtube-transcripts/{name}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Source: {url}\n\n")
            f.write(text)
        print(f"Saved: {name}")
    except Exception as e:
        print(f"Failed: {name} - {e}")
import json
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def get_youtube_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file("client.json", SCOPES)
        creds = flow.run_local_server(port=8080)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)


youtube = get_youtube_service()


def get_all_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet", videoId=video_id, maxResults=100
    )

    while request:
        response = request.execute()
        comments.append(response)

        request = youtube.commentThreads().list_next(request, response)

    with open("comments.json", "w") as f:
        json.dump(comments, f, indent=4)


def hide_comment(comment_id):
    youtube.comments().setModerationStatus(
        id=comment_id,
        moderationStatus="heldForReview",  # or "rejected" / "published"
    ).execute()
    print(f"🙈 Hid comment: {comment_id}")


def get_channel_metadata(channel_id):
    channel_info = (
        youtube.channels().list(part="snippet,statistics", id=channel_id).execute()
    )

    with open("meta.json", "w") as f:
        json.dump(channel_info, f, indent=4)


if __name__ == "__main__":
    videoId = "8nYW-HAQRFA"
    # get_all_comments(videoId)

    # hide_comment("UgwAAqL8EYKciv2gFOd4AaABAg")
    response = youtube.channels().list(part="id", forHandle="MokkaCommentry").execute()

    channel_id = response["items"][0]["id"]

    # get_channel_metadata("UCJroPv1EkUsXQlPPk7UyEMg")

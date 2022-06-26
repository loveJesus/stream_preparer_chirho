#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import datetime
import json
import logging
import os
import sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google.oauth2.credentials import Credentials
from colorama import Fore, Back, Style

scopes_chirho = ["https://www.googleapis.com/auth/youtube"]  # https://www.googleapis.com/auth/youtube.readonly"]
logger_chirho = logging.getLogger(__name__)
logger_chirho.setLevel(logging.INFO)
handler_chirho = logging.StreamHandler(sys.stdout)
formatter_chirho = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - ' + Back.YELLOW + Fore.BLUE + ' %(message)s' + Style.RESET_ALL)
handler_chirho.setFormatter(formatter_chirho)
logger_chirho.addHandler(handler_chirho)
logger_chirho.info("Starting... ALELUYA")


def main_chirho():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name_chirho = "youtube"
    api_version_chirho = "v3"
    client_secrets_file_chirho = "client_secret_28809006910-sf0tknirm06b2l2ibleecoa8rbfarrh9.apps.googleusercontent.com.json"

    # json_credentials_chirho = """
    # {"token": "ya29.a0ARrdaM-LVWoi5CBomyp31C9jZU4QzI5XXN3A0tcjZPAA6UhJR_md8hEVnrZQmmkZW7AuTgnoLrDFC01q1Uxb5UY7dHjh66zhFyMlC1chmjTbfH6HkrOD4_ZWw6O4bamHVlwJ2TRhE0t2U2dbXbjqwrjMLWvF",
    # "refresh_token": "1//0dPf7zVAGkBqVCgYIARAAGA0SNwF-L9IrkALBFzeomya7UmeG3VUl0jXBq0h6_pyHLnOnz9Ba81sFx_q-p3EEOvCCUBrCsImh8j8",
    # "token_uri": "https://oauth2.googleapis.com/token",
    # "client_id": "28809006910-sf0tknirm06b2l2ibleecoa8rbfarrh9.apps.googleusercontent.com",
    # "client_secret": "MWVOApcebbHLXn8H80SWP48a", "scopes": ["https://www.googleapis.com/auth/youtube.readonly"],
    # "expiry": "2022-06-25T23:01:17.305830Z"}
    # """
    # credentials_chirho = Credentials.from_authorized_user_info(json.loads(json_credentials_chirho))

    # Get credentials and create an API client
    flow_chirho = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file_chirho, scopes=scopes_chirho)
    credentials_chirho = flow_chirho.run_local_server(port=4422)

    # print(credentials_chirho.to_json())
    youtube_chirho = googleapiclient.discovery.build(
        api_service_name_chirho, api_version_chirho, credentials=credentials_chirho)

    logger_chirho.info(Fore.BLUE + "Youtube API client created")

    insert_broadcast_response_chirho = youtube_chirho.liveBroadcasts().insert(
        part="snippet,status,contentDetails",
        body={
            "contentDetails": dict(
                enableLowLatency=True, ),
            "snippet": dict(
                title="Love Jesus - Servicio Diario 2022-06-25 בְּרֵאשִׁית/Genesis 5 y ΜΑΘΘΑΙΟΝ/Mateo 4",
                description="""
                Jesucristo es Señor\n\n

                Aprendamos a leer la Palabra juntamente en las lenguas de los escritos.\n
                
                Oración / Lectura de la Palabra /Animo o Exhortación / Santa Cena / Cantar un Himno / Musica de Fondo
                """,
                scheduledStartTime=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                scheduledEndTime=(datetime.datetime.utcnow() + datetime.timedelta(hours=1)).strftime(
                    '%Y-%m-%dT%H:%M:%SZ'),
            ),
            "status": dict(
                privacyStatus="private", )  # options.privacy_status
        }
    ).execute()

    logger_chirho.info(Fore.BLUE + "Broadcast created")

    logger_chirho.debug(json.dumps(insert_broadcast_response_chirho, indent=4, sort_keys=True))

    videos_list_response_chirho = youtube_chirho.videos().list(
        part="snippet,status",
        id=insert_broadcast_response_chirho["id"], ).execute()["items"]

    logger_chirho.debug(json.dumps(videos_list_response_chirho, indent=4, sort_keys=True))

    videos_list_response_chirho[0]["snippet"]["categoryId"] = 27
    videos_list_response_chirho[0]["status"]["madeForKids"] = False
    videos_list_response_chirho[0]["status"]["selfDeclaredMadeForKids"] = False
    youtube_chirho.videos().update(
        part="snippet,status",
        body=dict(
            id=insert_broadcast_response_chirho["id"],
            snippet=videos_list_response_chirho[0]["snippet"],
            status=videos_list_response_chirho[0]["status"])).execute()

    logger_chirho.info("Video Permissions set ALELUYA")

    # insert_stream_response_chirho = youtube_chirho.liveStreams().insert(
    #     part="snippet,cdn",
    #     body=dict(
    #
    #         snippet=dict(
    #             title="NEW STREAM 4 TITLE TEST ALELUYA",
    #             description="NEW STREAM 4 DESCRIPTION TEST ALELUYA",
    #         ),
    #         cdn=dict(
    #             resolution="720p",
    #             format="720p",
    #             ingestionType="rtmp",
    #             frameRate="60fps",
    #         )
    #     )
    # ).execute()
    #
    # print(json.dumps(insert_stream_response_chirho, indent=4, sort_keys=True))

    bind_broadcast_response_chirho = youtube_chirho.liveBroadcasts().bind(
        part="id,contentDetails",
        id=insert_broadcast_response_chirho["id"],
        streamId="J880LYhXwEjWGBFMBQTMWg1656203433631884",  # insert_stream_response_chirho["id"],
    ).execute()

    logger_chirho.info("Broadcast bound to stream ALELUYA")

    logger_chirho.debug(json.dumps(bind_broadcast_response_chirho, indent=4, sort_keys=True))

    logger_chirho.info(
        "Broadcast '%s' was bound to stream '%s' with key  ." % (
            bind_broadcast_response_chirho["id"],
            bind_broadcast_response_chirho["contentDetails"]["boundStreamId"]))

    # broadcast_list_response_chirho = youtube_chirho.liveBroadcasts().list(
    #     mine=True,
    #     id=insert_broadcast_response_chirho["id"],
    #     part="id,snippet,contentDetails,status").execute()
    # print(
    #     json.dumps(broadcast_list_response_chirho, indent=4, sort_keys=True))
    # input("Press Enter to continue... ALELUYA")
    logger_chirho.info(Fore.GREEN + "Make sure stream has started and wait about 10 seconds - Hallelujah" + Fore.RESET)
    input("Then Press Enter to continue to stream test... ALELUYA")

    broadcast_transition_response_chirho = youtube_chirho.liveBroadcasts().transition(
        part="id,status",
        broadcastStatus="testing",
        id=insert_broadcast_response_chirho["id"]).execute()

    logger_chirho.debug(
        json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))
    logger_chirho.info("Broadcast TESTING BEGUN ALELUYA")
    logger_chirho.info(Fore.GREEN + "Make sure stream has started and wait about 10 seconds - Hallelujah" + Fore.RESET)
    input("Then Press Enter to continue... ALELUYA")

    broadcast_transition_response_chirho = youtube_chirho.liveBroadcasts().transition(
        part="id,status",
        broadcastStatus="live",
        id=insert_broadcast_response_chirho["id"]).execute()

    logger_chirho.debug(
        json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))
    logger_chirho.info(Fore.BLUE + "Finished - Hallelujah")

    # request_chirho = youtube_chirho.liveStreams().list(
    #     part="snippet,contentDetails,status",
    #     mine=True
    # )
    # response_chirho = request_chirho.execute()
    #
    # print(json.dumps(response_chirho))


if __name__ == "__main__":
    main_chirho()

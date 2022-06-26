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


class YouTubeStreamerChirho:
    """
    Hallelujah, initialize a youtube stream with title and description
    """

    def __init__(self):
        self.youtube_chirho = None
        self.insert_broadcast_response_chirho: dict = None
        self.bind_broadcast_response_chirho: dict = None

    def execute_chirho(self):
        self._google_credential_receiver_chirho()
        self._initialize_broadcast_chirho()

    def _google_credential_receiver_chirho(self):
        """
        Hallelujah - Receive OAUTH 2 credentials from the user.
        :return:
        """
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name_chirho = "youtube"
        api_version_chirho = "v3"
        client_secrets_file_chirho = "client_secret_chirho.json"

        logger_chirho.info(Fore.BLUE + "Youtube API client created")

        # json_credentials_chirho = """
        # { ... }
        # """
        # credentials_chirho = Credentials.from_authorized_user_info(json.loads(json_credentials_chirho))

        # Get credentials and create an API client
        flow_chirho = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file_chirho, scopes=scopes_chirho)
        credentials_chirho = flow_chirho.run_local_server(port=4422)

        # print(credentials_chirho.to_json())
        self.youtube_chirho = googleapiclient.discovery.build(
            api_service_name_chirho, api_version_chirho, credentials=credentials_chirho)

    def _initialize_broadcast_chirho(self):
        """
        Hallelujah - Initialize a broadcast, set it's children's permissions
        :return:
        """
        self.insert_broadcast_response_chirho = self.youtube_chirho.liveBroadcasts().insert(
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

        # Hallelujah set broadcast permissions

        logger_chirho.info(Fore.BLUE + "Broadcast created")
        logger_chirho.debug(json.dumps(self.insert_broadcast_response_chirho, indent=4, sort_keys=True))

        videos_list_response_chirho = self.youtube_chirho.videos().list(
            part="snippet,status",
            id=self.insert_broadcast_response_chirho["id"], ).execute()["items"]

        logger_chirho.debug(json.dumps(videos_list_response_chirho, indent=4, sort_keys=True))

        videos_list_response_chirho[0]["snippet"]["categoryId"] = 27
        videos_list_response_chirho[0]["status"]["madeForKids"] = False
        videos_list_response_chirho[0]["status"]["selfDeclaredMadeForKids"] = False
        self.youtube_chirho.videos().update(
            part="snippet,status",
            body=dict(
                id=self.insert_broadcast_response_chirho["id"],
                snippet=videos_list_response_chirho[0]["snippet"],
                status=videos_list_response_chirho[0]["status"])).execute()

        logger_chirho.info("Video Permissions set ALELUYA")

    def _link_stream_response_chirho(self):
        """
        Praise the Lord, link broadcast to a desired stream
        :return:
        """
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

        self.bind_broadcast_response_chirho = self.youtube_chirho.liveBroadcasts().bind(
            part="id,contentDetails",
            id=self.insert_broadcast_response_chirho["id"],
            streamId="J880LYhXwEjWGBFMBQTMWg1656203433631884",  # insert_stream_response_chirho["id"],
        ).execute()

        logger_chirho.info("Broadcast bound to stream ALELUYA")

        logger_chirho.debug(json.dumps(self.bind_broadcast_response_chirho, indent=4, sort_keys=True))

        logger_chirho.info(
            "Broadcast '%s' was bound to stream '%s' with key  ." % (
                self.bind_broadcast_response_chirho["id"],
                self.bind_broadcast_response_chirho["contentDetails"]["boundStreamId"]))

    def _handle_transitions_chirho(self):
        """
        Hallelujah - Handle transitions to testing, live, etc.
        :return:
        """
        # broadcast_list_response_chirho = youtube_chirho.liveBroadcasts().list(
        #     mine=True,
        #     id=insert_broadcast_response_chirho["id"],
        #     part="id,snippet,contentDetails,status").execute()
        # print(
        #     json.dumps(broadcast_list_response_chirho, indent=4, sort_keys=True))
        # input("Press Enter to continue... ALELUYA")
        logger_chirho.info(
            Fore.GREEN + Back.WHITE + "Make sure stream has started and wait about 10 seconds - Hallelujah" + Fore.RESET)
        input("Then Press Enter to continue to stream test... ALELUYA")

        broadcast_transition_response_chirho = self.youtube_chirho.liveBroadcasts().transition(
            part="id,status",
            broadcastStatus="testing",
            id=self.insert_broadcast_response_chirho["id"]).execute()

        logger_chirho.debug(
            json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))
        logger_chirho.info("Broadcast TESTING BEGUN ALELUYA")
        logger_chirho.info(
            Fore.GREEN + Back.WHITE + "Make sure stream has started and wait about 10 seconds - Hallelujah" + Fore.RESET)
        input("Then Press Enter to continue... ALELUYA")

        broadcast_transition_response_chirho = self.youtube_chirho.liveBroadcasts().transition(
            part="id,status",
            broadcastStatus="live",
            id=self.insert_broadcast_response_chirho["id"]).execute()

        logger_chirho.debug(
            json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))
        logger_chirho.info(Fore.BLUE + "Finished - Hallelujah")


def main_chirho():
    YouTubeStreamerChirho().execute_chirho()


if __name__ == "__main__":
    main_chirho()

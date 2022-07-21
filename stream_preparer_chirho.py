#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import argparse
import datetime
import json
import logging
import os
import sys
import yaml

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



class YouTubeStreamerChirho:
    """
    Hallelujah, initialize a youtube stream with title and description
    """

    def __init__(self):
        self.youtube_chirho = None
        self._settings_chirho: dict = None
        self.insert_broadcast_response_chirho: dict = None
        self.bind_broadcast_response_chirho: dict = None

    def execute_chirho(self):
        try:
            self._settings_chirho = yaml.safe_load(open("stream_preparer_chirho.yml"))
            logger_chirho.info("Settings loaded - Hallelujah")
        except Exception as e:
            logger_chirho.error(Back.RED + Fore.WHITE + " Hallelujah - Settings not loaded - %s" % e)
            sys.exit(1)
        self._twitch_preparer_chirho()
        self._google_credential_receiver_chirho()
        self._initialize_broadcast_chirho()
        self._link_stream_response_chirho()
        self._handle_transitions_chirho()

    def _twitch_preparer_chirho(self):
        """
        Hallelujah - Prepare the stream for twitch
        :return:
        """
        twitch_id_chirho = int(self._settings_chirho["video_info_chirho"]["twitch_id_chirho"])
        twitch_title_chirho = self._settings_chirho["video_info_chirho"]["video_title_chirho"].replace('"','\\"')
        logger_chirho.info("Twitch ID: %s" % twitch_id_chirho)
        result_code_chirho = os.system('twitch api patch channels -q broadcaster_id=%s -b \'{"title":"%s"}\'' % (
            twitch_id_chirho, twitch_title_chirho))
        if result_code_chirho != 0:
            logger_chirho.error(Back.RED + Fore.WHITE + " Hallelujah - Twitch title not set - Command Error %s" % result_code_chirho)


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
                    title=self._settings_chirho["video_info_chirho"]["video_title_chirho"],
                    description=self._settings_chirho["video_info_chirho"]["video_description_chirho"],
                    scheduledStartTime=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                    scheduledEndTime=(datetime.datetime.utcnow() + datetime.timedelta(hours=1)).strftime(
                        '%Y-%m-%dT%H:%M:%SZ'),
                ),
                "status": dict(
                    privacyStatus="public", )  # options.privacy_status
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
            streamId=self._settings_chirho["video_info_chirho"]["stream_id_chirho"],  # insert_stream_response_chirho["id"],
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
        input("Then Press Enter to continue to TRANSITION STREAM to TESTING - ALELUYA")

        broadcast_transition_response_chirho = self.youtube_chirho.liveBroadcasts().transition(
            part="id,status",
            broadcastStatus="testing",
            id=self.insert_broadcast_response_chirho["id"]).execute()

        logger_chirho.debug(
            json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))
        logger_chirho.info("Broadcast TESTING BEGUN ALELUYA")
        logger_chirho.info(
            Fore.GREEN + Back.WHITE + "Stream in Testing mode wait about 10 seconds - Hallelujah" + Fore.RESET)
        input("Then Press Enter to continue to TRANSITION STREAM to LIVE - ALELUYA")

        broadcast_transition_response_chirho = self.youtube_chirho.liveBroadcasts().transition(
            part="id,status",
            broadcastStatus="live",
            id=self.insert_broadcast_response_chirho["id"]).execute()

        logger_chirho.debug(
            json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))

        logger_chirho.info("Broadcast TESTING BEGUN ALELUYA")
        logger_chirho.info(
            Fore.GREEN + Back.WHITE + "Stream in Testing mode wait about 10 seconds - Hallelujah" + Fore.RESET)
        input("Then Press Enter to continue to TRANSITION STREAM to COMPLETE - ALELUYA")

        broadcast_transition_response_chirho = self.youtube_chirho.liveBroadcasts().transition(
            part="id,status",
            broadcastStatus="complete",
            id=self.insert_broadcast_response_chirho["id"]).execute()

        logger_chirho.debug(
            json.dumps(broadcast_transition_response_chirho, indent=4, sort_keys=True))

        logger_chirho.info(Fore.RED + "Finished - Hallelujah")


def parse_args_chirho():
    """
    Parse the command line arguments God willing
    :return:
    """
    parser = argparse.ArgumentParser(
        description="Prepare Twitch and/or Youtube Streams for Broadcast - Hallelujah",)
    parser.add_argument("--config_chirho", default="stream_preparer_chirho.yml", help="Config file - Hallelujah")
    parser.add_argument("--log_chirho", default=None, help="Log file - Hallelujah")
    parser.add_argument("--debug_chirho", action="store_true", help="Debug mode - Hallelujah")

    return parser.parse_args()


def main_chirho():
    options_chirho = parse_args_chirho()
    logger_chirho.info("Starting... ALELUYA")
    YouTubeStreamerChirho().execute_chirho()


if __name__ == "__main__":
    main_chirho()

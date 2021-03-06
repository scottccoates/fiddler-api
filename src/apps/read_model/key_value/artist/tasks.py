import logging

from src.apps.read_model.key_value.artist import service
from src.apps.read_model.key_value.artist.service import add_unique_track_id
from src.libs.datetime_utils.datetime_parser import get_datetime
from src.libs.job_utils.job_decorator import job

logger = logging.getLogger(__name__)


#
# @job(queue='default')
# def save_recent_eo_content_task(eo_id, eo_attrs, external_id, provider_type, provider_action_type, prospect_id):
#   log_message = (
#     "eo_id: %s, prospect_id: %s", eo_id, prospect_id
#   )
#
#   with log_wrapper(logger.info, *log_message):
#     return service.save_recent_eo_content(eo_id, eo_attrs, external_id, provider_type, provider_action_type,
#                                           prospect_id)
#
#
# @job(queue='default')
# def save_recent_prospect_discovery_network_connections_from_eo_task(eo_attrs, provider_type, prospect_id):
#   log_message = (
#     "prospect_id: %s", prospect_id
#   )
#   with log_wrapper(logger.info, *log_message):
#     service.save_recent_prospect_discovery_network_connections_from_eo(eo_attrs, provider_type, prospect_id)

@job(queue='high')
def set_album_external_id_task(album_id, name, popularity, release_date, provider_type, external_id):
  release_date = get_datetime(release_date)
  return service.set_album_info(album_id, name, popularity, release_date, provider_type, external_id)


@job(queue='high')
def set_album_id_task(album_id, provider_type, external_id):
  return service.set_album_id(album_id, provider_type, external_id)


@job(queue='high')
def add_album_to_artist_task(album_id, artist_id):
  return service.add_album_to_artist(album_id, artist_id)


@job(queue='high')
def add_track_to_album_task(album_id, track_data):
  return service.add_track_to_album(album_id, track_data)


@job(queue='high')
def save_track_info_task(track_id, track_data, album_id):
  return service.save_track_info(track_id, track_data, album_id)


@job(queue='high')
def set_track_external_id_task(track_id, provider_type, external_id):
  return service.set_track_external_id(track_id, provider_type, external_id)


@job(queue='high')
def add_external_artist_id_task(artist_id, provider_type, external_id):
  return service.add_external_artist_id(artist_id, provider_type, external_id)


@job(queue='high')
def add_unique_artist_id_task(artist_id, provider_type, external_id):
  return service.add_unique_artist_id(artist_id, provider_type, external_id)


@job(queue='high')
def add_artist_to_genre_task(name, genre_names):
  return service.add_artist_to_genre(name, genre_names)


@job(queue='high')
def save_artist_info_task(artist_id, name, genres, popularity):
  return service.save_artist_info(artist_id, name, genres, popularity)


@job(queue='high')
def save_artist_top_tracks_task(artist_id, track_data):
  return service.save_artist_top_tracks(artist_id, track_data)


@job(queue='high')
def add_unique_track_id_task(track_id, provider_type, external_id):
  return add_unique_track_id(track_id, provider_type, external_id)

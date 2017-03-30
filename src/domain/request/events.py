from src.libs.common_domain.domain_event import DomainEvent
from src.libs.common_domain.event_signal import EventSignal
from src.libs.python_utils.objects.object_utils import initializer


class RequestSubmitted1(DomainEvent):
  event_func_name = 'submitted_1'
  event_signal = EventSignal()

  @initializer
  def __init__(self, id, artists):
    super().__init__()


class PlaylistCreatedForRequest(DomainEvent):
  event_func_name = 'playlist_created_1'
  event_signal = EventSignal()

  @initializer
  def __init__(self, name, provider_type, external_id):
    super().__init__()


class AlbumAddedToRequest1(DomainEvent):
  event_func_name = 'album_added_1'
  event_signal = EventSignal()

  @initializer
  def __init__(self, album_id, artist_id):
    super().__init__()

class TrackAddedToPlaylist1(DomainEvent):
  event_func_name = 'track_added_1'
  event_signal = EventSignal()

  @initializer
  def __init__(self, track_id):
    super().__init__()

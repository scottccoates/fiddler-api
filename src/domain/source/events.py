from src.libs.common_domain.domain_event import DomainEvent
from src.libs.common_domain.event_signal import EventSignal
from src.libs.python_utils.objects.object_utils import initializer


class SourceCreated1(DomainEvent):
  event_func_name = 'created_1'
  event_signal = EventSignal()

  """ATTRS = source_attrs = {
    constants.ENTITY_TYPE: 'event',
    constants.ENTITY_ID: event.id,
    constants.URL: music_event_url,
  }
  """

  @initializer
  def __init__(self, id, name, provider_type, source_type, attrs):
    super().__init__()

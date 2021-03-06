from PyFloatplane.models.User import User
from PyFloatplane.models.Image import Image
from PyFloatplane.models.StreamOfflineInfo import StreamOfflineInfo


class LiveStream:
    def __init__(self, id=None, title=None, description=None, thumbnail=None,
                 owner=None, stream_path=None, offline=None, subscription_plans=None,
                 subscriber_count_display=None, income_display=None):
        if type(thumbnail) is dict:
            thumbnail = Image.generate(thumbnail)

        if type(owner) is dict:
            owner = User.generate(owner)

        if type(offline) is dict:
            offline = StreamOfflineInfo.generate(offline)

        self.id = id  # String : Id
        self.title = title  # String
        self.description = description  # String
        self.thumbnail = thumbnail  # Image
        self.owner = owner  # String : Id
        self.stream_path = stream_path
        self.offline = offline
        self.subscription_plans = subscription_plans
        self.subscriber_count_display = subscriber_count_display
        self.income_display = income_display

    @staticmethod
    def generate(source):
        return LiveStream(
            id=source['id'],
            title=source['title'],
            description=source['description'],
            thumbnail=source['thumbnail'],
            owner=source['owner'],
            stream_path=source['streamPath'] if 'streamPath' in source else source['stream_path'],
            offline=source['offline'],
            subscription_plans=source['subscriptionPlans'] if 'subscriptionPlans' in source else None,
            subscriber_count_display=source['subscriberCountDisplay'] if 'subscriberCountDisplay' in source else None,
            income_display=source['incomeDisplay'] if 'incomeDisplay' in source else None
        )

    def __repr__(self):
        return '<LiveStream id=\'{}\' title=\'{}\' stream_path=\'{}\'>'.format(
            self.id, self.title, self.stream_path
        )

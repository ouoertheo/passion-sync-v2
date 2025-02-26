from prometheus_client import Counter
from passion_sync.model.activity import Activity
from passion_sync.model.user import User
from passion_sync.service.user import get_user


activities_counter = Counter(
    name="net_tomeofjamin_passionsync_activities",
    documentation="Activities",
    labelnames=("id","name","type","value")
)

def add_activity(user: User, activity: Activity):
    labels = (user.id, user.name, activity.type, activity.value)
    activities_counter.labels(*labels).inc()
import csv
import uuid
from pathlib import Path

from locust import HttpUser, task

golden = Path('.').resolve().parent / 'tests/dream/test_dialogs_gold_phrases.csv'
with open(golden, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    phrases = [row[1] for row in reader][1:]


class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        phrase = next(self.data, None)
        if phrase is None:
            self.on_start()
            phrase = next(self.data)
        # print(f"you: {phrase}")
        ans = self.client.post("", json={"user_id": self.id, "payload": phrase})
        if ans.status_code != 200:
            print(ans.status_code, ans.text)
#        else:
#            print(f"bot: {ans.json()['response']}")

    def on_start(self):
        print('start')
        self.id = f'test_{uuid.uuid4().hex[5:]}'
        self.data = (p for p in phrases)

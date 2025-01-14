import webbrowser
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class PerplexityExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()

        if not query:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Ask Perplexity',
                    description='Type your question after "ask"',
                    on_enter=OpenUrlAction("https://www.perplexity.ai/")
                )
            ])

        url = f"https://www.perplexity.ai/search?q={query}"

        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'Ask Perplexity: {query}',
                description='Press enter to search on Perplexity',
                on_enter=OpenUrlAction(url)
            )
        ])

if __name__ == '__main__':
    PerplexityExtension().run()

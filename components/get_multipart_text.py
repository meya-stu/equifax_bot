# -*- coding: utf-8 -*-
from meya import Component

class GetMultiPartText(Component):
    """
    The nice thing about saying the text this way, is that long, related text
    can be stored in one CMS entry, but displayed in multiple cards.
    """

    def start(self):
        
        key = self.properties.get("key")
        space = self.properties.get("space")
        text, entity = self.cms.get(space, key)
        messages = []
        
        for part in text.split("\n"):
            message = self.create_message(text=part)
            messages.append(message)
            
        return self.respond(messages=messages, action="next")

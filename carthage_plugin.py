import carthage
from carthage import *

from .layout import Layout

@inject(injector=Injector, config=ConfigLayout)
def carthage_plugin(injector, config):
    injector.add_provider(Layout)

"""Translation extension for restricting building with translationed words in Grow."""

from grow import extensions
from grow.extensions import hooks


class Error(Exception):
    """General translation error."""
    pass


class TranslationError(Error):
    """Translation word found in build."""
    pass



class TranslationExtension(extensions.BaseExtension):
    """Translation extension."""

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return []

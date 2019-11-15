"""Translation extension for restricting building with translationed words in Grow."""

import os
from grow import extensions
from grow.extensions import hooks


class Error(Exception):
    """General translation error."""
    pass


class TranslationError(Error):
    """Translation word found in build."""
    pass


class TranslationPodspecStaticDirHook(hooks.PodspecStaticDirHook):
    """Handle the router add hook."""

    def trigger(self, previous_result, *_args, **_kwargs):
        """Execute pre deploy validation."""
        previous_result = previous_result or []

        serve_at = '/_grow/ext/translation/'
        static_dist_dir = os.path.dirname(__file__)[len(self.pod.root):]
        static_dist_dir = '{}/'.format(os.path.join(static_dist_dir, 'dist'))

        # Add the config for a static directory for the extension assets.
        previous_result.append({
            'static_dir': static_dist_dir,
            'serve_at': serve_at,
            'fingerprinted': True,
        })

        return previous_result


class TranslationExtension(extensions.BaseExtension):
    """Translation extension."""

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [TranslationPodspecStaticDirHook]

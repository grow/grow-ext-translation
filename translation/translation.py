"""Translation extension for restricting building with translationed words in Grow."""

import os
from grow import extensions
from grow.extensions import hooks
from grow.routing import router as grow_router


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


# class TranslationRouterAddHook(hooks.RouterAddHook):
#     """Handle the router add hook."""
#
#     def trigger(self, previous_result, router, concrete=True, *_args, **_kwargs):
#         """Execute pre deploy validation."""
#         serve_at = '/_grow/ext/translation/'
#         static_dist_dir = os.path.dirname(__file__)[len(self.pod.root):]
#         static_dist_dir = '{}/'.format(os.path.join(static_dist_dir, 'dist'))
#         print 'Static asset dir: {}'.format(static_dist_dir)
#
#         if concrete:
#             # Enumerate static files.
#             for root, dirs, files in self.pod.walk(static_dist_dir):
#                 for directory in dirs:
#                     if directory.startswith('.'):
#                         dirs.remove(directory)
#                 pod_dir = root.replace(self.pod.root, '')
#                 for file_name in files:
#                     pod_path = os.path.join(pod_dir, file_name)
#                     # Skip when the doc is in the unchanged pod paths set.
#                     if pod_path in unchanged_pod_paths:
#                         continue
#                     static_doc = self.pod.get_static(
#                         pod_path, locale=None)
#                     router.add_static_doc(
#                         static_doc, concrete=concrete)
#         else:
#             serve_at = self.pod.path_format.format_pod(
#                 serve_at, parameterize=True)
#             route_info = grow_router.RouteInfo('static', meta={
#                 'path_format': serve_at,
#                 'source_formats': [static_dist_dir],
#                 'localized': False,
#                 'fingerprinted': True,
#             })
#             router._add_to_routes(
#                 serve_at + '*', route_info, concrete=concrete,
#                 fingerprinted=True)
#
#         return previous_result


class TranslationExtension(extensions.BaseExtension):
    """Translation extension."""

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [TranslationPodspecStaticDirHook]

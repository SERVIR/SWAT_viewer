from tethys_sdk.base import TethysAppBase, url_map_maker


class swat(TethysAppBase):
    """
    Tethys app class for SWAT.
    """

    name = 'SWAT Data Viewer'
    index = 'swat:home'
    icon = 'swat/images/logo.png'
    package = 'swat'
    root_url = 'swat'
    color = '#2c3e50'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='swat/home',
                controller='swat.controllers.home'
            ),
            UrlMap(
                name='time-series',
                url='swat/timeseries',
                controller='swat.controllers.timeseries'
            ),
            UrlMap(
                name='upload_files',
                url='swat/upload',
                controller='swat.controllers.upload_files'
            )
        )

        return url_maps

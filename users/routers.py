from rest_framework.routers import Route, DynamicRoute, SimpleRouter


class CustomRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
    ]


class CustomRouter2(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={
                'get': 'list',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}$',
            mapping={
                'post': 'create',
            },
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'retrieve',
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
    ]

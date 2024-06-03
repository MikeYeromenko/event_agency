from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class AuthenticationV1API(GenericViewSet):

    @swagger_auto_schema(responses={200: SignInResponseSerializer})
    @action(
        detail=False,
        name="Sign In User",
        methods=("post",),
        url_path="sign-in",
        serializer_class=UserSignInSerializer,
        permission_classes=(IsAnonymous,),
    )
    def sign_in(self, *args, **kwargs):
        ...
        return Response(response_data)

    @swagger_auto_schema(responses={200: TokenSerializer})
    @action(
        detail=False,
        methods=("post",),
        name="Refresh token",
        url_path="refresh-token",
        serializer_class=RefreshTokenSerializer,
        permission_classes=(IsAuthenticated,),
    )
    def refresh_token(self, *_args, **_kwargs):
        ...
        return Response(response_serializer.data)


@swagger_auto_schema(methods=["post"], responses={200: SwaggerSuccessSerializer})
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request: Request, *_args, **_kwargs):
    """
    Users logout endpoint

    User logout
    """
    logout(request)
    return Response(SwaggerSuccessSerializer({"success": True}).data)

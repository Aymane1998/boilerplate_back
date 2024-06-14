from app_logs import permissions
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import response, status, views
from api import exceptions
from app_logs import utils
from drf_spectacular.utils import OpenApiParameter


@extend_schema_view(
    get=extend_schema(
        tags=["Logs"],
        operation_id="List of object logs",
        summary="List of object logs",
        description="",
        parameters=[
            OpenApiParameter(name="field", description="field change ", type=str),
            OpenApiParameter(
                name="user_id", description="user who made change", type=int
            ),
            OpenApiParameter(
                name="object_id", description="id of object change", type=int
            ),
        ],
    ),
)
class LogsViews(views.APIView):
    permission_classes = (permissions.LogsPermission,)

    def __get_query_model(self, model_name, object_id):
        model = utils.get_model_by_model_name(model_name)

        if model is None:
            raise exceptions.APIValidationError(
                status=status.HTTP_400_BAD_REQUEST, detail="Wrong model name."
            )

        if object_id:
            query_model = model.objects.filter(id=object_id)

            if query_model.count() == 0:
                exceptions.APIException(status=status.HTTP_404_NOT_FOUND)

        else:
            query_model = model.objects.all()

        return query_model

    def get(self, *args, **kwargs):
        model_name = kwargs.get("model")
        field_name = self.request.query_params.get("field")
        object_id = self.request.query_params.get("object_id")
        user_id = self.request.query_params.get("user_id")

        list_all_changes = []

        query_model = self.__get_query_model(model_name, object_id)

        for object in query_model:
            if user_id is not None:
                query_historys = object.history.filter(history_user_id=user_id)
            else:
                query_historys = object.history.all()

            list_change_one_object = utils.ListChangeObject(
                query_historys=query_historys,
                field=field_name,
            ).handler()

            list_all_changes.append(list_change_one_object)

        flat_result = [x for xs in list_all_changes for x in xs]

        all_changes_ordered = sorted(flat_result, key=lambda x: x["date"], reverse=True)

        return response.Response(
            status=status.HTTP_200_OK, data={"changes": all_changes_ordered}
        )

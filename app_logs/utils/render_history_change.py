from authentication import models as auth_models


class ListChangeObject:
    def __init__(self, query_historys, field):
        self.query_historys = query_historys
        self.field = field

    def __get_user_infos(self, history_user_id):
        if history_user_id:
            user = auth_models.User.objects.get(id=history_user_id)
            user_id = user.id
            user_username = user.username

        else:
            user_id = None
            user_username = ""

        return user_id, user_username

    def handler(self):

        all_changes = []

        for index, history in enumerate(self.query_historys):
            if index + 1 < len(self.query_historys):  # do not take the last item
                list_changes_one_change = []
                user_id, user_username = self.__get_user_infos(history.history_user_id)
                delta = history.diff_against(self.query_historys[index + 1])

                for change in delta.changes:

                    # filter by field or not
                    if self.field is None or self.field == change.field:
                        dict_change = {
                            "object_id": history.id,
                            "user_id": user_id,
                            "user_username": user_username,
                            "date": history.history_date,
                            "field_changed": change.field,
                            "old_value": change.old,
                            "new_value": change.new,
                        }
                        list_changes_one_change.append(dict_change)

                all_changes.append(list_changes_one_change)

        # flate all result of one object
        flat_result = [x for xs in all_changes for x in xs]
        return flat_result

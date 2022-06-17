import datetime

db.define_table(
    "collab_open_rooms",
    Field("course_name", type="string"),
    Field("activity", type="string"),
    Field("owner", type="string"),
    Field("room_name", type="string"),
    Field("conn_pass", type="string"),
    migrate=table_migrate_prefix + "collab_open_rooms.table",
)

db.define_table(
    "collab_active_users",
    Field("user_id", type="string"),
    Field("room_id", "reference collab_open_rooms"),
    migrate=table_migrate_prefix + "collab_active_users.table",
)
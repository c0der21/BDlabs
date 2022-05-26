from dbtable import *


class AutoTable(DbTable):
    def table_name(self):
        return self.dbconn.prefix + "autos"

    def columns(self):
        return {"person_id": ["integer", f"REFERENCES {self.dbconn.prefix}people(id) ON DELETE CASCADE"],
                "brand": ["varchar(12)", "NOT NULL"],
                "model": ["varchar(12)", "NOT NULL"],
                "color": ["varchar(12)", "NOT NULL"],
                "identity": ["varchar(12)", "PRIMARY KEY"],
                }

    def all_by_person_id(self, pid):
        sql = f"SELECT * FROM {self.table_name()} WHERE person_id = %s ORDER BY {', '.join(self.primary_key())}"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, [pid])
        return cur.fetchall()

    def primary_key(self):
        return ['identity']

    def update_one_by_field(self, field, field_val, autoBrand, autoModel, autoColor, autoId):
        is_exist = self.check_field_exist(field, str(field_val))
        if (is_exist):
            self.dbconn.conn.cursor().execute(
                sql.SQL(
                    f"""UPDATE {self.table_name()}
                        SET brand = %s, model = %s, color = %s, identity = %s
                        WHERE {{}} = %s"""
                ).format(sql.Identifier(field)), (autoBrand, autoModel, autoColor, autoId, field_val,))

        return is_exist
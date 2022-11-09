# XXX Use Abstract Base Classes?

from db.run_sql import run_sql

class BaseRepository:
    def get_mdo_factory(self):
        raise NotImplementedError()

    def select(self, id):
        values = [id]
        results = run_sql(self.SQL_SELECT, values)

        if results:
            row = results[0]
            make_mdo_from_row = self.get_mdo_factory()
            return make_mdo_from_row(row)
        return None

    def select_all(self):
        results = run_sql(self.SQL_SELECT_ALL)

        make_mdo_from_row = self.get_mdo_factory()
        model_objects = [make_mdo_from_row(row) for row in results]
        return model_objects

    def delete(self, id):
        values = [id]
        run_sql(self.SQL_DELETE, values, do_fetchall=False)

    def save(self, mdo):
        values = self.make_row_from_mdo(mdo)
        results = run_sql(self.SQL_INSERT, values)
        id = results[0]['id']
        mdo.id = id
        return mdo

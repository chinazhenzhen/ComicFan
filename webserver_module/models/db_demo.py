from app import db

class Cmad(db.Document):
    meta = {
        'collection': 'CmadItem',
    }
    # mongo数据库连接测试
    m_title = db.StringField()
    m_desc = db.StringField()

    def __str__(self):
        return "m_title:{}-m_desc:{}".format(self.m_title, self.m_desc)


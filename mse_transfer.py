from pprint import pprint

from config import db_p114tr1
from config import db_p114tr2
from database.models3p114tr2 import ReferralMse, Client
from database.models2p114tr1 import ReferralMse as Rm, Client as Cl


class CMergeActions:
    # with db.session_scope() as session:
    #     session = session
    #
    # mapping_typename_table = {
    #     "Text": ActionpropertyString,
    #     "String": ActionpropertyString,
    #     "Integer": ActionpropertyInteger,
    #     "Double": ActionpropertyDouble,
    #     "Date": ActionpropertyDate,
    # }
    def format_row(self, action):
        return {k: v for k,v in action.__dict__.items() if not k.startswith("_") and k != 'id'}

    def get_mse_info(self):
        with db_p114tr1.session_scope() as session:
            result = session.query(ReferralMse).filter(ReferralMse.deleted==0).all()
            for row in result:
                client = session.query(Client).filter(Client.id == row.client_id, Client.deleted == 0).first()
                with db_p114tr2.session_scope() as session2:
                    result = session2.query(Cl).filter(

                        Cl.SNILS == client.SNILS,
                        Cl.deleted == 0
                    ).first()
                    if not result:
                        print(f"Client not found for mse {row.id}")
                        continue
                    else:
                        print('FOUND')




if __name__ == '__main__':
    print(CMergeActions().get_mse_info())
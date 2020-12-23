
class CommitException(Exception):
    pass

class RollbackException(Exception):
    pass

def write_to_db():
    print("opening database connection....")
    print("start transaction.....")
    try:
        while True:
            try:
                data = yield
                print("writing data to database.....", data)
            except CommitException:
                print("commiting transaction....")
                print("opening next transaction.....")
            except RollbackException:
                print("aborting transaction....")
                print("opening next transaction.....")
    finally:
        print("generator closing....")
        print("abort transaction....")
        print("closing database connection.....")

if __name__ == "__main__":
    sql = write_to_db()
    next(sql)
    sql.send(100)
    sql.throw(CommitException)
    sql.send(200)
    sql.throw(RollbackException)
    sql.close()

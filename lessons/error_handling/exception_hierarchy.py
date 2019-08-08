# run in debug
try:
    try:
        try:
            raise Exception('hi')
        except Exception as e:
            raise e
    except Exception as e:
        raise e
except Exception as e:
    print(e)

import traceback

from ketchup_core.orchestrator import KetchupOrchestrator

if __name__ == '__main__':
    try:
        app = KetchupOrchestrator()
    except Exception as ex:
        # TODO:
        # 1. Understand what exceptions can occur in the starting phase
        # 2. Appropriately handle them (even by letting the app fail)
        # 3. Inform the user of what went wrong (and possibly how to fix it)
        print(ex)
    else:
        try:
            app.run()
        except Exception as ex:
            # TODO
            print("Exception happened:")
            print(ex)
            traceback.print_exc()

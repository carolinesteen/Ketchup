from ketchup_core.orchestrator import KetchupOrchestrator

if __name__ == '__main__':
    try:
        app = KetchupOrchestrator()
    except Exception as ex:
        # TODO:
        # 1. Understand what exceptions can occur in the starting phas
        # 2. Appropriately handle them (even by letting the app fail)
        # 3. Inform the user of what went wrong (and possibly how to fix it)
        pass
    else:
        try:
            app.run()
        except Exception as ex:
            # TODO: same as above
            pass



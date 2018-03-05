def is_database_synchronized(database):
    """
    Checks if migrations are applied to databse.

    May be helpful if AppConfig.ready() uses application models.
    """
    # Imports belongs to function to prevent
    # "AppRegistryNotReady: Apps aren't loaded yet" exception
    from django.db.migrations.executor import MigrationExecutor
    from django.db import connections
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return not executor.migration_plan(targets)

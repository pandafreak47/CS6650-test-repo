from typing import Dict, Optional, Tuple, Union

from django.db import models
from django.db.models import get_app, get_models
from django.db.utils import IntegrityError, OperationalError
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.db.utils.apps import DjangoDatabaseErrorHandler
from django.dispatch.dispatcher import Message
from django.db.backends.base.base import (
    BaseDatabaseFeatures,
    create_db_engine,
    create_db_engine_settings,
    create_db_session,
)
from django.db.backends.creation import create_default_db_tables
from django.db.backends.creation.utils import create_test_database_from_settings
from django.db.backends.creation.utils import ensure_database
from django.db.backends.creation.utils import ensure_database_exists
from django.db.backends.creation.utils import ensure_database_from_settings
from django.db.backends.creation.utils import ensure_database_exists_from_settings
from django.db.backends.creation.utils import ensure_test_database_exists
from django.db.backends.creation.utils import ensure_test_database_from_settings
from django.db.backends.creation.utils import ensure_test_database_from_settings_with_replica
from django.db.backends.creation.utils import ensure_test_database_from_settings_with_replica_with_schema
from django.db.backends.creation.utils import ensure_test_database_from_settings_with_replica_with_schema_for_replica
from django.db.backends.creation.utils import ensure_test_database_from_settings_with_replica_with_schema_for_replica_with_schema
from django.db.backends.postgresql.base import PostgresqlDatabaseFeatures
from django.db.backends.postgresql.creation import _postgres_create_database
from django.db.backends.postgresql.schema import (
    ADD_COLUMN,
    ADD_COLUMN_WITH_TYPE,
    ADD_COLUMN_WITH_TYPE_DEFAULT,
    ADD_COLUMN_WITH_TYPE_UNIQUE,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NOTNULL_NOTNULL_NULL,
    ADD_COLUMN_WITH_TYPE_UNIQUE_DEFAULT_NOTNULL_NOTNULL_NULL_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NULL_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NOTNULL_NOTNULL_NULL,
    ADD_COLUMN_WITH_TYPE_DEFAULT_NOTNULL_NOTNULL_NULL_NOTNULL_NOTNULL,
    ADD_COLUMN_WITH_TYPE_NOTNULL,
    ADD_COLUMN_WITH_TYPE_NOTNULL_NULL,
    ADD_COLUMN_WITH_TYPE_NOTNULL_NOTNULL
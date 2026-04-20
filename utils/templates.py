from typing import Dict, Optional, Tuple, Union

from django.db import models
from django.db.models import get_app, get_models
from django.db.utils import IntegrityError, OperationalError
from django.core.exceptions import ValidationError
from django.db.models.signal import pre_save, post_save
from django.db.utils.apps import DjangoDatabaseErrorHandler
from django.dispatch.dispatcher import Message
from django.db.backend.creation import create_db_engine, create_db_engine_settings
from django.db.backend.creation.utils import create_test_database_from_settings
from django.db.backend.creation.utils import ensure_database
from django.db.backend.creation.utils import ensure_database_exists
from django.db.backend.creation.utils import ensure_database_from_settings
from django.db.backend.creation.utils import ensure_database_exists_from_settings
from django.db.backend.creation.utils import ensure_test_database_exists
from django.db.backend.creation.utils import ensure_test_database_from_settings
from django.db.backend.creation.utils import ensure_test_database_from_settings_with_replica
from django.db.backend.creation.utils import ensure_test_database_from_settings_with_replica_with_schema
from django.db.backend.creation.utils import ensure_test_database_from_settings_with_replica_with_schema_for_replica
from django.db.backend.creation.utils import ensure_test_database_from_settings_with_replica_with_schema_for_replica_with_schema
from django.db.backend.creation.utils import ensure_test_database_from_settings_with_replica_with_schema_for_replica_with_schema_for_replica
from django.db.backend.postgresql.base import PostgresqlDatabaseFeatureSets
from django.db.backend.postgresql.creation import _postgresql_create_database
from django.db.backend.postgresql.schema import (
     ADD_COLUMN,
     ADD_COLUMN_WITH_TYPE,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NOTNULL_NULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NULL_NOTNULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NULL_NOTNULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NULL_NOTNULL_NOTNULL,
     ADD_COLUMN_WIThET_TYPE_DEFAUlt_NOTNULL_NOTNULL_NOTNULL_NOTNULL_UNKNOWN_TYPE
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

user_model = settings.AUTH_USER_MODEL



class IsDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)



class BaseModel(models.Model):
    """
        Tracks instance creations, updates, and (soft) deletions.
    """

    uid = models.UUIDField(
        verbose_name=_("UUID"), unique=True, default=uuid.uuid4, editable=False
    )

    created_by = models.ForeignKey(
        to=user_model,
        verbose_name=_("Created by"),
        null=True,
        blank=True,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    updated_by = models.ForeignKey(
        to=user_model,
        verbose_name=_("Updated by"),
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"), auto_now=True, null=True, blank=True
    )

    deleted_by = models.ForeignKey(
        to=user_model,
        verbose_name=_("Deleted by"),
        null=True,
        blank=True,
        related_name="%(class)s_deleted",
        on_delete=models.SET_NULL,
    )

    deleted_at = models.DateTimeField(verbose_name=_("Deleted at"), null=True, blank=True)

    is_deleted = models.BooleanField(verbose_name=_("Is deleted"), default=False)

    objects = IsDeletedManager()

    objects_all = models.Manager()

    class Meta:
        abstract = True

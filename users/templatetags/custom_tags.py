import json

from decimal import Decimal
from django import template
from django.db.models import QuerySet, Model
from django.core import serializers
from django.forms import model_to_dict
from django.utils.safestring import mark_safe

from users.api.serializers import UserSerializer

register = template.Library()


def handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, Model):
        model_dict = model_to_dict(obj)
        return model_dict
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return serializers.serialize('json', obj)
    if isinstance(obj, Model):
        model_dict = model_to_dict(obj)
        if hasattr(obj, 'extra_data'):
            for key in obj.extra_data:
                model_dict[key] = getattr(obj, key)
        return mark_safe(json.dumps(model_dict, default=handler))
    return mark_safe(json.dumps(obj, default=handler))
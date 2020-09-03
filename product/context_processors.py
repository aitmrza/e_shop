from product.models import Category
from feedback.forms import FeedBackForm


def category_tree(request):
    category_roots = Category.objects.filter(parent=None)
    categories = category_roots.get_descendants(include_self=True)
    return {'category_tree': categories}


def feedback_form(request):
    return {'feedback_form': FeedBackForm()}

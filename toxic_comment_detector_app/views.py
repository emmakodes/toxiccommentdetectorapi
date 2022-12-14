from rest_framework.views import APIView
from .services import check_toxicity


class DetectToxicComment(APIView):
    # def get(self, request, **kwargs):
    #     comment = kwargs.get('comment', None)
    #     result = check_toxicity(comment)
    #     return result
    def post(self, request, format=None):
        comments = request.data.get('comment')
        result = check_toxicity(comments)
        return result










